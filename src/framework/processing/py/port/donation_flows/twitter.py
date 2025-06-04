# Auto-generated Twitter extractors

import pandas as pd
import json
import logging
import io
import zipfile
import re
from port.helpers.donation_flow import donation_table, donation_flow

from port.structure_extractor_libraries.X_get_json_structure import structure_from_zip

logger = logging.getLogger(__name__)

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

def snake_case(name: str) -> str:
    return name.lower().replace("-", "_").replace(".json", "").replace(".js", "").replace(" ", "_")

def extract_path(row) -> list[str]:
    path = []
    if pd.notna(row.get("row_path")):
        path.append(str(row["row_path"]).strip())
    for i in range(1, 6):
        col_val = row.get(f"col_path_{i}")
        if pd.notna(col_val):
            path.append(str(col_val).strip())
    return path

def get_field_name(row) -> str:
    for i in reversed(range(1, 6)):
        val = row.get(f"col_path_{i}")
        if pd.notna(val):
            return str(val).strip()
    return None

def read_js(file_input: list[str], target_files: list[str]) -> list[dict]:
    extracted_data = []
    for zip_path in file_input:
        with zipfile.ZipFile(zip_path, "r") as z:
            for target_file in target_files:
                js_files = [f for f in z.namelist() if target_file in f]
                if js_files:
                    with z.open(js_files[0]) as raw_file:
                        with io.TextIOWrapper(raw_file, encoding="utf8") as text_file:
                            lines = text_file.readlines()
                        lines[0] = re.sub(r"^.*? = ", "", lines[0])
                        try:
                            data = json.loads("".join(lines))
                            extracted_data.extend(data)
                        except json.JSONDecodeError as e:
                            logger.error(f"Error decoding {target_file} in {zip_path}: {e}")
    return extracted_data

def account_creation_ip_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['account-creation-ip.js'])
    records = []
    for item in data:
        record = {}
        record['accountId'] = get_in(item, 'accountCreationIp', 'accountId')
        record['userCreationIp'] = get_in(item, 'accountCreationIp', 'userCreationIp')
        records.append(record)
    df = pd.DataFrame(records)
    return df


def account_label_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['account-label.js'])
    records = []
    for item in data:
        record = {}
        records.append(record)
    df = pd.DataFrame(records)
    return df


def account_suspension_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['account-suspension.js'])
    records = []
    for item in data:
        record = {}
        records.append(record)
    df = pd.DataFrame(records)
    return df


def account_timezone_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['account-timezone.js'])
    records = []
    for item in data:
        record = {}
        record['accountId'] = get_in(item, 'accountTimezone', 'accountId')
        records.append(record)
    df = pd.DataFrame(records)
    return df


def account_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['account.js'])
    records = []
    for item in data:
        record = {}
        record['accountDisplayName'] = get_in(item, 'account', 'accountDisplayName')
        record['accountId'] = get_in(item, 'account', 'accountId')
        record['createdAt'] = get_in(item, 'account', 'createdAt')
        record['createdVia'] = get_in(item, 'account', 'createdVia')
        record['email'] = get_in(item, 'account', 'email')
        record['username'] = get_in(item, 'account', 'username')
        records.append(record)
    df = pd.DataFrame(records)
    return df


def ad_engagements_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['ad-engagements.js'])
    records = []
    for item in data:
        record = {}
        records.append(record)
    df = pd.DataFrame(records)
    return df


def ad_impressions_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['ad-impressions.js'])
    records = []
    for item in data:
        record = {}
        records.append(record)
    df = pd.DataFrame(records)
    return df


def ad_mobile_conversions_attributed_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['ad-mobile-conversions-attributed.js'])
    records = []
    for item in data:
        record = {}
        records.append(record)
    df = pd.DataFrame(records)
    return df


def ad_mobile_conversions_unattributed_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['ad-mobile-conversions-unattributed.js'])
    records = []
    for item in data:
        record = {}
        records.append(record)
    df = pd.DataFrame(records)
    return df


def ad_online_conversions_attributed_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['ad-online-conversions-attributed.js'])
    records = []
    for item in data:
        record = {}
        records.append(record)
    df = pd.DataFrame(records)
    return df


def ad_online_conversions_unattributed_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['ad-online-conversions-unattributed.js'])
    records = []
    for item in data:
        record = {}
        records.append(record)
    df = pd.DataFrame(records)
    return df


def ads_revenue_sharing_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['ads-revenue-sharing.js'])
    records = []
    for item in data:
        record = {}
        record['payoutHistory'] = get_in(item, 'adsRevenueSharing', 'payoutHistory')
        records.append(record)
    df = pd.DataFrame(records)
    return df


def ageinfo_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['ageinfo.js'])
    records = []
    for item in data:
        record = {}
        record['age'] = get_in(item, 'ageMeta', 'ageInfo', 'age')
        record['birthDate'] = get_in(item, 'ageMeta', 'ageInfo', 'birthDate')
        records.append(record)
    df = pd.DataFrame(records)
    return df


def app_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['app.js'])
    records = []
    for item in data:
        record = {}
        records.append(record)
    df = pd.DataFrame(records)
    return df


def article_metadata_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['article-metadata.js'])
    records = []
    for item in data:
        record = {}
        records.append(record)
    df = pd.DataFrame(records)
    return df


def article_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['article.js'])
    records = []
    for item in data:
        record = {}
        records.append(record)
    df = pd.DataFrame(records)
    return df


def audio_video_calls_in_dm_recipient_sessions_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['audio-video-calls-in-dm-recipient-sessions.js'])
    records = []
    for item in data:
        record = {}
        records.append(record)
    df = pd.DataFrame(records)
    return df


def audio_video_calls_in_dm_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['audio-video-calls-in-dm.js'])
    records = []
    for item in data:
        record = {}
        records.append(record)
    df = pd.DataFrame(records)
    return df


def block_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['block.js'])
    records = []
    for item in data:
        record = {}
        records.append(record)
    df = pd.DataFrame(records)
    return df


def branch_links_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['branch-links.js'])
    records = []
    for item in data:
        record = {}
        records.append(record)
    df = pd.DataFrame(records)
    return df


def catalog_item_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['catalog-item.js'])
    records = []
    for item in data:
        record = {}
        records.append(record)
    df = pd.DataFrame(records)
    return df


def commerce_catalog_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['commerce-catalog.js'])
    records = []
    for item in data:
        record = {}
        records.append(record)
    df = pd.DataFrame(records)
    return df


def community_note_rating_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['community-note-rating.js'])
    records = []
    for item in data:
        record = {}
        records.append(record)
    df = pd.DataFrame(records)
    return df


def community_note_tombstone_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['community-note-tombstone.js'])
    records = []
    for item in data:
        record = {}
        records.append(record)
    df = pd.DataFrame(records)
    return df


def community_note_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['community-note.js'])
    records = []
    for item in data:
        record = {}
        records.append(record)
    df = pd.DataFrame(records)
    return df


def community_tweet_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['community-tweet.js'])
    records = []
    for item in data:
        record = {}
        records.append(record)
    df = pd.DataFrame(records)
    return df


def connected_application_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['connected-application.js'])
    records = []
    for item in data:
        record = {}
        records.append(record)
    df = pd.DataFrame(records)
    return df


def contact_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['contact.js'])
    records = []
    for item in data:
        record = {}
        records.append(record)
    df = pd.DataFrame(records)
    return df


def deleted_note_tweet_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['deleted-note-tweet.js'])
    records = []
    for item in data:
        record = {}
        records.append(record)
    df = pd.DataFrame(records)
    return df


def deleted_tweet_headers_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['deleted-tweet-headers.js'])
    records = []
    for item in data:
        record = {}
        records.append(record)
    df = pd.DataFrame(records)
    return df


def deleted_tweets_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['deleted-tweets.js'])
    records = []
    for item in data:
        record = {}
        records.append(record)
    df = pd.DataFrame(records)
    return df


def device_token_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['device-token.js'])
    records = []
    for item in data:
        record = {}
        record['clientApplicationId'] = get_in(item, 'deviceToken', 'clientApplicationId')
        record['clientApplicationName'] = get_in(item, 'deviceToken', 'clientApplicationName')
        record['createdAt'] = get_in(item, 'deviceToken', 'createdAt')
        record['lastSeenAt'] = get_in(item, 'deviceToken', 'lastSeenAt')
        record['token'] = get_in(item, 'deviceToken', 'token')
        records.append(record)
    df = pd.DataFrame(records)
    return df


def direct_message_group_headers_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['direct-message-group-headers.js'])
    records = []
    for item in data:
        record = {}
        records.append(record)
    df = pd.DataFrame(records)
    return df


def direct_message_headers_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['direct-message-headers.js'])
    records = []
    for item in data:
        record = {}
        records.append(record)
    df = pd.DataFrame(records)
    return df


def direct_message_mute_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['direct-message-mute.js'])
    records = []
    for item in data:
        record = {}
        records.append(record)
    df = pd.DataFrame(records)
    return df


def direct_messages_group_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['direct-messages-group.js'])
    records = []
    for item in data:
        record = {}
        records.append(record)
    df = pd.DataFrame(records)
    return df


def direct_messages_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['direct-messages.js'])
    records = []
    for item in data:
        record = {}
        records.append(record)
    df = pd.DataFrame(records)
    return df


def email_address_change_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['email-address-change.js'])
    records = []
    for item in data:
        record = {}
        record['accountId'] = get_in(item, 'emailAddressChange', 'accountId')
        record['changedAt'] = get_in(item, 'emailAddressChange', 'emailChange', 'changedAt')
        record['changedTo'] = get_in(item, 'emailAddressChange', 'emailChange', 'changedTo')
        records.append(record)
    df = pd.DataFrame(records)
    return df


def expanded_profile_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['expanded-profile.js'])
    records = []
    for item in data:
        record = {}
        records.append(record)
    df = pd.DataFrame(records)
    return df


def follower_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['follower.js'])
    records = []
    for item in data:
        record = {}
        records.append(record)
    df = pd.DataFrame(records)
    return df


def following_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['following.js'])
    records = []
    for item in data:
        record = {}
        records.append(record)
    df = pd.DataFrame(records)
    return df


def grok_chat_item_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['grok-chat-item.js'])
    records = []
    for item in data:
        record = {}
        records.append(record)
    df = pd.DataFrame(records)
    return df


def ip_audit_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['ip-audit.js'])
    records = []
    for item in data:
        record = {}
        records.append(record)
    df = pd.DataFrame(records)
    return df


def key_registry_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['key-registry.js'])
    records = []
    for item in data:
        record = {}
        record['deRegisteredDeviceMetadataList'] = get_in(item, 'keyRegistryData', 'deregisteredDevices', 'deRegisteredDeviceMetadataList')
        record['createdAt'] = get_in(item, 'keyRegistryData', 'registeredDevices', 'deviceMetadataList', 'createdAt')
        record['deviceId'] = get_in(item, 'keyRegistryData', 'registeredDevices', 'deviceMetadataList', 'deviceId')
        record['identityKey'] = get_in(item, 'keyRegistryData', 'registeredDevices', 'deviceMetadataList', 'identityKey')
        record['registrationToken'] = get_in(item, 'keyRegistryData', 'registeredDevices', 'deviceMetadataList', 'registrationToken')
        record['userAgent'] = get_in(item, 'keyRegistryData', 'registeredDevices', 'deviceMetadataList', 'userAgent')
        record['userId'] = get_in(item, 'keyRegistryData', 'userId')
        records.append(record)
    df = pd.DataFrame(records)
    return df


def like_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['like.js'])
    records = []
    for item in data:
        record = {}
        records.append(record)
    df = pd.DataFrame(records)
    return df


def lists_created_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['lists-created.js'])
    records = []
    for item in data:
        record = {}
        records.append(record)
    df = pd.DataFrame(records)
    return df


def lists_member_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['lists-member.js'])
    records = []
    for item in data:
        record = {}
        records.append(record)
    df = pd.DataFrame(records)
    return df


def lists_subscribed_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['lists-subscribed.js'])
    records = []
    for item in data:
        record = {}
        records.append(record)
    df = pd.DataFrame(records)
    return df


def manifest_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['manifest.js'])
    records = []
    for item in data:
        record = {}
        record['accountId'] = get_in(item, 'userInfo', 'accountId')
        record['displayName'] = get_in(item, 'userInfo', 'displayName')
        record['userName'] = get_in(item, 'userInfo', 'userName')
        records.append(record)
    df = pd.DataFrame(records)
    return df


def moment_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['moment.js'])
    records = []
    for item in data:
        record = {}
        records.append(record)
    df = pd.DataFrame(records)
    return df


def mute_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['mute.js'])
    records = []
    for item in data:
        record = {}
        records.append(record)
    df = pd.DataFrame(records)
    return df


def ni_devices_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['ni-devices.js'])
    records = []
    for item in data:
        record = {}
        records.append(record)
    df = pd.DataFrame(records)
    return df


def note_tweet_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['note-tweet.js'])
    records = []
    for item in data:
        record = {}
        records.append(record)
    df = pd.DataFrame(records)
    return df


def periscope_account_information_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['periscope-account-information.js'])
    records = []
    for item in data:
        record = {}
        records.append(record)
    df = pd.DataFrame(records)
    return df


def periscope_ban_information_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['periscope-ban-information.js'])
    records = []
    for item in data:
        record = {}
        records.append(record)
    df = pd.DataFrame(records)
    return df


def periscope_broadcast_metadata_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['periscope-broadcast-metadata.js'])
    records = []
    for item in data:
        record = {}
        records.append(record)
    df = pd.DataFrame(records)
    return df


def periscope_comments_made_by_user_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['periscope-comments-made-by-user.js'])
    records = []
    for item in data:
        record = {}
        records.append(record)
    df = pd.DataFrame(records)
    return df


def periscope_expired_broadcasts_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['periscope-expired-broadcasts.js'])
    records = []
    for item in data:
        record = {}
        records.append(record)
    df = pd.DataFrame(records)
    return df


def periscope_followers_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['periscope-followers.js'])
    records = []
    for item in data:
        record = {}
        records.append(record)
    df = pd.DataFrame(records)
    return df


def periscope_profile_description_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['periscope-profile-description.js'])
    records = []
    for item in data:
        record = {}
        records.append(record)
    df = pd.DataFrame(records)
    return df


def personalization_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['personalization.js'])
    records = []
    for item in data:
        record = {}
        record['gender'] = get_in(item, 'p13nData', 'demographics', 'genderInfo', 'gender')
        record['isDisabled'] = get_in(item, 'p13nData', 'demographics', 'languages', 'isDisabled')
        record['language'] = get_in(item, 'p13nData', 'demographics', 'languages', 'language')
        record['age'] = get_in(item, 'p13nData', 'inferredAgeInfo', 'age')
        record['birthDate'] = get_in(item, 'p13nData', 'inferredAgeInfo', 'birthDate')
        record['advertisers'] = get_in(item, 'p13nData', 'interests', 'audienceAndAdvertisers', 'advertisers')
        record['catalogAudienceAdvertisers'] = get_in(item, 'p13nData', 'interests', 'audienceAndAdvertisers', 'catalogAudienceAdvertisers')
        record['doNotReachAdvertisers'] = get_in(item, 'p13nData', 'interests', 'audienceAndAdvertisers', 'doNotReachAdvertisers')
        record['lookalikeAdvertisers'] = get_in(item, 'p13nData', 'interests', 'audienceAndAdvertisers', 'lookalikeAdvertisers')
        record['numAudiences'] = get_in(item, 'p13nData', 'interests', 'audienceAndAdvertisers', 'numAudiences')
        record['isDisabled'] = get_in(item, 'p13nData', 'interests', 'interests', 'isDisabled')
        record['name'] = get_in(item, 'p13nData', 'interests', 'interests', 'name')
        record['partnerInterests'] = get_in(item, 'p13nData', 'interests', 'partnerInterests')
        record['shows'] = get_in(item, 'p13nData', 'interests', 'shows')
        record['locationHistory'] = get_in(item, 'p13nData', 'locationHistory')
        records.append(record)
    df = pd.DataFrame(records)
    return df


def phone_number_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['phone-number.js'])
    records = []
    for item in data:
        record = {}
        records.append(record)
    df = pd.DataFrame(records)
    return df


def product_drop_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['product-drop.js'])
    records = []
    for item in data:
        record = {}
        records.append(record)
    df = pd.DataFrame(records)
    return df


def product_set_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['product-set.js'])
    records = []
    for item in data:
        record = {}
        records.append(record)
    df = pd.DataFrame(records)
    return df


def professional_data_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['professional-data.js'])
    records = []
    for item in data:
        record = {}
        records.append(record)
    df = pd.DataFrame(records)
    return df


def profile_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['profile.js'])
    records = []
    for item in data:
        record = {}
        record['avatarMediaUrl'] = get_in(item, 'profile', 'avatarMediaUrl')
        record['bio'] = get_in(item, 'profile', 'description', 'bio')
        record['location'] = get_in(item, 'profile', 'description', 'location')
        record['website'] = get_in(item, 'profile', 'description', 'website')
        records.append(record)
    df = pd.DataFrame(records)
    return df


def protected_history_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['protected-history.js'])
    records = []
    for item in data:
        record = {}
        records.append(record)
    df = pd.DataFrame(records)
    return df


def reply_prompt_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['reply-prompt.js'])
    records = []
    for item in data:
        record = {}
        records.append(record)
    df = pd.DataFrame(records)
    return df


def saved_search_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['saved-search.js'])
    records = []
    for item in data:
        record = {}
        records.append(record)
    df = pd.DataFrame(records)
    return df


def screen_name_change_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['screen-name-change.js'])
    records = []
    for item in data:
        record = {}
        record['accountId'] = get_in(item, 'screenNameChange', 'accountId')
        record['changedAt'] = get_in(item, 'screenNameChange', 'screenNameChange', 'changedAt')
        record['changedFrom'] = get_in(item, 'screenNameChange', 'screenNameChange', 'changedFrom')
        record['changedTo'] = get_in(item, 'screenNameChange', 'screenNameChange', 'changedTo')
        records.append(record)
    df = pd.DataFrame(records)
    return df


def shop_module_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['shop-module.js'])
    records = []
    for item in data:
        record = {}
        records.append(record)
    df = pd.DataFrame(records)
    return df


def shopify_account_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['shopify-account.js'])
    records = []
    for item in data:
        record = {}
        records.append(record)
    df = pd.DataFrame(records)
    return df


def smartblock_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['smartblock.js'])
    records = []
    for item in data:
        record = {}
        records.append(record)
    df = pd.DataFrame(records)
    return df


def spaces_metadata_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['spaces-metadata.js'])
    records = []
    for item in data:
        record = {}
        records.append(record)
    df = pd.DataFrame(records)
    return df


def sso_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['sso.js'])
    records = []
    for item in data:
        record = {}
        records.append(record)
    df = pd.DataFrame(records)
    return df


def tweet_headers_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['tweet-headers.js'])
    records = []
    for item in data:
        record = {}
        record['created_at'] = get_in(item, 'tweet', 'created_at')
        record['tweet_id'] = get_in(item, 'tweet', 'tweet_id')
        record['user_id'] = get_in(item, 'tweet', 'user_id')
        records.append(record)
    df = pd.DataFrame(records)
    return df


def tweetdeck_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['tweetdeck.js'])
    records = []
    for item in data:
        record = {}
        records.append(record)
    df = pd.DataFrame(records)
    return df


def tweets_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['tweets.js'])
    records = []
    for item in data:
        record = {}
        record['created_at'] = get_in(item, 'tweet', 'created_at')
        record['display_text_range'] = get_in(item, 'tweet', 'display_text_range')
        record['editTweetIds'] = get_in(item, 'tweet', 'edit_info', 'initial', 'editTweetIds')
        record['editableUntil'] = get_in(item, 'tweet', 'edit_info', 'initial', 'editableUntil')
        record['editsRemaining'] = get_in(item, 'tweet', 'edit_info', 'initial', 'editsRemaining')
        record['isEditEligible'] = get_in(item, 'tweet', 'edit_info', 'initial', 'isEditEligible')
        record['hashtags'] = get_in(item, 'tweet', 'entities', 'hashtags')
        record['symbols'] = get_in(item, 'tweet', 'entities', 'symbols')
        record['urls'] = get_in(item, 'tweet', 'entities', 'urls')
        record['id'] = get_in(item, 'tweet', 'entities', 'user_mentions', 'id')
        record['id_str'] = get_in(item, 'tweet', 'entities', 'user_mentions', 'id_str')
        record['indices'] = get_in(item, 'tweet', 'entities', 'user_mentions', 'indices')
        record['name'] = get_in(item, 'tweet', 'entities', 'user_mentions', 'name')
        record['screen_name'] = get_in(item, 'tweet', 'entities', 'user_mentions', 'screen_name')
        record['favorite_count'] = get_in(item, 'tweet', 'favorite_count')
        record['favorited'] = get_in(item, 'tweet', 'favorited')
        record['full_text'] = get_in(item, 'tweet', 'full_text')
        record['id'] = get_in(item, 'tweet', 'id')
        record['id_str'] = get_in(item, 'tweet', 'id_str')
        record['lang'] = get_in(item, 'tweet', 'lang')
        record['retweet_count'] = get_in(item, 'tweet', 'retweet_count')
        record['retweeted'] = get_in(item, 'tweet', 'retweeted')
        record['source'] = get_in(item, 'tweet', 'source')
        record['truncated'] = get_in(item, 'tweet', 'truncated')
        records.append(record)
    df = pd.DataFrame(records)
    return df


def twitter_shop_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['twitter-shop.js'])
    records = []
    for item in data:
        record = {}
        records.append(record)
    df = pd.DataFrame(records)
    return df


def user_link_clicks_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['user-link-clicks.js'])
    records = []
    for item in data:
        record = {}
        records.append(record)
    df = pd.DataFrame(records)
    return df


def verified_organization_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['verified-organization.js'])
    records = []
    for item in data:
        record = {}
        records.append(record)
    df = pd.DataFrame(records)
    return df


def verified_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['verified.js'])
    records = []
    for item in data:
        record = {}
        record['accountId'] = get_in(item, 'verified', 'accountId')
        record['verified'] = get_in(item, 'verified', 'verified')
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
        df = ageinfo_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='ageinfo', df=df, title={'en': 'ageinfo'})
            )
    except Exception as e:
        logger.error(f'Skipping ageinfo_df: {e}')

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
        df = community_tweet_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='community_tweet', df=df, title={'en': 'community_tweet'})
            )
    except Exception as e:
        logger.error(f'Skipping community_tweet_df: {e}')

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
        df = deleted_tweets_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='deleted_tweets', df=df, title={'en': 'deleted_tweets'})
            )
    except Exception as e:
        logger.error(f'Skipping deleted_tweets_df: {e}')

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
        df = expanded_profile_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='expanded_profile', df=df, title={'en': 'expanded_profile'})
            )
    except Exception as e:
        logger.error(f'Skipping expanded_profile_df: {e}')

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
        df = manifest_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='manifest', df=df, title={'en': 'manifest'})
            )
    except Exception as e:
        logger.error(f'Skipping manifest_df: {e}')

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
        df = periscope_followers_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='periscope_followers', df=df, title={'en': 'periscope_followers'})
            )
    except Exception as e:
        logger.error(f'Skipping periscope_followers_df: {e}')

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
        df = tweets_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='tweets', df=df, title={'en': 'tweets'})
            )
    except Exception as e:
        logger.error(f'Skipping tweets_df: {e}')

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