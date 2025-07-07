# Auto-generated Instagram extractors

import pandas as pd
import logging
from port.helpers.donation_flow import donation_table, donation_flow
from port.helpers.readers import read_json

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
    # Remove file extension
    name = re.sub(r"\.(json|js)$", "", name, flags=re.IGNORECASE)
    # Replace non-alphanumeric characters with underscore
    name = re.sub(r"[^\w]", "_", name)
    # Prefix with underscore if it starts with a digit
    if re.match(r"^\d", name):
        name = f"json_{name}"
    # Collapse multiple underscores
    name = re.sub(r"_+", "_", name)
    # Strip leading/trailing underscores
    return name.strip("_")

def extract_path(row):
    path = []
    for col in ["row_path"] + [f"col_path_{i}" for i in range(1, 6)]:
        val = row.get(col)
        if pd.notna(val) and str(val).strip().upper() != "MISSING":
            path.append(str(val).strip())
    return path

def ads_about_meta_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["/ads_about_meta.json"])
    records = []
    for item in data:
        base_row = {}
        base_row['fbid'] = get_in(item, 'fbid')
        base_row['ent_name'] = get_in(item, 'ent_name')
        base_row['media'] = get_in(item, 'media')
        for entry in get_list(item, 'label_values'):
            row = base_row.copy()
            row['__source_list__'] = 'label_values'
            row['ent_field_name'] = get_in(entry, 'ent_field_name')
            row['label'] = get_in(entry, 'label')
            row['value'] = get_in(entry, 'value')
            records.append(row)
    return pd.DataFrame(records)


def ads_clicked_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["/ads_clicked.json"])
    records = []
    for item in data:
        base_row = {}
        for entry in get_list(item, 'impressions_history_ads_clicked'):
            row = base_row.copy()
            row['__source_list__'] = 'impressions_history_ads_clicked'
            row['timestamp'] = get_in(entry, 'string_list_data', 'timestamp')
            row['title'] = get_in(entry, 'title')
            records.append(row)
    return pd.DataFrame(records)


def ads_viewed_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["/ads_viewed.json"])
    records = []
    for item in data:
        base_row = {}
        for entry in get_list(item, 'impressions_history_ads_seen'):
            row = base_row.copy()
            row['__source_list__'] = 'impressions_history_ads_seen'
            row['value'] = get_in(entry, 'string_map_data', 'Author', 'value')
            row['timestamp'] = get_in(entry, 'string_map_data', 'Time', 'timestamp')
            records.append(row)
    return pd.DataFrame(records)


def advertisers_using_your_activity_or_information_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["/advertisers_using_your_activity_or_information.json"])
    records = []
    for item in data:
        base_row = {}
        for entry in get_list(item, 'ig_custom_audiences_all_types'):
            row = base_row.copy()
            row['__source_list__'] = 'ig_custom_audiences_all_types'
            row['advertiser_name'] = get_in(entry, 'advertiser_name')
            row['has_data_file_custom_audience'] = get_in(entry, 'has_data_file_custom_audience')
            row['has_in_person_store_visit'] = get_in(entry, 'has_in_person_store_visit')
            row['has_remarketing_custom_audience'] = get_in(entry, 'has_remarketing_custom_audience')
            records.append(row)
    return pd.DataFrame(records)


def autofill_information_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["/autofill_information.json"])
    records = []
    for item in data:
        base_row = {}
        base_row['tel'] = get_in(item, 'ig_autofill_data', 'tel')
        base_row['tel_country_code'] = get_in(item, 'ig_autofill_data', 'tel_country_code')
        base_row['tel_national'] = get_in(item, 'ig_autofill_data', 'tel_national')
        base_row['tel_area_code'] = get_in(item, 'ig_autofill_data', 'tel_area_code')
        base_row['tel_local'] = get_in(item, 'ig_autofill_data', 'tel_local')
        base_row['tel_local_prefix'] = get_in(item, 'ig_autofill_data', 'tel_local_prefix')
        base_row['tel_local_suffix'] = get_in(item, 'ig_autofill_data', 'tel_local_suffix')
        base_row['street_address'] = get_in(item, 'ig_autofill_data', 'street_address')
        base_row['address_line1'] = get_in(item, 'ig_autofill_data', 'address_line1')
        base_row['address_line2'] = get_in(item, 'ig_autofill_data', 'address_line2')
        base_row['address_line3'] = get_in(item, 'ig_autofill_data', 'address_line3')
        base_row['address_level1'] = get_in(item, 'ig_autofill_data', 'address_level1')
        base_row['address_level2'] = get_in(item, 'ig_autofill_data', 'address_level2')
        base_row['address_level3'] = get_in(item, 'ig_autofill_data', 'address_level3')
        base_row['address_level4'] = get_in(item, 'ig_autofill_data', 'address_level4')
        base_row['country'] = get_in(item, 'ig_autofill_data', 'country')
        base_row['country_name'] = get_in(item, 'ig_autofill_data', 'country_name')
        base_row['postal_code'] = get_in(item, 'ig_autofill_data', 'postal_code')
        base_row['email'] = get_in(item, 'ig_autofill_data', 'email')
        base_row['family_name'] = get_in(item, 'ig_autofill_data', 'family_name')
        base_row['given_name'] = get_in(item, 'ig_autofill_data', 'given_name')
        records.append(base_row)
    return pd.DataFrame(records)


def avatar_items_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["/avatar_items.json"])
    records = []
    for item in data:
        base_row = {}
        for entry in get_list(item, 'ig_avatar_marketplace_avatar_items'):
            row = base_row.copy()
            row['__source_list__'] = 'ig_avatar_marketplace_avatar_items'
            row['acquisition_time'] = get_in(entry, 'acquisition_time')
            row['item'] = get_in(entry, 'item')
            row['type'] = get_in(entry, 'type')
            records.append(row)
    return pd.DataFrame(records)


def blocked_profiles_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["/blocked_profiles.json"])
    records = []
    for item in data:
        base_row = {}
        for entry in get_list(item, 'relationships_blocked_users'):
            row = base_row.copy()
            row['__source_list__'] = 'relationships_blocked_users'
            row['href'] = get_in(entry, 'string_list_data', 'href')
            row['timestamp'] = get_in(entry, 'string_list_data', 'timestamp')
            row['title'] = get_in(entry, 'title')
            records.append(row)
    return pd.DataFrame(records)


def camera_information_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["/camera_information.json"])
    records = []
    for item in data:
        base_row = {}
        for entry in get_list(item, 'devices_camera'):
            row = base_row.copy()
            row['__source_list__'] = 'devices_camera'
            row['media_map_data'] = get_in(entry, 'media_map_data')
            row['href'] = get_in(entry, 'string_map_data', 'Compression', 'href')
            row['timestamp'] = get_in(entry, 'string_map_data', 'Compression', 'timestamp')
            row['value'] = get_in(entry, 'string_map_data', 'Compression', 'value')
            row['href'] = get_in(entry, 'string_map_data', 'Device ID', 'href')
            row['timestamp'] = get_in(entry, 'string_map_data', 'Device ID', 'timestamp')
            row['value'] = get_in(entry, 'string_map_data', 'Device ID', 'value')
            row['href'] = get_in(entry, 'string_map_data', 'Face Tracker Version', 'href')
            row['timestamp'] = get_in(entry, 'string_map_data', 'Face Tracker Version', 'timestamp')
            row['value'] = get_in(entry, 'string_map_data', 'Face Tracker Version', 'value')
            row['href'] = get_in(entry, 'string_map_data', 'Supported SDK Versions', 'href')
            row['timestamp'] = get_in(entry, 'string_map_data', 'Supported SDK Versions', 'timestamp')
            row['value'] = get_in(entry, 'string_map_data', 'Supported SDK Versions', 'value')
            row['title'] = get_in(entry, 'title')
            records.append(row)
    return pd.DataFrame(records)


def close_friends_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["/close_friends.json"])
    records = []
    for item in data:
        base_row = {}
        for entry in get_list(item, 'relationships_close_friends'):
            row = base_row.copy()
            row['__source_list__'] = 'relationships_close_friends'
            row['media_list_data'] = get_in(entry, 'media_list_data')
            row['href'] = get_in(entry, 'string_list_data', 'href')
            row['timestamp'] = get_in(entry, 'string_list_data', 'timestamp')
            row['value'] = get_in(entry, 'string_list_data', 'value')
            row['title'] = get_in(entry, 'title')
            records.append(row)
    return pd.DataFrame(records)


def comments_allowed_from_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["/comments_allowed_from.json"])
    records = []
    for item in data:
        base_row = {}
        for entry in get_list(item, 'settings_allow_comments_from'):
            row = base_row.copy()
            row['__source_list__'] = 'settings_allow_comments_from'
            row['media_map_data'] = get_in(entry, 'media_map_data')
            row['href'] = get_in(entry, 'string_map_data', 'Comments Allowed From', 'href')
            row['timestamp'] = get_in(entry, 'string_map_data', 'Comments Allowed From', 'timestamp')
            row['value'] = get_in(entry, 'string_map_data', 'Comments Allowed From', 'value')
            row['title'] = get_in(entry, 'title')
            records.append(row)
    return pd.DataFrame(records)


def consents_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["/consents.json"])
    records = []
    for item in data:
        base_row = {}
        base_row['timestamp'] = get_in(item, 'timestamp')
        base_row['fbid'] = get_in(item, 'fbid')
        base_row['ent_name'] = get_in(item, 'ent_name')
        base_row['media'] = get_in(item, 'media')
        for entry in get_list(item, 'label_values'):
            row = base_row.copy()
            row['__source_list__'] = 'label_values'
            row['ent_field_name'] = get_in(entry, 'ent_field_name')
            row['label'] = get_in(entry, 'label')
            records.append(row)
    return pd.DataFrame(records)


def devices_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["/devices.json"])
    records = []
    for item in data:
        base_row = {}
        for entry in get_list(item, 'devices_devices'):
            row = base_row.copy()
            row['__source_list__'] = 'devices_devices'
            row['media_map_data'] = get_in(entry, 'media_map_data')
            row['href'] = get_in(entry, 'string_map_data', 'Last Login', 'href')
            row['timestamp'] = get_in(entry, 'string_map_data', 'Last Login', 'timestamp')
            row['value'] = get_in(entry, 'string_map_data', 'Last Login', 'value')
            row['href'] = get_in(entry, 'string_map_data', 'User Agent', 'href')
            row['timestamp'] = get_in(entry, 'string_map_data', 'User Agent', 'timestamp')
            row['value'] = get_in(entry, 'string_map_data', 'User Agent', 'value')
            row['title'] = get_in(entry, 'title')
            records.append(row)
    return pd.DataFrame(records)


def eligibility_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["/eligibility.json"])
    records = []
    for item in data:
        base_row = {}
        for entry in get_list(item, 'monetization_eligibility'):
            row = base_row.copy()
            row['__source_list__'] = 'monetization_eligibility'
            row['media_map_data'] = get_in(entry, 'media_map_data')
            row['href'] = get_in(entry, 'string_map_data', 'Decision', 'href')
            row['timestamp'] = get_in(entry, 'string_map_data', 'Decision', 'timestamp')
            row['value'] = get_in(entry, 'string_map_data', 'Decision', 'value')
            row['href'] = get_in(entry, 'string_map_data', 'Product Name', 'href')
            row['timestamp'] = get_in(entry, 'string_map_data', 'Product Name', 'timestamp')
            row['value'] = get_in(entry, 'string_map_data', 'Product Name', 'value')
            row['href'] = get_in(entry, 'string_map_data', 'Reason', 'href')
            row['timestamp'] = get_in(entry, 'string_map_data', 'Reason', 'timestamp')
            row['value'] = get_in(entry, 'string_map_data', 'Reason', 'value')
            row['title'] = get_in(entry, 'title')
            records.append(row)
    return pd.DataFrame(records)


def emoji_sliders_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["/emoji_sliders.json"])
    records = []
    for item in data:
        base_row = {}
        for entry in get_list(item, 'story_activities_emoji_sliders'):
            row = base_row.copy()
            row['__source_list__'] = 'story_activities_emoji_sliders'
            row['timestamp'] = get_in(entry, 'string_list_data', 'timestamp')
            row['value'] = get_in(entry, 'string_list_data', 'value')
            row['title'] = get_in(entry, 'title')
            records.append(row)
    return pd.DataFrame(records)


def follow_requests_you_ve_received_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["/follow_requests_you've_received.json"])
    records = []
    for item in data:
        base_row = {}
        for entry in get_list(item, 'relationships_follow_requests_received'):
            row = base_row.copy()
            row['__source_list__'] = 'relationships_follow_requests_received'
            row['media_list_data'] = get_in(entry, 'media_list_data')
            row['href'] = get_in(entry, 'string_list_data', 'href')
            row['timestamp'] = get_in(entry, 'string_list_data', 'timestamp')
            row['value'] = get_in(entry, 'string_list_data', 'value')
            row['title'] = get_in(entry, 'title')
            records.append(row)
    return pd.DataFrame(records)


def followers_1_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["/followers_1.json"])
    records = []
    for item in data:
        base_row = {}
        base_row['title'] = get_in(item, 'title')
        base_row['media_list_data'] = get_in(item, 'media_list_data')
        for entry in get_list(item, 'string_list_data'):
            row = base_row.copy()
            row['__source_list__'] = 'string_list_data'
            row['href'] = get_in(entry, 'href')
            row['timestamp'] = get_in(entry, 'timestamp')
            row['value'] = get_in(entry, 'value')
            records.append(row)
    return pd.DataFrame(records)


def following_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["/following.json"])
    records = []
    for item in data:
        base_row = {}
        for entry in get_list(item, 'relationships_following'):
            row = base_row.copy()
            row['__source_list__'] = 'relationships_following'
            row['media_list_data'] = get_in(entry, 'media_list_data')
            row['href'] = get_in(entry, 'string_list_data', 'href')
            row['timestamp'] = get_in(entry, 'string_list_data', 'timestamp')
            row['value'] = get_in(entry, 'string_list_data', 'value')
            row['title'] = get_in(entry, 'title')
            records.append(row)
    return pd.DataFrame(records)


def following_hashtags_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["/following_hashtags.json"])
    records = []
    for item in data:
        base_row = {}
        for entry in get_list(item, 'relationships_following_hashtags'):
            row = base_row.copy()
            row['__source_list__'] = 'relationships_following_hashtags'
            row['media_list_data'] = get_in(entry, 'media_list_data')
            row['href'] = get_in(entry, 'string_list_data', 'href')
            row['timestamp'] = get_in(entry, 'string_list_data', 'timestamp')
            row['value'] = get_in(entry, 'string_list_data', 'value')
            row['title'] = get_in(entry, 'title')
            records.append(row)
    return pd.DataFrame(records)


def in_app_browser_autofill_settings_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["/in-app_browser_autofill_settings.json"])
    records = []
    for item in data:
        base_row = {}
        base_row['media'] = get_in(item, 'media')
        base_row['fbid'] = get_in(item, 'fbid')
        for entry in get_list(item, 'label_values'):
            row = base_row.copy()
            row['__source_list__'] = 'label_values'
            row['label'] = get_in(entry, 'label')
            records.append(row)
    return pd.DataFrame(records)


def information_you_ve_submitted_to_advertisers_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["/information_you've_submitted_to_advertisers.json"])
    records = []
    for item in data:
        base_row = {}
        for entry in get_list(item, 'ig_lead_gen_info'):
            row = base_row.copy()
            row['__source_list__'] = 'ig_lead_gen_info'
            row['label'] = get_in(entry, 'label')
            row['value'] = get_in(entry, 'value')
            records.append(row)
    return pd.DataFrame(records)


def instagram_profile_information_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["/instagram_profile_information.json"])
    records = []
    for item in data:
        base_row = {}
        for entry in get_list(item, 'profile_account_insights'):
            row = base_row.copy()
            row['__source_list__'] = 'profile_account_insights'
            row['media_map_data'] = get_in(entry, 'media_map_data')
            row['href'] = get_in(entry, 'string_map_data', 'Contact Syncing', 'href')
            row['timestamp'] = get_in(entry, 'string_map_data', 'Contact Syncing', 'timestamp')
            row['value'] = get_in(entry, 'string_map_data', 'Contact Syncing', 'value')
            row['href'] = get_in(entry, 'string_map_data', 'First Close Friends Story Time', 'href')
            row['timestamp'] = get_in(entry, 'string_map_data', 'First Close Friends Story Time', 'timestamp')
            row['value'] = get_in(entry, 'string_map_data', 'First Close Friends Story Time', 'value')
            row['href'] = get_in(entry, 'string_map_data', 'First Country Code', 'href')
            row['timestamp'] = get_in(entry, 'string_map_data', 'First Country Code', 'timestamp')
            row['value'] = get_in(entry, 'string_map_data', 'First Country Code', 'value')
            row['href'] = get_in(entry, 'string_map_data', 'First Story Time', 'href')
            row['timestamp'] = get_in(entry, 'string_map_data', 'First Story Time', 'timestamp')
            row['value'] = get_in(entry, 'string_map_data', 'First Story Time', 'value')
            row['href'] = get_in(entry, 'string_map_data', 'Has Shared Live Video', 'href')
            row['timestamp'] = get_in(entry, 'string_map_data', 'Has Shared Live Video', 'timestamp')
            row['value'] = get_in(entry, 'string_map_data', 'Has Shared Live Video', 'value')
            row['href'] = get_in(entry, 'string_map_data', 'Last Login', 'href')
            row['timestamp'] = get_in(entry, 'string_map_data', 'Last Login', 'timestamp')
            row['value'] = get_in(entry, 'string_map_data', 'Last Login', 'value')
            row['href'] = get_in(entry, 'string_map_data', 'Last Logout', 'href')
            row['timestamp'] = get_in(entry, 'string_map_data', 'Last Logout', 'timestamp')
            row['value'] = get_in(entry, 'string_map_data', 'Last Logout', 'value')
            row['href'] = get_in(entry, 'string_map_data', 'Last Story Time', 'href')
            row['timestamp'] = get_in(entry, 'string_map_data', 'Last Story Time', 'timestamp')
            row['value'] = get_in(entry, 'string_map_data', 'Last Story Time', 'value')
            row['title'] = get_in(entry, 'title')
            records.append(row)
    return pd.DataFrame(records)


def instagram_signup_details_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["/instagram_signup_details.json"])
    records = []
    for item in data:
        base_row = {}
        for entry in get_list(item, 'account_history_registration_info'):
            row = base_row.copy()
            row['__source_list__'] = 'account_history_registration_info'
            row['media_map_data'] = get_in(entry, 'media_map_data')
            row['href'] = get_in(entry, 'string_map_data', 'Device', 'href')
            row['timestamp'] = get_in(entry, 'string_map_data', 'Device', 'timestamp')
            row['value'] = get_in(entry, 'string_map_data', 'Device', 'value')
            row['href'] = get_in(entry, 'string_map_data', 'Email', 'href')
            row['timestamp'] = get_in(entry, 'string_map_data', 'Email', 'timestamp')
            row['value'] = get_in(entry, 'string_map_data', 'Email', 'value')
            row['href'] = get_in(entry, 'string_map_data', 'IP Address', 'href')
            row['timestamp'] = get_in(entry, 'string_map_data', 'IP Address', 'timestamp')
            row['value'] = get_in(entry, 'string_map_data', 'IP Address', 'value')
            row['href'] = get_in(entry, 'string_map_data', 'Phone Number', 'href')
            row['timestamp'] = get_in(entry, 'string_map_data', 'Phone Number', 'timestamp')
            row['value'] = get_in(entry, 'string_map_data', 'Phone Number', 'value')
            row['href'] = get_in(entry, 'string_map_data', 'Time', 'href')
            row['timestamp'] = get_in(entry, 'string_map_data', 'Time', 'timestamp')
            row['value'] = get_in(entry, 'string_map_data', 'Time', 'value')
            row['href'] = get_in(entry, 'string_map_data', 'Username', 'href')
            row['timestamp'] = get_in(entry, 'string_map_data', 'Username', 'timestamp')
            row['value'] = get_in(entry, 'string_map_data', 'Username', 'value')
            row['title'] = get_in(entry, 'title')
            records.append(row)
    return pd.DataFrame(records)


def last_known_location_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["/last_known_location.json"])
    records = []
    for item in data:
        base_row = {}
        for entry in get_list(item, 'account_history_imprecise_last_known_location'):
            row = base_row.copy()
            row['__source_list__'] = 'account_history_imprecise_last_known_location'
            row['media_map_data'] = get_in(entry, 'media_map_data')
            row['href'] = get_in(entry, 'string_map_data', 'GPS Time Uploaded', 'href')
            row['timestamp'] = get_in(entry, 'string_map_data', 'GPS Time Uploaded', 'timestamp')
            row['value'] = get_in(entry, 'string_map_data', 'GPS Time Uploaded', 'value')
            row['href'] = get_in(entry, 'string_map_data', 'Imprecise Latitude', 'href')
            row['timestamp'] = get_in(entry, 'string_map_data', 'Imprecise Latitude', 'timestamp')
            row['value'] = get_in(entry, 'string_map_data', 'Imprecise Latitude', 'value')
            row['href'] = get_in(entry, 'string_map_data', 'Imprecise Longitude', 'href')
            row['timestamp'] = get_in(entry, 'string_map_data', 'Imprecise Longitude', 'timestamp')
            row['value'] = get_in(entry, 'string_map_data', 'Imprecise Longitude', 'value')
            row['href'] = get_in(entry, 'string_map_data', 'Precise Latitude', 'href')
            row['timestamp'] = get_in(entry, 'string_map_data', 'Precise Latitude', 'timestamp')
            row['value'] = get_in(entry, 'string_map_data', 'Precise Latitude', 'value')
            row['href'] = get_in(entry, 'string_map_data', 'Precise Longitude', 'href')
            row['timestamp'] = get_in(entry, 'string_map_data', 'Precise Longitude', 'timestamp')
            row['value'] = get_in(entry, 'string_map_data', 'Precise Longitude', 'value')
            row['title'] = get_in(entry, 'title')
            records.append(row)
    return pd.DataFrame(records)


def liked_comments_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["/liked_comments.json"])
    records = []
    for item in data:
        base_row = {}
        for entry in get_list(item, 'likes_comment_likes'):
            row = base_row.copy()
            row['__source_list__'] = 'likes_comment_likes'
            row['href'] = get_in(entry, 'string_list_data', 'href')
            row['timestamp'] = get_in(entry, 'string_list_data', 'timestamp')
            row['value'] = get_in(entry, 'string_list_data', 'value')
            row['title'] = get_in(entry, 'title')
            records.append(row)
    return pd.DataFrame(records)


def liked_posts_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["/liked_posts.json"])
    records = []
    for item in data:
        base_row = {}
        for entry in get_list(item, 'likes_media_likes'):
            row = base_row.copy()
            row['__source_list__'] = 'likes_media_likes'
            row['href'] = get_in(entry, 'string_list_data', 'href')
            row['timestamp'] = get_in(entry, 'string_list_data', 'timestamp')
            row['value'] = get_in(entry, 'string_list_data', 'value')
            row['title'] = get_in(entry, 'title')
            records.append(row)
    return pd.DataFrame(records)


def linked_meta_accounts_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["/linked_meta_accounts.json"])
    records = []
    for item in data:
        base_row = {}
        base_row['timestamp'] = get_in(item, 'timestamp')
        base_row['media'] = get_in(item, 'media')
        base_row['fbid'] = get_in(item, 'fbid')
        base_row['ent_name'] = get_in(item, 'ent_name')
        for entry in get_list(item, 'label_values'):
            row = base_row.copy()
            row['__source_list__'] = 'label_values'
            row['title'] = get_in(entry, 'title')
            records.append(row)
    return pd.DataFrame(records)


def locations_of_interest_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["/locations_of_interest.json"])
    records = []
    for item in data:
        base_row = {}
        base_row['fbid'] = get_in(item, 'fbid')
        base_row['ent_name'] = get_in(item, 'ent_name')
        base_row['media'] = get_in(item, 'media')
        for entry in get_list(item, 'label_values'):
            row = base_row.copy()
            row['__source_list__'] = 'label_values'
            row['ent_field_name'] = get_in(entry, 'ent_field_name')
            row['label'] = get_in(entry, 'label')
            row['value'] = get_in(entry, 'vec', 'value')
            records.append(row)
    return pd.DataFrame(records)


def login_activity_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["/login_activity.json"])
    records = []
    for item in data:
        base_row = {}
        for entry in get_list(item, 'account_history_login_history'):
            row = base_row.copy()
            row['__source_list__'] = 'account_history_login_history'
            row['media_map_data'] = get_in(entry, 'media_map_data')
            row['href'] = get_in(entry, 'string_map_data', 'Cookie Name', 'href')
            row['timestamp'] = get_in(entry, 'string_map_data', 'Cookie Name', 'timestamp')
            row['value'] = get_in(entry, 'string_map_data', 'Cookie Name', 'value')
            row['href'] = get_in(entry, 'string_map_data', 'IP Address', 'href')
            row['timestamp'] = get_in(entry, 'string_map_data', 'IP Address', 'timestamp')
            row['value'] = get_in(entry, 'string_map_data', 'IP Address', 'value')
            row['href'] = get_in(entry, 'string_map_data', 'Language Code', 'href')
            row['timestamp'] = get_in(entry, 'string_map_data', 'Language Code', 'timestamp')
            row['value'] = get_in(entry, 'string_map_data', 'Language Code', 'value')
            row['href'] = get_in(entry, 'string_map_data', 'Port', 'href')
            row['timestamp'] = get_in(entry, 'string_map_data', 'Port', 'timestamp')
            row['value'] = get_in(entry, 'string_map_data', 'Port', 'value')
            row['href'] = get_in(entry, 'string_map_data', 'Time', 'href')
            row['timestamp'] = get_in(entry, 'string_map_data', 'Time', 'timestamp')
            row['value'] = get_in(entry, 'string_map_data', 'Time', 'value')
            row['href'] = get_in(entry, 'string_map_data', 'User Agent', 'href')
            row['timestamp'] = get_in(entry, 'string_map_data', 'User Agent', 'timestamp')
            row['value'] = get_in(entry, 'string_map_data', 'User Agent', 'value')
            row['title'] = get_in(entry, 'title')
            records.append(row)
    return pd.DataFrame(records)


def message_1_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["/message_1.json"])
    records = []
    for item in data:
        base_row = {}
        base_row['title'] = get_in(item, 'title')
        base_row['is_still_participant'] = get_in(item, 'is_still_participant')
        base_row['thread_path'] = get_in(item, 'thread_path')
        base_row['is_pending'] = get_in(item, 'is_pending')
        base_row['magic_words'] = get_in(item, 'magic_words')
        base_row['mode'] = get_in(item, 'joinable_mode', 'mode')
        base_row['link'] = get_in(item, 'joinable_mode', 'link')
        base_row['uri'] = get_in(item, 'image', 'uri')
        base_row['creation_timestamp'] = get_in(item, 'image', 'creation_timestamp')
        for entry in get_list(item, 'participants'):
            row = base_row.copy()
            row['__source_list__'] = 'participants'
            row['name'] = get_in(entry, 'name')
            records.append(row)
        for entry in get_list(item, 'messages'):
            row = base_row.copy()
            row['__source_list__'] = 'messages'
            row['content'] = get_in(entry, 'content')
            row['is_geoblocked_for_viewer'] = get_in(entry, 'is_geoblocked_for_viewer')
            row['is_unsent_image_by_messenger_kid_parent'] = get_in(entry, 'is_unsent_image_by_messenger_kid_parent')
            row['creation_timestamp'] = get_in(entry, 'photos', 'creation_timestamp')
            row['uri'] = get_in(entry, 'photos', 'uri')
            row['actor'] = get_in(entry, 'reactions', 'actor')
            row['reaction'] = get_in(entry, 'reactions', 'reaction')
            row['timestamp'] = get_in(entry, 'reactions', 'timestamp')
            row['sender_name'] = get_in(entry, 'sender_name')
            row['link'] = get_in(entry, 'share', 'link')
            row['original_content_owner'] = get_in(entry, 'share', 'original_content_owner')
            row['share_text'] = get_in(entry, 'share', 'share_text')
            row['timestamp_ms'] = get_in(entry, 'timestamp_ms')
            records.append(row)
    return pd.DataFrame(records)


def note_interactions_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["/note_interactions.json"])
    records = []
    for item in data:
        base_row = {}
        for entry in get_list(item, 'profile_note_interactions'):
            row = base_row.copy()
            row['__source_list__'] = 'profile_note_interactions'
            row['media_map_data'] = get_in(entry, 'media_map_data')
            row['href'] = get_in(entry, 'string_map_data', 'Last Notes Seen Time', 'href')
            row['timestamp'] = get_in(entry, 'string_map_data', 'Last Notes Seen Time', 'timestamp')
            row['value'] = get_in(entry, 'string_map_data', 'Last Notes Seen Time', 'value')
            row['title'] = get_in(entry, 'title')
            records.append(row)
    return pd.DataFrame(records)


def notification_of_privacy_policy_updates_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["/notification_of_privacy_policy_updates.json"])
    records = []
    for item in data:
        base_row = {}
        for entry in get_list(item, 'policy_updates_and_permissions_notification_of_privacy_policy_updates'):
            row = base_row.copy()
            row['__source_list__'] = 'policy_updates_and_permissions_notification_of_privacy_policy_updates'
            row['value'] = get_in(entry, 'string_map_data', 'Consent Status', 'value')
            row['value'] = get_in(entry, 'string_map_data', 'Impression Time', 'value')
            records.append(row)
    return pd.DataFrame(records)


def notification_preferences_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["/notification_preferences.json"])
    records = []
    for item in data:
        base_row = {}
        for entry in get_list(item, 'settings_notification_preferences'):
            row = base_row.copy()
            row['__source_list__'] = 'settings_notification_preferences'
            row['value'] = get_in(entry, 'string_map_data', 'Channel', 'value')
            row['value'] = get_in(entry, 'string_map_data', 'Type', 'value')
            row['value'] = get_in(entry, 'string_map_data', 'Value', 'value')
            records.append(row)
    return pd.DataFrame(records)


def other_categories_used_to_reach_you_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["/other_categories_used_to_reach_you.json"])
    records = []
    for item in data:
        base_row = {}
        base_row['fbid'] = get_in(item, 'fbid')
        base_row['ent_name'] = get_in(item, 'ent_name')
        base_row['media'] = get_in(item, 'media')
        for entry in get_list(item, 'label_values'):
            row = base_row.copy()
            row['__source_list__'] = 'label_values'
            row['ent_field_name'] = get_in(entry, 'ent_field_name')
            row['label'] = get_in(entry, 'label')
            row['value'] = get_in(entry, 'vec', 'value')
            records.append(row)
    return pd.DataFrame(records)


def password_change_activity_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["/password_change_activity.json"])
    records = []
    for item in data:
        base_row = {}
        for entry in get_list(item, 'account_history_password_change_history'):
            row = base_row.copy()
            row['__source_list__'] = 'account_history_password_change_history'
            row['media_map_data'] = get_in(entry, 'media_map_data')
            row['href'] = get_in(entry, 'string_map_data', 'Time', 'href')
            row['timestamp'] = get_in(entry, 'string_map_data', 'Time', 'timestamp')
            row['value'] = get_in(entry, 'string_map_data', 'Time', 'value')
            row['title'] = get_in(entry, 'title')
            records.append(row)
    return pd.DataFrame(records)


def pending_follow_requests_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["/pending_follow_requests.json"])
    records = []
    for item in data:
        base_row = {}
        for entry in get_list(item, 'relationships_follow_requests_sent'):
            row = base_row.copy()
            row['__source_list__'] = 'relationships_follow_requests_sent'
            row['media_list_data'] = get_in(entry, 'media_list_data')
            row['href'] = get_in(entry, 'string_list_data', 'href')
            row['timestamp'] = get_in(entry, 'string_list_data', 'timestamp')
            row['value'] = get_in(entry, 'string_list_data', 'value')
            row['title'] = get_in(entry, 'title')
            records.append(row)
    return pd.DataFrame(records)


def personal_information_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["/personal_information.json"])
    records = []
    for item in data:
        base_row = {}
        for entry in get_list(item, 'profile_user'):
            row = base_row.copy()
            row['__source_list__'] = 'profile_user'
            row['media_map_data'] = get_in(entry, 'media_map_data')
            row['backup_uri'] = get_in(entry, 'media_map_data', 'Profile Photo', 'backup_uri')
            row['creation_timestamp'] = get_in(entry, 'media_map_data', 'Profile Photo', 'creation_timestamp')
            row['source_app'] = get_in(entry, 'media_map_data', 'Profile Photo', 'cross_post_source', 'source_app')
            row['has_camera_metadata'] = get_in(entry, 'media_map_data', 'Profile Photo', 'media_metadata', 'camera_metadata', 'has_camera_metadata')
            row['title'] = get_in(entry, 'media_map_data', 'Profile Photo', 'title')
            row['uri'] = get_in(entry, 'media_map_data', 'Profile Photo', 'uri')
            row['href'] = get_in(entry, 'string_map_data', 'Bio', 'href')
            row['timestamp'] = get_in(entry, 'string_map_data', 'Bio', 'timestamp')
            row['value'] = get_in(entry, 'string_map_data', 'Bio', 'value')
            row['href'] = get_in(entry, 'string_map_data', 'Date of birth', 'href')
            row['timestamp'] = get_in(entry, 'string_map_data', 'Date of birth', 'timestamp')
            row['value'] = get_in(entry, 'string_map_data', 'Date of birth', 'value')
            row['href'] = get_in(entry, 'string_map_data', 'Email', 'href')
            row['timestamp'] = get_in(entry, 'string_map_data', 'Email', 'timestamp')
            row['value'] = get_in(entry, 'string_map_data', 'Email', 'value')
            row['href'] = get_in(entry, 'string_map_data', 'Emoji Pong High Score', 'href')
            row['timestamp'] = get_in(entry, 'string_map_data', 'Emoji Pong High Score', 'timestamp')
            row['value'] = get_in(entry, 'string_map_data', 'Emoji Pong High Score', 'value')
            row['href'] = get_in(entry, 'string_map_data', 'Gender', 'href')
            row['timestamp'] = get_in(entry, 'string_map_data', 'Gender', 'timestamp')
            row['value'] = get_in(entry, 'string_map_data', 'Gender', 'value')
            row['href'] = get_in(entry, 'string_map_data', 'Name', 'href')
            row['timestamp'] = get_in(entry, 'string_map_data', 'Name', 'timestamp')
            row['value'] = get_in(entry, 'string_map_data', 'Name', 'value')
            row['href'] = get_in(entry, 'string_map_data', 'Phone Confirmation Method', 'href')
            row['timestamp'] = get_in(entry, 'string_map_data', 'Phone Confirmation Method', 'timestamp')
            row['value'] = get_in(entry, 'string_map_data', 'Phone Confirmation Method', 'value')
            row['href'] = get_in(entry, 'string_map_data', 'Phone Confirmed', 'href')
            row['timestamp'] = get_in(entry, 'string_map_data', 'Phone Confirmed', 'timestamp')
            row['value'] = get_in(entry, 'string_map_data', 'Phone Confirmed', 'value')
            row['href'] = get_in(entry, 'string_map_data', 'Phone Number', 'href')
            row['timestamp'] = get_in(entry, 'string_map_data', 'Phone Number', 'timestamp')
            row['value'] = get_in(entry, 'string_map_data', 'Phone Number', 'value')
            row['href'] = get_in(entry, 'string_map_data', 'Private Account', 'href')
            row['timestamp'] = get_in(entry, 'string_map_data', 'Private Account', 'timestamp')
            row['value'] = get_in(entry, 'string_map_data', 'Private Account', 'value')
            row['href'] = get_in(entry, 'string_map_data', 'Username', 'href')
            row['timestamp'] = get_in(entry, 'string_map_data', 'Username', 'timestamp')
            row['value'] = get_in(entry, 'string_map_data', 'Username', 'value')
            row['title'] = get_in(entry, 'title')
            records.append(row)
    return pd.DataFrame(records)


def polls_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["/polls.json"])
    records = []
    for item in data:
        base_row = {}
        for entry in get_list(item, 'story_activities_polls'):
            row = base_row.copy()
            row['__source_list__'] = 'story_activities_polls'
            row['timestamp'] = get_in(entry, 'string_list_data', 'timestamp')
            row['value'] = get_in(entry, 'string_list_data', 'value')
            row['title'] = get_in(entry, 'title')
            records.append(row)
    return pd.DataFrame(records)


def possible_emails_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["/possible_emails.json"])
    records = []
    for item in data:
        base_row = {}
        for entry in get_list(item, 'inferred_data_inferred_emails'):
            row = base_row.copy()
            row['__source_list__'] = 'inferred_data_inferred_emails'
            row['media_list_data'] = get_in(entry, 'media_list_data')
            row['href'] = get_in(entry, 'string_list_data', 'href')
            row['timestamp'] = get_in(entry, 'string_list_data', 'timestamp')
            row['value'] = get_in(entry, 'string_list_data', 'value')
            row['title'] = get_in(entry, 'title')
            records.append(row)
    return pd.DataFrame(records)


def post_comments_1_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["/post_comments_1.json"])
    records = []
    for item in data:
        base_row = {}
        base_row['value'] = get_in(item, 'string_map_data', 'Comment', 'value')
        base_row['timestamp'] = get_in(item, 'string_map_data', 'Time', 'timestamp')
        for entry in get_list(item, 'media_list_data'):
            row = base_row.copy()
            row['__source_list__'] = 'media_list_data'
            row['uri'] = get_in(entry, 'uri')
            records.append(row)
    return pd.DataFrame(records)


def posts_1_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["/posts_1.json"])
    records = []
    for item in data:
        base_row = {}
        base_row['title'] = get_in(item, 'title')
        base_row['creation_timestamp'] = get_in(item, 'creation_timestamp')
        for entry in get_list(item, 'media'):
            row = base_row.copy()
            row['__source_list__'] = 'media'
            row['creation_timestamp'] = get_in(entry, 'creation_timestamp')
            row['source_app'] = get_in(entry, 'cross_post_source', 'source_app')
            row['has_camera_metadata'] = get_in(entry, 'media_metadata', 'camera_metadata', 'has_camera_metadata')
            row['title'] = get_in(entry, 'title')
            row['uri'] = get_in(entry, 'uri')
            records.append(row)
    return pd.DataFrame(records)


def posts_viewed_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["/posts_viewed.json"])
    records = []
    for item in data:
        base_row = {}
        for entry in get_list(item, 'impressions_history_posts_seen'):
            row = base_row.copy()
            row['__source_list__'] = 'impressions_history_posts_seen'
            row['value'] = get_in(entry, 'string_map_data', 'Author', 'value')
            row['timestamp'] = get_in(entry, 'string_map_data', 'Time', 'timestamp')
            records.append(row)
    return pd.DataFrame(records)


def posts_you_re_not_interested_in_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["/posts_you're_not_interested_in.json"])
    records = []
    for item in data:
        base_row = {}
        for entry in get_list(item, 'impressions_history_posts_not_interested'):
            row = base_row.copy()
            row['__source_list__'] = 'impressions_history_posts_not_interested'
            row['href'] = get_in(entry, 'string_list_data', 'href')
            row['value'] = get_in(entry, 'string_list_data', 'value')
            records.append(row)
    return pd.DataFrame(records)


def professional_information_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["/professional_information.json"])
    records = []
    for item in data:
        base_row = {}
        for entry in get_list(item, 'profile_business'):
            row = base_row.copy()
            row['__source_list__'] = 'profile_business'
            row['media_map_data'] = get_in(entry, 'media_map_data')
            row['string_map_data'] = get_in(entry, 'string_map_data')
            row['title'] = get_in(entry, 'title')
            records.append(row)
    return pd.DataFrame(records)


def profile_based_in_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["/profile_based_in.json"])
    records = []
    for item in data:
        base_row = {}
        for entry in get_list(item, 'inferred_data_primary_location'):
            row = base_row.copy()
            row['__source_list__'] = 'inferred_data_primary_location'
            row['media_map_data'] = get_in(entry, 'media_map_data')
            row['href'] = get_in(entry, 'string_map_data', 'City Name', 'href')
            row['timestamp'] = get_in(entry, 'string_map_data', 'City Name', 'timestamp')
            row['value'] = get_in(entry, 'string_map_data', 'City Name', 'value')
            row['title'] = get_in(entry, 'title')
            records.append(row)
    return pd.DataFrame(records)


def profile_changes_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["/profile_changes.json"])
    records = []
    for item in data:
        base_row = {}
        for entry in get_list(item, 'profile_profile_change'):
            row = base_row.copy()
            row['__source_list__'] = 'profile_profile_change'
            row['media_map_data'] = get_in(entry, 'media_map_data')
            row['href'] = get_in(entry, 'string_map_data', 'Change Date', 'href')
            row['timestamp'] = get_in(entry, 'string_map_data', 'Change Date', 'timestamp')
            row['value'] = get_in(entry, 'string_map_data', 'Change Date', 'value')
            row['href'] = get_in(entry, 'string_map_data', 'Changed', 'href')
            row['timestamp'] = get_in(entry, 'string_map_data', 'Changed', 'timestamp')
            row['value'] = get_in(entry, 'string_map_data', 'Changed', 'value')
            row['href'] = get_in(entry, 'string_map_data', 'New Value', 'href')
            row['timestamp'] = get_in(entry, 'string_map_data', 'New Value', 'timestamp')
            row['value'] = get_in(entry, 'string_map_data', 'New Value', 'value')
            row['href'] = get_in(entry, 'string_map_data', 'Previous Value', 'href')
            row['timestamp'] = get_in(entry, 'string_map_data', 'Previous Value', 'timestamp')
            row['value'] = get_in(entry, 'string_map_data', 'Previous Value', 'value')
            row['title'] = get_in(entry, 'title')
            records.append(row)
    return pd.DataFrame(records)


def profile_photos_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["/profile_photos.json"])
    records = []
    for item in data:
        base_row = {}
        for entry in get_list(item, 'ig_profile_picture'):
            row = base_row.copy()
            row['__source_list__'] = 'ig_profile_picture'
            row['backup_uri'] = get_in(entry, 'backup_uri')
            row['creation_timestamp'] = get_in(entry, 'creation_timestamp')
            row['source_app'] = get_in(entry, 'cross_post_source', 'source_app')
            row['is_profile_picture'] = get_in(entry, 'is_profile_picture')
            row['has_camera_metadata'] = get_in(entry, 'media_metadata', 'camera_metadata', 'has_camera_metadata')
            row['title'] = get_in(entry, 'title')
            row['uri'] = get_in(entry, 'uri')
            records.append(row)
    return pd.DataFrame(records)


def profile_privacy_changes_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["/profile_privacy_changes.json"])
    records = []
    for item in data:
        base_row = {}
        for entry in get_list(item, 'account_history_account_privacy_history'):
            row = base_row.copy()
            row['__source_list__'] = 'account_history_account_privacy_history'
            row['media_map_data'] = get_in(entry, 'media_map_data')
            row['href'] = get_in(entry, 'string_map_data', 'Time', 'href')
            row['timestamp'] = get_in(entry, 'string_map_data', 'Time', 'timestamp')
            row['value'] = get_in(entry, 'string_map_data', 'Time', 'value')
            row['title'] = get_in(entry, 'title')
            records.append(row)
    return pd.DataFrame(records)


def profile_searches_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["/profile_searches.json"])
    records = []
    for item in data:
        base_row = {}
        for entry in get_list(item, 'searches_user'):
            row = base_row.copy()
            row['__source_list__'] = 'searches_user'
            row['media_map_data'] = get_in(entry, 'media_map_data')
            row['href'] = get_in(entry, 'string_map_data', 'Search', 'href')
            row['timestamp'] = get_in(entry, 'string_map_data', 'Search', 'timestamp')
            row['value'] = get_in(entry, 'string_map_data', 'Search', 'value')
            row['href'] = get_in(entry, 'string_map_data', 'Time', 'href')
            row['timestamp'] = get_in(entry, 'string_map_data', 'Time', 'timestamp')
            row['value'] = get_in(entry, 'string_map_data', 'Time', 'value')
            row['title'] = get_in(entry, 'title')
            records.append(row)
    return pd.DataFrame(records)


def profile_status_changes_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["/profile_status_changes.json"])
    records = []
    for item in data:
        base_row = {}
        for entry in get_list(item, 'account_history_account_active_status_changes'):
            row = base_row.copy()
            row['__source_list__'] = 'account_history_account_active_status_changes'
            row['media_map_data'] = get_in(entry, 'media_map_data')
            row['href'] = get_in(entry, 'string_map_data', 'Activation Type', 'href')
            row['timestamp'] = get_in(entry, 'string_map_data', 'Activation Type', 'timestamp')
            row['value'] = get_in(entry, 'string_map_data', 'Activation Type', 'value')
            row['href'] = get_in(entry, 'string_map_data', 'Automated', 'href')
            row['timestamp'] = get_in(entry, 'string_map_data', 'Automated', 'timestamp')
            row['value'] = get_in(entry, 'string_map_data', 'Automated', 'value')
            row['href'] = get_in(entry, 'string_map_data', 'Inactivation Reason', 'href')
            row['timestamp'] = get_in(entry, 'string_map_data', 'Inactivation Reason', 'timestamp')
            row['value'] = get_in(entry, 'string_map_data', 'Inactivation Reason', 'value')
            row['href'] = get_in(entry, 'string_map_data', 'Time', 'href')
            row['timestamp'] = get_in(entry, 'string_map_data', 'Time', 'timestamp')
            row['value'] = get_in(entry, 'string_map_data', 'Time', 'value')
            row['title'] = get_in(entry, 'title')
            records.append(row)
    return pd.DataFrame(records)


def profiles_you_re_not_interested_in_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["/profiles_you're_not_interested_in.json"])
    records = []
    for item in data:
        base_row = {}
        for entry in get_list(item, 'impressions_history_recs_hidden_authors'):
            row = base_row.copy()
            row['__source_list__'] = 'impressions_history_recs_hidden_authors'
            row['media_map_data'] = get_in(entry, 'media_map_data')
            row['href'] = get_in(entry, 'string_map_data', 'Time', 'href')
            row['timestamp'] = get_in(entry, 'string_map_data', 'Time', 'timestamp')
            row['value'] = get_in(entry, 'string_map_data', 'Time', 'value')
            row['href'] = get_in(entry, 'string_map_data', 'Username', 'href')
            row['timestamp'] = get_in(entry, 'string_map_data', 'Username', 'timestamp')
            row['value'] = get_in(entry, 'string_map_data', 'Username', 'value')
            row['title'] = get_in(entry, 'title')
            records.append(row)
    return pd.DataFrame(records)


def questions_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["/questions.json"])
    records = []
    for item in data:
        base_row = {}
        for entry in get_list(item, 'story_activities_questions'):
            row = base_row.copy()
            row['__source_list__'] = 'story_activities_questions'
            row['media_list_data'] = get_in(entry, 'media_list_data')
            row['href'] = get_in(entry, 'string_list_data', 'href')
            row['timestamp'] = get_in(entry, 'string_list_data', 'timestamp')
            row['value'] = get_in(entry, 'string_list_data', 'value')
            row['title'] = get_in(entry, 'title')
            records.append(row)
    return pd.DataFrame(records)


def quizzes_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["/quizzes.json"])
    records = []
    for item in data:
        base_row = {}
        for entry in get_list(item, 'story_activities_quizzes'):
            row = base_row.copy()
            row['__source_list__'] = 'story_activities_quizzes'
            row['timestamp'] = get_in(entry, 'string_list_data', 'timestamp')
            row['value'] = get_in(entry, 'string_list_data', 'value')
            row['title'] = get_in(entry, 'title')
            records.append(row)
    return pd.DataFrame(records)


def recent_follow_requests_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["/recent_follow_requests.json"])
    records = []
    for item in data:
        base_row = {}
        for entry in get_list(item, 'relationships_permanent_follow_requests'):
            row = base_row.copy()
            row['__source_list__'] = 'relationships_permanent_follow_requests'
            row['media_list_data'] = get_in(entry, 'media_list_data')
            row['href'] = get_in(entry, 'string_list_data', 'href')
            row['timestamp'] = get_in(entry, 'string_list_data', 'timestamp')
            row['value'] = get_in(entry, 'string_list_data', 'value')
            row['title'] = get_in(entry, 'title')
            records.append(row)
    return pd.DataFrame(records)


def recently_deleted_content_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["/recently_deleted_content.json"])
    records = []
    for item in data:
        base_row = {}
        for entry in get_list(item, 'ig_recently_deleted_media'):
            row = base_row.copy()
            row['__source_list__'] = 'ig_recently_deleted_media'
            row['media'] = get_in(entry, 'media')
            records.append(row)
    return pd.DataFrame(records)


def recently_unfollowed_profiles_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["/recently_unfollowed_profiles.json"])
    records = []
    for item in data:
        base_row = {}
        for entry in get_list(item, 'relationships_unfollowed_users'):
            row = base_row.copy()
            row['__source_list__'] = 'relationships_unfollowed_users'
            row['media_list_data'] = get_in(entry, 'media_list_data')
            row['href'] = get_in(entry, 'string_list_data', 'href')
            row['timestamp'] = get_in(entry, 'string_list_data', 'timestamp')
            row['value'] = get_in(entry, 'string_list_data', 'value')
            row['title'] = get_in(entry, 'title')
            records.append(row)
    return pd.DataFrame(records)


def recommended_topics_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["/recommended_topics.json"])
    records = []
    for item in data:
        base_row = {}
        for entry in get_list(item, 'topics_your_topics'):
            row = base_row.copy()
            row['__source_list__'] = 'topics_your_topics'
            row['media_map_data'] = get_in(entry, 'media_map_data')
            row['href'] = get_in(entry, 'string_map_data', 'Name', 'href')
            row['timestamp'] = get_in(entry, 'string_map_data', 'Name', 'timestamp')
            row['value'] = get_in(entry, 'string_map_data', 'Name', 'value')
            row['title'] = get_in(entry, 'title')
            records.append(row)
    return pd.DataFrame(records)


def reels_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["/reels.json"])
    records = []
    for item in data:
        base_row = {}
        for entry in get_list(item, 'ig_reels_media'):
            row = base_row.copy()
            row['__source_list__'] = 'ig_reels_media'
            row['creation_timestamp'] = get_in(entry, 'media', 'creation_timestamp')
            row['source_app'] = get_in(entry, 'media', 'cross_post_source', 'source_app')
            row['dubbing_info'] = get_in(entry, 'media', 'dubbing_info')
            row['has_camera_metadata'] = get_in(entry, 'media', 'media_metadata', 'camera_metadata', 'has_camera_metadata')
            row['camera_position'] = get_in(entry, 'media', 'media_metadata', 'video_metadata', 'exif_data', 'camera_position')
            row['device_id'] = get_in(entry, 'media', 'media_metadata', 'video_metadata', 'exif_data', 'device_id')
            row['source_type'] = get_in(entry, 'media', 'media_metadata', 'video_metadata', 'exif_data', 'source_type')
            row['music_genre'] = get_in(entry, 'media', 'media_metadata', 'video_metadata', 'music_genre')
            row['media_variants'] = get_in(entry, 'media', 'media_variants')
            row['title'] = get_in(entry, 'media', 'title')
            row['uri'] = get_in(entry, 'media', 'uri')
            records.append(row)
    return pd.DataFrame(records)


def reels_comments_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["/reels_comments.json"])
    records = []
    for item in data:
        base_row = {}
        for entry in get_list(item, 'comments_reels_comments'):
            row = base_row.copy()
            row['__source_list__'] = 'comments_reels_comments'
            row['value'] = get_in(entry, 'string_map_data', 'Comment', 'value')
            row['value'] = get_in(entry, 'string_map_data', 'Media Owner', 'value')
            row['timestamp'] = get_in(entry, 'string_map_data', 'Time', 'timestamp')
            records.append(row)
    return pd.DataFrame(records)


def removed_suggestions_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["/removed_suggestions.json"])
    records = []
    for item in data:
        base_row = {}
        for entry in get_list(item, 'relationships_dismissed_suggested_users'):
            row = base_row.copy()
            row['__source_list__'] = 'relationships_dismissed_suggested_users'
            row['media_list_data'] = get_in(entry, 'media_list_data')
            row['href'] = get_in(entry, 'string_list_data', 'href')
            row['timestamp'] = get_in(entry, 'string_list_data', 'timestamp')
            row['value'] = get_in(entry, 'string_list_data', 'value')
            row['title'] = get_in(entry, 'title')
            records.append(row)
    return pd.DataFrame(records)


def saved_collections_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["/saved_collections.json"])
    records = []
    for item in data:
        base_row = {}
        for entry in get_list(item, 'saved_saved_collections'):
            row = base_row.copy()
            row['__source_list__'] = 'saved_saved_collections'
            row['timestamp'] = get_in(entry, 'string_map_data', 'Creation Time', 'timestamp')
            row['value'] = get_in(entry, 'string_map_data', 'Name', 'value')
            row['timestamp'] = get_in(entry, 'string_map_data', 'Update Time', 'timestamp')
            row['title'] = get_in(entry, 'title')
            records.append(row)
    return pd.DataFrame(records)


def saved_posts_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["/saved_posts.json"])
    records = []
    for item in data:
        base_row = {}
        for entry in get_list(item, 'saved_saved_media'):
            row = base_row.copy()
            row['__source_list__'] = 'saved_saved_media'
            row['href'] = get_in(entry, 'string_map_data', 'Saved on', 'href')
            row['timestamp'] = get_in(entry, 'string_map_data', 'Saved on', 'timestamp')
            row['title'] = get_in(entry, 'title')
            records.append(row)
    return pd.DataFrame(records)


def secret_conversations_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["/secret_conversations.json"])
    records = []
    for item in data:
        base_row = {}
        base_row['calls'] = get_in(item, 'ig_secret_conversations', 'calls')
        for entry in get_list(item, 'ig_secret_conversations', 'armadillo_devices'):
            row = base_row.copy()
            row['__source_list__'] = 'armadillo_devices'
            row['device_manufacturer'] = get_in(entry, 'device_manufacturer')
            row['device_model'] = get_in(entry, 'device_model')
            row['device_os_version'] = get_in(entry, 'device_os_version')
            row['device_type'] = get_in(entry, 'device_type')
            row['last_active_time'] = get_in(entry, 'last_active_time')
            row['last_connected_ip'] = get_in(entry, 'last_connected_ip')
            row['online_since'] = get_in(entry, 'online_since')
            records.append(row)
    return pd.DataFrame(records)


def show_exclusive_story_promo_setting_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["/show_exclusive_story_promo_setting.json"])
    records = []
    for item in data:
        base_row = {}
        for entry in get_list(item, 'subscriptions_show_story_teaser_setting'):
            row = base_row.copy()
            row['__source_list__'] = 'subscriptions_show_story_teaser_setting'
            row['media_map_data'] = get_in(entry, 'media_map_data')
            row['href'] = get_in(entry, 'string_map_data', 'Exclusive Story Promo Setting', 'href')
            row['timestamp'] = get_in(entry, 'string_map_data', 'Exclusive Story Promo Setting', 'timestamp')
            row['value'] = get_in(entry, 'string_map_data', 'Exclusive Story Promo Setting', 'value')
            row['title'] = get_in(entry, 'title')
            records.append(row)
    return pd.DataFrame(records)


def signup_details_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["/signup_details.json"])
    records = []
    for item in data:
        base_row = {}
        for entry in get_list(item, 'account_history_registration_info'):
            row = base_row.copy()
            row['__source_list__'] = 'account_history_registration_info'
            row['media_map_data'] = get_in(entry, 'media_map_data')
            row['href'] = get_in(entry, 'string_map_data', 'Device', 'href')
            row['timestamp'] = get_in(entry, 'string_map_data', 'Device', 'timestamp')
            row['value'] = get_in(entry, 'string_map_data', 'Device', 'value')
            row['href'] = get_in(entry, 'string_map_data', 'Email', 'href')
            row['timestamp'] = get_in(entry, 'string_map_data', 'Email', 'timestamp')
            row['value'] = get_in(entry, 'string_map_data', 'Email', 'value')
            row['href'] = get_in(entry, 'string_map_data', 'IP Address', 'href')
            row['timestamp'] = get_in(entry, 'string_map_data', 'IP Address', 'timestamp')
            row['value'] = get_in(entry, 'string_map_data', 'IP Address', 'value')
            row['href'] = get_in(entry, 'string_map_data', 'Phone Number', 'href')
            row['timestamp'] = get_in(entry, 'string_map_data', 'Phone Number', 'timestamp')
            row['value'] = get_in(entry, 'string_map_data', 'Phone Number', 'value')
            row['href'] = get_in(entry, 'string_map_data', 'Time', 'href')
            row['timestamp'] = get_in(entry, 'string_map_data', 'Time', 'timestamp')
            row['value'] = get_in(entry, 'string_map_data', 'Time', 'value')
            row['href'] = get_in(entry, 'string_map_data', 'Username', 'href')
            row['timestamp'] = get_in(entry, 'string_map_data', 'Username', 'timestamp')
            row['value'] = get_in(entry, 'string_map_data', 'Username', 'value')
            row['title'] = get_in(entry, 'title')
            records.append(row)
    return pd.DataFrame(records)


def stories_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["/stories.json"])
    records = []
    for item in data:
        base_row = {}
        for entry in get_list(item, 'ig_stories'):
            row = base_row.copy()
            row['__source_list__'] = 'ig_stories'
            row['backup_uri'] = get_in(entry, 'backup_uri')
            row['creation_timestamp'] = get_in(entry, 'creation_timestamp')
            row['source_app'] = get_in(entry, 'cross_post_source', 'source_app')
            row['dubbing_info'] = get_in(entry, 'dubbing_info')
            row['has_camera_metadata'] = get_in(entry, 'media_metadata', 'camera_metadata', 'has_camera_metadata')
            row['aperture'] = get_in(entry, 'media_metadata', 'video_metadata', 'exif_data', 'aperture')
            row['camera_position'] = get_in(entry, 'media_metadata', 'video_metadata', 'exif_data', 'camera_position')
            row['date_time_digitized'] = get_in(entry, 'media_metadata', 'video_metadata', 'exif_data', 'date_time_digitized')
            row['date_time_original'] = get_in(entry, 'media_metadata', 'video_metadata', 'exif_data', 'date_time_original')
            row['device_id'] = get_in(entry, 'media_metadata', 'video_metadata', 'exif_data', 'device_id')
            row['focal_length'] = get_in(entry, 'media_metadata', 'video_metadata', 'exif_data', 'focal_length')
            row['iso'] = get_in(entry, 'media_metadata', 'video_metadata', 'exif_data', 'iso')
            row['lens_make'] = get_in(entry, 'media_metadata', 'video_metadata', 'exif_data', 'lens_make')
            row['lens_model'] = get_in(entry, 'media_metadata', 'video_metadata', 'exif_data', 'lens_model')
            row['metering_mode'] = get_in(entry, 'media_metadata', 'video_metadata', 'exif_data', 'metering_mode')
            row['scene_type'] = get_in(entry, 'media_metadata', 'video_metadata', 'exif_data', 'scene_type')
            row['shutter_speed'] = get_in(entry, 'media_metadata', 'video_metadata', 'exif_data', 'shutter_speed')
            row['software'] = get_in(entry, 'media_metadata', 'video_metadata', 'exif_data', 'software')
            row['source_type'] = get_in(entry, 'media_metadata', 'video_metadata', 'exif_data', 'source_type')
            row['music_genre'] = get_in(entry, 'media_metadata', 'video_metadata', 'music_genre')
            row['media_variants'] = get_in(entry, 'media_variants')
            row['title'] = get_in(entry, 'title')
            row['uri'] = get_in(entry, 'uri')
            records.append(row)
    return pd.DataFrame(records)


def story_likes_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["/story_likes.json"])
    records = []
    for item in data:
        base_row = {}
        for entry in get_list(item, 'story_activities_story_likes'):
            row = base_row.copy()
            row['__source_list__'] = 'story_activities_story_likes'
            row['timestamp'] = get_in(entry, 'string_list_data', 'timestamp')
            row['title'] = get_in(entry, 'title')
            records.append(row)
    return pd.DataFrame(records)


def subscription_for_no_ads_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["/subscription_for_no_ads.json"])
    records = []
    for item in data:
        base_row = {}
        base_row['media'] = get_in(item, 'media')
        base_row['fbid'] = get_in(item, 'fbid')
        for entry in get_list(item, 'label_values'):
            row = base_row.copy()
            row['__source_list__'] = 'label_values'
            row['label'] = get_in(entry, 'label')
            row['value'] = get_in(entry, 'value')
            records.append(row)
    return pd.DataFrame(records)


def suggested_profiles_viewed_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["/suggested_profiles_viewed.json"])
    records = []
    for item in data:
        base_row = {}
        for entry in get_list(item, 'impressions_history_chaining_seen'):
            row = base_row.copy()
            row['__source_list__'] = 'impressions_history_chaining_seen'
            row['timestamp'] = get_in(entry, 'string_map_data', 'Time', 'timestamp')
            row['value'] = get_in(entry, 'string_map_data', 'Username', 'value')
            records.append(row)
    return pd.DataFrame(records)


def synced_contacts_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["/synced_contacts.json"])
    records = []
    for item in data:
        base_row = {}
        for entry in get_list(item, 'contacts_contact_info'):
            row = base_row.copy()
            row['__source_list__'] = 'contacts_contact_info'
            row['media_map_data'] = get_in(entry, 'media_map_data')
            row['href'] = get_in(entry, 'string_map_data', 'Contact Information', 'href')
            row['timestamp'] = get_in(entry, 'string_map_data', 'Contact Information', 'timestamp')
            row['value'] = get_in(entry, 'string_map_data', 'Contact Information', 'value')
            row['href'] = get_in(entry, 'string_map_data', 'First Name', 'href')
            row['timestamp'] = get_in(entry, 'string_map_data', 'First Name', 'timestamp')
            row['value'] = get_in(entry, 'string_map_data', 'First Name', 'value')
            row['href'] = get_in(entry, 'string_map_data', 'Imported Time', 'href')
            row['timestamp'] = get_in(entry, 'string_map_data', 'Imported Time', 'timestamp')
            row['value'] = get_in(entry, 'string_map_data', 'Imported Time', 'value')
            row['href'] = get_in(entry, 'string_map_data', 'Last Name', 'href')
            row['timestamp'] = get_in(entry, 'string_map_data', 'Last Name', 'timestamp')
            row['value'] = get_in(entry, 'string_map_data', 'Last Name', 'value')
            row['title'] = get_in(entry, 'title')
            records.append(row)
    return pd.DataFrame(records)


def time_spent_on_instagram_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["/time_spent_on_instagram.json"])
    records = []
    for item in data:
        base_row = {}
        base_row['timestamp'] = get_in(item, 'timestamp')
        base_row['media'] = get_in(item, 'media')
        base_row['fbid'] = get_in(item, 'fbid')
        for entry in get_list(item, 'label_values'):
            row = base_row.copy()
            row['__source_list__'] = 'label_values'
            row['label'] = get_in(entry, 'label')
            row['label'] = get_in(entry, 'vec', 'label')
            row['timestamp_value'] = get_in(entry, 'vec', 'timestamp_value')
            records.append(row)
    return pd.DataFrame(records)


def use_cross_app_messaging_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["/use_cross-app_messaging.json"])
    records = []
    for item in data:
        base_row = {}
        for entry in get_list(item, 'settings_upgraded_to_cross_app_messaging'):
            row = base_row.copy()
            row['__source_list__'] = 'settings_upgraded_to_cross_app_messaging'
            row['media_map_data'] = get_in(entry, 'media_map_data')
            row['href'] = get_in(entry, 'string_map_data', 'Time Upgraded', 'href')
            row['timestamp'] = get_in(entry, 'string_map_data', 'Time Upgraded', 'timestamp')
            row['value'] = get_in(entry, 'string_map_data', 'Time Upgraded', 'value')
            row['href'] = get_in(entry, 'string_map_data', 'Upgraded To Cross-App Messaging', 'href')
            row['timestamp'] = get_in(entry, 'string_map_data', 'Upgraded To Cross-App Messaging', 'timestamp')
            row['value'] = get_in(entry, 'string_map_data', 'Upgraded To Cross-App Messaging', 'value')
            row['title'] = get_in(entry, 'title')
            records.append(row)
    return pd.DataFrame(records)


def videos_watched_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["/videos_watched.json"])
    records = []
    for item in data:
        base_row = {}
        for entry in get_list(item, 'impressions_history_videos_watched'):
            row = base_row.copy()
            row['__source_list__'] = 'impressions_history_videos_watched'
            row['value'] = get_in(entry, 'string_map_data', 'Author', 'value')
            row['timestamp'] = get_in(entry, 'string_map_data', 'Time', 'timestamp')
            records.append(row)
    return pd.DataFrame(records)


def word_or_phrase_searches_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["/word_or_phrase_searches.json"])
    records = []
    for item in data:
        base_row = {}
        for entry in get_list(item, 'searches_keyword'):
            row = base_row.copy()
            row['__source_list__'] = 'searches_keyword'
            row['media_map_data'] = get_in(entry, 'media_map_data')
            row['href'] = get_in(entry, 'string_map_data', 'Search', 'href')
            row['timestamp'] = get_in(entry, 'string_map_data', 'Search', 'timestamp')
            row['value'] = get_in(entry, 'string_map_data', 'Search', 'value')
            row['href'] = get_in(entry, 'string_map_data', 'Time', 'href')
            row['timestamp'] = get_in(entry, 'string_map_data', 'Time', 'timestamp')
            row['value'] = get_in(entry, 'string_map_data', 'Time', 'value')
            row['title'] = get_in(entry, 'title')
            records.append(row)
    return pd.DataFrame(records)


def your_activity_off_meta_technologies_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["/your_activity_off_meta_technologies.json"])
    records = []
    for item in data:
        base_row = {}
        for entry in get_list(item, 'apps_and_websites_off_meta_activity'):
            row = base_row.copy()
            row['__source_list__'] = 'apps_and_websites_off_meta_activity'
            row['id'] = get_in(entry, 'events', 'id')
            row['timestamp'] = get_in(entry, 'events', 'timestamp')
            row['type'] = get_in(entry, 'events', 'type')
            row['name'] = get_in(entry, 'name')
            records.append(row)
    return pd.DataFrame(records)


def your_activity_off_meta_technologies_settings_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["/your_activity_off_meta_technologies_settings.json"])
    records = []
    for item in data:
        base_row = {}
        base_row['timestamp'] = get_in(item, 'timestamp')
        base_row['fbid'] = get_in(item, 'fbid')
        base_row['ent_name'] = get_in(item, 'ent_name')
        base_row['media'] = get_in(item, 'media')
        for entry in get_list(item, 'label_values'):
            row = base_row.copy()
            row['__source_list__'] = 'label_values'
            row['ent_field_name'] = get_in(entry, 'ent_field_name')
            row['label'] = get_in(entry, 'label')
            row['value'] = get_in(entry, 'value')
            records.append(row)
    return pd.DataFrame(records)


def your_information_download_requests_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["/your_information_download_requests.json"])
    records = []
    for item in data:
        base_row = {}
        base_row['timestamp'] = get_in(item, 'timestamp')
        base_row['fbid'] = get_in(item, 'fbid')
        base_row['ent_name'] = get_in(item, 'ent_name')
        base_row['media'] = get_in(item, 'media')
        for entry in get_list(item, 'label_values'):
            row = base_row.copy()
            row['__source_list__'] = 'label_values'
            row['ent_field_name'] = get_in(entry, 'ent_field_name')
            row['label'] = get_in(entry, 'label')
            row['timestamp_value'] = get_in(entry, 'timestamp_value')
            records.append(row)
    return pd.DataFrame(records)


def your_muted_story_teaser_creators_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["/your_muted_story_teaser_creators.json"])
    records = []
    for item in data:
        base_row = {}
        for entry in get_list(item, 'subscriptions_muted_story_teaser_creators'):
            row = base_row.copy()
            row['__source_list__'] = 'subscriptions_muted_story_teaser_creators'
            row['media_map_data'] = get_in(entry, 'media_map_data')
            row['href'] = get_in(entry, 'string_map_data', 'Muted Creators', 'href')
            row['timestamp'] = get_in(entry, 'string_map_data', 'Muted Creators', 'timestamp')
            row['value'] = get_in(entry, 'string_map_data', 'Muted Creators', 'value')
            row['title'] = get_in(entry, 'title')
            records.append(row)
    return pd.DataFrame(records)


def your_topics_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["/your_topics.json"])
    records = []
    for item in data:
        base_row = {}
        for entry in get_list(item, 'topics_your_topics'):
            row = base_row.copy()
            row['__source_list__'] = 'topics_your_topics'
            row['media_map_data'] = get_in(entry, 'media_map_data')
            row['href'] = get_in(entry, 'string_map_data', 'Name', 'href')
            row['timestamp'] = get_in(entry, 'string_map_data', 'Name', 'timestamp')
            row['value'] = get_in(entry, 'string_map_data', 'Name', 'value')
            row['title'] = get_in(entry, 'title')
            records.append(row)
    return pd.DataFrame(records)


def create_donation_flow(file_input: list[str]):
    """Create a donation flow for Instagram data."""
    tables = []

    try:
        df = ads_about_meta_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='ads_about_meta', df=df, title={'en': 'ads_about_meta'})
            )
    except Exception as e:
        logger.error(f'Skipping ads_about_meta_df: {e}')

    try:
        df = ads_clicked_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='ads_clicked', df=df, title={'en': 'ads_clicked'})
            )
    except Exception as e:
        logger.error(f'Skipping ads_clicked_df: {e}')

    try:
        df = ads_viewed_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='ads_viewed', df=df, title={'en': 'ads_viewed'})
            )
    except Exception as e:
        logger.error(f'Skipping ads_viewed_df: {e}')

    try:
        df = advertisers_using_your_activity_or_information_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='advertisers_using_your_activity_or_information', df=df, title={'en': 'advertisers_using_your_activity_or_information'})
            )
    except Exception as e:
        logger.error(f'Skipping advertisers_using_your_activity_or_information_df: {e}')

    try:
        df = autofill_information_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='autofill_information', df=df, title={'en': 'autofill_information'})
            )
    except Exception as e:
        logger.error(f'Skipping autofill_information_df: {e}')

    try:
        df = avatar_items_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='avatar_items', df=df, title={'en': 'avatar_items'})
            )
    except Exception as e:
        logger.error(f'Skipping avatar_items_df: {e}')

    try:
        df = blocked_profiles_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='blocked_profiles', df=df, title={'en': 'blocked_profiles'})
            )
    except Exception as e:
        logger.error(f'Skipping blocked_profiles_df: {e}')

    try:
        df = camera_information_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='camera_information', df=df, title={'en': 'camera_information'})
            )
    except Exception as e:
        logger.error(f'Skipping camera_information_df: {e}')

    try:
        df = close_friends_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='close_friends', df=df, title={'en': 'close_friends'})
            )
    except Exception as e:
        logger.error(f'Skipping close_friends_df: {e}')

    try:
        df = comments_allowed_from_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='comments_allowed_from', df=df, title={'en': 'comments_allowed_from'})
            )
    except Exception as e:
        logger.error(f'Skipping comments_allowed_from_df: {e}')

    try:
        df = consents_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='consents', df=df, title={'en': 'consents'})
            )
    except Exception as e:
        logger.error(f'Skipping consents_df: {e}')

    try:
        df = devices_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='devices', df=df, title={'en': 'devices'})
            )
    except Exception as e:
        logger.error(f'Skipping devices_df: {e}')

    try:
        df = eligibility_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='eligibility', df=df, title={'en': 'eligibility'})
            )
    except Exception as e:
        logger.error(f'Skipping eligibility_df: {e}')

    try:
        df = emoji_sliders_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='emoji_sliders', df=df, title={'en': 'emoji_sliders'})
            )
    except Exception as e:
        logger.error(f'Skipping emoji_sliders_df: {e}')

    try:
        df = follow_requests_you_ve_received_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='follow_requests_you_ve_received', df=df, title={'en': 'follow_requests_you_ve_received'})
            )
    except Exception as e:
        logger.error(f'Skipping follow_requests_you_ve_received_df: {e}')

    try:
        df = followers_1_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='followers_1', df=df, title={'en': 'followers_1'})
            )
    except Exception as e:
        logger.error(f'Skipping followers_1_df: {e}')

    try:
        df = following_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='following', df=df, title={'en': 'following'})
            )
    except Exception as e:
        logger.error(f'Skipping following_df: {e}')

    try:
        df = following_hashtags_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='following_hashtags', df=df, title={'en': 'following_hashtags'})
            )
    except Exception as e:
        logger.error(f'Skipping following_hashtags_df: {e}')

    try:
        df = in_app_browser_autofill_settings_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='in_app_browser_autofill_settings', df=df, title={'en': 'in_app_browser_autofill_settings'})
            )
    except Exception as e:
        logger.error(f'Skipping in_app_browser_autofill_settings_df: {e}')

    try:
        df = information_you_ve_submitted_to_advertisers_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='information_you_ve_submitted_to_advertisers', df=df, title={'en': 'information_you_ve_submitted_to_advertisers'})
            )
    except Exception as e:
        logger.error(f'Skipping information_you_ve_submitted_to_advertisers_df: {e}')

    try:
        df = instagram_profile_information_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='instagram_profile_information', df=df, title={'en': 'instagram_profile_information'})
            )
    except Exception as e:
        logger.error(f'Skipping instagram_profile_information_df: {e}')

    try:
        df = instagram_signup_details_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='instagram_signup_details', df=df, title={'en': 'instagram_signup_details'})
            )
    except Exception as e:
        logger.error(f'Skipping instagram_signup_details_df: {e}')

    try:
        df = last_known_location_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='last_known_location', df=df, title={'en': 'last_known_location'})
            )
    except Exception as e:
        logger.error(f'Skipping last_known_location_df: {e}')

    try:
        df = liked_comments_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='liked_comments', df=df, title={'en': 'liked_comments'})
            )
    except Exception as e:
        logger.error(f'Skipping liked_comments_df: {e}')

    try:
        df = liked_posts_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='liked_posts', df=df, title={'en': 'liked_posts'})
            )
    except Exception as e:
        logger.error(f'Skipping liked_posts_df: {e}')

    try:
        df = linked_meta_accounts_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='linked_meta_accounts', df=df, title={'en': 'linked_meta_accounts'})
            )
    except Exception as e:
        logger.error(f'Skipping linked_meta_accounts_df: {e}')

    try:
        df = locations_of_interest_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='locations_of_interest', df=df, title={'en': 'locations_of_interest'})
            )
    except Exception as e:
        logger.error(f'Skipping locations_of_interest_df: {e}')

    try:
        df = login_activity_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='login_activity', df=df, title={'en': 'login_activity'})
            )
    except Exception as e:
        logger.error(f'Skipping login_activity_df: {e}')

    try:
        df = message_1_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='message_1', df=df, title={'en': 'message_1'})
            )
    except Exception as e:
        logger.error(f'Skipping message_1_df: {e}')

    try:
        df = note_interactions_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='note_interactions', df=df, title={'en': 'note_interactions'})
            )
    except Exception as e:
        logger.error(f'Skipping note_interactions_df: {e}')

    try:
        df = notification_of_privacy_policy_updates_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='notification_of_privacy_policy_updates', df=df, title={'en': 'notification_of_privacy_policy_updates'})
            )
    except Exception as e:
        logger.error(f'Skipping notification_of_privacy_policy_updates_df: {e}')

    try:
        df = notification_preferences_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='notification_preferences', df=df, title={'en': 'notification_preferences'})
            )
    except Exception as e:
        logger.error(f'Skipping notification_preferences_df: {e}')

    try:
        df = other_categories_used_to_reach_you_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='other_categories_used_to_reach_you', df=df, title={'en': 'other_categories_used_to_reach_you'})
            )
    except Exception as e:
        logger.error(f'Skipping other_categories_used_to_reach_you_df: {e}')

    try:
        df = password_change_activity_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='password_change_activity', df=df, title={'en': 'password_change_activity'})
            )
    except Exception as e:
        logger.error(f'Skipping password_change_activity_df: {e}')

    try:
        df = pending_follow_requests_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='pending_follow_requests', df=df, title={'en': 'pending_follow_requests'})
            )
    except Exception as e:
        logger.error(f'Skipping pending_follow_requests_df: {e}')

    try:
        df = personal_information_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='personal_information', df=df, title={'en': 'personal_information'})
            )
    except Exception as e:
        logger.error(f'Skipping personal_information_df: {e}')

    try:
        df = polls_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='polls', df=df, title={'en': 'polls'})
            )
    except Exception as e:
        logger.error(f'Skipping polls_df: {e}')

    try:
        df = possible_emails_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='possible_emails', df=df, title={'en': 'possible_emails'})
            )
    except Exception as e:
        logger.error(f'Skipping possible_emails_df: {e}')

    try:
        df = post_comments_1_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='post_comments_1', df=df, title={'en': 'post_comments_1'})
            )
    except Exception as e:
        logger.error(f'Skipping post_comments_1_df: {e}')

    try:
        df = posts_1_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='posts_1', df=df, title={'en': 'posts_1'})
            )
    except Exception as e:
        logger.error(f'Skipping posts_1_df: {e}')

    try:
        df = posts_viewed_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='posts_viewed', df=df, title={'en': 'posts_viewed'})
            )
    except Exception as e:
        logger.error(f'Skipping posts_viewed_df: {e}')

    try:
        df = posts_you_re_not_interested_in_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='posts_you_re_not_interested_in', df=df, title={'en': 'posts_you_re_not_interested_in'})
            )
    except Exception as e:
        logger.error(f'Skipping posts_you_re_not_interested_in_df: {e}')

    try:
        df = professional_information_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='professional_information', df=df, title={'en': 'professional_information'})
            )
    except Exception as e:
        logger.error(f'Skipping professional_information_df: {e}')

    try:
        df = profile_based_in_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='profile_based_in', df=df, title={'en': 'profile_based_in'})
            )
    except Exception as e:
        logger.error(f'Skipping profile_based_in_df: {e}')

    try:
        df = profile_changes_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='profile_changes', df=df, title={'en': 'profile_changes'})
            )
    except Exception as e:
        logger.error(f'Skipping profile_changes_df: {e}')

    try:
        df = profile_photos_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='profile_photos', df=df, title={'en': 'profile_photos'})
            )
    except Exception as e:
        logger.error(f'Skipping profile_photos_df: {e}')

    try:
        df = profile_privacy_changes_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='profile_privacy_changes', df=df, title={'en': 'profile_privacy_changes'})
            )
    except Exception as e:
        logger.error(f'Skipping profile_privacy_changes_df: {e}')

    try:
        df = profile_searches_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='profile_searches', df=df, title={'en': 'profile_searches'})
            )
    except Exception as e:
        logger.error(f'Skipping profile_searches_df: {e}')

    try:
        df = profile_status_changes_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='profile_status_changes', df=df, title={'en': 'profile_status_changes'})
            )
    except Exception as e:
        logger.error(f'Skipping profile_status_changes_df: {e}')

    try:
        df = profiles_you_re_not_interested_in_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='profiles_you_re_not_interested_in', df=df, title={'en': 'profiles_you_re_not_interested_in'})
            )
    except Exception as e:
        logger.error(f'Skipping profiles_you_re_not_interested_in_df: {e}')

    try:
        df = questions_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='questions', df=df, title={'en': 'questions'})
            )
    except Exception as e:
        logger.error(f'Skipping questions_df: {e}')

    try:
        df = quizzes_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='quizzes', df=df, title={'en': 'quizzes'})
            )
    except Exception as e:
        logger.error(f'Skipping quizzes_df: {e}')

    try:
        df = recent_follow_requests_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='recent_follow_requests', df=df, title={'en': 'recent_follow_requests'})
            )
    except Exception as e:
        logger.error(f'Skipping recent_follow_requests_df: {e}')

    try:
        df = recently_deleted_content_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='recently_deleted_content', df=df, title={'en': 'recently_deleted_content'})
            )
    except Exception as e:
        logger.error(f'Skipping recently_deleted_content_df: {e}')

    try:
        df = recently_unfollowed_profiles_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='recently_unfollowed_profiles', df=df, title={'en': 'recently_unfollowed_profiles'})
            )
    except Exception as e:
        logger.error(f'Skipping recently_unfollowed_profiles_df: {e}')

    try:
        df = recommended_topics_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='recommended_topics', df=df, title={'en': 'recommended_topics'})
            )
    except Exception as e:
        logger.error(f'Skipping recommended_topics_df: {e}')

    try:
        df = reels_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='reels', df=df, title={'en': 'reels'})
            )
    except Exception as e:
        logger.error(f'Skipping reels_df: {e}')

    try:
        df = reels_comments_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='reels_comments', df=df, title={'en': 'reels_comments'})
            )
    except Exception as e:
        logger.error(f'Skipping reels_comments_df: {e}')

    try:
        df = removed_suggestions_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='removed_suggestions', df=df, title={'en': 'removed_suggestions'})
            )
    except Exception as e:
        logger.error(f'Skipping removed_suggestions_df: {e}')

    try:
        df = saved_collections_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='saved_collections', df=df, title={'en': 'saved_collections'})
            )
    except Exception as e:
        logger.error(f'Skipping saved_collections_df: {e}')

    try:
        df = saved_posts_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='saved_posts', df=df, title={'en': 'saved_posts'})
            )
    except Exception as e:
        logger.error(f'Skipping saved_posts_df: {e}')

    try:
        df = secret_conversations_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='secret_conversations', df=df, title={'en': 'secret_conversations'})
            )
    except Exception as e:
        logger.error(f'Skipping secret_conversations_df: {e}')

    try:
        df = show_exclusive_story_promo_setting_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='show_exclusive_story_promo_setting', df=df, title={'en': 'show_exclusive_story_promo_setting'})
            )
    except Exception as e:
        logger.error(f'Skipping show_exclusive_story_promo_setting_df: {e}')

    try:
        df = signup_details_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='signup_details', df=df, title={'en': 'signup_details'})
            )
    except Exception as e:
        logger.error(f'Skipping signup_details_df: {e}')

    try:
        df = stories_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='stories', df=df, title={'en': 'stories'})
            )
    except Exception as e:
        logger.error(f'Skipping stories_df: {e}')

    try:
        df = story_likes_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='story_likes', df=df, title={'en': 'story_likes'})
            )
    except Exception as e:
        logger.error(f'Skipping story_likes_df: {e}')

    try:
        df = subscription_for_no_ads_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='subscription_for_no_ads', df=df, title={'en': 'subscription_for_no_ads'})
            )
    except Exception as e:
        logger.error(f'Skipping subscription_for_no_ads_df: {e}')

    try:
        df = suggested_profiles_viewed_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='suggested_profiles_viewed', df=df, title={'en': 'suggested_profiles_viewed'})
            )
    except Exception as e:
        logger.error(f'Skipping suggested_profiles_viewed_df: {e}')

    try:
        df = synced_contacts_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='synced_contacts', df=df, title={'en': 'synced_contacts'})
            )
    except Exception as e:
        logger.error(f'Skipping synced_contacts_df: {e}')

    try:
        df = time_spent_on_instagram_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='time_spent_on_instagram', df=df, title={'en': 'time_spent_on_instagram'})
            )
    except Exception as e:
        logger.error(f'Skipping time_spent_on_instagram_df: {e}')

    try:
        df = use_cross_app_messaging_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='use_cross_app_messaging', df=df, title={'en': 'use_cross_app_messaging'})
            )
    except Exception as e:
        logger.error(f'Skipping use_cross_app_messaging_df: {e}')

    try:
        df = videos_watched_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='videos_watched', df=df, title={'en': 'videos_watched'})
            )
    except Exception as e:
        logger.error(f'Skipping videos_watched_df: {e}')

    try:
        df = word_or_phrase_searches_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='word_or_phrase_searches', df=df, title={'en': 'word_or_phrase_searches'})
            )
    except Exception as e:
        logger.error(f'Skipping word_or_phrase_searches_df: {e}')

    try:
        df = your_activity_off_meta_technologies_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='your_activity_off_meta_technologies', df=df, title={'en': 'your_activity_off_meta_technologies'})
            )
    except Exception as e:
        logger.error(f'Skipping your_activity_off_meta_technologies_df: {e}')

    try:
        df = your_activity_off_meta_technologies_settings_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='your_activity_off_meta_technologies_settings', df=df, title={'en': 'your_activity_off_meta_technologies_settings'})
            )
    except Exception as e:
        logger.error(f'Skipping your_activity_off_meta_technologies_settings_df: {e}')

    try:
        df = your_information_download_requests_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='your_information_download_requests', df=df, title={'en': 'your_information_download_requests'})
            )
    except Exception as e:
        logger.error(f'Skipping your_information_download_requests_df: {e}')

    try:
        df = your_muted_story_teaser_creators_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='your_muted_story_teaser_creators', df=df, title={'en': 'your_muted_story_teaser_creators'})
            )
    except Exception as e:
        logger.error(f'Skipping your_muted_story_teaser_creators_df: {e}')

    try:
        df = your_topics_df(file_input)
        if not df.empty:
            tables.append(
                donation_table(name='your_topics', df=df, title={'en': 'your_topics'})
            )
    except Exception as e:
        logger.error(f'Skipping your_topics_df: {e}')

    if tables:
        return donation_flow(id='instagram', tables=tables)
    else:
        return None