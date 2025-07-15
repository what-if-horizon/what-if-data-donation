# %%
# Imports
# Note: to make sure vscode finds the port package, install with
#       pip install -e .[dev]

from pathlib import Path
from typing import Iterable

import pandas as pd
from port.helpers.parsers import Entry  # type: ignore

DOCSTRING = """
Donation file structure data for takeout flows

This file contains a list of Entries for each platform.
Each Entry represents a table to be generated from the appropriate file.

To generate this file, please run structure/flow_generation/generate_entries.py
which will use the Merged_structures_*.csv to determine the required entries.
"""

# %%
# Helper functions


def snake_case(name: str) -> str:
    return name.lower().replace("-", "_").replace(".json", "").replace(".js", "").replace(" ", "_")


def extract_path(row) -> tuple[str, ...]:
    path = []
    for col in ["row_path"] + [f"col_path_{i}" for i in range(1, 6)]:
        val = row.get(col)
        if pd.notna(val) and str(val).strip().upper() != "MISSING":
            path.append(str(val).strip())
    return tuple(path)


def extract_entry(filename: str, table: str, schema_group: pd.DataFrame) -> Entry:
    """Generate an Entry for a group of rows from the structure csv file

    Each entry represents a table that should be generated in the donation flow,
    with static_fields (one value for the whole table) and list_blocks (generating rows)

    Args:
        filename (str): the name of the file from which to extract the information
        table (str): a descriptive name for this table
        schema_group (pd.DataFrame): the Pandas group in the structure dataframe

    Returns:
        Entry: a single Entry object
    """

    # WvA: Note: One difference between the field mappings in TT and X
    #      was that in TT a field is ignored if followed by an empty LIST column
    #      E.g. for {'adsRevenueSharing': {'payoutHistory': ['array']}}
    #      The X structure creates a static field, but TT does not.
    #      Was this intentional?
    #      Resolution: a leaf node ['array'] should be ignored, a leaf node ['string'] should lead to a list

    entry = Entry(filename=filename, table=table, list_blocks={}, static_fields={})
    seen_static = set()

    for _, row in schema_group.iterrows():
        path = extract_path(row)

        # IF we encounter a LIST, create a list_block from that list. Otherwise, create a static_field
        for i in range(len(path)):
            if str(row.get(f"col_path_{i+1}_LIST", "")).strip().upper() == "LIST":
                list_path = tuple(path[: i + 1])
                subfield_path = tuple(path[i + 1 :])
                if subfield_path:
                    entry.list_blocks.setdefault(list_path, {})[subfield_path[-1]] = subfield_path
                break
        else:
            field = path[-1]
            if field not in seen_static:
                entry.static_fields[path[-1]] = path
                seen_static.add(field)

    return entry


def extract_entries_from_csv(infile: Path) -> Iterable[Entry]:
    schema_df = pd.read_csv(infile)
    schema_df.columns = schema_df.columns.str.strip()
    if "json_name" in schema_df.columns:
        schema_df = schema_df.dropna(subset=["json_name"])
    else:
        schema_df["json_name"] = None
    if "id" in schema_df:
        schema_df["table_id"] = schema_df["id"].str.split(":").str[0]
    else:
        schema_df["table_id"] = schema_df["variable"].apply(snake_case)

    schema_df = schema_df.dropna(subset=["row_path"])
    schema_df = schema_df[schema_df["row_path"] != "No data"]
    for table_id, group in schema_df.groupby("table_id"):
        (filename,) = set(group["json_name"])
        yield extract_entry(filename, table_id, group)


# %%
BASE_PATH = Path.cwd() / "structure_donations" / "Processed_structure_donations"
infiles = dict(
    TIKTOK=BASE_PATH / "TikTok/Final/Merged_structures_TT.csv", X=BASE_PATH / "Twitter/Final/Merged_structures_X.csv"
)


# %%
# Generate entries data file


lines = []
lines.append(f'"""\n{DOCSTRING.strip()}\n"""\n\n')
lines.append("from port.helpers.parsers import Entry\n\n")

for name, infile in infiles.items():
    lines.append(f"{name}_ENTRIES: list[Entry] = [\n")
    for entry in extract_entries_from_csv(infile):
        lines.append(f"    {repr(entry)},\n")
    lines.append("]\n\n")

outfile = "packages/python/port/helpers/entries_data.py"
print(f"Writing output to {outfile}")
with open(outfile, "w") as f:
    f.writelines(lines)
# %%
