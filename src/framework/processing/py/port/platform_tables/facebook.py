from port.helpers.table_templates import create_table, parse_json
import port.api.props as props
from typing import Callable

import pandas as pd



def parse_table1(zip: str) -> pd.DataFrame:
    """
    For every table, you need to define a function that reads the data from the zip file
    and returns a pandas DataFrame. Where possible use the helper functions (parse_json, parse_csv, etc.)
    to standardize the data extraction process, and make it easy to add aliases for different languages
    or when DDPs change.
    """

    df = parse_json(zip,
        filename=["example.json"],
        row_path=["$.data", "$.gegevens"],
        col_paths={
            "name": ["$.name", "$.naam"],
            "age": ["$.age", "$.leeftijd"],
            "date": ["$.timestamp"]
        })

    df["date"] = pd.to_datetime(df["date"], unit="s")
    df = df.sort_values("date")

    return df



def tables(zip: str) -> list[props.PropsUIPromptConsentFormTable]:
    """
    In this function you create the tables. Make sure this function is always called "tables"

    Here we specify everything about the table EXCEPT for the data (see parse_example).
    Initially, this will just be the name and title (with translations)
    """
    example = create_table("example_name", df = parse_table1(zip),
        title = { "en": "Example", "nl": "Voorbeeld" })



    return [example]
