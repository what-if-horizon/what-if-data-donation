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


def extract_entry(filename: str | None, table: str, schema_group: pd.DataFrame) -> Entry:
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

    def get_path(value):
        # If value is NaN (from Pandas) or empty string, return empty tuple
        if pd.isna(value) or value == '':
            return ()

        # Sometimes the CSV contains 'nan' as string
        if isinstance(value, str) and value.lower() == 'nan':
            return ()

        try:
            parsed = json.loads(value)
        except json.JSONDecodeError:
            # If JSON parsing fails, treat as a single string
            return (value,) if isinstance(value, str) else ()

        if isinstance(parsed, list):
            return tuple(parsed)
        return (parsed,)

    for _, row in schema_group.iterrows():
        colname = row["column_name"]
        subfield_path = get_path(row["subfield_path"])
        match row["var_type"]:
            case "skip":
                continue
            case "static":
                entry.static_fields[colname] = subfield_path
            case "list":
                list_path = get_path(row["list_path"])
                entry.list_blocks.setdefault(list_path, {})[colname] = subfield_path
            case _:
                raise ValueError(f"Unknown var_type: {row['var_type']}")
    return entry


def extract_entries_from_csv(infile: Path) -> Iterable[Entry]:
    schema_df = pd.read_csv(infile)
    schema_df.columns = schema_df.columns.str.strip()
    schema_df["table_id"] = schema_df["id"].str.split(":").str[0]

    for table_id, group in schema_df.groupby("table_id"):
        assert isinstance(table_id, str)
        if "variable" not in group:
            filename = None
        else:
            print(table_id, set(group["variable"]))
            (filename,) = set(group["variable"])
        yield extract_entry(filename, table_id, group)


# %%
BASE_PATH = Path.cwd() / "structure_donations" / "Processed_structure_donations"
infiles = dict(
    TIKTOK=BASE_PATH / "TikTok/Final/TT_Merged_structures.csv",
    X=BASE_PATH / "Twitter/Final/X_Merged_structures.csv",
    IG=BASE_PATH / "Instagram/Final/IG_Merged_structures.csv",
    FB=BASE_PATH / "Facebook/Final/FB_Merged_structures.csv",
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
