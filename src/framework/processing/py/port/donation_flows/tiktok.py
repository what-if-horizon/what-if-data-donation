from typing import List
import json
import pandas as pd
import logging
from port.helpers.donation_flow import donation_table, donation_flow

logger = logging.getLogger(__name__)

def get_in(data_dict, *keys):
    for k in keys:
        if isinstance(data_dict, dict):
            data_dict = data_dict.get(k, None)
        else:
            return None
        if data_dict is None:
            return None
    return data_dict
def ads_and_data_df(file_input: List[str]) -> pd.DataFrame:
    with open(file_input[0], 'r', encoding='utf-8') as f:
        data = json.load(f)
    root_data = get_in(data, 'Ads and data')
    if not root_data:
        print('No data found at path: Ads and data')
        return pd.DataFrame()

    row = {}
    sub = root_data.get('Ad Interests', {})
    row['AdInterestCategories'] = sub.get('AdInterestCategories', '.*?')
    sub = root_data.get('Instant Form Ads Responses', {})
    row['ResponsesList'] = sub.get('ResponsesList', '.*?')
    sub = root_data.get('Off TikTok Activity', {})
    row['OffTikTokActivityDataList'] = sub.get('OffTikTokActivityDataList', '.*?')
    flattened_data = [row]
    df = pd.DataFrame(flattened_data)
    return df


def app_settings_df(file_input: List[str]) -> pd.DataFrame:
    with open(file_input[0], 'r', encoding='utf-8') as f:
        data = json.load(f)
    root_data = get_in(data, 'App Settings')
    if not root_data:
        print('No data found at path: App Settings')
        return pd.DataFrame()

    row = {}
    sub = root_data.get('Block List', {})
    row['App'] = sub.get('App', '.*?')
    row['BlockList'] = sub.get('BlockList', '.*?')
    sub = root_data.get('Settings', {})
    row['App'] = sub.get('App', '.*?')
    row['SettingsMap'] = sub.get('SettingsMap', '.*?')
    flattened_data = [row]
    df = pd.DataFrame(flattened_data)
    return df


def comment_df(file_input: List[str]) -> pd.DataFrame:
    with open(file_input[0], 'r', encoding='utf-8') as f:
        data = json.load(f)
    root_data = get_in(data, 'Comment')
    if not root_data:
        print('No data found at path: Comment')
        return pd.DataFrame()

    row = {}
    sub = root_data.get('Comments', {})
    row['App'] = sub.get('App', '.*?')
    row['CommentsList'] = sub.get('CommentsList', '.*?')
    flattened_data = [row]
    df = pd.DataFrame(flattened_data)
    return df


def direct_message_df(file_input: List[str]) -> pd.DataFrame:
    with open(file_input[0], 'r', encoding='utf-8') as f:
        data = json.load(f)
    root_data = get_in(data, 'Direct Message')
    if not root_data:
        print('No data found at path: Direct Message')
        return pd.DataFrame()

    row = {}
    sub = root_data.get('Direct Messages', {})
    row['ChatHistory'] = sub.get('ChatHistory', '.*?')
    flattened_data = [row]
    df = pd.DataFrame(flattened_data)
    return df


def income_plus_wallet_transactions_df(file_input: List[str]) -> pd.DataFrame:
    with open(file_input[0], 'r', encoding='utf-8') as f:
        data = json.load(f)
    root_data = get_in(data, 'Income Plus Wallet Transactions')
    if not root_data:
        print('No data found at path: Income Plus Wallet Transactions')
        return pd.DataFrame()

    row = {}
    sub = root_data.get('Transaction History', {})
    row['TransactionsList'] = sub.get('TransactionsList', '.*?')
    flattened_data = [row]
    df = pd.DataFrame(flattened_data)
    return df


def location_review_df(file_input: List[str]) -> pd.DataFrame:
    with open(file_input[0], 'r', encoding='utf-8') as f:
        data = json.load(f)
    root_data = get_in(data, 'Location Review')
    if not root_data:
        print('No data found at path: Location Review')
        return pd.DataFrame()

    row = {}
    sub = root_data.get('Location Reviews', {})
    row['ReviewsList'] = sub.get('ReviewsList', '.*?')
    flattened_data = [row]
    df = pd.DataFrame(flattened_data)
    return df


def post_df(file_input: List[str]) -> pd.DataFrame:
    with open(file_input[0], 'r', encoding='utf-8') as f:
        data = json.load(f)
    root_data = get_in(data, 'Post')
    if not root_data:
        print('No data found at path: Post')
        return pd.DataFrame()

    row = {}
    sub = root_data.get('Posts', {})
    row['VideoList'] = sub.get('VideoList', '.*?')
    sub = root_data.get('Recently Deleted Posts', {})
    row['PostList'] = sub.get('PostList', '.*?')
    flattened_data = [row]
    df = pd.DataFrame(flattened_data)
    return df


def profile_df(file_input: List[str]) -> pd.DataFrame:
    with open(file_input[0], 'r', encoding='utf-8') as f:
        data = json.load(f)
    root_data = get_in(data, 'Profile')
    if not root_data:
        print('No data found at path: Profile')
        return pd.DataFrame()

    row = {}
    sub = root_data.get('AI-Moji', {})
    row['CreateDate'] = sub.get('CreateDate', '.*?')
    row['AIMojiList'] = sub.get('AIMojiList', '.*?')
    sub = root_data.get('Autofill', {})
    row['PhoneNumber'] = sub.get('PhoneNumber', '.*?')
    row['Email'] = sub.get('Email', '.*?')
    row['FirstName'] = sub.get('FirstName', '.*?')
    row['LastName'] = sub.get('LastName', '.*?')
    row['Address'] = sub.get('Address', '.*?')
    row['ZipCode'] = sub.get('ZipCode', '.*?')
    row['Unit'] = sub.get('Unit', '.*?')
    row['City'] = sub.get('City', '.*?')
    row['State'] = sub.get('State', '.*?')
    row['Country'] = sub.get('Country', '.*?')
    sub = root_data.get('Profile Info', {})
    row['App'] = sub.get('App', '.*?')
    row['ProfileMap'] = sub.get('ProfileMap', '.*?')
    flattened_data = [row]
    df = pd.DataFrame(flattened_data)
    return df


def tiktok_shop_df(file_input: List[str]) -> pd.DataFrame:
    with open(file_input[0], 'r', encoding='utf-8') as f:
        data = json.load(f)
    root_data = get_in(data, 'TikTok Shop')
    if not root_data:
        print('No data found at path: TikTok Shop')
        return pd.DataFrame()

    row = {}
    sub = root_data.get('Communication With Shops', {})
    row['CommunicationHistories'] = sub.get('CommunicationHistories', '.*?')
    sub = root_data.get('Current Payment Information', {})
    row['PayCard'] = sub.get('PayCard', '.*?')
    sub = root_data.get('Customer Support History', {})
    row['CustomerSupportHistories'] = sub.get('CustomerSupportHistories', '.*?')
    sub = root_data.get('Order Dispute History', {})
    row['OrderDisputeHistories'] = sub.get('OrderDisputeHistories', '.*?')
    sub = root_data.get('Order History', {})
    row['OrderHistories'] = sub.get('OrderHistories', '.*?')
    sub = root_data.get('Product Browsing History', {})
    row['ProductBrowsingHistories'] = sub.get('ProductBrowsingHistories', '.*?')
    sub = root_data.get('Product Reviews', {})
    row['ProductReviewHistories'] = sub.get('ProductReviewHistories', '.*?')
    sub = root_data.get('Returns and Refunds History', {})
    row['ReturnAndRefundHistories'] = sub.get('ReturnAndRefundHistories', '.*?')
    sub = root_data.get('Saved Address Information', {})
    row['SavedAddress'] = sub.get('SavedAddress', '.*?')
    sub = root_data.get('Shopping Cart List', {})
    row['ShoppingCart'] = sub.get('ShoppingCart', '.*?')
    sub = root_data.get('Vouchers', {})
    row['Vouchers'] = sub.get('Vouchers', '.*?')
    flattened_data = [row]
    df = pd.DataFrame(flattened_data)
    return df


def tiktok_live_df(file_input: List[str]) -> pd.DataFrame:
    with open(file_input[0], 'r', encoding='utf-8') as f:
        data = json.load(f)
    root_data = get_in(data, 'Tiktok Live')
    if not root_data:
        print('No data found at path: Tiktok Live')
        return pd.DataFrame()

    row = {}
    sub = root_data.get('Go Live History', {})
    row['GoLiveList'] = sub.get('GoLiveList', '.*?')
    sub = root_data.get('Go Live Settings', {})
    row['SettingsMap'] = sub.get('SettingsMap', '.*?')
    sub = root_data.get('Watch Live History', {})
    row['WatchLiveMap'] = sub.get('WatchLiveMap', '.*?')
    sub = root_data.get('Watch Live Settings', {})
    row['WatchLiveSettingsMap'] = sub.get('WatchLiveSettingsMap', '.*?')
    row['MostRecentModificationTimeInApp'] = sub.get('MostRecentModificationTimeInApp', '.*?')
    row['MostRecentModificationTimeInWeb'] = sub.get('MostRecentModificationTimeInWeb', '.*?')
    flattened_data = [row]
    df = pd.DataFrame(flattened_data)
    return df


def your_activity_df(file_input: List[str]) -> pd.DataFrame:
    with open(file_input[0], 'r', encoding='utf-8') as f:
        data = json.load(f)
    root_data = get_in(data, 'Activity')
    if not root_data:
        print('No data found at path: Your Activity')
        return pd.DataFrame()

    row = {}
    sub = root_data.get('Activity Summary', {})
    row['ActivitySummaryMap'] = sub.get('ActivitySummaryMap', '.*?')
    sub = root_data.get('Favorite Effects', {})
    row['FavoriteEffectsList'] = sub.get('FavoriteEffectsList', '.*?')
    sub = root_data.get('Favorite Hashtags', {})
    row['FavoriteHashtagList'] = sub.get('FavoriteHashtagList', '.*?')
    sub = root_data.get('Favorite Sounds', {})
    row['FavoriteSoundList'] = sub.get('FavoriteSoundList', '.*?')
    sub = root_data.get('Favorite Videos', {})
    row['App'] = sub.get('App', '.*?')
    row['FavoriteVideoList'] = sub.get('FavoriteVideoList', '.*?')
    sub = root_data.get('Follower', {})
    row['App'] = sub.get('App', '.*?')
    row['IsFastLane'] = sub.get('IsFastLane', '.*?')
    row['FansList'] = sub.get('FansList', '.*?')
    sub = root_data.get('Following', {})
    row['App'] = sub.get('App', '.*?')
    row['IsFastLane'] = sub.get('IsFastLane', '.*?')
    row['Following'] = sub.get('Following', '.*?')
    sub = root_data.get('Hashtag', {})
    row['HashtagList'] = sub.get('HashtagList', '.*?')
    sub = root_data.get('Like List', {})
    row['App'] = sub.get('App', '.*?')
    row['ItemFavoriteList'] = sub.get('ItemFavoriteList', '.*?')
    sub = root_data.get('Login History', {})
    row['LoginHistoryList'] = sub.get('LoginHistoryList', '.*?')
    sub = root_data.get('Most Recent Location Data', {})
    row['LocationData'] = sub.get('LocationData', '.*?')
    sub = root_data.get('Purchases', {})
    row['SendGifts'] = sub.get('SendGifts', '.*?')
    row['BuyGifts'] = sub.get('BuyGifts', '.*?')
    sub = root_data.get('Searches', {})
    row['SearchList'] = sub.get('SearchList', '.*?')
    sub = root_data.get('Share History', {})
    row['ShareHistoryList'] = sub.get('ShareHistoryList', '.*?')
    sub = root_data.get('Status', {})
    row['Status List'] = sub.get('Status List', '.*?')
    sub = root_data.get('Video Browsing History', {})
    row['VideoList'] = sub.get('VideoList', '.*?')
    flattened_data = [row]
    df = pd.DataFrame(flattened_data)
    return df


def create_donation_flow(file_input: List[str]):
    """Creates a donation flow for TikTok data."""
    tables = []

    try:
        ads_and_data_table = donation_table(
            name="Ads and data",
            df=ads_and_data_df(file_input),
            title={"en": "Ads and data", "nl": "Ads and data"},
        )
        tables.append(ads_and_data_table)
    except Exception as e:
        logger.warning(f"Skipping Ads and data: {e}")
        pass

    try:
        app_settings_table = donation_table(
            name="App Settings",
            df=app_settings_df(file_input),
            title={"en": "App Settings", "nl": "App Settings"},
        )
        tables.append(app_settings_table)
    except Exception as e:
        logger.warning(f"Skipping App Settings: {e}")
        pass

    try:
        comment_table = donation_table(
            name="Comment",
            df=comment_df(file_input),
            title={"en": "Comment", "nl": "Comment"},
        )
        tables.append(comment_table)
    except Exception as e:
        logger.warning(f"Skipping Comment: {e}")
        pass

    try:
        direct_message_table = donation_table(
            name="Direct Message",
            df=direct_message_df(file_input),
            title={"en": "Direct Message", "nl": "Direct Message"},
        )
        tables.append(direct_message_table)
    except Exception as e:
        logger.warning(f"Skipping Direct Message: {e}")
        pass

    try:
        income_plus_wallet_transactions_table = donation_table(
            name="Income Plus Wallet Transactions",
            df=income_plus_wallet_transactions_df(file_input),
            title={"en": "Income Plus Wallet Transactions", "nl": "Income Plus Wallet Transactions"},
        )
        tables.append(income_plus_wallet_transactions_table)
    except Exception as e:
        logger.warning(f"Skipping Income Plus Wallet Transactions: {e}")
        pass

    try:
        location_review_table = donation_table(
            name="Location Review",
            df=location_review_df(file_input),
            title={"en": "Location Review", "nl": "Location Review"},
        )
        tables.append(location_review_table)
    except Exception as e:
        logger.warning(f"Skipping Location Review: {e}")
        pass

    try:
        post_table = donation_table(
            name="Post",
            df=post_df(file_input),
            title={"en": "Post", "nl": "Post"},
        )
        tables.append(post_table)
    except Exception as e:
        logger.warning(f"Skipping Post: {e}")
        pass

    try:
        profile_table = donation_table(
            name="Profile",
            df=profile_df(file_input),
            title={"en": "Profile", "nl": "Profile"},
        )
        tables.append(profile_table)
    except Exception as e:
        logger.warning(f"Skipping Profile: {e}")
        pass

    try:
        tiktok_shop_table = donation_table(
            name="TikTok Shop",
            df=tiktok_shop_df(file_input),
            title={"en": "TikTok Shop", "nl": "TikTok Shop"},
        )
        tables.append(tiktok_shop_table)
    except Exception as e:
        logger.warning(f"Skipping TikTok Shop: {e}")
        pass

    try:
        tiktok_live_table = donation_table(
            name="Tiktok Live",
            df=tiktok_live_df(file_input),
            title={"en": "Tiktok Live", "nl": "Tiktok Live"},
        )
        tables.append(tiktok_live_table)
    except Exception as e:
        logger.warning(f"Skipping Tiktok Live: {e}")
        pass

    try:
        your_activity_table = donation_table(
            name="Your Activity",
            df=your_activity_df(file_input),
            title={"en": "Your Activity", "nl": "Your Activity"},
        )
        tables.append(your_activity_table)
    except Exception as e:
        logger.warning(f"Skipping Your Activity: {e}")
        pass

    if tables:
        return donation_flow(
            id="tiktok",
            tables=tables
        )
    else:
        return None