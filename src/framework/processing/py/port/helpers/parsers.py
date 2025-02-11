import pandas as pd
from jsonpath_ng import jsonpath, parse
from typing import Any
import logging
import argparse

import port.api.props as props

logger = logging.getLogger(__name__)

type JSON = dict[Any, Any] | list[Any]
type Translatable = dict[str, str]

def extract_rows_from_json(json: JSON, row_path: list[str]) -> JSON:
    for rp in row_path:
        row_expr = parse(rp)
        match = row_expr.find(json)
        if match:
            return match[0].value
    return []

def extract_columns_from_json(row: dict[str, Any], col_paths: dict[str, list[str]]) -> dict[str, Any]:
    columns = {}
    for col, cp in col_paths.items():
        for c in cp:
            col_expr = parse(c)
            value = col_expr.find(row)
            if value:
                columns[col] = value[0].value
                break
    return columns


def parse_json(json: JSON,
               row_path: list[str],
               col_paths: dict[str, list[str]]):
    """
    Parses a JSON file from a zip archive and extracts data into a DataFrame.

    This function reads a JSON file from a zip archive, extracts rows based on
    JSONPath expressions, and then extracts columns from those rows based on
    additional JSONPath expressions. The extracted data is returned as a pandas
    DataFrame.

    Parameters:
    zip (str): Path to the zip archive.
    filename (list[str]): List of possible filenames to read from the zip archive.
    row_path (list[str]): List of JSONPath expressions to extract rows.
    col_paths (dict[str, list[str]]): Dictionary of column names and JSONPath expressions
                                      to extract column values from each row.

    Returns:
    pd.DataFrame: DataFrame containing the extracted data.
    """

    try:
        rows = extract_rows_from_json(json, row_path)
        row_data = [extract_columns_from_json(row, col_paths) for row in rows]
        return pd.DataFrame.from_records(row_data)

    except Exception as e:
        logger.error("exception caught: %s", e)

    return pd.DataFrame()
