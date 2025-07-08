# Auto-generated TikTok extractors

from port.helpers.parsers import create_tt_df, snake_case
from port.helpers.donation_flow import donation_table, donation_flow

ENTRIES = [
    {'file_folder_name': 'Activity Summary', 'static_fields': [['Activity Summary', 'ActivitySummaryMap', 'note'], ['Activity Summary', 'ActivitySummaryMap', 'videosCommentedOnSinceAccountRegistration'], ['Activity Summary', 'ActivitySummaryMap', 'videosSharedSinceAccountRegistration'], ['Activity Summary', 'ActivitySummaryMap', 'videosWatchedToTheEndSinceAccountRegistration']], 'list_blocks': {}},
    {'file_folder_name': 'Favorite Effects', 'static_fields': [['Favorite Effects', 'FavoriteEffectsList']], 'list_blocks': {}},
    {'file_folder_name': 'Favorite Hashtags', 'static_fields': [['Favorite Hashtags', 'FavoriteHashtagList']], 'list_blocks': {}},
    {'file_folder_name': 'Favorite Sounds', 'static_fields': [['Favorite Sounds', 'FavoriteSoundList']], 'list_blocks': {}},
    {'file_folder_name': 'Favorite Videos', 'static_fields': [['Favorite Videos', 'App']], 'list_blocks': {('Favorite Videos', 'FavoriteVideoList'): {'Link', 'Date'}}},
    {'file_folder_name': 'Follower List', 'static_fields': [['Follower List', 'App'], ['Follower List', 'IsFastLane'], ['Follower List', 'FansList'], ['Follower List', 'App'], ['Follower List', 'IsFastLane']], 'list_blocks': {('Follower List', 'FansList'): {'UserName', 'Date'}}},
    {'file_folder_name': 'Following List', 'static_fields': [['Following List', 'App'], ['Following List', 'IsFastLane']], 'list_blocks': {('Following List', 'Following'): {'UserName', 'Date'}}},
    {'file_folder_name': 'Hashtag', 'static_fields': [], 'list_blocks': {('Hashtag', 'HashtagList'): {'HashtagName', 'HashtagLink'}}},
    {'file_folder_name': 'Like List', 'static_fields': [['Like List', 'App']], 'list_blocks': {('Like List', 'ItemFavoriteList'): {'link', 'date'}}},
    {'file_folder_name': 'Login History', 'static_fields': [], 'list_blocks': {('Login History', 'LoginHistoryList'): {'NetworkType', 'DeviceSystem', 'IP', 'Carrier', 'DeviceModel', 'Date'}}},
    {'file_folder_name': 'Most Recent Location Data', 'static_fields': [['Most Recent Location Data', 'LocationData', 'Date'], ['Most Recent Location Data', 'LocationData', 'GpsData'], ['Most Recent Location Data', 'LocationData', 'LastRegion']], 'list_blocks': {}},
    {'file_folder_name': 'Purchase History', 'static_fields': [['Purchase History', 'SendGifts', 'SendGifts'], ['Purchase History', 'BuyGifts', 'BuyGifts']], 'list_blocks': {}},
    {'file_folder_name': 'Search History', 'static_fields': [], 'list_blocks': {('Search History', 'SearchList'): {'SearchTerm', 'Date'}}},
    {'file_folder_name': 'Share History', 'static_fields': [], 'list_blocks': {('Share History', 'ShareHistoryList'): {'Method', 'Link', 'SharedContent', 'Date'}}},
    {'file_folder_name': 'Status', 'static_fields': [], 'list_blocks': {('Status', 'Status List'): {'App Version', 'Resolution', 'GAID', 'Web ID', 'Android ID', 'IDFV', 'IDFA'}}},
    {'file_folder_name': 'Video Browsing History', 'static_fields': [], 'list_blocks': {('Video Browsing History', 'VideoList'): {'Link', 'Date'}}},
]

def create_donation_flow(file_input: list[str]):
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
