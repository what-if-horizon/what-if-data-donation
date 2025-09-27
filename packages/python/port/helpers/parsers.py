import json
import logging
from typing import Annotated, Iterable, NamedTuple, TypeAlias

import pandas as pd
from port.helpers.readers import read_js, read_json

Columns: TypeAlias = Annotated[
    dict[str, tuple[str, ...]],
    "A collection of columns, where each columns maps a column name to a json path to find the values for that column",
]


class Entry(NamedTuple):
    table: Annotated[str, "ID of the table to generate"]
    filename: Annotated[str | None, "Filename from which to get information (or None for single-file donations)"]
    static_fields: Annotated[
        Columns,
        "A list of paths within the file that each gives a single values for each file."
        "Will be repeated in the resulting table if needed",
    ]
    list_blocks: Annotated[
        dict[tuple[str, ...], Columns],
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


def find_entries(d: dict, keys: tuple[str, ...]) -> Iterable[dict]:
    """Recursively traverse the json dictionary d with the keys, yielding the entries
    if there are no keys, return d
    If d is a dict, find the first key and recurse
    if it is a list, iterate over the list and recurse
    """
    print(f"**** get_in(d, keys={keys}) ****")
    print("d:", json.dumps(d, indent=2))
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
        # We were looking for a list, but found a scalar. What to do?
        raise ValueError(f"Find_entries value for {first_key} was {repr(e)}, expected a list or dict")


def get_list(d: dict, *keys):
    val = get_in(d, *keys)
    return val if isinstance(val, list) else []


def read_file(file_input: list[str], filename: str | None, search_subfolders=False):
    """Read the entry file from the input files"""
    if not filename:
        with open(file_input[0], "r", encoding="utf-8") as f:
            return [json.load(f)]
    # Read js or json file as required
    filenames = [("*/" if search_subfolders else "/") + str(filename)]
    if filename.endswith(".js"):
        return read_js(file_input, filenames)
    else:
        return read_json(file_input, filenames)


def create_entry_df(
    file_input: list[str], entry: Entry, json_root: str | None = None, search_subfolders=False
) -> pd.DataFrame | None:
    try:
        data = read_file(file_input, entry.filename, search_subfolders=search_subfolders)
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
            for row in resolve_list_block(item, list_path, columns):
                combined_row = base_row.copy() | row
                all_records.append(combined_row)
    return pd.DataFrame(all_records)


def resolve_list_block(item, list_path: tuple[str, ...], columns: Columns):
    for element in find_entries(item, list_path):
        row = dict(__source_list__=list_path[-1])
        for colname, path in sorted(columns.items()):
            row[colname] = get_in(element, *path)
        yield row


def create_table(
    file_input: list[str], entries: list[Entry], json_root: str | None = None, search_subfolders=False
) -> pd.DataFrame:
    tables = [
        create_entry_df(file_input, entry, json_root=json_root, search_subfolders=search_subfolders)
        for entry in entries
    ]
    tables = [t for t in tables if t is not None]
    if tables:
        result = pd.concat(tables, ignore_index=True)
        if len(tables) == 1 and not result.empty:
            result.drop("file", axis=1, inplace=True)
        return result
    else:
        return pd.DataFrame()
