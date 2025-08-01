# %%
# Imports
# Note: to make sure vscode finds the port package, install with
#       pip install -e .[dev]

import argparse
import json
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
    entry = Entry(filename=filename, table=table, list_blocks={}, static_fields={})
    seen_static = set()

    for _, row in schema_group.iterrows():
        colname = row["column_name"]
        subfield_path = tuple(row["subfield_path"].split("."))
        if row["var_type"] == "static":
            entry.static_fields[colname] = subfield_path
        else:
            list_path = tuple(row["list_path"].split("."))
            entry.list_blocks.setdefault(list_path, {})[colname] = subfield_path
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
    #TIKTOK=BASE_PATH / "TikTok/Final/Merged_structures_TT.csv",
    X=BASE_PATH / "Twitter/Final/Merged_structures_X.csv",
)


# % Generate single entry
def write_entries(outfile):
    lines = []
    lines.append(f'"""\n{DOCSTRING.strip()}\n"""\n\n')
    lines.append("from port.helpers.parsers import Entry\n\n")

    for name, infile in infiles.items():
        lines.append(f"{name}_ENTRIES: list[Entry] = [\n")
        for entry in extract_entries_from_csv(infile):
            lines.append(f"    {repr(entry)},\n")
        lines.append("]\n\n")

    print(f"Writing output to {outfile}")
    with open(outfile, "w") as f:
        f.writelines(lines)


# %%
# Generate entries data file
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "entry",
        nargs="?",
        help="Print a single platform:id entry to stdout rather than generating the entries file (for testing purposes)",
    )
    args = parser.parse_args()
    if args.entry:
        platform, table_id = args.entry.split(":")
        entries = {e.table: e for e in extract_entries_from_csv(infiles[platform])}
        print(json.dumps(entries[table_id]._asdict(), indent=2))
        print()
        print(entries[table_id])
    else:
        write_entries(outfile="packages/python/port/helpers/entries_data.py")
