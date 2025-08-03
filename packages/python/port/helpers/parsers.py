import json
from typing import Annotated, NamedTuple, TypeAlias

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


def get_list(d: dict, *keys):
    val = get_in(d, *keys)
    return val if isinstance(val, list) else []


def create_entry_df(file_input: list[str], entry: Entry, json_root: str | None = None) -> pd.DataFrame:
    if entry.filename:
        if entry.filename.endswith(".js"):
            data = read_js(file_input, ["/" + entry.filename])
        else:
            data = read_json(file_input, ["/" + str(entry.filename)])
    else:
        with open(file_input[0], "r", encoding="utf-8") as f:
            data = [json.load(f)]
    if json_root:
        data = [d[json_root] for d in data]
    all_records = []
    for item in data:
        base_row = {}
        for colname, path in entry.static_fields.items():
            base_row[colname] = get_in(item, *path)
        if not entry.list_blocks:
            # WvA: Should we not also return base_row if no entries found for list_blocks?
            all_records.append(base_row)
            continue

        for list_path, columns in entry.list_blocks.items():
            items = get_list(item, *list_path)
            for item in items:
                row = base_row.copy()
                row["__source_list__"] = list_path[-1]
                for colname, path in sorted(columns.items()):
                    row[colname] = get_in(item, *path)
                all_records.append(row)
    return pd.DataFrame(all_records)
