from port.helpers.tables import create_table, parse_json, extract_json
import port.api.props as props
from port.api.props import Translations

import pandas as pd


def parse_table1(zip_file: str) -> pd.DataFrame:
    """
    For every table, you need to define a function that reads the data from the zip file
    and returns a pandas DataFrame. Where possible use the helper functions (parse_json, parse_csv, etc.)
    to standardize the data extraction process, and make it easy to add aliases for different languages
    or when DDPs change.

    After parsing the data we can clean it a bit, like date parsing and sorting.
    But let's not overdo it!! The only benefit of parsing the data at this
    point is that it looks nicer for the participant. Note that in the example I also
    create a separate column for date, so that in case the to_datetime parsing goes wrong
    the researcher can still see the original timestamp.
    """
    json = extract_json(zip_file, ["connections/followers/who_you_ve_followed.json"])

    df = parse_json(json,
        row_path=["$.following_v3"],
        col_paths=dict(
           name = ["$.name"],
           time = ["$.timestamp"]
        )
    )

    df["date"] = pd.to_datetime(df["time"], unit="s")
    df = df.sort_values("date")

    return df


def create_tables(files: list[str]) -> list[props.PropsUIPromptConsentFormTable]:
    """
    In this function you create the tables. THIS FUNCTION NEEDS TO BE CALLED create_tables,
    and needs to return a list of tables, created with the create_table function.

    Here we specify everything about the table EXCEPT for the data (see parse_example).
    For now let's do the name and title, with title translations for en and nl
    (you can leave nl empty, but just specify it for the type checking)
    """

    ## input is always a list of file names, that you can read as you would normally
    ## read files in python. For FB it's a zip file.
    print(files)
    zip_file = files[0]

    ## we have special extract_ helper functions for zip files
    print(extract_json(zip_file, "connections/followers/who_you_ve_followed.json"))

    example = create_table("example_name", df = parse_table1(file_input),
        title = Translations(en= "Example", nl = "Voorbeeld"))

    return [example]
