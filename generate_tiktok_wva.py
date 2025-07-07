# %%
# import pandas as pd
import inspect
import json
from pathlib import Path
from typing import List

import pandas as pd


# -----------------------
# Utility Functions
# Note: Some or all of these can just be moved to helpers, to generate only the dynamic part
# -----------------------
def get_in(d: dict, *keys):
    for key in keys:
        if isinstance(d, dict):
            d = d.get(key)
        else:
            return None
    return d


def get_list(d: dict, *keys):
    val = get_in(d, *keys)
    return val if isinstance(val, list) else []


def snake_case(name: str) -> str:
    return name.lower().replace("-", "_").replace(".json", "").replace(".js", "").replace(" ", "_")


def create_tt_df(
    file_input: list[str], file_folder_name: str, static_fields: list[list[str]], list_blocks: dict[str, str]
) -> pd.DataFrame:

    try:
        with open(file_input[0], "r", encoding="utf-8") as f:
            data = json.load(f)
        root_data = get_in(data, "Activity", file_folder_name)
        if not root_data:
            print(f"⚠️ No data found at path: {file_folder_name}")
            return pd.DataFrame()

        base_row = {}
        for path in static_fields:
            base_row[path[-1]] = get_in(root_data, *path[1:])
        if not list_blocks:
            # WvA: Should we not also return base_row if no entries found for list_blocks?
            return pd.DataFrame([base_row])

        all_records = []
        for list_path, fields in list_blocks.items():
            items = get_list(root_data, *list_path[1:])
            for item in items:
                row = base_row.copy()
                row["__source_list__"] = list_path[-1]
                for field in sorted(fields):
                    row[field] = item.get(field, ".*?")
                all_records.append(row)
        return pd.DataFrame(all_records)
    except Exception as e:
        print(f"❌ Error in {file_folder_name}: {e}")
        return pd.DataFrame()


def create_donation_flow(file_input: List[str]):
    """Create donation flow from TikTok JSON."""
    tables = []
    for entry in ENTRIES:
        name = snake_case(entry["file_folder_name"])
        try:
            df = create_tt_df(file_input, **entry)
            if not df.empty:
                tables.append(donation_table(name=name, df=df, title={"en": name}))
        except Exception as e:
            print(f"Error in {name}:", e)
    if tables:
        return donation_flow(id="tiktok", tables=tables)
    else:
        return None


# %% --------------------
# Extract Field Paths
# -----------------------


def build_field_mappings(schema_group: pd.DataFrame):
    static_fields = []
    list_blocks = {}

    for _, row in schema_group.iterrows():
        path = []
        list_path = []
        last_key = None
        row_path = row["row_path"]
        path.append(row_path)

        for i in range(1, 6):
            col_val = row.get(f"col_path_{i}")
            list_status = row.get(f"col_path_{i}_LIST", "NO LIST")
            if pd.notna(col_val):
                path.append(col_val)
                if list_status == "LIST":
                    list_path = path.copy()

        last_key = path[-1] if path else None

        if list_path:
            list_path_tuple = tuple(list_path[:-1])
            field = list_path[-1]
            list_blocks.setdefault(list_path_tuple, set()).add(field)
        elif last_key:
            static_fields.append(path)

    return static_fields, list_blocks


# %% -----------------------
# Load Schema & Create entries list
# -----------------------
schema_path = "Merged_structures_TT.csv"
schema_df = pd.read_csv(schema_path)
schema_df.columns = schema_df.columns.str.strip()

entries = []
for fn, group in schema_df.groupby("row_path"):
    static_fields, list_blocks = build_field_mappings(group)
    entry = dict(file_folder_name=fn, static_fields=static_fields, list_blocks=list_blocks)
    entries.append(entry)


# %% -----------------------
# Generate file
# -----------------------

output_path = Path("packages/python/port/donation_flows/tiktok.py")
with open(output_path, "w", encoding="utf-8") as f:
    f.write("# Auto-generated TikTok extractors\n\n")
    f.write("import pandas as pd\n")
    f.write("import json\n")
    f.write("import logging\n")
    f.write("from port.helpers.donation_flow import donation_table, donation_flow\n")
    f.write("from typing import List\n\n")
    f.write(f"ENTRIES = [\n")
    for field in entries:
        f.write(f"    {repr(field)},\n")
    f.write("]\n\n")
    f.write(inspect.getsource(get_in))
    f.write("\n")
    f.write(inspect.getsource(get_list))
    f.write("\n")
    f.write(inspect.getsource(snake_case))
    f.write("\n")
    f.write(inspect.getsource(create_tt_df))
    f.write("\n\n")
    f.write(inspect.getsource(create_donation_flow))

print(f"Extractors written to {output_path}")

# %%
