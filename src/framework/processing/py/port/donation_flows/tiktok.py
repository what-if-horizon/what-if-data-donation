# Auto-generated TikTok extractors

import pandas as pd
import json
import logging
from port.helpers.donation_flow import donation_table, donation_flow
from typing import List

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


def activity_summary_df(file_input: List[str]) -> pd.DataFrame:
    try:
        with open(file_input[0], 'r', encoding='utf-8') as f:
            data = json.load(f)
        root_data = get_in(data, 'Activity','Activity Summary')
        if not root_data:
            print(f'⚠️ No data found at path: Activity Summary')
            return pd.DataFrame()

        base_row = {}
        base_row['note'] = get_in(root_data, 'ActivitySummaryMap', 'note')
        base_row['videosCommentedOnSinceAccountRegistration'] = get_in(root_data, 'ActivitySummaryMap', 'videosCommentedOnSinceAccountRegistration')
        base_row['videosSharedSinceAccountRegistration'] = get_in(root_data, 'ActivitySummaryMap', 'videosSharedSinceAccountRegistration')
        base_row['videosWatchedToTheEndSinceAccountRegistration'] = get_in(root_data, 'ActivitySummaryMap', 'videosWatchedToTheEndSinceAccountRegistration')
        return pd.DataFrame([base_row])
    except Exception as e:
        print(f'❌ Error in activity_summary_df:', e)
        return pd.DataFrame()


def favorite_effects_df(file_input: List[str]) -> pd.DataFrame:
    try:
        with open(file_input[0], 'r', encoding='utf-8') as f:
            data = json.load(f)
        root_data = get_in(data, 'Activity','Favorite Effects')
        if not root_data:
            print(f'⚠️ No data found at path: Favorite Effects')
            return pd.DataFrame()

        base_row = {}
        base_row['FavoriteEffectsList'] = get_in(root_data, 'FavoriteEffectsList')
        return pd.DataFrame([base_row])
    except Exception as e:
        print(f'❌ Error in favorite_effects_df:', e)
        return pd.DataFrame()


def favorite_hashtags_df(file_input: List[str]) -> pd.DataFrame:
    try:
        with open(file_input[0], 'r', encoding='utf-8') as f:
            data = json.load(f)
        root_data = get_in(data, 'Activity','Favorite Hashtags')
        if not root_data:
            print(f'⚠️ No data found at path: Favorite Hashtags')
            return pd.DataFrame()

        base_row = {}
        base_row['FavoriteHashtagList'] = get_in(root_data, 'FavoriteHashtagList')
        return pd.DataFrame([base_row])
    except Exception as e:
        print(f'❌ Error in favorite_hashtags_df:', e)
        return pd.DataFrame()


def favorite_sounds_df(file_input: List[str]) -> pd.DataFrame:
    try:
        with open(file_input[0], 'r', encoding='utf-8') as f:
            data = json.load(f)
        root_data = get_in(data, 'Activity','Favorite Sounds')
        if not root_data:
            print(f'⚠️ No data found at path: Favorite Sounds')
            return pd.DataFrame()

        base_row = {}
        base_row['FavoriteSoundList'] = get_in(root_data, 'FavoriteSoundList')
        return pd.DataFrame([base_row])
    except Exception as e:
        print(f'❌ Error in favorite_sounds_df:', e)
        return pd.DataFrame()


def favorite_videos_df(file_input: List[str]) -> pd.DataFrame:
    try:
        with open(file_input[0], 'r', encoding='utf-8') as f:
            data = json.load(f)
        root_data = get_in(data, 'Activity','Favorite Videos')
        if not root_data:
            print(f'⚠️ No data found at path: Favorite Videos')
            return pd.DataFrame()

        base_row = {}
        base_row['App'] = get_in(root_data, 'App')
        all_records = []
        items = get_list(root_data, 'FavoriteVideoList')
        for item in items:
            row = base_row.copy()
            row['__source_list__'] = 'FavoriteVideoList'
            row['Date'] = item.get('Date', '.*?')
            row['Link'] = item.get('Link', '.*?')
            all_records.append(row)
        return pd.DataFrame(all_records)
    except Exception as e:
        print(f'❌ Error in favorite_videos_df:', e)
        return pd.DataFrame()


def follower_list_df(file_input: List[str]) -> pd.DataFrame:
    try:
        with open(file_input[0], 'r', encoding='utf-8') as f:
            data = json.load(f)
        root_data = get_in(data, 'Activity','Follower List')
        if not root_data:
            print(f'⚠️ No data found at path: Follower List')
            return pd.DataFrame()

        base_row = {}
        base_row['App'] = get_in(root_data, 'App')
        base_row['IsFastLane'] = get_in(root_data, 'IsFastLane')
        base_row['FansList'] = get_in(root_data, 'FansList')
        base_row['App'] = get_in(root_data, 'App')
        base_row['IsFastLane'] = get_in(root_data, 'IsFastLane')
        all_records = []
        items = get_list(root_data, 'FansList')
        for item in items:
            row = base_row.copy()
            row['__source_list__'] = 'FansList'
            row['Date'] = item.get('Date', '.*?')
            row['UserName'] = item.get('UserName', '.*?')
            all_records.append(row)
        return pd.DataFrame(all_records)
    except Exception as e:
        print(f'❌ Error in follower_list_df:', e)
        return pd.DataFrame()


def following_list_df(file_input: List[str]) -> pd.DataFrame:
    try:
        with open(file_input[0], 'r', encoding='utf-8') as f:
            data = json.load(f)
        root_data = get_in(data, 'Activity','Following List')
        if not root_data:
            print(f'⚠️ No data found at path: Following List')
            return pd.DataFrame()

        base_row = {}
        base_row['App'] = get_in(root_data, 'App')
        base_row['IsFastLane'] = get_in(root_data, 'IsFastLane')
        all_records = []
        items = get_list(root_data, 'Following')
        for item in items:
            row = base_row.copy()
            row['__source_list__'] = 'Following'
            row['Date'] = item.get('Date', '.*?')
            row['UserName'] = item.get('UserName', '.*?')
            all_records.append(row)
        return pd.DataFrame(all_records)
    except Exception as e:
        print(f'❌ Error in following_list_df:', e)
        return pd.DataFrame()


def hashtag_df(file_input: List[str]) -> pd.DataFrame:
    try:
        with open(file_input[0], 'r', encoding='utf-8') as f:
            data = json.load(f)
        root_data = get_in(data, 'Activity','Hashtag')
        if not root_data:
            print(f'⚠️ No data found at path: Hashtag')
            return pd.DataFrame()

        base_row = {}
        all_records = []
        items = get_list(root_data, 'HashtagList')
        for item in items:
            row = base_row.copy()
            row['__source_list__'] = 'HashtagList'
            row['HashtagLink'] = item.get('HashtagLink', '.*?')
            row['HashtagName'] = item.get('HashtagName', '.*?')
            all_records.append(row)
        return pd.DataFrame(all_records)
    except Exception as e:
        print(f'❌ Error in hashtag_df:', e)
        return pd.DataFrame()


def like_list_df(file_input: List[str]) -> pd.DataFrame:
    try:
        with open(file_input[0], 'r', encoding='utf-8') as f:
            data = json.load(f)
        root_data = get_in(data, 'Activity','Like List')
        if not root_data:
            print(f'⚠️ No data found at path: Like List')
            return pd.DataFrame()

        base_row = {}
        base_row['App'] = get_in(root_data, 'App')
        all_records = []
        items = get_list(root_data, 'ItemFavoriteList')
        for item in items:
            row = base_row.copy()
            row['__source_list__'] = 'ItemFavoriteList'
            row['date'] = item.get('date', '.*?')
            row['link'] = item.get('link', '.*?')
            all_records.append(row)
        return pd.DataFrame(all_records)
    except Exception as e:
        print(f'❌ Error in like_list_df:', e)
        return pd.DataFrame()


def login_history_df(file_input: List[str]) -> pd.DataFrame:
    try:
        with open(file_input[0], 'r', encoding='utf-8') as f:
            data = json.load(f)
        root_data = get_in(data, 'Activity','Login History')
        if not root_data:
            print(f'⚠️ No data found at path: Login History')
            return pd.DataFrame()

        base_row = {}
        all_records = []
        items = get_list(root_data, 'LoginHistoryList')
        for item in items:
            row = base_row.copy()
            row['__source_list__'] = 'LoginHistoryList'
            row['Carrier'] = item.get('Carrier', '.*?')
            row['Date'] = item.get('Date', '.*?')
            row['DeviceModel'] = item.get('DeviceModel', '.*?')
            row['DeviceSystem'] = item.get('DeviceSystem', '.*?')
            row['IP'] = item.get('IP', '.*?')
            row['NetworkType'] = item.get('NetworkType', '.*?')
            all_records.append(row)
        return pd.DataFrame(all_records)
    except Exception as e:
        print(f'❌ Error in login_history_df:', e)
        return pd.DataFrame()


def most_recent_location_data_df(file_input: List[str]) -> pd.DataFrame:
    try:
        with open(file_input[0], 'r', encoding='utf-8') as f:
            data = json.load(f)
        root_data = get_in(data, 'Activity','Most Recent Location Data')
        if not root_data:
            print(f'⚠️ No data found at path: Most Recent Location Data')
            return pd.DataFrame()

        base_row = {}
        base_row['Date'] = get_in(root_data, 'LocationData', 'Date')
        base_row['GpsData'] = get_in(root_data, 'LocationData', 'GpsData')
        base_row['LastRegion'] = get_in(root_data, 'LocationData', 'LastRegion')
        return pd.DataFrame([base_row])
    except Exception as e:
        print(f'❌ Error in most_recent_location_data_df:', e)
        return pd.DataFrame()


def purchase_history_df(file_input: List[str]) -> pd.DataFrame:
    try:
        with open(file_input[0], 'r', encoding='utf-8') as f:
            data = json.load(f)
        root_data = get_in(data, 'Activity','Purchase History')
        if not root_data:
            print(f'⚠️ No data found at path: Purchase History')
            return pd.DataFrame()

        base_row = {}
        base_row['SendGifts'] = get_in(root_data, 'SendGifts', 'SendGifts')
        base_row['BuyGifts'] = get_in(root_data, 'BuyGifts', 'BuyGifts')
        return pd.DataFrame([base_row])
    except Exception as e:
        print(f'❌ Error in purchase_history_df:', e)
        return pd.DataFrame()


def search_history_df(file_input: List[str]) -> pd.DataFrame:
    try:
        with open(file_input[0], 'r', encoding='utf-8') as f:
            data = json.load(f)
        root_data = get_in(data, 'Activity','Search History')
        if not root_data:
            print(f'⚠️ No data found at path: Search History')
            return pd.DataFrame()

        base_row = {}
        all_records = []
        items = get_list(root_data, 'SearchList')
        for item in items:
            row = base_row.copy()
            row['__source_list__'] = 'SearchList'
            row['Date'] = item.get('Date', '.*?')
            row['SearchTerm'] = item.get('SearchTerm', '.*?')
            all_records.append(row)
        return pd.DataFrame(all_records)
    except Exception as e:
        print(f'❌ Error in search_history_df:', e)
        return pd.DataFrame()


def share_history_df(file_input: List[str]) -> pd.DataFrame:
    try:
        with open(file_input[0], 'r', encoding='utf-8') as f:
            data = json.load(f)
        root_data = get_in(data, 'Activity','Share History')
        if not root_data:
            print(f'⚠️ No data found at path: Share History')
            return pd.DataFrame()

        base_row = {}
        all_records = []
        items = get_list(root_data, 'ShareHistoryList')
        for item in items:
            row = base_row.copy()
            row['__source_list__'] = 'ShareHistoryList'
            row['Date'] = item.get('Date', '.*?')
            row['Link'] = item.get('Link', '.*?')
            row['Method'] = item.get('Method', '.*?')
            row['SharedContent'] = item.get('SharedContent', '.*?')
            all_records.append(row)
        return pd.DataFrame(all_records)
    except Exception as e:
        print(f'❌ Error in share_history_df:', e)
        return pd.DataFrame()


def status_df(file_input: List[str]) -> pd.DataFrame:
    try:
        with open(file_input[0], 'r', encoding='utf-8') as f:
            data = json.load(f)
        root_data = get_in(data, 'Activity','Status')
        if not root_data:
            print(f'⚠️ No data found at path: Status')
            return pd.DataFrame()

        base_row = {}
        all_records = []
        items = get_list(root_data, 'Status List')
        for item in items:
            row = base_row.copy()
            row['__source_list__'] = 'Status List'
            row['Android ID'] = item.get('Android ID', '.*?')
            row['App Version'] = item.get('App Version', '.*?')
            row['GAID'] = item.get('GAID', '.*?')
            row['IDFA'] = item.get('IDFA', '.*?')
            row['IDFV'] = item.get('IDFV', '.*?')
            row['Resolution'] = item.get('Resolution', '.*?')
            row['Web ID'] = item.get('Web ID', '.*?')
            all_records.append(row)
        return pd.DataFrame(all_records)
    except Exception as e:
        print(f'❌ Error in status_df:', e)
        return pd.DataFrame()


def video_browsing_history_df(file_input: List[str]) -> pd.DataFrame:
    try:
        with open(file_input[0], 'r', encoding='utf-8') as f:
            data = json.load(f)
        root_data = get_in(data, 'Activity','Video Browsing History')
        if not root_data:
            print(f'⚠️ No data found at path: Video Browsing History')
            return pd.DataFrame()

        base_row = {}
        all_records = []
        items = get_list(root_data, 'VideoList')
        for item in items:
            row = base_row.copy()
            row['__source_list__'] = 'VideoList'
            row['Date'] = item.get('Date', '.*?')
            row['Link'] = item.get('Link', '.*?')
            all_records.append(row)
        return pd.DataFrame(all_records)
    except Exception as e:
        print(f'❌ Error in video_browsing_history_df:', e)
        return pd.DataFrame()


def create_donation_flow(file_input: List[str]):
    """Create donation flow from TikTok JSON."""
    tables = []

    try:
        df = activity_summary_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='activity_summary', df=df, title={'en': 'activity_summary'})
            )
    except Exception as e:
        print(f'Error in activity_summary_df:', e)

    try:
        df = favorite_effects_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='favorite_effects', df=df, title={'en': 'favorite_effects'})
            )
    except Exception as e:
        print(f'Error in favorite_effects_df:', e)

    try:
        df = favorite_hashtags_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='favorite_hashtags', df=df, title={'en': 'favorite_hashtags'})
            )
    except Exception as e:
        print(f'Error in favorite_hashtags_df:', e)

    try:
        df = favorite_sounds_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='favorite_sounds', df=df, title={'en': 'favorite_sounds'})
            )
    except Exception as e:
        print(f'Error in favorite_sounds_df:', e)

    try:
        df = favorite_videos_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='favorite_videos', df=df, title={'en': 'favorite_videos'})
            )
    except Exception as e:
        print(f'Error in favorite_videos_df:', e)

    try:
        df = follower_list_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='follower_list', df=df, title={'en': 'follower_list'})
            )
    except Exception as e:
        print(f'Error in follower_list_df:', e)

    try:
        df = following_list_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='following_list', df=df, title={'en': 'following_list'})
            )
    except Exception as e:
        print(f'Error in following_list_df:', e)

    try:
        df = hashtag_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='hashtag', df=df, title={'en': 'hashtag'})
            )
    except Exception as e:
        print(f'Error in hashtag_df:', e)

    try:
        df = like_list_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='like_list', df=df, title={'en': 'like_list'})
            )
    except Exception as e:
        print(f'Error in like_list_df:', e)

    try:
        df = login_history_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='login_history', df=df, title={'en': 'login_history'})
            )
    except Exception as e:
        print(f'Error in login_history_df:', e)

    try:
        df = most_recent_location_data_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='most_recent_location_data', df=df, title={'en': 'most_recent_location_data'})
            )
    except Exception as e:
        print(f'Error in most_recent_location_data_df:', e)

    try:
        df = purchase_history_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='purchase_history', df=df, title={'en': 'purchase_history'})
            )
    except Exception as e:
        print(f'Error in purchase_history_df:', e)

    try:
        df = search_history_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='search_history', df=df, title={'en': 'search_history'})
            )
    except Exception as e:
        print(f'Error in search_history_df:', e)

    try:
        df = share_history_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='share_history', df=df, title={'en': 'share_history'})
            )
    except Exception as e:
        print(f'Error in share_history_df:', e)

    try:
        df = status_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='status', df=df, title={'en': 'status'})
            )
    except Exception as e:
        print(f'Error in status_df:', e)

    try:
        df = video_browsing_history_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='video_browsing_history', df=df, title={'en': 'video_browsing_history'})
            )
    except Exception as e:
        print(f'Error in video_browsing_history_df:', e)

    if tables:
        return donation_flow(id='tiktok', tables=tables)
    else:
        return None