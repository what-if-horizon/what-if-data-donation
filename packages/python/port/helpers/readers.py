import fnmatch
import io
import json
import logging
import re
import time
import zipfile
from typing import Any

import pandas as pd
from jsonpath_ng import jsonpath, parse

logger = logging.getLogger(__name__)

JSON = dict[Any, Any] | list[Any]
Translatable = dict[str, str]


def match_filename(file_paths: list[str], lookup: list[str]):
    for file_path in file_paths:
        for lookup_str in lookup:
            if fnmatch.fnmatch(file_path, lookup_str):
                return file_path
    return None


def find_file_in_zip(zip_filepath: str, file_paths: list[str]):
    with zipfile.ZipFile(zip_filepath, "r") as zip_ref:
        match = match_filename(zip_ref.namelist(), file_paths)
        if match is None:
            return None
        with zip_ref.open(match) as file:
            file_content = file.read()
            return file_content


def read_binary(file_input: list[str], file_paths: list[str]):
    """
    Reads a binary file from a list of file paths.

    Parameters:
    file_input (list[str]): List of file paths to search for the binary file.
    file_paths (list[str]): List of possible file paths to read from.

    Returns:
    bytes: Binary content of the file.

    Raises:
    ValueError: If no file is found with the provided paths.
    """

    match = match_filename(file_input, file_paths)
    if match is not None:
        with open(match, "rb") as file:
            return file.read()
    for filename in file_input:
        type = filename.split(".")[-1]
        if type == "zip":
            file_content = find_file_in_zip(filename, file_paths)
            if file_content is not None:
                return file_content

    raise ValueError("No file found with paths: " + str(file_paths))


def read_text(file_input: list[str], file_paths: list[str], encoding: str = "utf-8") -> str:
    """
    Reads a text file from a list of file paths.

    Parameters:
    file_input (list[str]): List of file paths to search for the text file.
    file_paths (list[str]): List of possible file paths to read from.
    encoding (str): Encoding to use for decoding the binary content. Default is 'utf-8'.

    Returns:
    str: Decoded text content.

    Raises:
    ValueError: If no file is found with the provided paths or if the binary content cannot be decoded.
    """
    bin = read_binary(file_input, file_paths)
    try:
        return bin.decode(encoding)
    except:
        raise ValueError("Could not decode binary file to text with encoding: " + encoding)


def read_json(file_input: list[str], file_paths: list[str]) -> JSON:
    """
    Reads a JSON file from a list of file paths.

    Parameters:
    file_input (list[str]): List of file paths to search for the JSON file.
    file_paths (list[str]): List of possible file paths to read from.

    Returns:
    JSON: Parsed JSON object.

    Raises:
    ValueError: If no file is found with the provided paths or if the file content cannot be decoded.
    """
    t = time.time()
    text_content = read_text(file_input, file_paths)
    result = json.loads(text_content)
    print(f"Parsed {file_paths} in {time.time() - t:1.2f}s")
    return result


def read_csv(file_input: list[str], file_paths: list[str], encoding: str = "utf-8", **kwargs) -> pd.DataFrame:
    """
    Reads a CSV file from a list of file paths.

    Parameters:
    file_input (list[str]): List of file paths to search for the CSV file.
    file_paths (list[str]): List of possible file paths to read from.
    encoding (str): Encoding to use for reading the text content. Default is 'utf-8'.
    **kwargs: Additional keyword arguments to pass to `pd.read_csv`.

    Returns:
    pd.DataFrame: DataFrame containing the parsed CSV data.

    Raises:
    ValueError: If no file is found with the provided paths or if the file content cannot be decoded.
    """
    bin_content = read_binary(file_input, file_paths)
    bin_io = io.BytesIO(bin_content)
    return pd.read_csv(bin_io, **kwargs)


def read_js(file_input: list[str], target_files: list[str]) -> list[dict]:
    extracted_data = []
    for zip_path in file_input:
        with zipfile.ZipFile(zip_path, "r") as z:
            for target_file in target_files:
                js_files = [f for f in z.namelist() if target_file in f]
                if js_files:
                    with z.open(js_files[0]) as raw_file:
                        with io.TextIOWrapper(raw_file, encoding="utf8") as text_file:
                            lines = text_file.readlines()
                        lines[0] = re.sub(r"^.*? = ", "", lines[0])
                        try:
                            data = json.loads("".join(lines))

                            if isinstance(data, list):
                                extracted_data.extend(data)
                            else:
                                extracted_data.append(data)

                        except json.JSONDecodeError as e:
                            logger.error(f"Error decoding {target_file} in {zip_path}: {e}")
    return extracted_data
