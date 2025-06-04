# Auto-generated Twitter extractors

import pandas as pd
import json
import logging
import io
import zipfile
import re
from port.helpers.donation_flow import donation_table, donation_flow
from port.helpers.parsers import parse_json

from port.structure_extractor_libraries.X_get_json_structure import structure_from_zip

logger = logging.getLogger(__name__)

def read_js(file_input: list[str], target_files: list[str]) -> list:
    """Extracts JSON content from matching .js files inside the ZIP."""
    extracted_data = []

    for zip_path in file_input:
        with zipfile.ZipFile(zip_path, "r") as z:
            for target_file in target_files:
                js_files = [f for f in z.namelist() if target_file in f]
                if js_files:
                    with z.open(js_files[0]) as raw_file:
                        with io.TextIOWrapper(raw_file, encoding="utf8") as text_file:
                            lines = text_file.readlines()
                        lines[0] = re.sub(r"^.*? = ", "", lines[0])  # remove variable assignment
                        try:
                            data = json.loads("".join(lines))
                            extracted_data.extend(data)  # assuming a list inside
                        except json.JSONDecodeError as e:
                            logger.error(f"Error decoding {target_file} in {zip_path}: {e}")

    return extracted_data


def account_creation_ip_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['account-creation-ip.js'])

    records = []
    for item in data:
        record = {}
        account_creation_ip = item.get('account_creation_ip', {})
        record['accountId'] = account_creation_ip.get('accountId', '.*?')
        account_creation_ip = item.get('account_creation_ip', {})
        record['userCreationIp'] = account_creation_ip.get('userCreationIp', '.*?')
        records.append(record)

    df = pd.DataFrame(records)
    return df


def account_label_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['account-label.js'])

    records = []
    for item in data:
        record = {}
        account_label = item.get('account_label', {})
        record['label'] = account_label.get('label', '.*?')
        account_label = item.get('account_label', {})
        record['managedByScreenName'] = account_label.get('managedByScreenName', '.*?')
        records.append(record)

    df = pd.DataFrame(records)
    return df


def account_suspension_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['account-suspension.js'])

    records = []
    for item in data:
        record = {}
        account_suspension = item.get('account_suspension', {})
        record['timeStamp'] = account_suspension.get('timeStamp', '.*?')
        account_suspension = item.get('account_suspension', {})
        record['action'] = account_suspension.get('action', '.*?')
        records.append(record)

    df = pd.DataFrame(records)
    return df


def account_timezone_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['account-timezone.js'])

    records = []
    for item in data:
        record = {}
        account_timezone = item.get('account_timezone', {})
        record['accountId'] = account_timezone.get('accountId', '.*?')
        account_timezone = item.get('account_timezone', {})
        record['timeZone'] = account_timezone.get('timeZone', '.*?')
        records.append(record)

    df = pd.DataFrame(records)
    return df


def account_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['account.js'])

    records = []
    for item in data:
        record = {}
        account = item.get('account', {})
        record['email'] = account.get('email', '.*?')
        account = item.get('account', {})
        record['createdVia'] = account.get('createdVia', '.*?')
        account = item.get('account', {})
        record['username'] = account.get('username', '.*?')
        account = item.get('account', {})
        record['accountId'] = account.get('accountId', '.*?')
        account = item.get('account', {})
        record['createdAt'] = account.get('createdAt', '.*?')
        account = item.get('account', {})
        record['accountDisplayName'] = account.get('accountDisplayName', '.*?')
        records.append(record)

    df = pd.DataFrame(records)
    return df




    data = read_json(file_input, ["*/cities_you_have_checked_into.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")


def ad_engagements_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['ad-engagements.js'])

    df = parse_json(data,
        row_path=["$.ad"],
        col_paths=dict(
        )
    )

    print(df)

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def ad_impressions_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['ad-impressions.js'])

    records = []
    for item in data:
        record = {}
        ad_impressions = item.get('ad_impressions', {})
        record['ad'] = ad_impressions.get('ad', '.*?')
        ad_impressions = item.get('ad_impressions', {})
        record['deviceInfo'] = ad_impressions.get('deviceInfo', '.*?')
        ad_impressions = item.get('ad_impressions', {})
        record['displayLocation'] = ad_impressions.get('displayLocation', '.*?')
        ad_impressions = item.get('ad_impressions', {})
        record['promotedTweetInfo'] = ad_impressions.get('promotedTweetInfo', '.*?')
        ad_impressions = item.get('ad_impressions', {})
        record['advertiserInfo'] = ad_impressions.get('advertiserInfo', '.*?')
        ad_impressions = item.get('ad_impressions', {})
        record['matchedTargetingCriteria'] = ad_impressions.get('matchedTargetingCriteria', '.*?')
        ad_impressions = item.get('ad_impressions', {})
        record['impressionTime'] = ad_impressions.get('impressionTime', '.*?')
        records.append(record)

    df = pd.DataFrame(records)
    return df


def ad_mobile_conversions_attributed_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['ad-mobile-conversions-attributed.js'])

    records = []
    for item in data:
        record = {}
        ad_mobile_conversions_attributed = item.get('ad_mobile_conversions_attributed', {})
        record['ad'] = ad_mobile_conversions_attributed.get('ad', '.*?')
        ad_mobile_conversions_attributed = item.get('ad_mobile_conversions_attributed', {})
        record['attributedConversionType'] = ad_mobile_conversions_attributed.get('attributedConversionType', '.*?')
        ad_mobile_conversions_attributed = item.get('ad_mobile_conversions_attributed', {})
        record['mobilePlatform'] = ad_mobile_conversions_attributed.get('mobilePlatform', '.*?')
        ad_mobile_conversions_attributed = item.get('ad_mobile_conversions_attributed', {})
        record['conversionEvent'] = ad_mobile_conversions_attributed.get('conversionEvent', '.*?')
        ad_mobile_conversions_attributed = item.get('ad_mobile_conversions_attributed', {})
        record['applicationName'] = ad_mobile_conversions_attributed.get('applicationName', '.*?')
        ad_mobile_conversions_attributed = item.get('ad_mobile_conversions_attributed', {})
        record['conversionValue'] = ad_mobile_conversions_attributed.get('conversionValue', '.*?')
        ad_mobile_conversions_attributed = item.get('ad_mobile_conversions_attributed', {})
        record['conversionTime'] = ad_mobile_conversions_attributed.get('conversionTime', '.*?')
        ad_mobile_conversions_attributed = item.get('ad_mobile_conversions_attributed', {})
        record['additionalParameters'] = ad_mobile_conversions_attributed.get('additionalParameters', '.*?')
        records.append(record)

    df = pd.DataFrame(records)
    return df


def ad_mobile_conversions_unattributed_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['ad-mobile-conversions-unattributed.js'])

    records = []
    for item in data:
        record = {}
        ad_mobile_conversions_unattributed = item.get('ad_mobile_conversions_unattributed', {})
        record['ad'] = ad_mobile_conversions_unattributed.get('ad', '.*?')
        ad_mobile_conversions_unattributed = item.get('ad_mobile_conversions_unattributed', {})
        record['mobilePlatform'] = ad_mobile_conversions_unattributed.get('mobilePlatform', '.*?')
        ad_mobile_conversions_unattributed = item.get('ad_mobile_conversions_unattributed', {})
        record['conversionEvent'] = ad_mobile_conversions_unattributed.get('conversionEvent', '.*?')
        ad_mobile_conversions_unattributed = item.get('ad_mobile_conversions_unattributed', {})
        record['applicationName'] = ad_mobile_conversions_unattributed.get('applicationName', '.*?')
        ad_mobile_conversions_unattributed = item.get('ad_mobile_conversions_unattributed', {})
        record['conversionValue'] = ad_mobile_conversions_unattributed.get('conversionValue', '.*?')
        ad_mobile_conversions_unattributed = item.get('ad_mobile_conversions_unattributed', {})
        record['conversionTime'] = ad_mobile_conversions_unattributed.get('conversionTime', '.*?')
        ad_mobile_conversions_unattributed = item.get('ad_mobile_conversions_unattributed', {})
        record['additionalParameters'] = ad_mobile_conversions_unattributed.get('additionalParameters', '.*?')
        records.append(record)

    df = pd.DataFrame(records)
    return df


def ad_online_conversions_attributed_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['ad-online-conversions-attributed.js'])

    records = []
    for item in data:
        record = {}
        ad_online_conversions_attributed = item.get('ad_online_conversions_attributed', {})
        record['ad'] = ad_online_conversions_attributed.get('ad', '.*?')
        ad_online_conversions_attributed = item.get('ad_online_conversions_attributed', {})
        record['attributedConversionType'] = ad_online_conversions_attributed.get('attributedConversionType', '.*?')
        ad_online_conversions_attributed = item.get('ad_online_conversions_attributed', {})
        record['eventType'] = ad_online_conversions_attributed.get('eventType', '.*?')
        ad_online_conversions_attributed = item.get('ad_online_conversions_attributed', {})
        record['conversionPlatform'] = ad_online_conversions_attributed.get('conversionPlatform', '.*?')
        ad_online_conversions_attributed = item.get('ad_online_conversions_attributed', {})
        record['advertiserInfo'] = ad_online_conversions_attributed.get('advertiserInfo', '.*?')
        ad_online_conversions_attributed = item.get('ad_online_conversions_attributed', {})
        record['conversionValue'] = ad_online_conversions_attributed.get('conversionValue', '.*?')
        ad_online_conversions_attributed = item.get('ad_online_conversions_attributed', {})
        record['conversionTime'] = ad_online_conversions_attributed.get('conversionTime', '.*?')
        ad_online_conversions_attributed = item.get('ad_online_conversions_attributed', {})
        record['additionalParameters'] = ad_online_conversions_attributed.get('additionalParameters', '.*?')
        records.append(record)

    df = pd.DataFrame(records)
    return df


def ad_online_conversions_unattributed_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['ad-online-conversions-unattributed.js'])

    records = []
    for item in data:
        record = {}
        ad_online_conversions_unattributed = item.get('ad_online_conversions_unattributed', {})
        record['ad'] = ad_online_conversions_unattributed.get('ad', '.*?')
        ad_online_conversions_unattributed = item.get('ad_online_conversions_unattributed', {})
        record['eventType'] = ad_online_conversions_unattributed.get('eventType', '.*?')
        ad_online_conversions_unattributed = item.get('ad_online_conversions_unattributed', {})
        record['conversionPlatform'] = ad_online_conversions_unattributed.get('conversionPlatform', '.*?')
        ad_online_conversions_unattributed = item.get('ad_online_conversions_unattributed', {})
        record['conversionUrl'] = ad_online_conversions_unattributed.get('conversionUrl', '.*?')
        ad_online_conversions_unattributed = item.get('ad_online_conversions_unattributed', {})
        record['advertiserInfo'] = ad_online_conversions_unattributed.get('advertiserInfo', '.*?')
        ad_online_conversions_unattributed = item.get('ad_online_conversions_unattributed', {})
        record['conversionValue'] = ad_online_conversions_unattributed.get('conversionValue', '.*?')
        ad_online_conversions_unattributed = item.get('ad_online_conversions_unattributed', {})
        record['conversionTime'] = ad_online_conversions_unattributed.get('conversionTime', '.*?')
        ad_online_conversions_unattributed = item.get('ad_online_conversions_unattributed', {})
        record['additionalParameters'] = ad_online_conversions_unattributed.get('additionalParameters', '.*?')
        records.append(record)

    df = pd.DataFrame(records)
    return df


def ads_revenue_sharing_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['ads-revenue-sharing.js'])

    records = []
    for item in data:
        record = {}
        ads_revenue_sharing = item.get('ads_revenue_sharing', {})
        record['status'] = ads_revenue_sharing.get('status', '.*?')
        ads_revenue_sharing = item.get('ads_revenue_sharing', {})
        record['enrolledAt'] = ads_revenue_sharing.get('enrolledAt', '.*?')
        ads_revenue_sharing = item.get('ads_revenue_sharing', {})
        record['paidAt'] = ads_revenue_sharing.get('paidAt', '.*?')
        ads_revenue_sharing = item.get('ads_revenue_sharing', {})
        record['payoutAmountUsd'] = ads_revenue_sharing.get('payoutAmountUsd', '.*?')
        records.append(record)

    df = pd.DataFrame(records)
    return df


def app_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['app.js'])

    records = []
    for item in data:
        record = {}
        app = item.get('app', {})
        record['appId'] = app.get('appId', '.*?')
        app = item.get('app', {})
        record['appNames'] = app.get('appNames', '.*?')
        records.append(record)

    df = pd.DataFrame(records)
    return df


def article_metadata_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['article-metadata.js'])

    records = []
    for item in data:
        record = {}
        article_metadata = item.get('article_metadata', {})
        record['authorId'] = article_metadata.get('authorId', '.*?')
        article_metadata = item.get('article_metadata', {})
        record['createdatMs'] = article_metadata.get('createdatMs', '.*?')
        article_metadata = item.get('article_metadata', {})
        record['updatedAtMs'] = article_metadata.get('updatedAtMs', '.*?')
        article_metadata = item.get('article_metadata', {})
        record['visibility'] = article_metadata.get('visibility', '.*?')
        article_metadata = item.get('article_metadata', {})
        record['tweetId'] = article_metadata.get('tweetId', '.*?')
        article_metadata = item.get('article_metadata', {})
        record['firstPublishedAtMs'] = article_metadata.get('firstPublishedAtMs', '.*?')
        article_metadata = item.get('article_metadata', {})
        record['lifecycleState'] = article_metadata.get('lifecycleState', '.*?')
        records.append(record)

    df = pd.DataFrame(records)
    return df


def article_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['article.js'])

    records = []
    for item in data:
        record = {}
        article = item.get('article', {})
        record['id'] = article.get('id', '.*?')
        article = item.get('article', {})
        record['title'] = article.get('title', '.*?')
        article = item.get('article', {})
        record['content'] = article.get('content', '.*?')
        article = item.get('article', {})
        record['coverMedia'] = article.get('coverMedia', '.*?')
        article = item.get('article', {})
        record['media'] = article.get('media', '.*?')
        records.append(record)

    df = pd.DataFrame(records)
    return df


def audio_video_calls_in_dm_recipient_sessions_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['audio-video-calls-in-dm-recipient-sessions.js'])

    records = []
    for item in data:
        record = {}
        audio_video_calls_in_dm_recipient_sessions = item.get('audio_video_calls_in_dm_recipient_sessions', {})
        record['createdAt'] = audio_video_calls_in_dm_recipient_sessions.get('createdAt', '.*?')
        audio_video_calls_in_dm_recipient_sessions = item.get('audio_video_calls_in_dm_recipient_sessions', {})
        record['publishedAt'] = audio_video_calls_in_dm_recipient_sessions.get('publishedAt', '.*?')
        audio_video_calls_in_dm_recipient_sessions = item.get('audio_video_calls_in_dm_recipient_sessions', {})
        record['startedAt'] = audio_video_calls_in_dm_recipient_sessions.get('startedAt', '.*?')
        audio_video_calls_in_dm_recipient_sessions = item.get('audio_video_calls_in_dm_recipient_sessions', {})
        record['lastPingedAt'] = audio_video_calls_in_dm_recipient_sessions.get('lastPingedAt', '.*?')
        audio_video_calls_in_dm_recipient_sessions = item.get('audio_video_calls_in_dm_recipient_sessions', {})
        record['endedAt'] = audio_video_calls_in_dm_recipient_sessions.get('endedAt', '.*?')
        audio_video_calls_in_dm_recipient_sessions = item.get('audio_video_calls_in_dm_recipient_sessions', {})
        record['endReason'] = audio_video_calls_in_dm_recipient_sessions.get('endReason', '.*?')
        audio_video_calls_in_dm_recipient_sessions = item.get('audio_video_calls_in_dm_recipient_sessions', {})
        record['hostBroadcastID'] = audio_video_calls_in_dm_recipient_sessions.get('hostBroadcastID', '.*?')
        records.append(record)

    df = pd.DataFrame(records)
    return df


def audio_video_calls_in_dm_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['audio-video-calls-in-dm.js'])

    records = []
    for item in data:
        record = {}
        audio_video_calls_in_dm = item.get('audio_video_calls_in_dm', {})
        record['broadcast'] = audio_video_calls_in_dm.get('broadcast', '.*?')
        audio_video_calls_in_dm = item.get('audio_video_calls_in_dm', {})
        record['sessions'] = audio_video_calls_in_dm.get('sessions', '.*?')
        records.append(record)

    df = pd.DataFrame(records)
    return df


def block_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['block.js'])

    records = []
    for item in data:
        record = {}
        block = item.get('block', {})
        record['accountId'] = block.get('accountId', '.*?')
        block = item.get('block', {})
        record['userLink'] = block.get('userLink', '.*?')
        records.append(record)

    df = pd.DataFrame(records)
    return df


def branch_links_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['branch-links.js'])

    records = []
    for item in data:
        record = {}
        branch_links = item.get('branch_links', {})
        record['timestamp'] = branch_links.get('timestamp', '.*?')
        branch_links = item.get('branch_links', {})
        record['landingPage'] = branch_links.get('landingPage', '.*?')
        branch_links = item.get('branch_links', {})
        record['externalReferrerUrl'] = branch_links.get('externalReferrerUrl', '.*?')
        branch_links = item.get('branch_links', {})
        record['channel'] = branch_links.get('channel', '.*?')
        branch_links = item.get('branch_links', {})
        record['feature'] = branch_links.get('feature', '.*?')
        branch_links = item.get('branch_links', {})
        record['campaign'] = branch_links.get('campaign', '.*?')
        records.append(record)

    df = pd.DataFrame(records)
    return df


def catalog_item_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['catalog-item.js'])

    records = []
    for item in data:
        record = {}
        catalog_item = item.get('catalog_item', {})
        record['catalogProduct'] = catalog_item.get('catalogProduct', '.*?')
        catalog_item = item.get('catalog_item', {})
        record['productKey'] = catalog_item.get('productKey', '.*?')
        catalog_item = item.get('catalog_item', {})
        record['productId'] = catalog_item.get('productId', '.*?')
        catalog_item = item.get('catalog_item', {})
        record['catalogId'] = catalog_item.get('catalogId', '.*?')
        catalog_item = item.get('catalog_item', {})
        record['lastUpdatedAt'] = catalog_item.get('lastUpdatedAt', '.*?')
        catalog_item = item.get('catalog_item', {})
        record['createdFromDataSource'] = catalog_item.get('createdFromDataSource', '.*?')
        catalog_item = item.get('catalog_item', {})
        record['updatedFromDataSource'] = catalog_item.get('updatedFromDataSource', '.*?')
        catalog_item = item.get('catalog_item', {})
        record['title'] = catalog_item.get('title', '.*?')
        catalog_item = item.get('catalog_item', {})
        record['description'] = catalog_item.get('description', '.*?')
        catalog_item = item.get('catalog_item', {})
        record['productUrl'] = catalog_item.get('productUrl', '.*?')
        catalog_item = item.get('catalog_item', {})
        record['price'] = catalog_item.get('price', '.*?')
        catalog_item = item.get('catalog_item', {})
        record['coverMedia'] = catalog_item.get('coverMedia', '.*?')
        catalog_item = item.get('catalog_item', {})
        record['additionalMedia'] = catalog_item.get('additionalMedia', '.*?')
        catalog_item = item.get('catalog_item', {})
        record['mobileUrl'] = catalog_item.get('mobileUrl', '.*?')
        catalog_item = item.get('catalog_item', {})
        record['salePrice'] = catalog_item.get('salePrice', '.*?')
        catalog_item = item.get('catalog_item', {})
        record['saleStartTime'] = catalog_item.get('saleStartTime', '.*?')
        catalog_item = item.get('catalog_item', {})
        record['saleEndTime'] = catalog_item.get('saleEndTime', '.*?')
        catalog_item = item.get('catalog_item', {})
        record['googleProductCategory'] = catalog_item.get('googleProductCategory', '.*?')
        catalog_item = item.get('catalog_item', {})
        record['customProductType'] = catalog_item.get('customProductType', '.*?')
        catalog_item = item.get('catalog_item', {})
        record['brand'] = catalog_item.get('brand', '.*?')
        catalog_item = item.get('catalog_item', {})
        record['catalogProductGroup'] = catalog_item.get('catalogProductGroup', '.*?')
        catalog_item = item.get('catalog_item', {})
        record['productGroupKey'] = catalog_item.get('productGroupKey', '.*?')
        catalog_item = item.get('catalog_item', {})
        record['productGroupId'] = catalog_item.get('productGroupId', '.*?')
        catalog_item = item.get('catalog_item', {})
        record['products'] = catalog_item.get('products', '.*?')
        records.append(record)

    df = pd.DataFrame(records)
    return df


def commerce_catalog_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['commerce-catalog.js'])

    records = []
    for item in data:
        record = {}
        commerce_catalog = item.get('commerce_catalog', {})
        record['catalogId'] = commerce_catalog.get('catalogId', '.*?')
        commerce_catalog = item.get('commerce_catalog', {})
        record['catalogName'] = commerce_catalog.get('catalogName', '.*?')
        commerce_catalog = item.get('commerce_catalog', {})
        record['catalogType'] = commerce_catalog.get('catalogType', '.*?')
        commerce_catalog = item.get('commerce_catalog', {})
        record['authorUserId'] = commerce_catalog.get('authorUserId', '.*?')
        commerce_catalog = item.get('commerce_catalog', {})
        record['lastUpdatedAt'] = commerce_catalog.get('lastUpdatedAt', '.*?')
        records.append(record)

    df = pd.DataFrame(records)
    return df


def community_note_rating_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['community-note-rating.js'])

    records = []
    for item in data:
        record = {}
        community_note_rating = item.get('community_note_rating', {})
        record['noteId'] = community_note_rating.get('noteId', '.*?')
        community_note_rating = item.get('community_note_rating', {})
        record['userId'] = community_note_rating.get('userId', '.*?')
        community_note_rating = item.get('community_note_rating', {})
        record['createdAt'] = community_note_rating.get('createdAt', '.*?')
        community_note_rating = item.get('community_note_rating', {})
        record['agree'] = community_note_rating.get('agree', '.*?')
        community_note_rating = item.get('community_note_rating', {})
        record['helpful'] = community_note_rating.get('helpful', '.*?')
        community_note_rating = item.get('community_note_rating', {})
        record['helpfulTags'] = community_note_rating.get('helpfulTags', '.*?')
        community_note_rating = item.get('community_note_rating', {})
        record['nothelpfulTags'] = community_note_rating.get('nothelpfulTags', '.*?')
        community_note_rating = item.get('community_note_rating', {})
        record['helpfulnessLevel'] = community_note_rating.get('helpfulnessLevel', '.*?')
        community_note_rating = item.get('community_note_rating', {})
        record['userAlias'] = community_note_rating.get('userAlias', '.*?')
        records.append(record)

    df = pd.DataFrame(records)
    return df


def community_note_tombstone_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['community-note-tombstone.js'])

    records = []
    for item in data:
        record = {}
        community_note_tombstone = item.get('community_note_tombstone', {})
        record['noteId'] = community_note_tombstone.get('noteId', '.*?')
        community_note_tombstone = item.get('community_note_tombstone', {})
        record['userId'] = community_note_tombstone.get('userId', '.*?')
        community_note_tombstone = item.get('community_note_tombstone', {})
        record['createdAt'] = community_note_tombstone.get('createdAt', '.*?')
        community_note_tombstone = item.get('community_note_tombstone', {})
        record['deletedAt'] = community_note_tombstone.get('deletedAt', '.*?')
        records.append(record)

    df = pd.DataFrame(records)
    return df


def community_note_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['community-note.js'])

    records = []
    for item in data:
        record = {}
        community_note = item.get('community_note', {})
        record['noteId'] = community_note.get('noteId', '.*?')
        community_note = item.get('community_note', {})
        record['userId'] = community_note.get('userId', '.*?')
        community_note = item.get('community_note', {})
        record['createdAt'] = community_note.get('createdAt', '.*?')
        community_note = item.get('community_note', {})
        record['tweetId'] = community_note.get('tweetId', '.*?')
        community_note = item.get('community_note', {})
        record['summary'] = community_note.get('summary', '.*?')
        community_note = item.get('community_note', {})
        record['classification'] = community_note.get('classification', '.*?')
        community_note = item.get('community_note', {})
        record['believable'] = community_note.get('believable', '.*?')
        community_note = item.get('community_note', {})
        record['trustworthySources'] = community_note.get('trustworthySources', '.*?')
        community_note = item.get('community_note', {})
        record['misleadingTags'] = community_note.get('misleadingTags', '.*?')
        community_note = item.get('community_note', {})
        record['notMisleadingTags'] = community_note.get('notMisleadingTags', '.*?')
        community_note = item.get('community_note', {})
        record['harmful'] = community_note.get('harmful', '.*?')
        community_note = item.get('community_note', {})
        record['validation'] = community_note.get('validation', '.*?')
        community_note = item.get('community_note', {})
        record['userAlias'] = community_note.get('userAlias', '.*?')
        records.append(record)

    df = pd.DataFrame(records)
    return df


def connected_application_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['connected-application.js'])

    records = []
    for item in data:
        record = {}
        connected_application = item.get('connected_application', {})
        record['name'] = connected_application.get('name', '.*?')
        connected_application = item.get('connected_application', {})
        record['description'] = connected_application.get('description', '.*?')
        connected_application = item.get('connected_application', {})
        record['approvedAt'] = connected_application.get('approvedAt', '.*?')
        connected_application = item.get('connected_application', {})
        record['permissions'] = connected_application.get('permissions', '.*?')
        connected_application = item.get('connected_application', {})
        record['id'] = connected_application.get('id', '.*?')
        records.append(record)

    df = pd.DataFrame(records)
    return df


def contact_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['contact.js'])

    records = []
    for item in data:
        record = {}
        contact = item.get('contact', {})
        record['id'] = contact.get('id', '.*?')
        contact = item.get('contact', {})
        record['emails'] = contact.get('emails', '.*?')
        contact = item.get('contact', {})
        record['phoneNumbers'] = contact.get('phoneNumbers', '.*?')
        records.append(record)

    df = pd.DataFrame(records)
    return df


def deleted_note_tweet_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['deleted-note-tweet.js'])

    records = []
    for item in data:
        record = {}
        deleted_note_tweet = item.get('deleted_note_tweet', {})
        record['noteTweetId'] = deleted_note_tweet.get('noteTweetId', '.*?')
        deleted_note_tweet = item.get('deleted_note_tweet', {})
        record['createdAt'] = deleted_note_tweet.get('createdAt', '.*?')
        deleted_note_tweet = item.get('deleted_note_tweet', {})
        record['lifecycle'] = deleted_note_tweet.get('lifecycle', '.*?')
        deleted_note_tweet = item.get('deleted_note_tweet', {})
        record['updatedAt'] = deleted_note_tweet.get('updatedAt', '.*?')
        deleted_note_tweet = item.get('deleted_note_tweet', {})
        record['core'] = deleted_note_tweet.get('core', '.*?')
        records.append(record)

    df = pd.DataFrame(records)
    return df


def deleted_tweet_headers_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['deleted-tweet-headers.js'])

    records = []
    for item in data:
        record = {}
        deleted_tweet_headers = item.get('deleted_tweet_headers', {})
        record['tweetId'] = deleted_tweet_headers.get('tweetId', '.*?')
        deleted_tweet_headers = item.get('deleted_tweet_headers', {})
        record['userId'] = deleted_tweet_headers.get('userId', '.*?')
        deleted_tweet_headers = item.get('deleted_tweet_headers', {})
        record['createdAt'] = deleted_tweet_headers.get('createdAt', '.*?')
        deleted_tweet_headers = item.get('deleted_tweet_headers', {})
        record['deletedAt'] = deleted_tweet_headers.get('deletedAt', '.*?')
        records.append(record)

    df = pd.DataFrame(records)
    return df


def device_token_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['device-token.js'])

    records = []
    for item in data:
        record = {}
        device_token = item.get('device_token', {})
        record['token'] = device_token.get('token', '.*?')
        device_token = item.get('device_token', {})
        record['lastSeenAt'] = device_token.get('lastSeenAt', '.*?')
        device_token = item.get('device_token', {})
        record['clientApplicationId'] = device_token.get('clientApplicationId', '.*?')
        device_token = item.get('device_token', {})
        record['clientApplicationName'] = device_token.get('clientApplicationName', '.*?')
        device_token = item.get('device_token', {})
        record['createdAt'] = device_token.get('createdAt', '.*?')
        records.append(record)

    df = pd.DataFrame(records)
    return df


def direct_message_group_headers_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['direct-message-group-headers.js'])

    records = []
    for item in data:
        record = {}
        direct_message_group_headers = item.get('direct_message_group_headers', {})
        record['conversationId'] = direct_message_group_headers.get('conversationId', '.*?')
        direct_message_group_headers = item.get('direct_message_group_headers', {})
        record['id'] = direct_message_group_headers.get('id', '.*?')
        direct_message_group_headers = item.get('direct_message_group_headers', {})
        record['senderId'] = direct_message_group_headers.get('senderId', '.*?')
        direct_message_group_headers = item.get('direct_message_group_headers', {})
        record['createdAt'] = direct_message_group_headers.get('createdAt', '.*?')
        direct_message_group_headers = item.get('direct_message_group_headers', {})
        record['joinConversation'] = direct_message_group_headers.get('joinConversation', '.*?')
        direct_message_group_headers = item.get('direct_message_group_headers', {})
        record['participantsJoin'] = direct_message_group_headers.get('participantsJoin', '.*?')
        direct_message_group_headers = item.get('direct_message_group_headers', {})
        record['participantsLeave'] = direct_message_group_headers.get('participantsLeave', '.*?')
        records.append(record)

    df = pd.DataFrame(records)
    return df


def direct_message_headers_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['direct-message-headers.js'])

    records = []
    for item in data:
        record = {}
        direct_message_headers = item.get('direct_message_headers', {})
        record['id'] = direct_message_headers.get('id', '.*?')
        direct_message_headers = item.get('direct_message_headers', {})
        record['senderId'] = direct_message_headers.get('senderId', '.*?')
        direct_message_headers = item.get('direct_message_headers', {})
        record['recipientId'] = direct_message_headers.get('recipientId', '.*?')
        direct_message_headers = item.get('direct_message_headers', {})
        record['createdAt'] = direct_message_headers.get('createdAt', '.*?')
        records.append(record)

    df = pd.DataFrame(records)
    return df


def direct_message_mute_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['direct-message-mute.js'])

    records = []
    for item in data:
        record = {}
        direct_message_mute = item.get('direct_message_mute', {})
        record['accountId'] = direct_message_mute.get('accountId', '.*?')
        direct_message_mute = item.get('direct_message_mute', {})
        record['userLink'] = direct_message_mute.get('userLink', '.*?')
        records.append(record)

    df = pd.DataFrame(records)
    return df


def direct_messages_group_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['direct-messages-group.js'])

    records = []
    for item in data:
        record = {}
        direct_messages_group = item.get('direct_messages_group', {})
        record['conversationId'] = direct_messages_group.get('conversationId', '.*?')
        direct_messages_group = item.get('direct_messages_group', {})
        record['text'] = direct_messages_group.get('text', '.*?')
        direct_messages_group = item.get('direct_messages_group', {})
        record['mediaUrls'] = direct_messages_group.get('mediaUrls', '.*?')
        direct_messages_group = item.get('direct_messages_group', {})
        record['senderId'] = direct_messages_group.get('senderId', '.*?')
        direct_messages_group = item.get('direct_messages_group', {})
        record['id'] = direct_messages_group.get('id', '.*?')
        direct_messages_group = item.get('direct_messages_group', {})
        record['createdAt'] = direct_messages_group.get('createdAt', '.*?')
        direct_messages_group = item.get('direct_messages_group', {})
        record['reactionSenderID'] = direct_messages_group.get('reactionSenderID', '.*?')
        direct_messages_group = item.get('direct_messages_group', {})
        record['reactionKey'] = direct_messages_group.get('reactionKey', '.*?')
        direct_messages_group = item.get('direct_messages_group', {})
        record['reactionEventID'] = direct_messages_group.get('reactionEventID', '.*?')
        direct_messages_group = item.get('direct_messages_group', {})
        record['reactionCreatedAt'] = direct_messages_group.get('reactionCreatedAt', '.*?')
        direct_messages_group = item.get('direct_messages_group', {})
        record['joinConversation'] = direct_messages_group.get('joinConversation', '.*?')
        direct_messages_group = item.get('direct_messages_group', {})
        record['participantsJoin'] = direct_messages_group.get('participantsJoin', '.*?')
        direct_messages_group = item.get('direct_messages_group', {})
        record['participantsLeave'] = direct_messages_group.get('participantsLeave', '.*?')
        direct_messages_group = item.get('direct_messages_group', {})
        record['conversationNameUpdate'] = direct_messages_group.get('conversationNameUpdate', '.*?')
        records.append(record)

    df = pd.DataFrame(records)
    return df


def direct_messages_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['direct-messages.js'])

    records = []
    for item in data:
        record = {}
        direct_messages = item.get('direct_messages', {})
        record['recipientId'] = direct_messages.get('recipientId', '.*?')
        direct_messages = item.get('direct_messages', {})
        record['text'] = direct_messages.get('text', '.*?')
        direct_messages = item.get('direct_messages', {})
        record['reactionSenderID'] = direct_messages.get('reactionSenderID', '.*?')
        direct_messages = item.get('direct_messages', {})
        record['reactionKey'] = direct_messages.get('reactionKey', '.*?')
        direct_messages = item.get('direct_messages', {})
        record['reactionEventID'] = direct_messages.get('reactionEventID', '.*?')
        direct_messages = item.get('direct_messages', {})
        record['reactionCreatedAt'] = direct_messages.get('reactionCreatedAt', '.*?')
        direct_messages = item.get('direct_messages', {})
        record['mediaUrls'] = direct_messages.get('mediaUrls', '.*?')
        direct_messages = item.get('direct_messages', {})
        record['urls'] = direct_messages.get('urls', '.*?')
        direct_messages = item.get('direct_messages', {})
        record['senderId'] = direct_messages.get('senderId', '.*?')
        direct_messages = item.get('direct_messages', {})
        record['id'] = direct_messages.get('id', '.*?')
        direct_messages = item.get('direct_messages', {})
        record['createdAt'] = direct_messages.get('createdAt', '.*?')
        records.append(record)

    df = pd.DataFrame(records)
    return df


def email_address_change_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['email-address-change.js'])

    records = []
    for item in data:
        record = {}
        email_address_change = item.get('email_address_change', {})
        record['accountId'] = email_address_change.get('accountId', '.*?')
        email_address_change = item.get('email_address_change', {})
        record['changedAt'] = email_address_change.get('changedAt', '.*?')
        email_address_change = item.get('email_address_change', {})
        record['changedFrom'] = email_address_change.get('changedFrom', '.*?')
        email_address_change = item.get('email_address_change', {})
        record['changedTo'] = email_address_change.get('changedTo', '.*?')
        records.append(record)

    df = pd.DataFrame(records)
    return df


def follower_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['follower.js'])

    records = []
    for item in data:
        record = {}
        follower = item.get('follower', {})
        record['accountId'] = follower.get('accountId', '.*?')
        follower = item.get('follower', {})
        record['userLink'] = follower.get('userLink', '.*?')
        records.append(record)

    df = pd.DataFrame(records)
    return df


def following_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['following.js'])

    records = []
    for item in data:
        record = {}
        following = item.get('following', {})
        record['accountId'] = following.get('accountId', '.*?')
        following = item.get('following', {})
        record['userLink'] = following.get('userLink', '.*?')
        records.append(record)

    df = pd.DataFrame(records)
    return df


def grok_chat_item_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['grok-chat-item.js'])

    records = []
    for item in data:
        record = {}
        grok_chat_item = item.get('grok_chat_item', {})
        record['accountId'] = grok_chat_item.get('accountId', '.*?')
        grok_chat_item = item.get('grok_chat_item', {})
        record['createdAt'] = grok_chat_item.get('createdAt', '.*?')
        grok_chat_item = item.get('grok_chat_item', {})
        record['chatId'] = grok_chat_item.get('chatId', '.*?')
        grok_chat_item = item.get('grok_chat_item', {})
        record['message'] = grok_chat_item.get('message', '.*?')
        grok_chat_item = item.get('grok_chat_item', {})
        record['sender'] = grok_chat_item.get('sender', '.*?')
        grok_chat_item = item.get('grok_chat_item', {})
        record['postIds'] = grok_chat_item.get('postIds', '.*?')
        grok_chat_item = item.get('grok_chat_item', {})
        record['grokMode'] = grok_chat_item.get('grokMode', '.*?')
        records.append(record)

    df = pd.DataFrame(records)
    return df


def ip_audit_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['ip-audit.js'])

    records = []
    for item in data:
        record = {}
        ip_audit = item.get('ipAudit', {})
        record['accountId'] = ip_audit.get('accountId', '.*?')
        ip_audit = item.get('ipAudit', {})
        record['createdAt'] = ip_audit.get('createdAt', '.*?')
        ip_audit = item.get('ipAudit', {})
        record['loginIp'] = ip_audit.get('loginIp', '.*?')
        ip_audit = item.get('ipAudit', {})
        record['loginPortNumber'] = ip_audit.get('loginPortNumber', '.*?')
        records.append(record)

    df = pd.DataFrame(records)
    return df


def key_registry_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['key-registry.js'])

    records = []
    for item in data:
        record = {}
        key_registry = item.get('key_registry', {})
        record['userId'] = key_registry.get('userId', '.*?')
        key_registry = item.get('key_registry', {})
        record['deviceId'] = key_registry.get('deviceId', '.*?')
        key_registry = item.get('key_registry', {})
        record['registrationToken'] = key_registry.get('registrationToken', '.*?')
        key_registry = item.get('key_registry', {})
        record['identityKey'] = key_registry.get('identityKey', '.*?')
        key_registry = item.get('key_registry', {})
        record['userAgent'] = key_registry.get('userAgent', '.*?')
        key_registry = item.get('key_registry', {})
        record['createdAt'] = key_registry.get('createdAt', '.*?')
        records.append(record)

    df = pd.DataFrame(records)
    return df


def like_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['like.js'])

    records = []
    for item in data:
        record = {}
        like = item.get('like', {})
        record['tweetId'] = like.get('tweetId', '.*?')
        like = item.get('like', {})
        record['expandedUrl'] = like.get('expandedUrl', '.*?')
        like = item.get('like', {})
        record['fullText'] = like.get('fullText', '.*?')
        records.append(record)

    df = pd.DataFrame(records)
    return df


def lists_created_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['lists-created.js'])

    records = []
    for item in data:
        record = {}
        lists_created = item.get('lists_created', {})
        record['urls'] = lists_created.get('urls', '.*?')
        records.append(record)

    df = pd.DataFrame(records)
    return df


def lists_member_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['lists-member.js'])

    records = []
    for item in data:
        record = {}
        lists_member = item.get('lists_member', {})
        record['urls'] = lists_member.get('urls', '.*?')
        records.append(record)

    df = pd.DataFrame(records)
    return df


def lists_subscribed_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['lists-subscribed.js'])

    records = []
    for item in data:
        record = {}
        lists_subscribed = item.get('lists_subscribed', {})
        record['urls'] = lists_subscribed.get('urls', '.*?')
        records.append(record)

    df = pd.DataFrame(records)
    return df


def moment_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['moment.js'])

    records = []
    for item in data:
        record = {}
        moment = item.get('moment', {})
        record['momentId'] = moment.get('momentId', '.*?')
        moment = item.get('moment', {})
        record['createdAt'] = moment.get('createdAt', '.*?')
        moment = item.get('moment', {})
        record['createdBy'] = moment.get('createdBy', '.*?')
        moment = item.get('moment', {})
        record['title'] = moment.get('title', '.*?')
        moment = item.get('moment', {})
        record['tweets'] = moment.get('tweets', '.*?')
        moment = item.get('moment', {})
        record['description'] = moment.get('description', '.*?')
        records.append(record)

    df = pd.DataFrame(records)
    return df


def mute_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['mute.js'])

    records = []
    for item in data:
        record = {}
        mute = item.get('mute', {})
        record['accountId'] = mute.get('accountId', '.*?')
        mute = item.get('mute', {})
        record['userLink'] = mute.get('userLink', '.*?')
        records.append(record)

    df = pd.DataFrame(records)
    return df


def ni_devices_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['ni-devices.js'])

    records = []
    for item in data:
        record = {}
        ni_devices = item.get('ni_devices', {})
        record['deviceType'] = ni_devices.get('deviceType', '.*?')
        ni_devices = item.get('ni_devices', {})
        record['carrier'] = ni_devices.get('carrier', '.*?')
        ni_devices = item.get('ni_devices', {})
        record['phone_number'] = ni_devices.get('phone_number', '.*?')
        ni_devices = item.get('ni_devices', {})
        record['deviceVersion'] = ni_devices.get('deviceVersion', '.*?')
        ni_devices = item.get('ni_devices', {})
        record['createdDate'] = ni_devices.get('createdDate', '.*?')
        ni_devices = item.get('ni_devices', {})
        record['updatedDate'] = ni_devices.get('updatedDate', '.*?')
        ni_devices = item.get('ni_devices', {})
        record['udid'] = ni_devices.get('udid', '.*?')
        records.append(record)

    df = pd.DataFrame(records)
    return df


def note_tweet_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['note-tweet.js'])

    records = []
    for item in data:
        record = {}
        note_tweet = item.get('note_tweet', {})
        record['noteTweetId'] = note_tweet.get('noteTweetId', '.*?')
        note_tweet = item.get('note_tweet', {})
        record['createdAt'] = note_tweet.get('createdAt', '.*?')
        note_tweet = item.get('note_tweet', {})
        record['lifecycle'] = note_tweet.get('lifecycle', '.*?')
        note_tweet = item.get('note_tweet', {})
        record['updatedAt'] = note_tweet.get('updatedAt', '.*?')
        note_tweet = item.get('note_tweet', {})
        record['core'] = note_tweet.get('core', '.*?')
        records.append(record)

    df = pd.DataFrame(records)
    return df


def periscope_account_information_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['periscope-account-information.js'])

    records = []
    for item in data:
        record = {}
        periscope_account_information = item.get('periscope_account_information', {})
        record['id'] = periscope_account_information.get('id', '.*?')
        periscope_account_information = item.get('periscope_account_information', {})
        record['displayName'] = periscope_account_information.get('displayName', '.*?')
        periscope_account_information = item.get('periscope_account_information', {})
        record['username'] = periscope_account_information.get('username', '.*?')
        periscope_account_information = item.get('periscope_account_information', {})
        record['createdAt'] = periscope_account_information.get('createdAt', '.*?')
        periscope_account_information = item.get('periscope_account_information', {})
        record['isTwitterUser'] = periscope_account_information.get('isTwitterUser', '.*?')
        periscope_account_information = item.get('periscope_account_information', {})
        record['twitterId'] = periscope_account_information.get('twitterId', '.*?')
        periscope_account_information = item.get('periscope_account_information', {})
        record['twitterScreenName'] = periscope_account_information.get('twitterScreenName', '.*?')
        records.append(record)

    df = pd.DataFrame(records)
    return df


def periscope_ban_information_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['periscope-ban-information.js'])

    records = []
    for item in data:
        record = {}
        periscope_ban_information = item.get('periscope_ban_information', {})
        record['periscopeBanActions'] = periscope_ban_information.get('periscopeBanActions', '.*?')
        periscope_ban_information = item.get('periscope_ban_information', {})
        record['periscopeBanOverrideActions'] = periscope_ban_information.get('periscopeBanOverrideActions', '.*?')
        records.append(record)

    df = pd.DataFrame(records)
    return df


def periscope_broadcast_metadata_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['periscope-broadcast-metadata.js'])

    records = []
    for item in data:
        record = {}
        periscope_broadcast_metadata = item.get('periscope_broadcast_metadata', {})
        record['id'] = periscope_broadcast_metadata.get('id', '.*?')
        periscope_broadcast_metadata = item.get('periscope_broadcast_metadata', {})
        record['hasLocation'] = periscope_broadcast_metadata.get('hasLocation', '.*?')
        periscope_broadcast_metadata = item.get('periscope_broadcast_metadata', {})
        record['latitude'] = periscope_broadcast_metadata.get('latitude', '.*?')
        periscope_broadcast_metadata = item.get('periscope_broadcast_metadata', {})
        record['longitude'] = periscope_broadcast_metadata.get('longitude', '.*?')
        periscope_broadcast_metadata = item.get('periscope_broadcast_metadata', {})
        record['city'] = periscope_broadcast_metadata.get('city', '.*?')
        periscope_broadcast_metadata = item.get('periscope_broadcast_metadata', {})
        record['country'] = periscope_broadcast_metadata.get('country', '.*?')
        periscope_broadcast_metadata = item.get('periscope_broadcast_metadata', {})
        record['createdAt'] = periscope_broadcast_metadata.get('createdAt', '.*?')
        periscope_broadcast_metadata = item.get('periscope_broadcast_metadata', {})
        record['updatedAt'] = periscope_broadcast_metadata.get('updatedAt', '.*?')
        records.append(record)

    df = pd.DataFrame(records)
    return df


def periscope_comments_made_by_user_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['periscope-comments-made-by-user.js'])

    records = []
    for item in data:
        record = {}
        periscope_comments_made_by_user = item.get('periscope_comments_made_by_user', {})
        record['broadcastId'] = periscope_comments_made_by_user.get('broadcastId', '.*?')
        periscope_comments_made_by_user = item.get('periscope_comments_made_by_user', {})
        record['byAccountId'] = periscope_comments_made_by_user.get('byAccountId', '.*?')
        periscope_comments_made_by_user = item.get('periscope_comments_made_by_user', {})
        record['createdAt'] = periscope_comments_made_by_user.get('createdAt', '.*?')
        periscope_comments_made_by_user = item.get('periscope_comments_made_by_user', {})
        record['text'] = periscope_comments_made_by_user.get('text', '.*?')
        records.append(record)

    df = pd.DataFrame(records)
    return df


def periscope_expired_broadcasts_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['periscope-expired-broadcasts.js'])

    records = []
    for item in data:
        record = {}
        periscope_expired_broadcasts = item.get('periscope_expired_broadcasts', {})
        record['broadcastIds'] = periscope_expired_broadcasts.get('broadcastIds', '.*?')
        periscope_expired_broadcasts = item.get('periscope_expired_broadcasts', {})
        record['reason'] = periscope_expired_broadcasts.get('reason', '.*?')
        records.append(record)

    df = pd.DataFrame(records)
    return df


def periscope_profile_description_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['periscope-profile-description.js'])

    records = []
    for item in data:
        record = {}
        periscope_profile_description = item.get('periscope_profile_description', {})
        record['description'] = periscope_profile_description.get('description', '.*?')
        periscope_profile_description = item.get('periscope_profile_description', {})
        record['profileImageUrls'] = periscope_profile_description.get('profileImageUrls', '.*?')
        records.append(record)

    df = pd.DataFrame(records)
    return df


def personalization_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['personalization.js'])

    records = []
    for item in data:
        record = {}
        personalization = item.get('personalization', {})
        record['languages'] = personalization.get('languages', '.*?')
        personalization = item.get('personalization', {})
        record['genderInfo'] = personalization.get('genderInfo', '.*?')
        personalization = item.get('personalization', {})
        record['interests'] = personalization.get('interests', '.*?')
        personalization = item.get('personalization', {})
        record['partnerInterests'] = personalization.get('partnerInterests', '.*?')
        personalization = item.get('personalization', {})
        record['numAudiences'] = personalization.get('numAudiences', '.*?')
        personalization = item.get('personalization', {})
        record['advertisers'] = personalization.get('advertisers', '.*?')
        personalization = item.get('personalization', {})
        record['lookalikeAdvertisers'] = personalization.get('lookalikeAdvertisers', '.*?')
        personalization = item.get('personalization', {})
        record['inferredAgeInfo'] = personalization.get('inferredAgeInfo', '.*?')
        personalization = item.get('personalization', {})
        record['locationHistory'] = personalization.get('locationHistory', '.*?')
        personalization = item.get('personalization', {})
        record['shows'] = personalization.get('shows', '.*?')
        personalization = item.get('personalization', {})
        record['doNotReachAdvertisers'] = personalization.get('doNotReachAdvertisers', '.*?')
        personalization = item.get('personalization', {})
        record['ageInfo'] = personalization.get('ageInfo', '.*?')
        records.append(record)

    df = pd.DataFrame(records)
    return df


def phone_number_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['phone-number.js'])

    records = []
    for item in data:
        record = {}
        phone_number = item.get('phone_number', {})
        record['phoneNumber'] = phone_number.get('phoneNumber', '.*?')
        records.append(record)

    df = pd.DataFrame(records)
    return df


def product_drop_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['product-drop.js'])

    records = []
    for item in data:
        record = {}
        product_drop = item.get('product_drop', {})
        record['id'] = product_drop.get('id', '.*?')
        product_drop = item.get('product_drop', {})
        record['userId'] = product_drop.get('userId', '.*?')
        product_drop = item.get('product_drop', {})
        record['productSetId'] = product_drop.get('productSetId', '.*?')
        product_drop = item.get('product_drop', {})
        record['hashtag'] = product_drop.get('hashtag', '.*?')
        product_drop = item.get('product_drop', {})
        record['dropTime'] = product_drop.get('dropTime', '.*?')
        records.append(record)

    df = pd.DataFrame(records)
    return df


def product_set_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['product-set.js'])

    records = []
    for item in data:
        record = {}
        product_set = item.get('product_set', {})
        record['productSetId'] = product_set.get('productSetId', '.*?')
        product_set = item.get('product_set', {})
        record['catalogId'] = product_set.get('catalogId', '.*?')
        product_set = item.get('product_set', {})
        record['productSetType'] = product_set.get('productSetType', '.*?')
        product_set = item.get('product_set', {})
        record['name'] = product_set.get('name', '.*?')
        product_set = item.get('product_set', {})
        record['description'] = product_set.get('description', '.*?')
        product_set = item.get('product_set', {})
        record['lastUpdatedAt'] = product_set.get('lastUpdatedAt', '.*?')
        product_set = item.get('product_set', {})
        record['items'] = product_set.get('items', '.*?')
        records.append(record)

    df = pd.DataFrame(records)
    return df


def professional_data_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['professional_data.js'])

    records = []
    for item in data:
        record = {}
        professional_data = item.get('professional_data', {})
        record['accountId'] = professional_data.get('accountId', '.*?')
        professional_data = item.get('professional_data', {})
        record['professionalId'] = professional_data.get('professionalId', '.*?')
        professional_data = item.get('professional_data', {})
        record['professionalType'] = professional_data.get('professionalType', '.*?')
        professional_data = item.get('professional_data', {})
        record['categoryName'] = professional_data.get('categoryName', '.*?')
        professional_data = item.get('professional_data', {})
        record['setToDisplay'] = professional_data.get('setToDisplay', '.*?')
        professional_data = item.get('professional_data', {})
        record['createdAt'] = professional_data.get('createdAt', '.*?')
        professional_data = item.get('professional_data', {})
        record['creationSource'] = professional_data.get('creationSource', '.*?')
        professional_data = item.get('professional_data', {})
        record['moduleId'] = professional_data.get('moduleId', '.*?')
        professional_data = item.get('professional_data', {})
        record['website'] = professional_data.get('website', '.*?')
        professional_data = item.get('professional_data', {})
        record['addresssLine1'] = professional_data.get('addresssLine1', '.*?')
        professional_data = item.get('professional_data', {})
        record['city'] = professional_data.get('city', '.*?')
        professional_data = item.get('professional_data', {})
        record['administrativeArea'] = professional_data.get('administrativeArea', '.*?')
        professional_data = item.get('professional_data', {})
        record['postalCode'] = professional_data.get('postalCode', '.*?')
        professional_data = item.get('professional_data', {})
        record['country'] = professional_data.get('country', '.*?')
        professional_data = item.get('professional_data', {})
        record['phone'] = professional_data.get('phone', '.*?')
        professional_data = item.get('professional_data', {})
        record['countryCode'] = professional_data.get('countryCode', '.*?')
        professional_data = item.get('professional_data', {})
        record['number'] = professional_data.get('number', '.*?')
        professional_data = item.get('professional_data', {})
        record['email'] = professional_data.get('email', '.*?')
        professional_data = item.get('professional_data', {})
        record['timezone'] = professional_data.get('timezone', '.*?')
        professional_data = item.get('professional_data', {})
        record['openTimes'] = professional_data.get('openTimes', '.*?')
        professional_data = item.get('professional_data', {})
        record['openTimesType'] = professional_data.get('openTimesType', '.*?')
        professional_data = item.get('professional_data', {})
        record['regular'] = professional_data.get('regular', '.*?')
        professional_data = item.get('professional_data', {})
        record['weekday'] = professional_data.get('weekday', '.*?')
        professional_data = item.get('professional_data', {})
        record['slots'] = professional_data.get('slots', '.*?')
        professional_data = item.get('professional_data', {})
        record['hourOpen'] = professional_data.get('hourOpen', '.*?')
        professional_data = item.get('professional_data', {})
        record['minuteOpen'] = professional_data.get('minuteOpen', '.*?')
        professional_data = item.get('professional_data', {})
        record['hourClose'] = professional_data.get('hourClose', '.*?')
        professional_data = item.get('professional_data', {})
        record['minuteClose'] = professional_data.get('minuteClose', '.*?')
        professional_data = item.get('professional_data', {})
        record['appleAppStore'] = professional_data.get('appleAppStore', '.*?')
        professional_data = item.get('professional_data', {})
        record['googlePlayStore'] = professional_data.get('googlePlayStore', '.*?')
        professional_data = item.get('professional_data', {})
        record['rawUrl'] = professional_data.get('rawUrl', '.*?')
        professional_data = item.get('professional_data', {})
        record['ctaDisplay'] = professional_data.get('ctaDisplay', '.*?')
        records.append(record)

    df = pd.DataFrame(records)
    return df


def profile_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['profile.js'])

    records = []
    for item in data:
        record = {}
        profile = item.get('profile', {})
        record['bio'] = profile.get('bio', '.*?')
        profile = item.get('profile', {})
        record['website'] = profile.get('website', '.*?')
        profile = item.get('profile', {})
        record['location'] = profile.get('location', '.*?')
        profile = item.get('profile', {})
        record['avatarMediaUrl'] = profile.get('avatarMediaUrl', '.*?')
        profile = item.get('profile', {})
        record['headerMediaUrl'] = profile.get('headerMediaUrl', '.*?')
        records.append(record)

    df = pd.DataFrame(records)
    return df


def protected_history_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['protected-history.js'])

    records = []
    for item in data:
        record = {}
        protected_history = item.get('protected_history', {})
        record['protectedAt'] = protected_history.get('protectedAt', '.*?')
        protected_history = item.get('protected_history', {})
        record['action'] = protected_history.get('action', '.*?')
        records.append(record)

    df = pd.DataFrame(records)
    return df


def reply_prompt_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['reply-prompt.js'])

    records = []
    for item in data:
        record = {}
        reply_prompt = item.get('reply_prompt', {})
        record['promptId'] = reply_prompt.get('promptId', '.*?')
        reply_prompt = item.get('reply_prompt', {})
        record['userId'] = reply_prompt.get('userId', '.*?')
        reply_prompt = item.get('reply_prompt', {})
        record['proposedTweetText'] = reply_prompt.get('proposedTweetText', '.*?')
        reply_prompt = item.get('reply_prompt', {})
        record['inReplyToTweetId'] = reply_prompt.get('inReplyToTweetId', '.*?')
        reply_prompt = item.get('reply_prompt', {})
        record['createdAt'] = reply_prompt.get('createdAt', '.*?')
        reply_prompt = item.get('reply_prompt', {})
        record['promptActionType'] = reply_prompt.get('promptActionType', '.*?')
        records.append(record)

    df = pd.DataFrame(records)
    return df


def saved_search_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['saved-search.js'])

    records = []
    for item in data:
        record = {}
        saved_search = item.get('saved_search', {})
        record['savedSearchId'] = saved_search.get('savedSearchId', '.*?')
        saved_search = item.get('saved_search', {})
        record['query'] = saved_search.get('query', '.*?')
        records.append(record)

    df = pd.DataFrame(records)
    return df


def screen_name_change_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['screen-name-change.js'])

    records = []
    for item in data:
        record = {}
        screen_name_change = item.get('screen_name_change', {})
        record['accountId'] = screen_name_change.get('accountId', '.*?')
        screen_name_change = item.get('screen_name_change', {})
        record['changedAt'] = screen_name_change.get('changedAt', '.*?')
        screen_name_change = item.get('screen_name_change', {})
        record['changedFrom'] = screen_name_change.get('changedFrom', '.*?')
        screen_name_change = item.get('screen_name_change', {})
        record['changedTo'] = screen_name_change.get('changedTo', '.*?')
        records.append(record)

    df = pd.DataFrame(records)
    return df


def shop_module_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['shop-module.js'])

    records = []
    for item in data:
        record = {}
        shop_module = item.get('shop_module', {})
        record['moduleId'] = shop_module.get('moduleId', '.*?')
        shop_module = item.get('shop_module', {})
        record['userId'] = shop_module.get('userId', '.*?')
        shop_module = item.get('shop_module', {})
        record['isEnabled'] = shop_module.get('isEnabled', '.*?')
        shop_module = item.get('shop_module', {})
        record['productSetIds'] = shop_module.get('productSetIds', '.*?')
        shop_module = item.get('shop_module', {})
        record['displayType'] = shop_module.get('displayType', '.*?')
        records.append(record)

    df = pd.DataFrame(records)
    return df


def shopify_account_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['shopify-account.js'])

    records = []
    for item in data:
        record = {}
        shopify_account = item.get('shopify_account', {})
        record['shopDomain'] = shopify_account.get('shopDomain', '.*?')
        shopify_account = item.get('shopify_account', {})
        record['termsOfServiceAccepted'] = shopify_account.get('termsOfServiceAccepted', '.*?')
        shopify_account = item.get('shopify_account', {})
        record['appOnboardingComplete'] = shopify_account.get('appOnboardingComplete', '.*?')
        shopify_account = item.get('shopify_account', {})
        record['userId'] = shopify_account.get('userId', '.*?')
        shopify_account = item.get('shopify_account', {})
        record['catalogId'] = shopify_account.get('catalogId', '.*?')
        shopify_account = item.get('shopify_account', {})
        record['shopCurrency'] = shopify_account.get('shopCurrency', '.*?')
        shopify_account = item.get('shopify_account', {})
        record['createdAt'] = shopify_account.get('createdAt', '.*?')
        shopify_account = item.get('shopify_account', {})
        record['updatedAt'] = shopify_account.get('updatedAt', '.*?')
        records.append(record)

    df = pd.DataFrame(records)
    return df


def smartblock_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['smartblock.js'])

    records = []
    for item in data:
        record = {}
        smartblock = item.get('smartblock', {})
        record['accountId'] = smartblock.get('accountId', '.*?')
        smartblock = item.get('smartblock', {})
        record['userLink'] = smartblock.get('userLink', '.*?')
        smartblock = item.get('smartblock', {})
        record['createdAt'] = smartblock.get('createdAt', '.*?')
        smartblock = item.get('smartblock', {})
        record['expiresAt'] = smartblock.get('expiresAt', '.*?')
        smartblock = item.get('smartblock', {})
        record['ttl'] = smartblock.get('ttl', '.*?')
        records.append(record)

    df = pd.DataFrame(records)
    return df


def spaces_metadata_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['spaces-metadata.js'])

    records = []
    for item in data:
        record = {}
        spaces_metadata = item.get('spaces_metadata', {})
        record['id'] = spaces_metadata.get('id', '.*?')
        spaces_metadata = item.get('spaces_metadata', {})
        record['creatorUserId'] = spaces_metadata.get('creatorUserId', '.*?')
        spaces_metadata = item.get('spaces_metadata', {})
        record['hostUserIds'] = spaces_metadata.get('hostUserIds', '.*?')
        spaces_metadata = item.get('spaces_metadata', {})
        record['speakers'] = spaces_metadata.get('speakers', '.*?')
        spaces_metadata = item.get('spaces_metadata', {})
        record['createdAt'] = spaces_metadata.get('createdAt', '.*?')
        spaces_metadata = item.get('spaces_metadata', {})
        record['endedAt'] = spaces_metadata.get('endedAt', '.*?')
        spaces_metadata = item.get('spaces_metadata', {})
        record['totalParticipating'] = spaces_metadata.get('totalParticipating', '.*?')
        spaces_metadata = item.get('spaces_metadata', {})
        record['totalParticipated'] = spaces_metadata.get('totalParticipated', '.*?')
        spaces_metadata = item.get('spaces_metadata', {})
        record['invitedUserIds'] = spaces_metadata.get('invitedUserIds', '.*?')
        records.append(record)

    df = pd.DataFrame(records)
    return df


def sso_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['sso.js'])

    records = []
    for item in data:
        record = {}
        sso = item.get('sso', {})
        record['ssoId'] = sso.get('ssoId', '.*?')
        sso = item.get('sso', {})
        record['ssoEmail'] = sso.get('ssoEmail', '.*?')
        sso = item.get('sso', {})
        record['associationMethodType'] = sso.get('associationMethodType', '.*?')
        sso = item.get('sso', {})
        record['createdAt'] = sso.get('createdAt', '.*?')
        records.append(record)

    df = pd.DataFrame(records)
    return df


def tweet_headers_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['tweet-headers.js'])

    records = []
    for item in data:
        record = {}
        tweet_headers = item.get('tweet_headers', {})
        record['tweetId'] = tweet_headers.get('tweetId', '.*?')
        tweet_headers = item.get('tweet_headers', {})
        record['userId'] = tweet_headers.get('userId', '.*?')
        tweet_headers = item.get('tweet_headers', {})
        record['createdAt'] = tweet_headers.get('createdAt', '.*?')
        records.append(record)

    df = pd.DataFrame(records)
    return df


def tweetdeck_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['tweetdeck.js'])

    records = []
    for item in data:
        record = {}
        tweetdeck = item.get('tweetdeck', {})
        record['title'] = tweetdeck.get('title', '.*?')
        tweetdeck = item.get('tweetdeck', {})
        record['columns'] = tweetdeck.get('columns', '.*?')
        tweetdeck = item.get('tweetdeck', {})
        record['pathname'] = tweetdeck.get('pathname', '.*?')
        records.append(record)

    df = pd.DataFrame(records)
    return df


def twitter_shop_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['twitter-shop.js'])

    records = []
    for item in data:
        record = {}
        twitter_shop = item.get('twitter_shop', {})
        record['shopId'] = twitter_shop.get('shopId', '.*?')
        twitter_shop = item.get('twitter_shop', {})
        record['userId'] = twitter_shop.get('userId', '.*?')
        twitter_shop = item.get('twitter_shop', {})
        record['isEnabled'] = twitter_shop.get('isEnabled', '.*?')
        twitter_shop = item.get('twitter_shop', {})
        record['name'] = twitter_shop.get('name', '.*?')
        twitter_shop = item.get('twitter_shop', {})
        record['description'] = twitter_shop.get('description', '.*?')
        twitter_shop = item.get('twitter_shop', {})
        record['productSetIds'] = twitter_shop.get('productSetIds', '.*?')
        records.append(record)

    df = pd.DataFrame(records)
    return df


def user_link_clicks_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['user-link-clicks.js'])

    records = []
    for item in data:
        record = {}
        user_link_clicks = item.get('user_link_clicks', {})
        record['tweetId'] = user_link_clicks.get('tweetId', '.*?')
        user_link_clicks = item.get('user_link_clicks', {})
        record['finalUrl'] = user_link_clicks.get('finalUrl', '.*?')
        user_link_clicks = item.get('user_link_clicks', {})
        record['timeStampOfInteraction'] = user_link_clicks.get('timeStampOfInteraction', '.*?')
        records.append(record)

    df = pd.DataFrame(records)
    return df


def verified_organization_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['verified-organization.js'])

    records = []
    for item in data:
        record = {}
        verified_organization = item.get('verified_organization', {})
        record['affiliatedToAccounts'] = verified_organization.get('affiliatedToAccounts', '.*?')
        verified_organization = item.get('verified_organization', {})
        record['affiliates'] = verified_organization.get('affiliates', '.*?')
        verified_organization = item.get('verified_organization', {})
        record['screenName'] = verified_organization.get('screenName', '.*?')
        verified_organization = item.get('verified_organization', {})
        record['verfiedType'] = verified_organization.get('verfiedType', '.*?')
        verified_organization = item.get('verified_organization', {})
        record['createdAt'] = verified_organization.get('createdAt', '.*?')
        records.append(record)

    df = pd.DataFrame(records)
    return df


def verified_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['verified.js'])

    records = []
    for item in data:
        record = {}
        verified = item.get('verified', {})
        record['accountId'] = verified.get('accountId', '.*?')
        verified = item.get('verified', {})
        record['verified'] = verified.get('verified', '.*?')
        records.append(record)

    df = pd.DataFrame(records)
    return df


def create_donation_flow(file_input: list[str]):
    """Create a donation flow for Twitter data."""
    tables = []

    try:
        df = account_creation_ip_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='account_creation_ip', df=df, title={'en': 'account_creation_ip'})
            )
    except Exception as e:
        logger.error(f'Skipping account_creation_ip_df: {e}')

    try:
        df = account_label_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='account_label', df=df, title={'en': 'account_label'})
            )
    except Exception as e:
        logger.error(f'Skipping account_label_df: {e}')

    try:
        df = account_suspension_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='account_suspension', df=df, title={'en': 'account_suspension'})
            )
    except Exception as e:
        logger.error(f'Skipping account_suspension_df: {e}')

    try:
        df = account_timezone_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='account_timezone', df=df, title={'en': 'account_timezone'})
            )
    except Exception as e:
        logger.error(f'Skipping account_timezone_df: {e}')

    try:
        df = account_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='account', df=df, title={'en': 'account'})
            )
    except Exception as e:
        logger.error(f'Skipping account_df: {e}')

    try:
        df = ad_engagements_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='ad_engagements', df=df, title={'en': 'ad_engagements'})
            )
    except Exception as e:
        logger.error(f'Skipping ad_engagements_df: {e}')

    try:
        df = ad_impressions_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='ad_impressions', df=df, title={'en': 'ad_impressions'})
            )
    except Exception as e:
        logger.error(f'Skipping ad_impressions_df: {e}')

    try:
        df = ad_mobile_conversions_attributed_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='ad_mobile_conversions_attributed', df=df, title={'en': 'ad_mobile_conversions_attributed'})
            )
    except Exception as e:
        logger.error(f'Skipping ad_mobile_conversions_attributed_df: {e}')

    try:
        df = ad_mobile_conversions_unattributed_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='ad_mobile_conversions_unattributed', df=df, title={'en': 'ad_mobile_conversions_unattributed'})
            )
    except Exception as e:
        logger.error(f'Skipping ad_mobile_conversions_unattributed_df: {e}')

    try:
        df = ad_online_conversions_attributed_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='ad_online_conversions_attributed', df=df, title={'en': 'ad_online_conversions_attributed'})
            )
    except Exception as e:
        logger.error(f'Skipping ad_online_conversions_attributed_df: {e}')

    try:
        df = ad_online_conversions_unattributed_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='ad_online_conversions_unattributed', df=df, title={'en': 'ad_online_conversions_unattributed'})
            )
    except Exception as e:
        logger.error(f'Skipping ad_online_conversions_unattributed_df: {e}')

    try:
        df = ads_revenue_sharing_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='ads_revenue_sharing', df=df, title={'en': 'ads_revenue_sharing'})
            )
    except Exception as e:
        logger.error(f'Skipping ads_revenue_sharing_df: {e}')

    try:
        df = app_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='app', df=df, title={'en': 'app'})
            )
    except Exception as e:
        logger.error(f'Skipping app_df: {e}')

    try:
        df = article_metadata_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='article_metadata', df=df, title={'en': 'article_metadata'})
            )
    except Exception as e:
        logger.error(f'Skipping article_metadata_df: {e}')

    try:
        df = article_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='article', df=df, title={'en': 'article'})
            )
    except Exception as e:
        logger.error(f'Skipping article_df: {e}')

    try:
        df = audio_video_calls_in_dm_recipient_sessions_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='audio_video_calls_in_dm_recipient_sessions', df=df, title={'en': 'audio_video_calls_in_dm_recipient_sessions'})
            )
    except Exception as e:
        logger.error(f'Skipping audio_video_calls_in_dm_recipient_sessions_df: {e}')

    try:
        df = audio_video_calls_in_dm_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='audio_video_calls_in_dm', df=df, title={'en': 'audio_video_calls_in_dm'})
            )
    except Exception as e:
        logger.error(f'Skipping audio_video_calls_in_dm_df: {e}')

    try:
        df = block_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='block', df=df, title={'en': 'block'})
            )
    except Exception as e:
        logger.error(f'Skipping block_df: {e}')

    try:
        df = branch_links_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='branch_links', df=df, title={'en': 'branch_links'})
            )
    except Exception as e:
        logger.error(f'Skipping branch_links_df: {e}')

    try:
        df = catalog_item_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='catalog_item', df=df, title={'en': 'catalog_item'})
            )
    except Exception as e:
        logger.error(f'Skipping catalog_item_df: {e}')

    try:
        df = commerce_catalog_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='commerce_catalog', df=df, title={'en': 'commerce_catalog'})
            )
    except Exception as e:
        logger.error(f'Skipping commerce_catalog_df: {e}')

    try:
        df = community_note_rating_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='community_note_rating', df=df, title={'en': 'community_note_rating'})
            )
    except Exception as e:
        logger.error(f'Skipping community_note_rating_df: {e}')

    try:
        df = community_note_tombstone_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='community_note_tombstone', df=df, title={'en': 'community_note_tombstone'})
            )
    except Exception as e:
        logger.error(f'Skipping community_note_tombstone_df: {e}')

    try:
        df = community_note_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='community_note', df=df, title={'en': 'community_note'})
            )
    except Exception as e:
        logger.error(f'Skipping community_note_df: {e}')

    try:
        df = connected_application_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='connected_application', df=df, title={'en': 'connected_application'})
            )
    except Exception as e:
        logger.error(f'Skipping connected_application_df: {e}')

    try:
        df = contact_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='contact', df=df, title={'en': 'contact'})
            )
    except Exception as e:
        logger.error(f'Skipping contact_df: {e}')

    try:
        df = deleted_note_tweet_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='deleted_note_tweet', df=df, title={'en': 'deleted_note_tweet'})
            )
    except Exception as e:
        logger.error(f'Skipping deleted_note_tweet_df: {e}')

    try:
        df = deleted_tweet_headers_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='deleted_tweet_headers', df=df, title={'en': 'deleted_tweet_headers'})
            )
    except Exception as e:
        logger.error(f'Skipping deleted_tweet_headers_df: {e}')

    try:
        df = device_token_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='device_token', df=df, title={'en': 'device_token'})
            )
    except Exception as e:
        logger.error(f'Skipping device_token_df: {e}')

    try:
        df = direct_message_group_headers_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='direct_message_group_headers', df=df, title={'en': 'direct_message_group_headers'})
            )
    except Exception as e:
        logger.error(f'Skipping direct_message_group_headers_df: {e}')

    try:
        df = direct_message_headers_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='direct_message_headers', df=df, title={'en': 'direct_message_headers'})
            )
    except Exception as e:
        logger.error(f'Skipping direct_message_headers_df: {e}')

    try:
        df = direct_message_mute_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='direct_message_mute', df=df, title={'en': 'direct_message_mute'})
            )
    except Exception as e:
        logger.error(f'Skipping direct_message_mute_df: {e}')

    try:
        df = direct_messages_group_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='direct_messages_group', df=df, title={'en': 'direct_messages_group'})
            )
    except Exception as e:
        logger.error(f'Skipping direct_messages_group_df: {e}')

    try:
        df = direct_messages_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='direct_messages', df=df, title={'en': 'direct_messages'})
            )
    except Exception as e:
        logger.error(f'Skipping direct_messages_df: {e}')

    try:
        df = email_address_change_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='email_address_change', df=df, title={'en': 'email_address_change'})
            )
    except Exception as e:
        logger.error(f'Skipping email_address_change_df: {e}')

    try:
        df = follower_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='follower', df=df, title={'en': 'follower'})
            )
    except Exception as e:
        logger.error(f'Skipping follower_df: {e}')

    try:
        df = following_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='following', df=df, title={'en': 'following'})
            )
    except Exception as e:
        logger.error(f'Skipping following_df: {e}')

    try:
        df = grok_chat_item_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='grok_chat_item', df=df, title={'en': 'grok_chat_item'})
            )
    except Exception as e:
        logger.error(f'Skipping grok_chat_item_df: {e}')

    try:
        df = ip_audit_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='ip_audit', df=df, title={'en': 'ip_audit'})
            )
    except Exception as e:
        logger.error(f'Skipping ip_audit_df: {e}')

    try:
        df = key_registry_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='key_registry', df=df, title={'en': 'key_registry'})
            )
    except Exception as e:
        logger.error(f'Skipping key_registry_df: {e}')

    try:
        df = like_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='like', df=df, title={'en': 'like'})
            )
    except Exception as e:
        logger.error(f'Skipping like_df: {e}')

    try:
        df = lists_created_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='lists_created', df=df, title={'en': 'lists_created'})
            )
    except Exception as e:
        logger.error(f'Skipping lists_created_df: {e}')

    try:
        df = lists_member_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='lists_member', df=df, title={'en': 'lists_member'})
            )
    except Exception as e:
        logger.error(f'Skipping lists_member_df: {e}')

    try:
        df = lists_subscribed_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='lists_subscribed', df=df, title={'en': 'lists_subscribed'})
            )
    except Exception as e:
        logger.error(f'Skipping lists_subscribed_df: {e}')

    try:
        df = moment_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='moment', df=df, title={'en': 'moment'})
            )
    except Exception as e:
        logger.error(f'Skipping moment_df: {e}')

    try:
        df = mute_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='mute', df=df, title={'en': 'mute'})
            )
    except Exception as e:
        logger.error(f'Skipping mute_df: {e}')

    try:
        df = ni_devices_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='ni_devices', df=df, title={'en': 'ni_devices'})
            )
    except Exception as e:
        logger.error(f'Skipping ni_devices_df: {e}')

    try:
        df = note_tweet_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='note_tweet', df=df, title={'en': 'note_tweet'})
            )
    except Exception as e:
        logger.error(f'Skipping note_tweet_df: {e}')

    try:
        df = periscope_account_information_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='periscope_account_information', df=df, title={'en': 'periscope_account_information'})
            )
    except Exception as e:
        logger.error(f'Skipping periscope_account_information_df: {e}')

    try:
        df = periscope_ban_information_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='periscope_ban_information', df=df, title={'en': 'periscope_ban_information'})
            )
    except Exception as e:
        logger.error(f'Skipping periscope_ban_information_df: {e}')

    try:
        df = periscope_broadcast_metadata_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='periscope_broadcast_metadata', df=df, title={'en': 'periscope_broadcast_metadata'})
            )
    except Exception as e:
        logger.error(f'Skipping periscope_broadcast_metadata_df: {e}')

    try:
        df = periscope_comments_made_by_user_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='periscope_comments_made_by_user', df=df, title={'en': 'periscope_comments_made_by_user'})
            )
    except Exception as e:
        logger.error(f'Skipping periscope_comments_made_by_user_df: {e}')

    try:
        df = periscope_expired_broadcasts_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='periscope_expired_broadcasts', df=df, title={'en': 'periscope_expired_broadcasts'})
            )
    except Exception as e:
        logger.error(f'Skipping periscope_expired_broadcasts_df: {e}')

    try:
        df = periscope_profile_description_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='periscope_profile_description', df=df, title={'en': 'periscope_profile_description'})
            )
    except Exception as e:
        logger.error(f'Skipping periscope_profile_description_df: {e}')

    try:
        df = personalization_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='personalization', df=df, title={'en': 'personalization'})
            )
    except Exception as e:
        logger.error(f'Skipping personalization_df: {e}')

    try:
        df = phone_number_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='phone_number', df=df, title={'en': 'phone_number'})
            )
    except Exception as e:
        logger.error(f'Skipping phone_number_df: {e}')

    try:
        df = product_drop_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='product_drop', df=df, title={'en': 'product_drop'})
            )
    except Exception as e:
        logger.error(f'Skipping product_drop_df: {e}')

    try:
        df = product_set_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='product_set', df=df, title={'en': 'product_set'})
            )
    except Exception as e:
        logger.error(f'Skipping product_set_df: {e}')

    try:
        df = professional_data_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='professional_data', df=df, title={'en': 'professional_data'})
            )
    except Exception as e:
        logger.error(f'Skipping professional_data_df: {e}')

    try:
        df = profile_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='profile', df=df, title={'en': 'profile'})
            )
    except Exception as e:
        logger.error(f'Skipping profile_df: {e}')

    try:
        df = protected_history_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='protected_history', df=df, title={'en': 'protected_history'})
            )
    except Exception as e:
        logger.error(f'Skipping protected_history_df: {e}')

    try:
        df = reply_prompt_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='reply_prompt', df=df, title={'en': 'reply_prompt'})
            )
    except Exception as e:
        logger.error(f'Skipping reply_prompt_df: {e}')

    try:
        df = saved_search_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='saved_search', df=df, title={'en': 'saved_search'})
            )
    except Exception as e:
        logger.error(f'Skipping saved_search_df: {e}')

    try:
        df = screen_name_change_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='screen_name_change', df=df, title={'en': 'screen_name_change'})
            )
    except Exception as e:
        logger.error(f'Skipping screen_name_change_df: {e}')

    try:
        df = shop_module_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='shop_module', df=df, title={'en': 'shop_module'})
            )
    except Exception as e:
        logger.error(f'Skipping shop_module_df: {e}')

    try:
        df = shopify_account_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='shopify_account', df=df, title={'en': 'shopify_account'})
            )
    except Exception as e:
        logger.error(f'Skipping shopify_account_df: {e}')

    try:
        df = smartblock_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='smartblock', df=df, title={'en': 'smartblock'})
            )
    except Exception as e:
        logger.error(f'Skipping smartblock_df: {e}')

    try:
        df = spaces_metadata_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='spaces_metadata', df=df, title={'en': 'spaces_metadata'})
            )
    except Exception as e:
        logger.error(f'Skipping spaces_metadata_df: {e}')

    try:
        df = sso_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='sso', df=df, title={'en': 'sso'})
            )
    except Exception as e:
        logger.error(f'Skipping sso_df: {e}')

    try:
        df = tweet_headers_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='tweet_headers', df=df, title={'en': 'tweet_headers'})
            )
    except Exception as e:
        logger.error(f'Skipping tweet_headers_df: {e}')

    try:
        df = tweetdeck_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='tweetdeck', df=df, title={'en': 'tweetdeck'})
            )
    except Exception as e:
        logger.error(f'Skipping tweetdeck_df: {e}')

    try:
        df = twitter_shop_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='twitter_shop', df=df, title={'en': 'twitter_shop'})
            )
    except Exception as e:
        logger.error(f'Skipping twitter_shop_df: {e}')

    try:
        df = user_link_clicks_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='user_link_clicks', df=df, title={'en': 'user_link_clicks'})
            )
    except Exception as e:
        logger.error(f'Skipping user_link_clicks_df: {e}')

    try:
        df = verified_organization_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='verified_organization', df=df, title={'en': 'verified_organization'})
            )
    except Exception as e:
        logger.error(f'Skipping verified_organization_df: {e}')

    try:
        df = verified_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='verified', df=df, title={'en': 'verified'})
            )
    except Exception as e:
        logger.error(f'Skipping verified_df: {e}')

    if tables:
        return donation_flow(id='twitter', tables=tables)
    else:
        return None