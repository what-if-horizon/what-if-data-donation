# %%
# Imports
# Note: to make sure vscode finds the port package, install with
#       pip install -e .[dev]

import argparse
import json
from copy import deepcopy
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
        # Deal with .-separated paths
        if "[" not in value:
            return tuple(value.split("."))
        # Convert ' into " (workaround for #86)
        value = value.replace("'", '"')
        value = json.loads(value)
        if isinstance(value, list):
            return tuple(value)
        assert isinstance(value, tuple)
        return value

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


def extract_entries_from_csv(infile: Path, platform: str) -> Iterable[Entry]:
    # Columns used by the extraction
    # keepID - (only) used as a filter
    # file_path - which file to find in the zip (for all formats except TT, which is a single file)
    # table_name - name of the resulting table. For now, derive from json_name if not given
    # var_type - is this a static field or a list
    # list_path - for list fields, the location of a list in the json, where each element will yield a table row
    # subfield_path - identifier of the column to extract
    # column_name - name of the resulting column

    def tablename(json_name):
        return json_name.replace(".json", "").replace(".js", "").replace("_", " ").title()

    def tablename_from_id(id):
        return tablename(id.split(":")[0])

    schema_df = pd.read_csv(infile)
    schema_df.columns = schema_df.columns.str.strip()
    schema_df = schema_df[(schema_df["keepID"].notna()) & (schema_df["keepID"] != "")]

    if "file_path" not in schema_df:
        if "variable" in schema_df:
            schema_df.rename(columns={"variable": "file_path"}, inplace=True)  # Temporary measure for X
        else:
            schema_df["file_path"] = ""  # For TT
    if "table_name" not in schema_df:
        # Remporary measure until table names are properly integrated
        if platform == "TIKTOK":
            schema_df["table_name"] = schema_df["id"].map(tablename_from_id)
        else:
            schema_df["table_name"] = schema_df["json_name"].map(tablename)

    for table_name, table_rows in schema_df.groupby("table_name"):
        for file_path, group in table_rows.groupby("file_path"):
            assert isinstance(table_name, str)
            assert isinstance(file_path, str)
            if platform == "TIKTOK":
                file_path = None
            yield extract_entry(file_path, table_name, group)


def extract_entries_as_dict(infile: Path, platform: str) -> dict[str, list[Entry]]:
    result: dict[str, list[Entry]] = {}
    for e in extract_entries_from_csv(infile, platform=platform):
        result.setdefault(e.table, []).append(e)

    new_result: dict[str, list[Entry]] = {}
    for table, entries in result.items():
        merged = [merge_listblocks(e) for e in entries]
        if any(x != y for (x, y) in zip(entries, merged)):
            new_result[f"{table} (Original)"] = entries
            new_result[f"{table} (Merged)"] = [merge_listblocks(e) for e in entries]
        else:
            new_result[f"{table} (Unchanged)"] = entries

    return new_result


def merge_listblocks(entry: Entry):
    result = deepcopy(entry)
    for list_path, columns in entry.list_blocks.items():
        # is there a list_block whose path is a prefix of this block?
        for i in range(1, len(list_path)):
            prefix, suffix = list_path[:i], list_path[i:]
            if prefix in result.list_blocks:
                # Yes, so we can merge with that list_block
                target = result.list_blocks[prefix]
                # Merge by append the remainder of the list_path to the column_paths
                # and adding to the target list_block
                for colname, colpath in columns.items():
                    if colname in target.keys():
                        colname = ".".join(suffix + (colname,))
                    target[colname] = suffix + colpath
                # we can now drop this list block
                del result.list_blocks[list_path]
                break
    if entry.list_blocks != result.list_blocks:

        def pprint(list_blocks: dict[tuple[str, ...], dict[str, tuple[str, ...]]]):
            lines = []
            for list_path, columns in list_blocks.items():
                columns = ", ".join(f"{colname}: [{'::'.join(colpath)}]" for colname, colpath in columns.items())
                lines.append(f" - list_path: [{'::'.join(list_path)}], column(s): {columns}")
            return "\n".join(lines)

        print(f"## [{entry.table}] Merged list blocks ##")
        print(f"Original:\n{pprint(entry.list_blocks)}")
        print(f"Merged:\n{pprint(result.list_blocks)} \n")
    return result


# %%
BASE_PATH = Path.cwd() / "structure_donations" / "Annotated_schema_df"
infiles = dict(
    TIKTOK=BASE_PATH / "TT_merged_structure_annotated.csv",
    X=BASE_PATH / "X_merged_structure_annotated.csv",
    IG=BASE_PATH / "IG_merged_structure_annotated.csv",
    FB=BASE_PATH / "FB_merged_structure_annotated.csv",
)


def write_entries_dict(outfile):
    lines = []
    lines.append(f'"""\n{DOCSTRING.strip()}\n"""\n\n')
    lines.append("from port.helpers.parsers import Entry\n\n")

    for name, infile in infiles.items():
        lines.append(f"{name}_ENTRIES: dict[str, list[Entry]] = {{\n")
        all_entries = extract_entries_as_dict(infile, platform=name)
        for table, entries in all_entries.items():
            lines.append(f"    {repr(table)}: [\n")
            for entry in entries:
                lines.append(f"        {repr(entry)},\n")
            lines.append("    ],\n")
        lines.append("}\n\n")

    print(f"Writing output to {outfile}")
    with open(outfile, "w") as f:
        f.writelines(lines)


# Generate entries data file
if __name__ == "__main__":
    write_entries_dict(outfile="packages/python/port/helpers/entries_data.py")
