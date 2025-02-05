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

    After parsing the data we can clean it a bit, like date parsing and sorting.
    But let's not overdo it!! The only benefit of parsing the data at this
    point is that it looks nicer for the participant. Note that in the example I also
    create a separate column for date, so that in case the parsing goes wrong
    the researcher can still see the original timestamp
    """

    df = parse_json(zip,
        filename=["likes_and_reactions.json"],
        row_path=["$.data", "$.gegevens"],
        col_paths={
            "timestamp": ["$.timestamp"],
            "label_values": ["$.label_values"]
        })

    df["date"] = pd.to_datetime(df["timestamp"], unit="s")
    df = df.sort_values("date")

    return df





def create_tables(zip: str) -> list[props.PropsUIPromptConsentFormTable]:
    """
    In this function you create the tables.

    Here we specify everything about the table EXCEPT for the data (see parse_example).
    For now let's do the name and title, with title translations for en and nl
    (you can leave nl empty, but just specify it for the type checking)
    """

    example = create_table("example_name", df = parse_table1(zip),
        title = { "en": "Example", "nl": "" })

    return [example]


if __name__ == "__main__":
    # Make sure to create an object called tables here, using the create_tables function
    # This is what allows the easy testing
    print('jeej')

    tables = create_tables("test.zip")
