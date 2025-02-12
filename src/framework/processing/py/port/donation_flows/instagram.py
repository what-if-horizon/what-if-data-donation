from port.helpers.donation_flow import donation_table, donation_flow
from port.helpers.parsers import parse_json
from port.helpers.readers import read_json

import pandas as pd
import json

def posts_viewed_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/posts_viewed.json"])

    df = parse_json(data,
        row_path = ["$.impressions_history_posts_seen"],
        col_paths = dict(
           name = ["string_map_data.Author.value"],
           time = ["string_map_data.Time.timestamp"]
        )
    )

    df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
    df = df.sort_values("date")

    return df


def ad_preferences_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/ad_preferences.json"])

    df = parse_json(data,
        row_path = ["$.label_values"],
        col_paths = dict(
           label = ["label"],
        )
    )

    return df

def create_donation_flow(file_input: list[str]):
    posts_viewed_table = donation_table(
        name = "followers",
        df = posts_viewed_df(file_input),
        title = {"en": "Example", "nl": "Voorbeeld"}
    )


    return donation_flow(
        id = "facebook",
        tables = [posts_viewed_table],
    )
