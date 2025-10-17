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
    "A collection of columns, where each column maps a name to a json path for that value",
]


class Entry(NamedTuple):
    table: Annotated[str, "ID of the table to generate"]
    filename: Annotated[
        str | None,
        "Filename from which to get information (or None for single-file donations)",
    ]
    static_fields: Annotated[
        Columns,
        "A list of paths within the file that each gives a single value for each file."
        "Will be repeated in the resulting table if needed",
    ]
    list_blocks: Annotated[
        dict[JsonPath, Columns],
        "A dict of rowpath: columns items that define a list of objects and the elements to extract from each object."
        "This will result in one row for each entry in the list, and one column for each item in the values",
    ]


def get_in(d: dict, *keys):
    """Safely get nested dict values."""
    for key in keys:
        if isinstance(d, dict):
            d = d.get(key)
        else:
            return None
    return d


def find_entries(d: dict, keys: JsonPath) -> Iterable[dict]:
    """Recursively traverse the json dictionary `d` with the given path `keys`."""
    if not keys:
        yield d
        return

    first_key, remaining_keys = keys[0], keys[1:]
    if not isinstance(d, dict) or first_key not in d:
        return

    e = d[first_key]
    if isinstance(e, dict):
        yield from find_entries(e, remaining_keys)
    elif isinstance(e, list):
        for element in e:
            yield from find_entries(element, remaining_keys)
    else:
        # Only yield if this is a terminal value
        if not remaining_keys:
            yield e


def get_list(d: dict, *keys):
    """Return the value at the given keys if it's a list, else []."""
    val = get_in(d, *keys)
    return val if isinstance(val, list) else []


def read_file(file_input: list[str], filename: str | None):
    """Read the entry file from the input files."""
    if not filename:
        with open(file_input[0], "r", encoding="utf-8") as f:
            return [json.load(f)]

    filenames = [filename, f"*/{filename}", f"{filename}"]
    if filename.endswith(".js"):
        return read_js(file_input, filenames)
    else:
        return read_json(file_input, filenames)
        

#  --- STEP 1: Build Block Tree ---

def build_block_tree(list_blocks: dict[JsonPath, Columns]) -> dict:
    """Build a nested dictionary tree representing list_blocks, including root-level lists."""
    tree = {"columns": {}, "children": {}}
    for path, cols in list_blocks.items():
        current = tree
        for part in path:
            current = current["children"].setdefault((part,), {"columns": {}, "children": {}})
        current["columns"] = cols
    return tree


# ----------------------------------------------------------------------
#  STEP 2: Unified Recursive Extractor
# ----------------------------------------------------------------------
def extract_rows(item, block_tree, context=None, path_prefix=()):
    """
    Recursively extract rows from nested lists/dicts.
    - Produces one row per object in nested lists.
    - Preserves static fields from context.
    - Keeps empty dicts and lists as {} instead of null.
    """
    if context is None:
        context = {}
    rows = []

    base = context.copy()

    # Extract current-level columns
    local_cols = block_tree.get("columns", {})
    for colname, path in local_cols.items():
        val = get_in(item, *path)
        full_colname = ".".join(path_prefix + (colname,))

        if isinstance(val, dict):
            if val:
                # Flatten dict recursively
                for k, v in val.items():
                    base[f"{full_colname}.{k}"] = v
            else:
                base[full_colname] = {}  # empty dict
        elif isinstance(val, list):
            if val and all(isinstance(v, dict) for v in val):
                # Flatten each dict in the list
                list_rows = []
                for d in val:
                    list_rows.extend(extract_rows(d, {"columns": {}, "children": {}}, context=base, path_prefix=path_prefix + (colname,)))
                if list_rows:
                    rows.extend(list_rows)
                else:
                    # List was empty, yield base with empty object
                    base[full_colname] = [{}]
                    rows.append(base)
                continue
            elif val:
                base[full_colname] = val
            else:
                base[full_colname] = []  # empty list
        else:
            base[full_colname] = val

    # Process children recursively
    # Process children recursively
    children = block_tree.get("children", {})
    if children:
        any_child_rows = False
        for (list_name,), sub_tree in children.items():
            sub_item = get_in(item, list_name)
            if isinstance(sub_item, list):
                if sub_item:  # only if non-empty
                    for element in sub_item:
                        new_prefix = path_prefix + (list_name,)
                        sub_rows = extract_rows(element, sub_tree, context=base, path_prefix=new_prefix)
                        rows.extend(sub_rows)
                        any_child_rows = True
                else:
                    # list exists but empty — do not block parent emission
                    base[".".join(path_prefix + (list_name,))] = []
            elif isinstance(sub_item, dict):
                if sub_item:
                    new_prefix = path_prefix + (list_name,)
                    sub_rows = extract_rows(sub_item, sub_tree, context=base, path_prefix=new_prefix)
                    rows.extend(sub_rows)
                    any_child_rows = True
                else:
                    base[".".join(path_prefix + (list_name,))] = {}
        if not any_child_rows and not rows:
            rows.append(base)

    else:
        if not rows:
            rows.append(base)

    return rows


# ----------------------------------------------------------------------
#  STEP 3: Integrate into create_entry_df
# ----------------------------------------------------------------------
def create_entry_df(file_input: list[str], entry: Entry, json_root: str | None = None) -> pd.DataFrame | None:
    """Create a dataframe for a single entry."""
    try:
        data = read_file(file_input, entry.filename)
    except FileNotFoundError as e:
        logging.error(f"{entry.table}: Cannot find file {entry.filename} ({e})")
        return None

    if json_root:
        data = [d[json_root] for d in data]
    if isinstance(data, dict):
        data = [data]

    block_tree = build_block_tree(entry.list_blocks)
    all_records = []

    for item in data:
        # Gather static (file-level) fields
        base_context = {"file": entry.filename}
        for colname, path in entry.static_fields.items():
            base_context[colname] = get_in(item, *path)

        # Extract rows recursively
        if entry.list_blocks:
            for row in extract_rows(item, block_tree, context=base_context):
                all_records.append(row)
        else:
            all_records.append(base_context)

    if not all_records:
        return None
    return pd.DataFrame(all_records)


def create_table(file_input: list[str], entries: list[Entry], json_root: str | None = None) -> pd.DataFrame:
    tables = [create_entry_df(file_input, entry, json_root=json_root) for entry in entries]
    tables = [t for t in tables if t is not None]
    if not tables:
        return pd.DataFrame()

    result = pd.concat(tables, ignore_index=True)
    if len(tables) == 1 and not result.empty:
        result.drop("file", axis=1, inplace=True)
    return result



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