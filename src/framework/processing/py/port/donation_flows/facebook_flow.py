from port.helpers.donation_flow import donation_table, donation_flow
from port.helpers.parsers import parse_json
from port.helpers.readers import read_json

import port.api.props as props
from port.api.props import Translations

import pandas as pd
import json


def followers_df(file_input: list[str]) -> pd.DataFrame:
    """
    For every table, you need to define a function that reads the data from the zip file
    and returns a pandas DataFrame.
    """

    ## file_input is a list of file names, that you can read as you would normally
    ## read files in python. We also have helper functions to make it easy to
    ## read files from anywhere in the file_input (including zip).
    ## - read_json(zip_file, file_path)
    ## - read_csv(zip_file, file_path, [optional arguments to pd.read_csv])
    ## - read_binary(file_input, file_paths)
    ## - read_text(file_input, file_paths, encoding = 'utf-8')

    ## The file_paths argument is an array of possible paths. The first path that matches will be used.
    ## This way we can add paths for different languages without having to know what language the user's data is in.
    data = read_json(file_input, ["*/who_you_ve_followed.json"])

    ## For debugging you can print, and it will show on the dev page (when using "npm run dev:facebook")
    print(json.dumps(data, indent=2))

    ## For some file types we can make parsers to standardize the data extraction process,
    ## and make it easy to add aliases for different languages or when DDPs change.
    df = parse_json(data,
        row_path=["$.following_v3"],
        col_paths=dict(
           name = ["name"],
           time = ["timestamp"]
        )
    )

    ## Here we can clean the data a bit. For What If we shouldn't do this too much,
    ## because cleaning is mostly to make it nicer for users. We can always parse
    ## the data afterwards, but if we mess up the parsing here we lose it.
    ## So here when parsing the data, I make sure to keep the original time column
    df["date"] = pd.to_datetime(df["time"), unit="s")
    df = df.sort_values("date")

    return df


def create_donation_flow(file_input: list[str]) -> props.PropsUIPromptConsentForm:
    """
    In this function you create the donation tables with the "donation_table" function,
    and return a donation flow created with the "donation_flow" function.

    !! THIS FUNCTION NEEDS TO BE CALLED "create_donation_flow",
    """

    followers_table = donation_table(
        name = "followers",
        df = followers_df(file_input),
        title = Translations(en= "Example", nl = "Voorbeeld")
    )

    return donation_flow(
        id = "facebook",
        tables = [followers_table],
    )
