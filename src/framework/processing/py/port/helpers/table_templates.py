import io
import pandas as pd
from jsonpath_ng import jsonpath, parse
from typing import Any
import zipfile
import logging
import argparse

import port.api.props as props
import port.helpers.extraction_helpers as eh

logger = logging.getLogger(__name__)

type JSON = dict[Any, Any] | list[Any]
type Translatable = dict[str, str]

def read_json(zip: str, filename_options: list[str]) -> JSON:
    for filename in filename_options:
        contents = eh.extract_file_from_zip(zip, filename)
        if contents:
            return eh.read_json_from_bytes(contents)
    return {}

def extract_rows_from_json(json: JSON, row_path: list[str]) -> JSON:
    for rp in row_path:
        row_expr = parse(rp)
        match = row_expr.find(json)
        if match:
            return [m.value for m in match]
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


def parse_json(zip: str, filename: list[str], row_path: list[str], col_paths: dict[str, list[str]]):
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
    json = read_json(zip, filename)

    try:
        rows = extract_rows_from_json(json, row_path)
        row_data = [extract_columns_from_json(row, col_paths) for row in rows]
        return pd.DataFrame.from_records(row_data)

    except Exception as e:
        logger.error("exception caught: %s", e)

    return pd.DataFrame()


def create_table(
    name: str,
    title: props.Translations,
    df: pd.DataFrame,
    description: props.Translations | None = None,
    visualizations: list | None = None
    ):
    return props.PropsUIPromptConsentFormTable(
        name,
        title = props.Translatable(title),
        data_frame = df,
        description = props.Translatable(description) if description else None,
        visualizations = visualizations
    )



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process JSON data from a zip archive.")
    parser.add_argument("zip", type=str, help="Path to the zip archive.")
    args = parser.parse_args()

    df = parse_json(
        args.zip,
        filename=["example.json"],
        row_path=["$.data", "$.gegevens"],
        col_paths={
            "name": ["$.name", "$.naam"],
            "age": ["$.age", "$.leeftijd"],
            "date": ["$.timestamp"]
        })

    # PANDAS DATA PROCESSING
    df["date"] = pd.to_datetime(df["date"], unit="s")
    df = df.sort_values("date")

    create_table("example",
        title = { "en": "Example", "nl": "Voorbeeld" },
        df = df
    )
