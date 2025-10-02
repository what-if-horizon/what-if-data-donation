import itertools
import json
import logging
import os
import zipfile
from typing import Annotated, Iterable, NamedTuple, TypeAlias

import pandas as pd
from port.helpers.readers import read_csv, read_js, read_json

JsonPath: TypeAlias = Annotated[tuple[str, ...], "A tuple correspondiong to a json path to find values"]

Columns: TypeAlias = Annotated[
    dict[str, JsonPath],
    "A collection of columns, where each columns maps a column name to a json path to find the values for that column",
]


class Entry(NamedTuple):
    table: Annotated[str, "ID of the table to generate"]
    filename: Annotated[
        str | None,
        "Filename from which to get information (or None for single-file donations)",
    ]
    static_fields: Annotated[
        Columns,
        "A list of paths within the file that each gives a single values for each file."
        "Will be repeated in the resulting table if needed",
    ]
    list_blocks: Annotated[
        dict[JsonPath, Columns],
        "A dict of rowpath: columns items that define a list of objects and the element to extract from each object"
        "This will result in one row for each entry in the list, and one column for each item in the values",
    ]


def get_in(d: dict, *keys):
    for key in keys:
        if isinstance(d, dict):
            d = d.get(key)
        else:
            return None
    return d


def find_entries(d: dict, keys: JsonPath) -> Iterable[dict]:
    """Recursively traverse the json dictionary d with the keys, yielding the entries
    if there are no keys, return d
    If d is a dict, find the first key and recurse
    if it is a list, iterate over the list and recurse
    """
    if not keys:
        yield d
        return
    # Just like in the prolog days!
    first_key, remaining_keys = keys[0], keys[1:]
    if not (e := d.get(first_key)):
        return
    if isinstance(e, dict):
        yield from find_entries(e, remaining_keys)
    elif isinstance(e, list):
        for element in e:
            yield from find_entries(element, remaining_keys)
    else:
        yield e


def get_list(d: dict, *keys):
    val = get_in(d, *keys)
    return val if isinstance(val, list) else []


def read_file(file_input: list[str], filename: str | None):
    """Read the entry file from the input files"""

    print(file_input)

    if not filename:
        with open(file_input[0], "r", encoding="utf-8") as f:
            return [json.load(f)]

    # Always allow both root and recursive matches
    filenames = [filename, f"*/{filename}", f"{filename}"]  # root  # one folder deep

    if filename.endswith(".js"):
        return read_js(file_input, filenames)
    else:
        return read_json(file_input, filenames)


def create_entry_df(file_input: list[str], entry: Entry, json_root: str | None = None) -> pd.DataFrame | None:
    try:
        data = read_file(file_input, entry.filename)
    except FileNotFoundError as e:
        logging.error(f"{entry.table}: Cannot find file {entry.filename} ({e})")
        return None
    if json_root:
        data = [d[json_root] for d in data]
    all_records = []
    if isinstance(data, dict):
        data = [data]
    for item in data:
        base_row = {"file": entry.filename}
        for colname, path in entry.static_fields.items():
            base_row[colname] = get_in(item, *path)
        if not entry.list_blocks:
            all_records.append(base_row)
            continue
        for list_path, columns in entry.list_blocks.items():
            print(f"list_path: {list_path}\nitem: {item}\ncolumns:{columns}")
            for row in resolve_list_block(item, list_path, columns):
                combined_row = base_row.copy() | row
                all_records.append(combined_row)
    return pd.DataFrame(all_records)


list_block = {
    "label": ("label",),
    "ent_field_name": ("ent_field_name",),
    "dict.label": ("dict", "label"),
    "value": ("dict", "value"),
}


def extract_columns(element, columns: Columns) -> Iterable[dict]:
    # First, create 'base rows' for all leaf nodes, i.e. columns without a path of length one
    # Separate columns by path_prefix
    leaf_columns = {colname: path for (colname, path) in columns.items() if len(path) == 1}
    values = {colname: list(find_entries(element, leaf_columns[colname])) for colname in leaf_columns}
    # Drop empty values
    values = {k: v for (k, v) in values.items() if v}
    # Leaf rows are the product of all (non-empty) values --> single row if all values are scalar
    leaf_rows = [dict(zip(values.keys(), sublist)) for sublist in itertools.product(*values.values())]

    # Now, find out all unique prefixes for columns with a longer path
    columns_by_prefix: dict[JsonPath, Columns] = {}  # {prefix: Columns}
    for colname, path in columns.items():
        if len(path) > 1:
            columns_by_prefix.setdefault(path[:1], {})[colname] = path[1:]
    # Iterate over all prefixes
    yielded_children = False
    for prefix, columns in columns_by_prefix.items():
        # Find all elements correspondiong to the prefix
        for child in find_entries(element, prefix):
            # Recursively extract columns for that prefix
            # and yield all combinations of leaf rows and child rows
            for child_row in extract_columns(child, columns):
                yielded_children = True
                yield from (leaf_row | child_row for leaf_row in leaf_rows)

    # If we never yield any children, just yield the leaf_rows
    if not yielded_children:
        yield from leaf_rows


def resolve_list_block(item, list_path: tuple[str, ...], columns: Columns):
    if not list_path:
        return  # Nothing to iterate
    for element in find_entries(item, list_path):
        base_row = dict(__source_list__=list_path[-1])

        for row in extract_columns(element, columns):
            yield base_row | row


def create_table(file_input: list[str], entries: list[Entry], json_root: str | None = None) -> pd.DataFrame:
    tables = [create_entry_df(file_input, entry, json_root=json_root) for entry in entries]
    tables = [t for t in tables if t is not None]
    if tables:
        result = pd.concat(tables, ignore_index=True)
        if len(tables) == 1 and not result.empty:
            result.drop("file", axis=1, inplace=True)
        return result
    else:
        return pd.DataFrame()


# --- Preparing parser for Youtube csv ---
def read_csv_from_file_input(file_input: list[str], csv_filename: str) -> pd.DataFrame:
    """
    Reads a CSV file from a zip inside file_input.

    Args:
        file_input (list[str]): List of file paths, including the zip file.
        csv_filename (str): Name of the CSV file inside the zip.

    Returns:
        pd.DataFrame: The loaded DataFrame.
    """
    filenames = [csv_filename, f"*/{csv_filename}", f"{csv_filename}"]  # root  # one folder deep

    for path in file_input:
        if path.endswith(".zip"):
            with zipfile.ZipFile(path, "r") as zip_ref:
                for name in zip_ref.namelist():
                    if name.endswith(tuple(filenames)):
                        with zip_ref.open(name) as f:
                            try:
                                return pd.read_csv(f, encoding="utf-8")
                            except UnicodeDecodeError:
                                f.seek(0)
                                return pd.read_csv(f, encoding="latin1")
    raise FileNotFoundError(f"{filenames} not found in ZIP files: {file_input}")


def create_csv_table(file_input: list[str], entries: list[Entry]) -> pd.DataFrame:
    all_tables = []

    for entry in entries:
        try:
            df = read_csv_from_file_input(file_input, entry.filename)
        except FileNotFoundError:
            logging.warning(f"CSV not found: {entry.filename}")
            continue

        logging.error(f"[CSV DEBUG] Raw headers: {[repr(c) for c in df.columns]}")

        expected_columns = list(entry.static_fields.keys())

        logging.error(f"[CSV DEBUG] Raw schema: {[repr(c) for c in expected_columns]}")

        existing_columns = [col for col in expected_columns if col in df.columns]

        logging.error(f"[CSV DEBUG] Raw schema: {existing_columns}")

        df = df[existing_columns]

        logging.error(f"[CSV DEBUG] Raw schema: {df}")

        all_tables.append(df)

    if all_tables:
        return pd.concat(all_tables, ignore_index=True)
    return pd.DataFrame()
