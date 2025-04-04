#==================================================================================================================
# Imports from other scripts
#==================================================================================================================
from port.helpers.donation_flow import donation_table, donation_flow
from port.helpers.parsers import parse_json
from port.helpers.readers import read_json

#==================================================================================================================
# Imports from Pyodide
#==================================================================================================================
import pandas as pd
import json

import io
import re
import zipfile
import os
import logging
import requests
from io import StringIO

import pyodide.http
#==================================================================================================================
# Logeer
#==================================================================================================================
logger = logging.getLogger(__name__)

#==================================================================================================================
# Import Schema data
#==================================================================================================================
async def load_csv_from_github(url):
    response = await pyodide.http.pyfetch(url)
    csv_data = await response.text()
    
    # Convert CSV to DataFrame
    from io import StringIO
    df = pd.read_csv(StringIO(csv_data))
    return df


url = "https://raw.githubusercontent.com/what-if-horizon/what-if-data-donation/refs/heads/master/json_structure_donations/schema.csv"
schema_df = await load_csv_from_github(url)

schema_df.columns = schema_df.columns.str.replace(r'\(.*\)', '', regex=True)
schema_df.columns = schema_df.columns.str.strip()

#==================================================================================================================
# Reader
#==================================================================================================================
def bytesio_to_listdict(bytes_to_read: io.BytesIO) -> list[dict]:
    """
    Converts a io.BytesIO buffer containing a .js file into a list of dicts.

    This function removes unnecessary JS syntax and parses the content as JSON.
    """

    out = []
    lines = []

    try:
        with io.TextIOWrapper(bytes_to_read, encoding="utf8") as f:
            lines = f.readlines()

        # Remove any JS variable assignment (e.g., `window.YTD.account.part0 =`)
        lines[0] = re.sub(r"^.*? = ", "", lines[0])

        # Convert to JSON
        out = json.loads("".join(lines))

    except json.decoder.JSONDecodeError as e:
        logger.error("Invalid JSON format in file: %s", e)
    except IndexError as e:
        logger.error("File appears empty: %s", e)
    except Exception as e:
        logger.error("Unexpected error: %s", e)

    return out

#==================================================================================================================
# Parser
#==================================================================================================================
def extract_and_parse_json(zip_path: str, target_file: str) -> list[dict]:
    """
    Extracts and parses a .json file inside a ZIP archive.

    Args:
        zip_path (str): Path to the ZIP archive.
        target_file (str): The .json file to extract.

    Returns:
        list[dict]: Parsed JSON data.
    """

    with zipfile.ZipFile(zip_path, "r") as z:
        # Find JSON files that contain the expected filename
        json_files = [f for f in z.namelist() if target_file in f and f.endswith('.json')]

        if not json_files:
            logger.error(f"No matching file for '{target_file}' found in {zip_path}")
            return []

        # Extract and parse the first matching file
        with z.open(json_files[0]) as f:
            try:
                return json.load(io.TextIOWrapper(f, encoding="utf-8"))
            except json.JSONDecodeError as e:
                logger.error(f"Failed to parse JSON: {e}")
                return []
        
#==================================================================================================================
# Function to generate the functions for each table
#==================================================================================================================
def generate_extraction_functions(schema_df):
    """Dynamically creates a function for each JSON file based on the schema."""
    
    function_dict = {}

    for file_name in schema_df["level01"].dropna().unique():
        # Define the extraction function for each JSON file based on the schema
        def file_extraction_func(file_input: str, file_name=file_name):
            """Extracts data from a ZIP file and converts it into a DataFrame."""

            # Ensure file_input is a valid ZIP file
            if isinstance(file_input, list) and len(file_input) > 0:
                file_input = file_input[0]  # Extract the first ZIP file from the list

            if not isinstance(file_input, str) or not file_input.endswith(".zip"):
                logger.error(f"Invalid file input: {file_input}. Expected a ZIP file.")
                return pd.DataFrame()

            try:
                with zipfile.ZipFile(file_input, "r") as zip_ref:
                    zip_file_list = zip_ref.namelist()  # List of all files inside the ZIP
                    # print("DEBUG: Files inside ZIP ->", zip_file_list)  # Debugging log

                    # Dynamically find the JSON file that matches `file_name`
                    matched_files = [f for f in zip_file_list if file_name in f and f.endswith('.json')]

                    if not matched_files:
                        logger.error(f"No matching file found for {file_name} in ZIP contents.")
                        return pd.DataFrame()

                    # Extract and process the first matched file
                    json_file = matched_files[0]
                    data = extract_and_parse_json(file_input, json_file)
                    
                    return pd.DataFrame() if not data else pd.json_normalize(data)

            except zipfile.BadZipFile:
                logger.error("Uploaded file is not a valid ZIP archive.")
                return pd.DataFrame()
            except Exception as e:
                logger.error(f"Error processing ZIP file: {e}")
                return pd.DataFrame()

        # Store the function dynamically
        function_dict[file_name] = file_extraction_func 
    
    return function_dict

#==================================================================================================================
# Generate functions using the existing schema
#==================================================================================================================
extraction_functions = generate_extraction_functions(schema_df)
#print(extraction_functions)

#==================================================================================================================
# Generate donation flow
#==================================================================================================================
def create_donation_flow(file_input: list[str]):
    """Creates a donation flow dynamically using extracted data from multiple .json files."""
    

    tables = []
    
    for file_name, extract_func in extraction_functions.items():
        df = extract_func(file_input)
        if not df.empty:
            tables.append(
                donation_table(
                    name=file_name.capitalize(),
                    df=df,
                    title={"en": file_name.capitalize()}
                )
            )

    return donation_flow(
        id="Instagram",
        tables=tables
    )

