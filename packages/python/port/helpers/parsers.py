import json
import pandas as pd

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
