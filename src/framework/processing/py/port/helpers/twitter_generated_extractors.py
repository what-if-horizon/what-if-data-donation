# Auto-generated Twitter extractors

import pandas as pd
import json
import logging
import io
import zipfile
import re
from port.helpers.donation_flow import donation_table, donation_flow

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

def extract_path(row):
    path = []
    for col in ["row_path"] + [f"col_path_{i}" for i in range(1, 6)]:
        val = row.get(col)
        if pd.notna(val) and str(val).strip().upper() != "MISSING":
            path.append(str(val).strip())
    return path

def get_field_name(row):
    for i in reversed(range(1, 6)):
        val = row.get(f"col_path_{i}")
        if pd.notna(val) and val != 'MISSING':
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

                            if isinstance(data,list):
                                extracted_data.extend(data)
                            else:
                                extracted_data.append(data)

                        except json.JSONDecodeError as e:
                            logger.error(f"Error decoding {target_file} in {zip_path}: {e}")
    return extracted_data

def account_creation_ip_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['/account-creation-ip.js'])
    records = []
    for item in data:
        base_row = {}
        base_row['accountId'] = get_in(item, 'accountCreationIp', 'accountId')
        base_row['userCreationIp'] = get_in(item, 'accountCreationIp', 'userCreationIp')
        records.append(base_row)
    return pd.DataFrame(records)


def account_timezone_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['/account-timezone.js'])
    records = []
    for item in data:
        base_row = {}
        base_row['accountId'] = get_in(item, 'accountTimezone', 'accountId')
        records.append(base_row)
    return pd.DataFrame(records)


def account_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['/account.js'])
    records = []
    for item in data:
        base_row = {}
        base_row['email'] = get_in(item, 'account', 'email')
        base_row['createdVia'] = get_in(item, 'account', 'createdVia')
        base_row['username'] = get_in(item, 'account', 'username')
        base_row['accountId'] = get_in(item, 'account', 'accountId')
        base_row['createdAt'] = get_in(item, 'account', 'createdAt')
        base_row['accountDisplayName'] = get_in(item, 'account', 'accountDisplayName')
        records.append(base_row)
    return pd.DataFrame(records)


def ads_revenue_sharing_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['/ads-revenue-sharing.js'])
    records = []
    for item in data:
        base_row = {}
        records.append(base_row)
    return pd.DataFrame(records)


def ageinfo_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['/ageinfo.js'])
    records = []
    for item in data:
        base_row = {}
        base_row['birthDate'] = get_in(item, 'ageMeta', 'ageInfo', 'birthDate')
        records.append(base_row)
    return pd.DataFrame(records)


def connected_application_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['/connected-application.js'])
    records = []
    for item in data:
        base_row = {}
        base_row['name'] = get_in(item, 'connectedApplication', 'organization', 'name')
        base_row['url'] = get_in(item, 'connectedApplication', 'organization', 'url')
        base_row['description'] = get_in(item, 'connectedApplication', 'description')
        base_row['approvedAt'] = get_in(item, 'connectedApplication', 'approvedAt')
        base_row['id'] = get_in(item, 'connectedApplication', 'id')
        records.append(base_row)
    return pd.DataFrame(records)


def device_token_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['/device-token.js'])
    records = []
    for item in data:
        base_row = {}
        base_row['clientApplicationId'] = get_in(item, 'deviceToken', 'clientApplicationId')
        base_row['token'] = get_in(item, 'deviceToken', 'token')
        base_row['createdAt'] = get_in(item, 'deviceToken', 'createdAt')
        base_row['lastSeenAt'] = get_in(item, 'deviceToken', 'lastSeenAt')
        base_row['clientApplicationName'] = get_in(item, 'deviceToken', 'clientApplicationName')
        records.append(base_row)
    return pd.DataFrame(records)


def direct_message_group_headers_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['/direct-message-group-headers.js'])
    records = []
    for item in data:
        base_row = {}
        base_row['conversationId'] = get_in(item, 'dmConversation', 'conversationId')
        for entry in get_list(item, 'dmConversation', 'messages'):
            row = base_row.copy()
            row['__source_list__'] = 'messages'
            row['createdAt'] = get_in(entry, 'messageCreate', 'createdAt')
            row['id'] = get_in(entry, 'messageCreate', 'id')
            row['senderId'] = get_in(entry, 'messageCreate', 'senderId')
            records.append(row)
    return pd.DataFrame(records)


def direct_messages_group_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['/direct-messages-group.js'])
    records = []
    for item in data:
        base_row = {}
        base_row['conversationId'] = get_in(item, 'dmConversation', 'conversationId')
        for entry in get_list(item, 'dmConversation', 'messages'):
            row = base_row.copy()
            row['__source_list__'] = 'messages'
            row['createdAt'] = get_in(entry, 'messageCreate', 'createdAt')
            row['editHistory'] = get_in(entry, 'messageCreate', 'editHistory')
            row['id'] = get_in(entry, 'messageCreate', 'id')
            row['mediaUrls'] = get_in(entry, 'messageCreate', 'mediaUrls')
            row['reactions'] = get_in(entry, 'messageCreate', 'reactions')
            row['senderId'] = get_in(entry, 'messageCreate', 'senderId')
            row['text'] = get_in(entry, 'messageCreate', 'text')
            row['display'] = get_in(entry, 'messageCreate', 'urls', 'display')
            row['expanded'] = get_in(entry, 'messageCreate', 'urls', 'expanded')
            row['url'] = get_in(entry, 'messageCreate', 'urls', 'url')
            records.append(row)
    return pd.DataFrame(records)


def email_address_change_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['/email-address-change.js'])
    records = []
    for item in data:
        base_row = {}
        base_row['accountId'] = get_in(item, 'emailAddressChange', 'accountId')
        base_row['changedAt'] = get_in(item, 'emailAddressChange', 'emailChange', 'changedAt')
        base_row['changedTo'] = get_in(item, 'emailAddressChange', 'emailChange', 'changedTo')
        records.append(base_row)
    return pd.DataFrame(records)


def key_registry_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['/key-registry.js'])
    records = []
    for item in data:
        base_row = {}
        base_row['userId'] = get_in(item, 'keyRegistryData', 'userId')
        for entry in get_list(item, 'keyRegistryData', 'registeredDevices', 'deviceMetadataList'):
            row = base_row.copy()
            row['__source_list__'] = 'deviceMetadataList'
            row['createdAt'] = get_in(entry, 'createdAt')
            row['deviceId'] = get_in(entry, 'deviceId')
            row['identityKey'] = get_in(entry, 'identityKey')
            row['registrationToken'] = get_in(entry, 'registrationToken')
            row['userAgent'] = get_in(entry, 'userAgent')
            records.append(row)
    return pd.DataFrame(records)


def manifest_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['/manifest.js'])
    records = []
    for item in data:
        base_row = {}
        base_row['accountId'] = get_in(item, 'userInfo', 'accountId')
        base_row['userName'] = get_in(item, 'userInfo', 'userName')
        base_row['displayName'] = get_in(item, 'userInfo', 'displayName')
        base_row['sizeBytes'] = get_in(item, 'archiveInfo', 'sizeBytes')
        base_row['generationDate'] = get_in(item, 'archiveInfo', 'generationDate')
        base_row['isPartialArchive'] = get_in(item, 'archiveInfo', 'isPartialArchive')
        base_row['maxPartSizeBytes'] = get_in(item, 'archiveInfo', 'maxPartSizeBytes')
        base_row['fileName'] = get_in(item, 'readmeInfo', 'fileName')
        base_row['directory'] = get_in(item, 'readmeInfo', 'directory')
        base_row['name'] = get_in(item, 'readmeInfo', 'name')
        base_row['mediaDirectory'] = get_in(item, 'dataTypes', 'communityTweet', 'mediaDirectory')
        for entry in get_list(item, 'dataTypes', 'account', 'files'):
            row = base_row.copy()
            row['__source_list__'] = 'files'
            row['count'] = get_in(entry, 'count')
            row['fileName'] = get_in(entry, 'fileName')
            row['globalName'] = get_in(entry, 'globalName')
            records.append(row)
        for entry in get_list(item, 'dataTypes', 'accountCreationIp', 'files'):
            row = base_row.copy()
            row['__source_list__'] = 'files'
            row['count'] = get_in(entry, 'count')
            row['fileName'] = get_in(entry, 'fileName')
            row['globalName'] = get_in(entry, 'globalName')
            records.append(row)
        for entry in get_list(item, 'dataTypes', 'accountLabel', 'files'):
            row = base_row.copy()
            row['__source_list__'] = 'files'
            row['count'] = get_in(entry, 'count')
            row['fileName'] = get_in(entry, 'fileName')
            row['globalName'] = get_in(entry, 'globalName')
            records.append(row)
        for entry in get_list(item, 'dataTypes', 'accountSuspension', 'files'):
            row = base_row.copy()
            row['__source_list__'] = 'files'
            row['count'] = get_in(entry, 'count')
            row['fileName'] = get_in(entry, 'fileName')
            row['globalName'] = get_in(entry, 'globalName')
            records.append(row)
        for entry in get_list(item, 'dataTypes', 'accountTimezone', 'files'):
            row = base_row.copy()
            row['__source_list__'] = 'files'
            row['count'] = get_in(entry, 'count')
            row['fileName'] = get_in(entry, 'fileName')
            row['globalName'] = get_in(entry, 'globalName')
            records.append(row)
        for entry in get_list(item, 'dataTypes', 'adEngagements', 'files'):
            row = base_row.copy()
            row['__source_list__'] = 'files'
            row['count'] = get_in(entry, 'count')
            row['fileName'] = get_in(entry, 'fileName')
            row['globalName'] = get_in(entry, 'globalName')
            records.append(row)
        for entry in get_list(item, 'dataTypes', 'adImpressions', 'files'):
            row = base_row.copy()
            row['__source_list__'] = 'files'
            row['count'] = get_in(entry, 'count')
            row['fileName'] = get_in(entry, 'fileName')
            row['globalName'] = get_in(entry, 'globalName')
            records.append(row)
        for entry in get_list(item, 'dataTypes', 'adMobileConversionsAttributed', 'files'):
            row = base_row.copy()
            row['__source_list__'] = 'files'
            row['count'] = get_in(entry, 'count')
            row['fileName'] = get_in(entry, 'fileName')
            row['globalName'] = get_in(entry, 'globalName')
            records.append(row)
        for entry in get_list(item, 'dataTypes', 'adMobileConversionsUnattributed', 'files'):
            row = base_row.copy()
            row['__source_list__'] = 'files'
            row['count'] = get_in(entry, 'count')
            row['fileName'] = get_in(entry, 'fileName')
            row['globalName'] = get_in(entry, 'globalName')
            records.append(row)
        for entry in get_list(item, 'dataTypes', 'adOnlineConversionsAttributed', 'files'):
            row = base_row.copy()
            row['__source_list__'] = 'files'
            row['count'] = get_in(entry, 'count')
            row['fileName'] = get_in(entry, 'fileName')
            row['globalName'] = get_in(entry, 'globalName')
            records.append(row)
        for entry in get_list(item, 'dataTypes', 'adOnlineConversionsUnattributed', 'files'):
            row = base_row.copy()
            row['__source_list__'] = 'files'
            row['count'] = get_in(entry, 'count')
            row['fileName'] = get_in(entry, 'fileName')
            row['globalName'] = get_in(entry, 'globalName')
            records.append(row)
        for entry in get_list(item, 'dataTypes', 'adsRevenueSharing', 'files'):
            row = base_row.copy()
            row['__source_list__'] = 'files'
            row['count'] = get_in(entry, 'count')
            row['fileName'] = get_in(entry, 'fileName')
            row['globalName'] = get_in(entry, 'globalName')
            records.append(row)
        for entry in get_list(item, 'dataTypes', 'ageinfo', 'files'):
            row = base_row.copy()
            row['__source_list__'] = 'files'
            row['count'] = get_in(entry, 'count')
            row['fileName'] = get_in(entry, 'fileName')
            row['globalName'] = get_in(entry, 'globalName')
            records.append(row)
        for entry in get_list(item, 'dataTypes', 'app', 'files'):
            row = base_row.copy()
            row['__source_list__'] = 'files'
            row['count'] = get_in(entry, 'count')
            row['fileName'] = get_in(entry, 'fileName')
            row['globalName'] = get_in(entry, 'globalName')
            records.append(row)
        for entry in get_list(item, 'dataTypes', 'article', 'files'):
            row = base_row.copy()
            row['__source_list__'] = 'files'
            row['count'] = get_in(entry, 'count')
            row['fileName'] = get_in(entry, 'fileName')
            row['globalName'] = get_in(entry, 'globalName')
            records.append(row)
        for entry in get_list(item, 'dataTypes', 'articleMetadata', 'files'):
            row = base_row.copy()
            row['__source_list__'] = 'files'
            row['count'] = get_in(entry, 'count')
            row['fileName'] = get_in(entry, 'fileName')
            row['globalName'] = get_in(entry, 'globalName')
            records.append(row)
        for entry in get_list(item, 'dataTypes', 'audioVideoCallsInDm', 'files'):
            row = base_row.copy()
            row['__source_list__'] = 'files'
            row['count'] = get_in(entry, 'count')
            row['fileName'] = get_in(entry, 'fileName')
            row['globalName'] = get_in(entry, 'globalName')
            records.append(row)
        for entry in get_list(item, 'dataTypes', 'audioVideoCallsInDmRecipientSessions', 'files'):
            row = base_row.copy()
            row['__source_list__'] = 'files'
            row['count'] = get_in(entry, 'count')
            row['fileName'] = get_in(entry, 'fileName')
            row['globalName'] = get_in(entry, 'globalName')
            records.append(row)
        for entry in get_list(item, 'dataTypes', 'block', 'files'):
            row = base_row.copy()
            row['__source_list__'] = 'files'
            row['count'] = get_in(entry, 'count')
            row['fileName'] = get_in(entry, 'fileName')
            row['globalName'] = get_in(entry, 'globalName')
            records.append(row)
        for entry in get_list(item, 'dataTypes', 'branchLinks', 'files'):
            row = base_row.copy()
            row['__source_list__'] = 'files'
            row['count'] = get_in(entry, 'count')
            row['fileName'] = get_in(entry, 'fileName')
            row['globalName'] = get_in(entry, 'globalName')
            records.append(row)
        for entry in get_list(item, 'dataTypes', 'catalogItem', 'files'):
            row = base_row.copy()
            row['__source_list__'] = 'files'
            row['count'] = get_in(entry, 'count')
            row['fileName'] = get_in(entry, 'fileName')
            row['globalName'] = get_in(entry, 'globalName')
            records.append(row)
        for entry in get_list(item, 'dataTypes', 'commerceCatalog', 'files'):
            row = base_row.copy()
            row['__source_list__'] = 'files'
            row['count'] = get_in(entry, 'count')
            row['fileName'] = get_in(entry, 'fileName')
            row['globalName'] = get_in(entry, 'globalName')
            records.append(row)
        for entry in get_list(item, 'dataTypes', 'communityNote', 'files'):
            row = base_row.copy()
            row['__source_list__'] = 'files'
            row['count'] = get_in(entry, 'count')
            row['fileName'] = get_in(entry, 'fileName')
            row['globalName'] = get_in(entry, 'globalName')
            records.append(row)
        for entry in get_list(item, 'dataTypes', 'communityNoteBatsignal', 'files'):
            row = base_row.copy()
            row['__source_list__'] = 'files'
            row['count'] = get_in(entry, 'count')
            row['fileName'] = get_in(entry, 'fileName')
            row['globalName'] = get_in(entry, 'globalName')
            records.append(row)
        for entry in get_list(item, 'dataTypes', 'communityNoteRating', 'files'):
            row = base_row.copy()
            row['__source_list__'] = 'files'
            row['count'] = get_in(entry, 'count')
            row['fileName'] = get_in(entry, 'fileName')
            row['globalName'] = get_in(entry, 'globalName')
            records.append(row)
        for entry in get_list(item, 'dataTypes', 'communityNoteTombstone', 'files'):
            row = base_row.copy()
            row['__source_list__'] = 'files'
            row['count'] = get_in(entry, 'count')
            row['fileName'] = get_in(entry, 'fileName')
            row['globalName'] = get_in(entry, 'globalName')
            records.append(row)
        for entry in get_list(item, 'dataTypes', 'communityTweet', 'files'):
            row = base_row.copy()
            row['__source_list__'] = 'files'
            row['count'] = get_in(entry, 'count')
            row['fileName'] = get_in(entry, 'fileName')
            row['globalName'] = get_in(entry, 'globalName')
            records.append(row)
        for entry in get_list(item, 'dataTypes', 'connectedApplication', 'files'):
            row = base_row.copy()
            row['__source_list__'] = 'files'
            row['count'] = get_in(entry, 'count')
            row['fileName'] = get_in(entry, 'fileName')
            row['globalName'] = get_in(entry, 'globalName')
            records.append(row)
        for entry in get_list(item, 'dataTypes', 'contact', 'files'):
            row = base_row.copy()
            row['__source_list__'] = 'files'
            row['count'] = get_in(entry, 'count')
            row['fileName'] = get_in(entry, 'fileName')
            row['globalName'] = get_in(entry, 'globalName')
            records.append(row)
        for entry in get_list(item, 'dataTypes', 'deletedNoteTweet', 'files'):
            row = base_row.copy()
            row['__source_list__'] = 'files'
            row['count'] = get_in(entry, 'count')
            row['fileName'] = get_in(entry, 'fileName')
            row['globalName'] = get_in(entry, 'globalName')
            records.append(row)
        for entry in get_list(item, 'dataTypes', 'deletedTweetHeaders', 'files'):
            row = base_row.copy()
            row['__source_list__'] = 'files'
            row['count'] = get_in(entry, 'count')
            row['fileName'] = get_in(entry, 'fileName')
            row['globalName'] = get_in(entry, 'globalName')
            records.append(row)
        for entry in get_list(item, 'dataTypes', 'deletedTweets', 'files'):
            row = base_row.copy()
            row['__source_list__'] = 'files'
            row['count'] = get_in(entry, 'count')
            row['fileName'] = get_in(entry, 'fileName')
            row['globalName'] = get_in(entry, 'globalName')
            records.append(row)
        for entry in get_list(item, 'dataTypes', 'deviceToken', 'files'):
            row = base_row.copy()
            row['__source_list__'] = 'files'
            row['count'] = get_in(entry, 'count')
            row['fileName'] = get_in(entry, 'fileName')
            row['globalName'] = get_in(entry, 'globalName')
            records.append(row)
        for entry in get_list(item, 'dataTypes', 'directMessageGroupHeaders', 'files'):
            row = base_row.copy()
            row['__source_list__'] = 'files'
            row['count'] = get_in(entry, 'count')
            row['fileName'] = get_in(entry, 'fileName')
            row['globalName'] = get_in(entry, 'globalName')
            records.append(row)
        for entry in get_list(item, 'dataTypes', 'directMessageHeaders', 'files'):
            row = base_row.copy()
            row['__source_list__'] = 'files'
            row['count'] = get_in(entry, 'count')
            row['fileName'] = get_in(entry, 'fileName')
            row['globalName'] = get_in(entry, 'globalName')
            records.append(row)
        for entry in get_list(item, 'dataTypes', 'directMessageMute', 'files'):
            row = base_row.copy()
            row['__source_list__'] = 'files'
            row['count'] = get_in(entry, 'count')
            row['fileName'] = get_in(entry, 'fileName')
            row['globalName'] = get_in(entry, 'globalName')
            records.append(row)
        for entry in get_list(item, 'dataTypes', 'directMessages', 'files'):
            row = base_row.copy()
            row['__source_list__'] = 'files'
            row['count'] = get_in(entry, 'count')
            row['fileName'] = get_in(entry, 'fileName')
            row['globalName'] = get_in(entry, 'globalName')
            records.append(row)
        for entry in get_list(item, 'dataTypes', 'directMessagesGroup', 'files'):
            row = base_row.copy()
            row['__source_list__'] = 'files'
            row['count'] = get_in(entry, 'count')
            row['fileName'] = get_in(entry, 'fileName')
            row['globalName'] = get_in(entry, 'globalName')
            records.append(row)
        for entry in get_list(item, 'dataTypes', 'emailAddressChange', 'files'):
            row = base_row.copy()
            row['__source_list__'] = 'files'
            row['count'] = get_in(entry, 'count')
            row['fileName'] = get_in(entry, 'fileName')
            row['globalName'] = get_in(entry, 'globalName')
            records.append(row)
        for entry in get_list(item, 'dataTypes', 'expandedProfile', 'files'):
            row = base_row.copy()
            row['__source_list__'] = 'files'
            row['count'] = get_in(entry, 'count')
            row['fileName'] = get_in(entry, 'fileName')
            row['globalName'] = get_in(entry, 'globalName')
            records.append(row)
        for entry in get_list(item, 'dataTypes', 'follower', 'files'):
            row = base_row.copy()
            row['__source_list__'] = 'files'
            row['count'] = get_in(entry, 'count')
            row['fileName'] = get_in(entry, 'fileName')
            row['globalName'] = get_in(entry, 'globalName')
            records.append(row)
        for entry in get_list(item, 'dataTypes', 'following', 'files'):
            row = base_row.copy()
            row['__source_list__'] = 'files'
            row['count'] = get_in(entry, 'count')
            row['fileName'] = get_in(entry, 'fileName')
            row['globalName'] = get_in(entry, 'globalName')
            records.append(row)
        for entry in get_list(item, 'dataTypes', 'grokChatItem', 'files'):
            row = base_row.copy()
            row['__source_list__'] = 'files'
            row['count'] = get_in(entry, 'count')
            row['fileName'] = get_in(entry, 'fileName')
            row['globalName'] = get_in(entry, 'globalName')
            records.append(row)
        for entry in get_list(item, 'dataTypes', 'ipAudit', 'files'):
            row = base_row.copy()
            row['__source_list__'] = 'files'
            row['count'] = get_in(entry, 'count')
            row['fileName'] = get_in(entry, 'fileName')
            row['globalName'] = get_in(entry, 'globalName')
            records.append(row)
        for entry in get_list(item, 'dataTypes', 'keyRegistry', 'files'):
            row = base_row.copy()
            row['__source_list__'] = 'files'
            row['count'] = get_in(entry, 'count')
            row['fileName'] = get_in(entry, 'fileName')
            row['globalName'] = get_in(entry, 'globalName')
            records.append(row)
        for entry in get_list(item, 'dataTypes', 'like', 'files'):
            row = base_row.copy()
            row['__source_list__'] = 'files'
            row['count'] = get_in(entry, 'count')
            row['fileName'] = get_in(entry, 'fileName')
            row['globalName'] = get_in(entry, 'globalName')
            records.append(row)
        for entry in get_list(item, 'dataTypes', 'listsCreated', 'files'):
            row = base_row.copy()
            row['__source_list__'] = 'files'
            row['count'] = get_in(entry, 'count')
            row['fileName'] = get_in(entry, 'fileName')
            row['globalName'] = get_in(entry, 'globalName')
            records.append(row)
        for entry in get_list(item, 'dataTypes', 'listsMember', 'files'):
            row = base_row.copy()
            row['__source_list__'] = 'files'
            row['count'] = get_in(entry, 'count')
            row['fileName'] = get_in(entry, 'fileName')
            row['globalName'] = get_in(entry, 'globalName')
            records.append(row)
        for entry in get_list(item, 'dataTypes', 'listsSubscribed', 'files'):
            row = base_row.copy()
            row['__source_list__'] = 'files'
            row['count'] = get_in(entry, 'count')
            row['fileName'] = get_in(entry, 'fileName')
            row['globalName'] = get_in(entry, 'globalName')
            records.append(row)
        for entry in get_list(item, 'dataTypes', 'moment', 'files'):
            row = base_row.copy()
            row['__source_list__'] = 'files'
            row['count'] = get_in(entry, 'count')
            row['fileName'] = get_in(entry, 'fileName')
            row['globalName'] = get_in(entry, 'globalName')
            records.append(row)
        for entry in get_list(item, 'dataTypes', 'mute', 'files'):
            row = base_row.copy()
            row['__source_list__'] = 'files'
            row['count'] = get_in(entry, 'count')
            row['fileName'] = get_in(entry, 'fileName')
            row['globalName'] = get_in(entry, 'globalName')
            records.append(row)
        for entry in get_list(item, 'dataTypes', 'niDevices', 'files'):
            row = base_row.copy()
            row['__source_list__'] = 'files'
            row['count'] = get_in(entry, 'count')
            row['fileName'] = get_in(entry, 'fileName')
            row['globalName'] = get_in(entry, 'globalName')
            records.append(row)
        for entry in get_list(item, 'dataTypes', 'noteTweet', 'files'):
            row = base_row.copy()
            row['__source_list__'] = 'files'
            row['count'] = get_in(entry, 'count')
            row['fileName'] = get_in(entry, 'fileName')
            row['globalName'] = get_in(entry, 'globalName')
            records.append(row)
        for entry in get_list(item, 'dataTypes', 'periscopeAccountInformation', 'files'):
            row = base_row.copy()
            row['__source_list__'] = 'files'
            row['count'] = get_in(entry, 'count')
            row['fileName'] = get_in(entry, 'fileName')
            row['globalName'] = get_in(entry, 'globalName')
            records.append(row)
        for entry in get_list(item, 'dataTypes', 'periscopeBanInformation', 'files'):
            row = base_row.copy()
            row['__source_list__'] = 'files'
            row['count'] = get_in(entry, 'count')
            row['fileName'] = get_in(entry, 'fileName')
            row['globalName'] = get_in(entry, 'globalName')
            records.append(row)
        for entry in get_list(item, 'dataTypes', 'periscopeBroadcastMetadata', 'files'):
            row = base_row.copy()
            row['__source_list__'] = 'files'
            row['count'] = get_in(entry, 'count')
            row['fileName'] = get_in(entry, 'fileName')
            row['globalName'] = get_in(entry, 'globalName')
            records.append(row)
        for entry in get_list(item, 'dataTypes', 'periscopeCommentsMadeByUser', 'files'):
            row = base_row.copy()
            row['__source_list__'] = 'files'
            row['count'] = get_in(entry, 'count')
            row['fileName'] = get_in(entry, 'fileName')
            row['globalName'] = get_in(entry, 'globalName')
            records.append(row)
        for entry in get_list(item, 'dataTypes', 'periscopeExpiredBroadcasts', 'files'):
            row = base_row.copy()
            row['__source_list__'] = 'files'
            row['count'] = get_in(entry, 'count')
            row['fileName'] = get_in(entry, 'fileName')
            row['globalName'] = get_in(entry, 'globalName')
            records.append(row)
        for entry in get_list(item, 'dataTypes', 'periscopeFollowers', 'files'):
            row = base_row.copy()
            row['__source_list__'] = 'files'
            row['count'] = get_in(entry, 'count')
            row['fileName'] = get_in(entry, 'fileName')
            row['globalName'] = get_in(entry, 'globalName')
            records.append(row)
        for entry in get_list(item, 'dataTypes', 'periscopeProfileDescription', 'files'):
            row = base_row.copy()
            row['__source_list__'] = 'files'
            row['count'] = get_in(entry, 'count')
            row['fileName'] = get_in(entry, 'fileName')
            row['globalName'] = get_in(entry, 'globalName')
            records.append(row)
        for entry in get_list(item, 'dataTypes', 'personalization', 'files'):
            row = base_row.copy()
            row['__source_list__'] = 'files'
            row['count'] = get_in(entry, 'count')
            row['fileName'] = get_in(entry, 'fileName')
            row['globalName'] = get_in(entry, 'globalName')
            records.append(row)
        for entry in get_list(item, 'dataTypes', 'phoneNumber', 'files'):
            row = base_row.copy()
            row['__source_list__'] = 'files'
            row['count'] = get_in(entry, 'count')
            row['fileName'] = get_in(entry, 'fileName')
            row['globalName'] = get_in(entry, 'globalName')
            records.append(row)
        for entry in get_list(item, 'dataTypes', 'productDrop', 'files'):
            row = base_row.copy()
            row['__source_list__'] = 'files'
            row['count'] = get_in(entry, 'count')
            row['fileName'] = get_in(entry, 'fileName')
            row['globalName'] = get_in(entry, 'globalName')
            records.append(row)
        for entry in get_list(item, 'dataTypes', 'productSet', 'files'):
            row = base_row.copy()
            row['__source_list__'] = 'files'
            row['count'] = get_in(entry, 'count')
            row['fileName'] = get_in(entry, 'fileName')
            row['globalName'] = get_in(entry, 'globalName')
            records.append(row)
        for entry in get_list(item, 'dataTypes', 'professionalData', 'files'):
            row = base_row.copy()
            row['__source_list__'] = 'files'
            row['count'] = get_in(entry, 'count')
            row['fileName'] = get_in(entry, 'fileName')
            row['globalName'] = get_in(entry, 'globalName')
            records.append(row)
        for entry in get_list(item, 'dataTypes', 'profile', 'files'):
            row = base_row.copy()
            row['__source_list__'] = 'files'
            row['count'] = get_in(entry, 'count')
            row['fileName'] = get_in(entry, 'fileName')
            row['globalName'] = get_in(entry, 'globalName')
            records.append(row)
        for entry in get_list(item, 'dataTypes', 'protectedHistory', 'files'):
            row = base_row.copy()
            row['__source_list__'] = 'files'
            row['count'] = get_in(entry, 'count')
            row['fileName'] = get_in(entry, 'fileName')
            row['globalName'] = get_in(entry, 'globalName')
            records.append(row)
        for entry in get_list(item, 'dataTypes', 'replyPrompt', 'files'):
            row = base_row.copy()
            row['__source_list__'] = 'files'
            row['count'] = get_in(entry, 'count')
            row['fileName'] = get_in(entry, 'fileName')
            row['globalName'] = get_in(entry, 'globalName')
            records.append(row)
        for entry in get_list(item, 'dataTypes', 'savedSearch', 'files'):
            row = base_row.copy()
            row['__source_list__'] = 'files'
            row['count'] = get_in(entry, 'count')
            row['fileName'] = get_in(entry, 'fileName')
            row['globalName'] = get_in(entry, 'globalName')
            records.append(row)
        for entry in get_list(item, 'dataTypes', 'screenNameChange', 'files'):
            row = base_row.copy()
            row['__source_list__'] = 'files'
            row['count'] = get_in(entry, 'count')
            row['fileName'] = get_in(entry, 'fileName')
            row['globalName'] = get_in(entry, 'globalName')
            records.append(row)
        for entry in get_list(item, 'dataTypes', 'shopModule', 'files'):
            row = base_row.copy()
            row['__source_list__'] = 'files'
            row['count'] = get_in(entry, 'count')
            row['fileName'] = get_in(entry, 'fileName')
            row['globalName'] = get_in(entry, 'globalName')
            records.append(row)
        for entry in get_list(item, 'dataTypes', 'shopifyAccount', 'files'):
            row = base_row.copy()
            row['__source_list__'] = 'files'
            row['count'] = get_in(entry, 'count')
            row['fileName'] = get_in(entry, 'fileName')
            row['globalName'] = get_in(entry, 'globalName')
            records.append(row)
        for entry in get_list(item, 'dataTypes', 'smartblock', 'files'):
            row = base_row.copy()
            row['__source_list__'] = 'files'
            row['count'] = get_in(entry, 'count')
            row['fileName'] = get_in(entry, 'fileName')
            row['globalName'] = get_in(entry, 'globalName')
            records.append(row)
        for entry in get_list(item, 'dataTypes', 'spacesMetadata', 'files'):
            row = base_row.copy()
            row['__source_list__'] = 'files'
            row['count'] = get_in(entry, 'count')
            row['fileName'] = get_in(entry, 'fileName')
            row['globalName'] = get_in(entry, 'globalName')
            records.append(row)
        for entry in get_list(item, 'dataTypes', 'sso', 'files'):
            row = base_row.copy()
            row['__source_list__'] = 'files'
            row['count'] = get_in(entry, 'count')
            row['fileName'] = get_in(entry, 'fileName')
            row['globalName'] = get_in(entry, 'globalName')
            records.append(row)
        for entry in get_list(item, 'dataTypes', 'tweetHeaders', 'files'):
            row = base_row.copy()
            row['__source_list__'] = 'files'
            row['count'] = get_in(entry, 'count')
            row['fileName'] = get_in(entry, 'fileName')
            row['globalName'] = get_in(entry, 'globalName')
            records.append(row)
        for entry in get_list(item, 'dataTypes', 'tweetdeck', 'files'):
            row = base_row.copy()
            row['__source_list__'] = 'files'
            row['count'] = get_in(entry, 'count')
            row['fileName'] = get_in(entry, 'fileName')
            row['globalName'] = get_in(entry, 'globalName')
            records.append(row)
        for entry in get_list(item, 'dataTypes', 'tweets', 'files'):
            row = base_row.copy()
            row['__source_list__'] = 'files'
            row['count'] = get_in(entry, 'count')
            row['fileName'] = get_in(entry, 'fileName')
            row['globalName'] = get_in(entry, 'globalName')
            records.append(row)
        for entry in get_list(item, 'dataTypes', 'twitterShop', 'files'):
            row = base_row.copy()
            row['__source_list__'] = 'files'
            row['count'] = get_in(entry, 'count')
            row['fileName'] = get_in(entry, 'fileName')
            row['globalName'] = get_in(entry, 'globalName')
            records.append(row)
        for entry in get_list(item, 'dataTypes', 'userLinkClicks', 'files'):
            row = base_row.copy()
            row['__source_list__'] = 'files'
            row['count'] = get_in(entry, 'count')
            row['fileName'] = get_in(entry, 'fileName')
            row['globalName'] = get_in(entry, 'globalName')
            records.append(row)
        for entry in get_list(item, 'dataTypes', 'verified', 'files'):
            row = base_row.copy()
            row['__source_list__'] = 'files'
            row['count'] = get_in(entry, 'count')
            row['fileName'] = get_in(entry, 'fileName')
            row['globalName'] = get_in(entry, 'globalName')
            records.append(row)
        for entry in get_list(item, 'dataTypes', 'verifiedOrganization', 'files'):
            row = base_row.copy()
            row['__source_list__'] = 'files'
            row['count'] = get_in(entry, 'count')
            row['fileName'] = get_in(entry, 'fileName')
            row['globalName'] = get_in(entry, 'globalName')
            records.append(row)
    return pd.DataFrame(records)


def periscope_account_information_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['/periscope-account-information.js'])
    records = []
    for item in data:
        base_row = {}
        base_row['displayName'] = get_in(item, 'periscopeAccountInformation', 'displayName')
        base_row['digitsId'] = get_in(item, 'periscopeAccountInformation', 'digitsId')
        base_row['username'] = get_in(item, 'periscopeAccountInformation', 'username')
        base_row['twitterId'] = get_in(item, 'periscopeAccountInformation', 'twitterId')
        base_row['id'] = get_in(item, 'periscopeAccountInformation', 'id')
        base_row['twitterScreenName'] = get_in(item, 'periscopeAccountInformation', 'twitterScreenName')
        base_row['isTwitterUser'] = get_in(item, 'periscopeAccountInformation', 'isTwitterUser')
        base_row['createdAt'] = get_in(item, 'periscopeAccountInformation', 'createdAt')
        records.append(base_row)
    return pd.DataFrame(records)


def periscope_profile_description_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['/periscope-profile-description.js'])
    records = []
    for item in data:
        base_row = {}
        base_row['bio'] = get_in(item, 'periscopeProfileDescription', 'bio')
        records.append(base_row)
    return pd.DataFrame(records)


def personalization_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['/personalization.js'])
    records = []
    for item in data:
        base_row = {}
        base_row['gender'] = get_in(item, 'p13nData', 'demographics', 'genderInfo', 'gender')
        base_row['numAudiences'] = get_in(item, 'p13nData', 'interests', 'audienceAndAdvertisers', 'numAudiences')
        base_row['birthDate'] = get_in(item, 'p13nData', 'inferredAgeInfo', 'birthDate')
        for entry in get_list(item, 'p13nData', 'demographics', 'languages'):
            row = base_row.copy()
            row['__source_list__'] = 'languages'
            row['isDisabled'] = get_in(entry, 'isDisabled')
            row['language'] = get_in(entry, 'language')
            records.append(row)
        for entry in get_list(item, 'p13nData', 'interests', 'interests'):
            row = base_row.copy()
            row['__source_list__'] = 'interests'
            row['isDisabled'] = get_in(entry, 'isDisabled')
            row['name'] = get_in(entry, 'name')
            records.append(row)
    return pd.DataFrame(records)


def profile_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['/profile.js'])
    records = []
    for item in data:
        base_row = {}
        base_row['bio'] = get_in(item, 'profile', 'description', 'bio')
        base_row['website'] = get_in(item, 'profile', 'description', 'website')
        base_row['location'] = get_in(item, 'profile', 'description', 'location')
        base_row['avatarMediaUrl'] = get_in(item, 'profile', 'avatarMediaUrl')
        base_row['headerMediaUrl'] = get_in(item, 'profile', 'headerMediaUrl')
        records.append(base_row)
    return pd.DataFrame(records)


def screen_name_change_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['/screen-name-change.js'])
    records = []
    for item in data:
        base_row = {}
        base_row['accountId'] = get_in(item, 'screenNameChange', 'accountId')
        base_row['changedAt'] = get_in(item, 'screenNameChange', 'screenNameChange', 'changedAt')
        base_row['changedFrom'] = get_in(item, 'screenNameChange', 'screenNameChange', 'changedFrom')
        base_row['changedTo'] = get_in(item, 'screenNameChange', 'screenNameChange', 'changedTo')
        records.append(base_row)
    return pd.DataFrame(records)


def tweet_headers_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['/tweet-headers.js'])
    records = []
    for item in data:
        base_row = {}
        base_row['tweet_id'] = get_in(item, 'tweet', 'tweet_id')
        base_row['user_id'] = get_in(item, 'tweet', 'user_id')
        base_row['created_at'] = get_in(item, 'tweet', 'created_at')
        records.append(base_row)
    return pd.DataFrame(records)


def tweets_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['/tweets.js'])
    records = []
    for item in data:
        base_row = {}
        base_row['editableUntil'] = get_in(item, 'tweet', 'edit_info', 'initial', 'editableUntil')
        base_row['editsRemaining'] = get_in(item, 'tweet', 'edit_info', 'initial', 'editsRemaining')
        base_row['isEditEligible'] = get_in(item, 'tweet', 'edit_info', 'initial', 'isEditEligible')
        base_row['retweeted'] = get_in(item, 'tweet', 'retweeted')
        base_row['source'] = get_in(item, 'tweet', 'source')
        base_row['favorite_count'] = get_in(item, 'tweet', 'favorite_count')
        base_row['id_str'] = get_in(item, 'tweet', 'id_str')
        base_row['truncated'] = get_in(item, 'tweet', 'truncated')
        base_row['retweet_count'] = get_in(item, 'tweet', 'retweet_count')
        base_row['id'] = get_in(item, 'tweet', 'id')
        base_row['created_at'] = get_in(item, 'tweet', 'created_at')
        base_row['favorited'] = get_in(item, 'tweet', 'favorited')
        base_row['full_text'] = get_in(item, 'tweet', 'full_text')
        base_row['lang'] = get_in(item, 'tweet', 'lang')
        for entry in get_list(item, 'tweet', 'entities', 'user_mentions'):
            row = base_row.copy()
            row['__source_list__'] = 'user_mentions'
            row['id'] = get_in(entry, 'id')
            row['id_str'] = get_in(entry, 'id_str')
            row['indices'] = get_in(entry, 'indices')
            row['name'] = get_in(entry, 'name')
            row['screen_name'] = get_in(entry, 'screen_name')
            records.append(row)
    return pd.DataFrame(records)


def verified_df(file_input: list[str]) -> pd.DataFrame:
    data = read_js(file_input, ['/verified.js'])
    records = []
    for item in data:
        base_row = {}
        base_row['accountId'] = get_in(item, 'verified', 'accountId')
        base_row['verified'] = get_in(item, 'verified', 'verified')
        records.append(base_row)
    return pd.DataFrame(records)


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
        df = connected_application_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='connected_application', df=df, title={'en': 'connected_application'})
            )
    except Exception as e:
        logger.error(f'Skipping connected_application_df: {e}')

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
        df = direct_messages_group_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='direct_messages_group', df=df, title={'en': 'direct_messages_group'})
            )
    except Exception as e:
        logger.error(f'Skipping direct_messages_group_df: {e}')

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
        df = key_registry_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='key_registry', df=df, title={'en': 'key_registry'})
            )
    except Exception as e:
        logger.error(f'Skipping key_registry_df: {e}')

    try:
        df = manifest_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='manifest', df=df, title={'en': 'manifest'})
            )
    except Exception as e:
        logger.error(f'Skipping manifest_df: {e}')

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
        df = profile_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='profile', df=df, title={'en': 'profile'})
            )
    except Exception as e:
        logger.error(f'Skipping profile_df: {e}')

    try:
        df = screen_name_change_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='screen_name_change', df=df, title={'en': 'screen_name_change'})
            )
    except Exception as e:
        logger.error(f'Skipping screen_name_change_df: {e}')

    try:
        df = tweet_headers_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='tweet_headers', df=df, title={'en': 'tweet_headers'})
            )
    except Exception as e:
        logger.error(f'Skipping tweet_headers_df: {e}')

    try:
        df = tweets_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='tweets', df=df, title={'en': 'tweets'})
            )
    except Exception as e:
        logger.error(f'Skipping tweets_df: {e}')

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