from port.helpers.donation_flow import donation_table, donation_flow
from port.helpers.parsers import parse_json
from port.helpers.readers import read_json

import port.api.props as props
from port.api.props import Translations

import pandas as pd
import json

def posts_viewed_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/posts_viewed.json"])

    print(json.dumps(data, indent=2))

    ## For some file types we can make parsers to standardize the data extraction process,
    ## and make it easy to add aliases for different languages or when DDPs change.
    df = parse_json(data,
        row_path = ["$.impressions_history_posts_seen"],
        col_paths = dict(
           name = ["string_map_data.Author.value"],
           time = ["string_map_data.Time.timestamp"]
        )
    )

    ## Here we can clean the data a bit. For What If we shouldn't do this too much,
    ## because cleaning is mostly to make it nicer for users. We can always parse
    ## the data afterwards, but if we mess up the parsing here we lose it.
    ## So here when parsing the data, I make sure to keep the original time column
    df["date"] = pd.to_datetime(df["time"], unit="ms")
    df = df.sort_values("date")

    return df


def create_donation_flow(file_input: list[str]) -> props.PropsUIPromptConsentForm:
    posts_viewed_table = donation_table(
        name = "followers",
        df = posts_viewed_df(file_input),
        title = Translations(en= "Example", nl = "Voorbeeld")
    )

    return donation_flow(
        id = "facebook",
        tables = [posts_viewed_table],
    )
