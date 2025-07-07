# Auto-generated TikTok extractors

import pandas as pd
import json
import logging
from port.helpers.donation_flow import donation_table, donation_flow
from typing import List

ENTRIES = [
    {'file_folder_name': 'Activity Summary', 'static_fields': [['Activity Summary', 'ActivitySummaryMap', 'note'], ['Activity Summary', 'ActivitySummaryMap', 'videosCommentedOnSinceAccountRegistration'], ['Activity Summary', 'ActivitySummaryMap', 'videosSharedSinceAccountRegistration'], ['Activity Summary', 'ActivitySummaryMap', 'videosWatchedToTheEndSinceAccountRegistration']], 'list_blocks': {}},
    {'file_folder_name': 'Favorite Effects', 'static_fields': [['Favorite Effects', 'FavoriteEffectsList']], 'list_blocks': {}},
    {'file_folder_name': 'Favorite Hashtags', 'static_fields': [['Favorite Hashtags', 'FavoriteHashtagList']], 'list_blocks': {}},
    {'file_folder_name': 'Favorite Sounds', 'static_fields': [['Favorite Sounds', 'FavoriteSoundList']], 'list_blocks': {}},
    {'file_folder_name': 'Favorite Videos', 'static_fields': [['Favorite Videos', 'App']], 'list_blocks': {('Favorite Videos', 'FavoriteVideoList'): {'Link', 'Date'}}},
    {'file_folder_name': 'Follower List', 'static_fields': [['Follower List', 'App'], ['Follower List', 'IsFastLane'], ['Follower List', 'FansList'], ['Follower List', 'App'], ['Follower List', 'IsFastLane']], 'list_blocks': {('Follower List', 'FansList'): {'UserName', 'Date'}}},
    {'file_folder_name': 'Following List', 'static_fields': [['Following List', 'App'], ['Following List', 'IsFastLane']], 'list_blocks': {('Following List', 'Following'): {'UserName', 'Date'}}},
    {'file_folder_name': 'Hashtag', 'static_fields': [], 'list_blocks': {('Hashtag', 'HashtagList'): {'HashtagLink', 'HashtagName'}}},
    {'file_folder_name': 'Like List', 'static_fields': [['Like List', 'App']], 'list_blocks': {('Like List', 'ItemFavoriteList'): {'link', 'date'}}},
    {'file_folder_name': 'Login History', 'static_fields': [], 'list_blocks': {('Login History', 'LoginHistoryList'): {'IP', 'Date', 'NetworkType', 'DeviceSystem', 'DeviceModel', 'Carrier'}}},
    {'file_folder_name': 'Most Recent Location Data', 'static_fields': [['Most Recent Location Data', 'LocationData', 'Date'], ['Most Recent Location Data', 'LocationData', 'GpsData'], ['Most Recent Location Data', 'LocationData', 'LastRegion']], 'list_blocks': {}},
    {'file_folder_name': 'Purchase History', 'static_fields': [['Purchase History', 'SendGifts', 'SendGifts'], ['Purchase History', 'BuyGifts', 'BuyGifts']], 'list_blocks': {}},
    {'file_folder_name': 'Search History', 'static_fields': [], 'list_blocks': {('Search History', 'SearchList'): {'SearchTerm', 'Date'}}},
    {'file_folder_name': 'Share History', 'static_fields': [], 'list_blocks': {('Share History', 'ShareHistoryList'): {'SharedContent', 'Method', 'Link', 'Date'}}},
    {'file_folder_name': 'Status', 'static_fields': [], 'list_blocks': {('Status', 'Status List'): {'IDFA', 'IDFV', 'GAID', 'Web ID', 'Android ID', 'App Version', 'Resolution'}}},
    {'file_folder_name': 'Video Browsing History', 'static_fields': [], 'list_blocks': {('Video Browsing History', 'VideoList'): {'Link', 'Date'}}},
]

def get_in(d: dict, *keys):
    for key in keys:
        if isinstance(d, dict):
            d = d.get(key)
        else:
            return None
    return d

def get_list(d: dict, *keys):
    val = get_in(d, *keys)
    return val if isinstance(val, list) else []

def snake_case(name: str) -> str:
    return name.lower().replace("-", "_").replace(".json", "").replace(".js", "").replace(" ", "_")

def create_tt_df(
    file_input: list[str], file_folder_name: str, static_fields: list[list[str]], list_blocks: dict[str, str]
) -> pd.DataFrame:

    try:
        with open(file_input[0], "r", encoding="utf-8") as f:
            data = json.load(f)
        root_data = get_in(data, "Activity", file_folder_name)
        if not root_data:
            print(f"⚠️ No data found at path: {file_folder_name}")
            return pd.DataFrame()

        base_row = {}
        for path in static_fields:
            base_row[path[-1]] = get_in(root_data, *path[1:])
        if not list_blocks:
            # WvA: Should we not also return base_row if no entries found for list_blocks?
            return pd.DataFrame([base_row])

        all_records = []
        for list_path, fields in list_blocks.items():
            items = get_list(root_data, *list_path[1:])
            for item in items:
                row = base_row.copy()
                row["__source_list__"] = list_path[-1]
                for field in sorted(fields):
                    row[field] = item.get(field, ".*?")
                all_records.append(row)
        return pd.DataFrame(all_records)
    except Exception as e:
        print(f"❌ Error in {file_folder_name}: {e}")
        return pd.DataFrame()


def create_donation_flow(file_input: List[str]):
    """Create donation flow from TikTok JSON."""
    tables = []
    for entry in ENTRIES:
        name = snake_case(entry["file_folder_name"])
        try:
            df = create_tt_df(file_input, **entry)
            if not df.empty:
                tables.append(donation_table(name=name, df=df, title={"en": name}))
        except Exception as e:
            print(f"Error in {name}:", e)
    if tables:
        return donation_flow(id="tiktok", tables=tables)
    else:
        return None
