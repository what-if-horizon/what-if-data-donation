# Auto-generated TikTok extractors

import pandas as pd
import json
import logging
from port.helpers.donation_flow import donation_table, donation_flow
from typing import List


import sys
import os

# Automatically add the project root (3 levels up from this file) to sys.path
current_file = os.path.abspath(__file__)
project_root = os.path.abspath(os.path.join(current_file, "../../.."))
sys.path.insert(0, project_root)

from structure_donations.Data_structure_extractors.TT_get_json_structure import structure_from_zip



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

def get_dict(d: dict, *keys):
    val = get_in(d, *keys)
    return val if isinstance(val, dict) else {}


def activity_df(file_input: List[str]) -> pd.DataFrame:
    try:
        with open(file_input[0], 'r', encoding='utf-8') as f:
            data = json.load(f)
        root_data = get_in(data, 'Activity')
        if not root_data:
            print(f'⚠️ No data found at path: Activity')
            return pd.DataFrame()

        base_row = {}
        base_row['note'] = get_in(root_data, 'Activity Summary', 'ActivitySummaryMap', 'note')
        base_row['videosCommentedOnSinceAccountRegistration'] = get_in(root_data, 'Activity Summary', 'ActivitySummaryMap', 'videosCommentedOnSinceAccountRegistration')
        base_row['videosSharedSinceAccountRegistration'] = get_in(root_data, 'Activity Summary', 'ActivitySummaryMap', 'videosSharedSinceAccountRegistration')
        base_row['videosWatchedToTheEndSinceAccountRegistration'] = get_in(root_data, 'Activity Summary', 'ActivitySummaryMap', 'videosWatchedToTheEndSinceAccountRegistration')
        base_row['FavoriteEffectsList'] = get_in(root_data, 'Favorite Effects', 'FavoriteEffectsList')
        base_row['FavoriteHashtagList'] = get_in(root_data, 'Favorite Hashtags', 'FavoriteHashtagList')
        base_row['FavoriteSoundList'] = get_in(root_data, 'Favorite Sounds', 'FavoriteSoundList')
        base_row['App'] = get_in(root_data, 'Favorite Videos', 'App')
        base_row['IsFastLane'] = get_in(root_data, 'Follower List', 'IsFastLane')
        base_row['Date'] = get_in(root_data, 'Most Recent Location Data', 'LocationData', 'Date')
        base_row['GpsData'] = get_in(root_data, 'Most Recent Location Data', 'LocationData', 'GpsData')
        base_row['LastRegion'] = get_in(root_data, 'Most Recent Location Data', 'LocationData', 'LastRegion')
        base_row['SendGifts'] = get_in(root_data, 'Purchase History', 'SendGifts', 'SendGifts')
        base_row['BuyGifts'] = get_in(root_data, 'Purchase History', 'BuyGifts', 'BuyGifts')
        all_records = []
        items = get_list(root_data, 'Favorite Videos', 'FavoriteVideoList')
        for item in items:
            row = base_row.copy()
            row['__source_list__'] = 'FavoriteVideoList'
            row['Date'] = item.get('Date', '.*?')
            row['Link'] = item.get('Link', '.*?')
            all_records.append(row)
        items = get_list(root_data, 'Follower List', 'FansList')
        for item in items:
            row = base_row.copy()
            row['__source_list__'] = 'FansList'
            row['Date'] = item.get('Date', '.*?')
            row['UserName'] = item.get('UserName', '.*?')
            all_records.append(row)
        items = get_list(root_data, 'Following List', 'Following')
        for item in items:
            row = base_row.copy()
            row['__source_list__'] = 'Following'
            row['Date'] = item.get('Date', '.*?')
            row['UserName'] = item.get('UserName', '.*?')
            all_records.append(row)
        items = get_list(root_data, 'Hashtag', 'HashtagList')
        for item in items:
            row = base_row.copy()
            row['__source_list__'] = 'HashtagList'
            row['HashtagLink'] = item.get('HashtagLink', '.*?')
            row['HashtagName'] = item.get('HashtagName', '.*?')
            all_records.append(row)
        items = get_list(root_data, 'Like List', 'ItemFavoriteList')
        for item in items:
            row = base_row.copy()
            row['__source_list__'] = 'ItemFavoriteList'
            row['date'] = item.get('date', '.*?')
            row['link'] = item.get('link', '.*?')
            all_records.append(row)
        items = get_list(root_data, 'Login History', 'LoginHistoryList')
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
        items = get_list(root_data, 'Search History', 'SearchList')
        for item in items:
            row = base_row.copy()
            row['__source_list__'] = 'SearchList'
            row['Date'] = item.get('Date', '.*?')
            row['SearchTerm'] = item.get('SearchTerm', '.*?')
            all_records.append(row)
        items = get_list(root_data, 'Share History', 'ShareHistoryList')
        for item in items:
            row = base_row.copy()
            row['__source_list__'] = 'ShareHistoryList'
            row['Date'] = item.get('Date', '.*?')
            row['Link'] = item.get('Link', '.*?')
            row['Method'] = item.get('Method', '.*?')
            row['SharedContent'] = item.get('SharedContent', '.*?')
            all_records.append(row)
        items = get_list(root_data, 'Status', 'Status List')
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
        items = get_list(root_data, 'Video Browsing History', 'VideoList')
        for item in items:
            row = base_row.copy()
            row['__source_list__'] = 'VideoList'
            row['Date'] = item.get('Date', '.*?')
            row['Link'] = item.get('Link', '.*?')
            all_records.append(row)
        return pd.DataFrame(all_records)
    except Exception as e:
        print(f'❌ Error in activity_df:', e)
        return pd.DataFrame()


def ads_and_data_df(file_input: List[str]) -> pd.DataFrame:
    try:
        with open(file_input[0], 'r', encoding='utf-8') as f:
            data = json.load(f)
        root_data = get_in(data, 'Ads and data')
        if not root_data:
            print(f'⚠️ No data found at path: Ads and data')
            return pd.DataFrame()

        base_row = {}
        base_row['AdInterestCategories'] = get_in(root_data, 'Ad Interests', 'AdInterestCategories')
        base_row['ResponsesList'] = get_in(root_data, 'Instant Form Ads Responses', 'ResponsesList')
        base_row['OffTikTokActivityDataList'] = get_in(root_data, 'Off TikTok Activity', 'OffTikTokActivityDataList')
        return pd.DataFrame([base_row])
    except Exception as e:
        print(f'❌ Error in ads_and_data_df:', e)
        return pd.DataFrame()


def app_settings_df(file_input: List[str]) -> pd.DataFrame:
    try:
        with open(file_input[0], 'r', encoding='utf-8') as f:
            data = json.load(f)
        root_data = get_in(data, 'App Settings')
        if not root_data:
            print(f'⚠️ No data found at path: App Settings')
            return pd.DataFrame()

        base_row = {}
        base_row['App'] = get_in(root_data, 'Block', 'App')
        base_row['BlockList'] = get_in(root_data, 'Block', 'BlockList')
        base_row['Allow DownLoad'] = get_in(root_data, 'Settings', 'SettingsMap', 'Allow DownLoad')
        base_row['Allow Others to Find Me'] = get_in(root_data, 'Settings', 'SettingsMap', 'Allow Others to Find Me')
        base_row['App Language'] = get_in(root_data, 'Settings', 'SettingsMap', 'App Language')
        base_row['Keyword filters for videos in Following feed'] = get_in(root_data, 'Settings', 'SettingsMap', 'Content Preferences', 'Keyword filters for videos in Following feed')
        base_row['Keyword filters for videos in For You feed'] = get_in(root_data, 'Settings', 'SettingsMap', 'Content Preferences', 'Keyword filters for videos in For You feed')
        base_row['Video Languages Preferences'] = get_in(root_data, 'Settings', 'SettingsMap', 'Content Preferences', 'Video Languages Preferences')
        base_row['Filter Comments'] = get_in(root_data, 'Settings', 'SettingsMap', 'Filter Comments')
        base_row['Interests'] = get_in(root_data, 'Settings', 'SettingsMap', 'Interests')
        base_row['Personalized Ads'] = get_in(root_data, 'Settings', 'SettingsMap', 'Personalized Ads')
        base_row['Private Account'] = get_in(root_data, 'Settings', 'SettingsMap', 'Private Account')
        base_row['Desktop notification'] = get_in(root_data, 'Settings', 'SettingsMap', 'Push Notification', 'Desktop notification')
        base_row['New Comments on My Video'] = get_in(root_data, 'Settings', 'SettingsMap', 'Push Notification', 'New Comments on My Video')
        base_row['New Fans'] = get_in(root_data, 'Settings', 'SettingsMap', 'Push Notification', 'New Fans')
        base_row['New Likes on My Video'] = get_in(root_data, 'Settings', 'SettingsMap', 'Push Notification', 'New Likes on My Video')
        base_row['Suggest your account to Facebook friends'] = get_in(root_data, 'Settings', 'SettingsMap', 'Suggest your account to Facebook friends')
        base_row['Suggest your account to contacts'] = get_in(root_data, 'Settings', 'SettingsMap', 'Suggest your account to contacts')
        base_row['Suggest your account to people who open or send links to you'] = get_in(root_data, 'Settings', 'SettingsMap', 'Suggest your account to people who open or send links to you')
        base_row['Web Language'] = get_in(root_data, 'Settings', 'SettingsMap', 'Web Language')
        base_row['Who Can Duet With Me'] = get_in(root_data, 'Settings', 'SettingsMap', 'Who Can Duet With Me')
        base_row['Who Can Post Comments'] = get_in(root_data, 'Settings', 'SettingsMap', 'Who Can Post Comments')
        base_row['Who Can Send Me Message'] = get_in(root_data, 'Settings', 'SettingsMap', 'Who Can Send Me Message')
        base_row['Who Can Stitch with your videos'] = get_in(root_data, 'Settings', 'SettingsMap', 'Who Can Stitch with your videos')
        base_row['Who Can View Videos I Liked'] = get_in(root_data, 'Settings', 'SettingsMap', 'Who Can View Videos I Liked')
        return pd.DataFrame([base_row])
    except Exception as e:
        print(f'❌ Error in app_settings_df:', e)
        return pd.DataFrame()


def comment_df(file_input: List[str]) -> pd.DataFrame:
    try:
        with open(file_input[0], 'r', encoding='utf-8') as f:
            data = json.load(f)
        root_data = get_in(data, 'Comment')
        if not root_data:
            print(f'⚠️ No data found at path: Comment')
            return pd.DataFrame()

        base_row = {}
        base_row['App'] = get_in(root_data, 'Comments', 'App')
        all_records = []
        items = get_list(root_data, 'Comments', 'CommentsList')
        for item in items:
            row = base_row.copy()
            row['__source_list__'] = 'CommentsList'
            row['comment'] = item.get('comment', '.*?')
            row['date'] = item.get('date', '.*?')
            row['photo'] = item.get('photo', '.*?')
            row['url'] = item.get('url', '.*?')
            all_records.append(row)
        return pd.DataFrame(all_records)
    except Exception as e:
        print(f'❌ Error in comment_df:', e)
        return pd.DataFrame()


def income_plus_wallet_transactions_df(file_input: List[str]) -> pd.DataFrame:
    try:
        with open(file_input[0], 'r', encoding='utf-8') as f:
            data = json.load(f)
        root_data = get_in(data, 'Income Plus Wallet Transactions')
        if not root_data:
            print(f'⚠️ No data found at path: Income Plus Wallet Transactions')
            return pd.DataFrame()

        base_row = {}
        base_row['TransactionsList'] = get_in(root_data, 'Income Plus Wallet Transaction', 'TransactionsList')
        return pd.DataFrame([base_row])
    except Exception as e:
        print(f'❌ Error in income_plus_wallet_transactions_df:', e)
        return pd.DataFrame()


def poi_review_df(file_input: List[str]) -> pd.DataFrame:
    try:
        with open(file_input[0], 'r', encoding='utf-8') as f:
            data = json.load(f)
        root_data = get_in(data, 'Poi Review')
        if not root_data:
            print(f'⚠️ No data found at path: Poi Review')
            return pd.DataFrame()

        base_row = {}
        all_records = []
        items = get_list(root_data, 'POI Review', 'ReviewsList')
        for item in items:
            row = base_row.copy()
            row['__source_list__'] = 'ReviewsList'
            row['Date'] = item.get('Date', '.*?')
            row['Likes'] = item.get('Likes', '.*?')
            row['PlaceName'] = item.get('PlaceName', '.*?')
            row['Rating'] = item.get('Rating', '.*?')
            row['ReviewText'] = item.get('ReviewText', '.*?')
            row['Status'] = item.get('Status', '.*?')
            all_records.append(row)
        return pd.DataFrame(all_records)
    except Exception as e:
        print(f'❌ Error in poi_review_df:', e)
        return pd.DataFrame()


def profile_df(file_input: List[str]) -> pd.DataFrame:
    try:
        with open(file_input[0], 'r', encoding='utf-8') as f:
            data = json.load(f)
        root_data = get_in(data, 'Profile')
        if not root_data:
            print(f'⚠️ No data found at path: Profile')
            return pd.DataFrame()

        base_row = {}
        base_row['CreateDate'] = get_in(root_data, 'AIMoji', 'CreateDate')
        base_row['AIMojiList'] = get_in(root_data, 'AIMoji', 'AIMojiList')
        base_row['PhoneNumber'] = get_in(root_data, 'Auto Fill', 'PhoneNumber')
        base_row['Email'] = get_in(root_data, 'Auto Fill', 'Email')
        base_row['FirstName'] = get_in(root_data, 'Auto Fill', 'FirstName')
        base_row['LastName'] = get_in(root_data, 'Auto Fill', 'LastName')
        base_row['Address'] = get_in(root_data, 'Auto Fill', 'Address')
        base_row['ZipCode'] = get_in(root_data, 'Auto Fill', 'ZipCode')
        base_row['Unit'] = get_in(root_data, 'Auto Fill', 'Unit')
        base_row['City'] = get_in(root_data, 'Auto Fill', 'City')
        base_row['State'] = get_in(root_data, 'Auto Fill', 'State')
        base_row['Country'] = get_in(root_data, 'Auto Fill', 'Country')
        base_row['App'] = get_in(root_data, 'Profile Information', 'App')
        base_row['bioDescription'] = get_in(root_data, 'Profile Information', 'ProfileMap', 'bioDescription')
        base_row['birthDate'] = get_in(root_data, 'Profile Information', 'ProfileMap', 'birthDate')
        base_row['emailAddress'] = get_in(root_data, 'Profile Information', 'ProfileMap', 'emailAddress')
        base_row['likesReceived'] = get_in(root_data, 'Profile Information', 'ProfileMap', 'likesReceived')
        base_row['profilePhoto'] = get_in(root_data, 'Profile Information', 'ProfileMap', 'profilePhoto')
        base_row['profileVideo'] = get_in(root_data, 'Profile Information', 'ProfileMap', 'profileVideo')
        base_row['telephoneNumber'] = get_in(root_data, 'Profile Information', 'ProfileMap', 'telephoneNumber')
        base_row['userName'] = get_in(root_data, 'Profile Information', 'ProfileMap', 'userName')
        all_records = []
        items = get_list(root_data, 'Profile Information', 'ProfileMap', 'PlatformInfo')
        for item in items:
            row = base_row.copy()
            row['__source_list__'] = 'PlatformInfo'
            row['Description'] = item.get('Description', '.*?')
            row['Name'] = item.get('Name', '.*?')
            row['Platform'] = item.get('Platform', '.*?')
            row['Profile Photo'] = item.get('Profile Photo', '.*?')
            all_records.append(row)
        return pd.DataFrame(all_records)
    except Exception as e:
        print(f'❌ Error in profile_df:', e)
        return pd.DataFrame()


def tiktok_live_df(file_input: List[str]) -> pd.DataFrame:
    try:
        with open(file_input[0], 'r', encoding='utf-8') as f:
            data = json.load(f)
        root_data = get_in(data, 'Tiktok Live')
        if not root_data:
            print(f'⚠️ No data found at path: Tiktok Live')
            return pd.DataFrame()

        base_row = {}
        base_row['GoLiveList'] = get_in(root_data, 'Go Live History', 'GoLiveList')
        base_row['Allow agencies to find and invite you'] = get_in(root_data, 'Go Live Settings', 'SettingsMap', 'Allow agencies to find and invite you')
        base_row['Allow others to invite you to co-host in LIVE'] = get_in(root_data, 'Go Live Settings', 'SettingsMap', 'Allow others to invite you to co-host in LIVE')
        base_row['Allow people to send and receive comments during your LIVE'] = get_in(root_data, 'Go Live Settings', 'SettingsMap', 'Allow people to send and receive comments during your LIVE')
        base_row['Allow suggested LIVE hosts to invite you to co-host in LIVE'] = get_in(root_data, 'Go Live Settings', 'SettingsMap', 'Allow suggested LIVE hosts to invite you to co-host in LIVE')
        base_row['Allow viewers to request to go LIVE with you'] = get_in(root_data, 'Go Live Settings', 'SettingsMap', 'Allow viewers to request to go LIVE with you')
        base_row['Allow viewers to see and send questions and answers in your LIVE'] = get_in(root_data, 'Go Live Settings', 'SettingsMap', 'Allow viewers to see and send questions and answers in your LIVE')
        base_row['Allow viewers to send you gifts during your LIVE'] = get_in(root_data, 'Go Live Settings', 'SettingsMap', 'Allow viewers to send you gifts during your LIVE')
        base_row['Hide potential spam or offensive comments from your LIVE'] = get_in(root_data, 'Go Live Settings', 'SettingsMap', 'Hide potential spam or offensive comments from your LIVE')
        base_row['Show your username and gift information in features with ranking lists'] = get_in(root_data, 'Go Live Settings', 'SettingsMap', 'Show your username and gift information in features with ranking lists')
        base_row['app'] = get_in(root_data, 'Watch Live Settings', 'WatchLiveSettingsMap', 'app')
        base_row['web'] = get_in(root_data, 'Watch Live Settings', 'WatchLiveSettingsMap', 'web')
        base_row['MostRecentModificationTimeInApp'] = get_in(root_data, 'Watch Live Settings', 'MostRecentModificationTimeInApp')
        base_row['MostRecentModificationTimeInWeb'] = get_in(root_data, 'Watch Live Settings', 'MostRecentModificationTimeInWeb')
        return pd.DataFrame([base_row])
    except Exception as e:
        print(f'❌ Error in tiktok_live_df:', e)
        return pd.DataFrame()


def tiktok_shopping_df(file_input: List[str]) -> pd.DataFrame:
    try:
        with open(file_input[0], 'r', encoding='utf-8') as f:
            data = json.load(f)
        root_data = get_in(data, 'Tiktok Shopping')
        if not root_data:
            print(f'⚠️ No data found at path: Tiktok Shopping')
            return pd.DataFrame()

        base_row = {}
        base_row['CommunicationHistories'] = get_in(root_data, 'Communication History', 'CommunicationHistories')
        base_row['PayCard'] = get_in(root_data, 'Current Payment Information', 'PayCard')
        base_row['CustomerSupportHistories'] = get_in(root_data, 'Customer Support History', 'CustomerSupportHistories')
        base_row['OrderDisputeHistories'] = get_in(root_data, 'Order Dispute History', 'OrderDisputeHistories')
        base_row['OrderHistories'] = get_in(root_data, 'Order History', 'OrderHistories')
        base_row['ProductBrowsingHistories'] = get_in(root_data, 'Product Browsing History', 'ProductBrowsingHistories')
        base_row['ProductReviewHistories'] = get_in(root_data, 'Product Review History', 'ProductReviewHistories')
        base_row['ReturnAndRefundHistories'] = get_in(root_data, 'Return and Refund History', 'ReturnAndRefundHistories')
        base_row['SavedAddress'] = get_in(root_data, 'Saved Address Information', 'SavedAddress')
        base_row['ShoppingCart'] = get_in(root_data, 'Shopping Cart List', 'ShoppingCart')
        base_row['Vouchers'] = get_in(root_data, 'Vouchers', 'Vouchers')
        return pd.DataFrame([base_row])
    except Exception as e:
        print(f'❌ Error in tiktok_shopping_df:', e)
        return pd.DataFrame()


def video_df(file_input: List[str]) -> pd.DataFrame:
    try:
        with open(file_input[0], 'r', encoding='utf-8') as f:
            data = json.load(f)
        root_data = get_in(data, 'Video')
        if not root_data:
            print(f'⚠️ No data found at path: Video')
            return pd.DataFrame()

        base_row = {}
        all_records = []
        items = get_list(root_data, 'RecentlyDeletedPosts', 'PostList')
        for item in items:
            row = base_row.copy()
            row['__source_list__'] = 'PostList'
            row['AIGeneratedContent'] = item.get('AIGeneratedContent', '.*?')
            row['AddYoursText'] = item.get('AddYoursText', '.*?')
            row['ContentDisclosure'] = item.get('ContentDisclosure', '.*?')
            row['Date'] = item.get('Date', '.*?')
            row['DateDeleted'] = item.get('DateDeleted', '.*?')
            row['Likes'] = item.get('Likes', '.*?')
            row['Link'] = item.get('Link', '.*?')
            row['Location'] = item.get('Location', '.*?')
            row['Sound'] = item.get('Sound', '.*?')
            row['Title'] = item.get('Title', '.*?')
            all_records.append(row)
        items = get_list(root_data, 'Videos', 'VideoList')
        for item in items:
            row = base_row.copy()
            row['__source_list__'] = 'VideoList'
            row['AIGeneratedContent'] = item.get('AIGeneratedContent', '.*?')
            row['AddYoursText'] = item.get('AddYoursText', '.*?')
            row['AllowComments'] = item.get('AllowComments', '.*?')
            row['AllowDuets'] = item.get('AllowDuets', '.*?')
            row['AllowSharingToStory'] = item.get('AllowSharingToStory', '.*?')
            row['AllowStickers'] = item.get('AllowStickers', '.*?')
            row['AllowStitches'] = item.get('AllowStitches', '.*?')
            row['ContentDisclosure'] = item.get('ContentDisclosure', '.*?')
            row['Date'] = item.get('Date', '.*?')
            row['Likes'] = item.get('Likes', '.*?')
            row['Link'] = item.get('Link', '.*?')
            row['Location'] = item.get('Location', '.*?')
            row['Sound'] = item.get('Sound', '.*?')
            row['Title'] = item.get('Title', '.*?')
            row['WhoCanView'] = item.get('WhoCanView', '.*?')
            all_records.append(row)
        return pd.DataFrame(all_records)
    except Exception as e:
        print(f'❌ Error in video_df:', e)
        return pd.DataFrame()



def create_donation_flow(file_input: List[str]):
    """Create donation flow from TikTok JSON."""
    tables = []

    try:
        df = pd.DataFrame({
                            'id': [1],
                            'json_data': [json.dumps(structure_from_zip(file_input[0]))]
                            })
        if not df.empty:
            tables.append(
                donation_table(name='Json_structure', df=df, title={'en': 'Json_structure'})
            )
    except Exception as e:
        print(f'Error in Json_structure:', e)

    

    try:
        df = activity_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='activity', df=df, title={'en': 'activity'})
            )
    except Exception as e:
        print(f'Error in activity_df:', e)

    try:
        df = ads_and_data_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='ads_and_data', df=df, title={'en': 'ads_and_data'})
            )
    except Exception as e:
        print(f'Error in ads_and_data_df:', e)

    try:
        df = app_settings_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='app_settings', df=df, title={'en': 'app_settings'})
            )
    except Exception as e:
        print(f'Error in app_settings_df:', e)

    try:
        df = comment_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='comment', df=df, title={'en': 'comment'})
            )
    except Exception as e:
        print(f'Error in comment_df:', e)

    try:
        df = income_plus_wallet_transactions_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='income_plus_wallet_transactions', df=df, title={'en': 'income_plus_wallet_transactions'})
            )
    except Exception as e:
        print(f'Error in income_plus_wallet_transactions_df:', e)

    try:
        df = poi_review_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='poi_review', df=df, title={'en': 'poi_review'})
            )
    except Exception as e:
        print(f'Error in poi_review_df:', e)

    try:
        df = profile_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='profile', df=df, title={'en': 'profile'})
            )
    except Exception as e:
        print(f'Error in profile_df:', e)

    try:
        df = tiktok_live_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='tiktok_live', df=df, title={'en': 'tiktok_live'})
            )
    except Exception as e:
        print(f'Error in tiktok_live_df:', e)

    try:
        df = tiktok_shopping_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='tiktok_shopping', df=df, title={'en': 'tiktok_shopping'})
            )
    except Exception as e:
        print(f'Error in tiktok_shopping_df:', e)

    try:
        df = video_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='video', df=df, title={'en': 'video'})
            )
    except Exception as e:
        print(f'Error in video_df:', e)

    if tables:
        return donation_flow(id='tiktok', tables=tables)
    else:
        return None