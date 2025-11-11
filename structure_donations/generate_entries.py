# %%
# Imports
# Note: to make sure vscode finds the port package, install with
#       pip install -e .[dev]

import argparse
import json
import math
from pathlib import Path
from typing import Iterable, Literal, NamedTuple

import numpy as np
import pandas as pd
from port.helpers.parsers import Entry, JsonPath, Node  # type: ignore

DOCSTRING = """
Donation file structure data for takeout flows

This file contains a list of Entries for each platform.
Each Entry represents a table to be generated from the appropriate file.

To generate this file, please run structure/flow_generation/generate_entries.py
which will use the Merged_structures_*.csv to determine the required entries.
"""


class FieldSpec(NamedTuple):
    column_name: str
    var_type: Literal["skip", "static", "list"]
    subfield_path: JsonPath
    list_path: JsonPath

    @classmethod
    def from_row(cls, row):
        def get_path(value):
            if pd.isna(value) or value is None or value == "":
                return tuple()
            value = str(value)
            if "[" not in value:
                return tuple(value.split("."))
            value = value.replace("'", '"')
            value = json.loads(value)
            if isinstance(value, list):
                return tuple(value)
            assert isinstance(value, tuple)
            return value

        assert row["var_type"] in ["skip", "static", "list"]
        return FieldSpec(
            column_name=row["column_name"],
            var_type=row["var_type"],
            subfield_path=get_path(row["subfield_path"]),
            list_path=get_path(row["list_path"]),
        )


def extract_entry(filename: str | None, table: str, fields: list[FieldSpec]) -> Entry:
    """Generate an Entry for a group of rows from the structure csv file"""
    entry = Entry(filename=filename, table=table, tree=Node.empty(), static_fields={})

    for field in fields:
        colname = field.column_name
        match field.var_type:
            case "skip":
                continue
            case "static":
                entry.static_fields[colname] = field.subfield_path
            case "list":
                # SAFEGUARD: only check when list_path is not empty
                if field.list_path:
                    # WvA: I think the next check also catches this, and it is never triggered, so we can remove it?
                    # Skip self-referential definitions
                    # if field.subfield_path and field.subfield_path == (field.list_path[-1],):
                    #    print(
                    #        f":warning: Skipping self-referential path in {table}: list_path={field.list_path}, subfield_path={field.subfield_path}, col={colname}"
                    #    )
                    #    raise Exception("!")
                    #    continue
                    # Check for redundant nested patterns like ('media', 'media')
                    if field.list_path[-1] in field.subfield_path:
                        raise ValueError(
                            f"Redundant nested path in {table}: list_path={field.list_path}, subfield_path={field.subfield_path}, col={colname}"
                        )
                current = entry.tree
                for path in field.list_path:
                    current = current.children.setdefault(path, Node.empty())
                current.columns[colname] = field.subfield_path
            case _:
                raise ValueError(f"Unknown var_type: {field.var_type}")
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
    print("!!!", infile)
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

        if platform == "TIKTOK":
            fields = [FieldSpec.from_row(row) for _, row in table_rows.iterrows()]
            # Treat all TikTok rows as a single file group
            yield extract_entry(None, str(table_name), fields)
        else:
            for file_path, group in table_rows.groupby("file_path"):
                fields = [FieldSpec.from_row(row) for _, row in group.iterrows()]
                yield extract_entry(str(file_path), str(table_name), fields)


def extract_entries_as_dict(infile: Path, platform: str) -> dict[str, list[Entry]]:
    result: dict[str, list[Entry]] = {}
    for e in extract_entries_from_csv(infile, platform=platform):
        result.setdefault(e.table, []).append(e)
    return result


# --- Functions to create CSV entries for YT
def extract_csv_entry(filename: str, table: str, schema_group: pd.DataFrame) -> Entry:
    """Generate an Entry object for CSV files (columns become static fields)."""
    entry = Entry(filename=filename, table=table, tree=Node.empty(), static_fields={})
    for _, row in schema_group.iterrows():
        colname = row["Column_names"]
        entry.static_fields[colname] = (colname,)
    return entry


def extract_csv_entries(schema_file: Path) -> Iterable[Entry]:
    """Generate Entry objects from CSV schema."""
    df = pd.read_csv(schema_file)
    df.columns = df.columns.str.strip()
    df = df[df["keepID"].notna() & (df["keepID"] != "")]
    df["table_name"] = df["id"].apply(lambda x: x.split(":")[0])

    for table_name, table_rows in df.groupby("table_name"):
        for file_name, group in table_rows.groupby("File_name"):
            yield extract_csv_entry(str(file_name), str(table_name), group)


def csv_entries_as_dict(schema_file: Path) -> dict[str, list[Entry]]:
    """Return dictionary table_name -> list[Entry] objects for CSV files."""
    result: dict[str, list[Entry]] = {}
    for e in extract_csv_entries(schema_file):
        result.setdefault(e.table, []).append(e)
    return result


# ---

# %%
BASE_PATH = Path.cwd() / "structure_donations" / "Annotated_Merged_Structures"
infiles = dict(
    # TIKTOK=BASE_PATH / "TT_merged_structure_annotated.csv",
    # X=BASE_PATH / "X_merged_structure_annotated.csv",
    # IG=BASE_PATH / "IG_merged_structure_annotated.csv",
    FB=BASE_PATH / "FB_merged_structure_annotated.csv",
    # YT=BASE_PATH / "YT_merged_structure_annotated.csv",
)


def write_entries_dict(outfile):
    lines = []
    lines.append(f'"""\n{DOCSTRING.strip()}\n"""\n\n')
    lines.append("from port.helpers.parsers import Entry, Node\n\n")

    for name, infile in infiles.items():
        lines.append(f"{name}_ENTRIES: dict[str, list[Entry]] = {{\n")
        all_entries = extract_entries_as_dict(infile, platform=name)
        for table, entries in all_entries.items():
            lines.append(f"    {repr(table)}: [\n")
            for entry in entries:
                lines.append(f"        {repr(entry)},\n")
            lines.append("    ],\n")
        lines.append("}\n\n")

    CSV_SCHEMA = BASE_PATH / "YT_merged_column_names_annotated.csv"
    csv_entries = {}  # csv_entries_as_dict(CSV_SCHEMA)

    lines.append("YT_CSV_ENTRIES: dict[str, list[Entry]] = {\n")
    for table, entries in csv_entries.items():
        lines.append(f"    {repr(table)}: [\n")
        for entry in entries:
            lines.append(f"        {repr(entry)},\n")
        lines.append("    ],\n")
    lines.append("}\n")

    print(f"Writing output to {outfile}")
    with open(outfile, "w") as f:
        f.writelines(lines)


# Generate entries data file
if __name__ == "__main__":
    write_entries_dict(outfile="packages/python/port/helpers/entries_data.py")
