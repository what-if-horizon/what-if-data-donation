# Auto-generated Instagram extractors

import pandas as pd
import logging
from port.helpers.donation_flow import donation_table, donation_flow
from port.helpers.readers import read_json
from port.helpers.parsers import parse_json

logger = logging.getLogger(__name__)

def _0_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/0.json"])

    df = parse_json(data,
        row_path=["$.name"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def _1_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/1.json"])

    df = parse_json(data,
        row_path=["$.name"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def _2_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/2.json"])

    df = parse_json(data,
        row_path=["$.name"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def _3_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/3.json"])

    df = parse_json(data,
        row_path=["$.name"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def _4_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/4.json"])

    df = parse_json(data,
        row_path=["$.name"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def _5_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/5.json"])

    df = parse_json(data,
        row_path=["$.name"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def _6_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/6.json"])

    df = parse_json(data,
        row_path=["$.name"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def _7_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/7.json"])

    df = parse_json(data,
        row_path=["$.name"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def _8_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/8.json"])

    df = parse_json(data,
        row_path=["$.name"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def account_activity_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/account_activity.json"])

    df = parse_json(data,
        row_path=["$.account_activity_v2"],
        col_paths=dict(
        action = ['action'],
        city = ['city'],
        country = ['country'],
        datr_cookie = ['datr_cookie'],
        ip_address = ['ip_address'],
        port = ['port'],
        region = ['region'],
        site_name = ['site_name'],
        timestamp = ['timestamp'],
        user_agent = ['user_agent'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def ad_preferences_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/ad_preferences.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def ads_about_meta_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/ads_about_meta.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def ads_clicked_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/ads_clicked.json"])

    df = parse_json(data,
        row_path=["$.impressions_history_ads_clicked"],
        col_paths=dict(
        timestamp = ['string_list_data.timestamp'],
        title = ['title'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def ads_interests_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/ads_interests.json"])

    df = parse_json(data,
        row_path=["$.topics_v2"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def ads_personalization_consent_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/ads_personalization_consent.json"])

    df = parse_json(data,
        row_path=["$.timestamp"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def ads_viewed_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/ads_viewed.json"])

    df = parse_json(data,
        row_path=["$.impressions_history_ads_seen"],
        col_paths=dict(
        value = ['string_map_data.Author.value'],
        timestamp = ['string_map_data.Time.timestamp'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def advertisers_using_your_activity_or_information_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/advertisers_using_your_activity_or_information.json"])

    df = parse_json(data,
        row_path=["$.ig_custom_audiences_all_types"],
        col_paths=dict(
        advertiser_name = ['advertiser_name'],
        has_data_file_custom_audience = ['has_data_file_custom_audience'],
        has_in_person_store_visit = ['has_in_person_store_visit'],
        has_remarketing_custom_audience = ['has_remarketing_custom_audience'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def autofill_information_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/autofill_information.json"])

    df = parse_json(data,
        row_path=["$.autofill_information_v2"],
        col_paths=dict(
        CITY = ['CITY'],
        address_level1 = ['address_level1'],
        address_level2 = ['address_level2'],
        address_level3 = ['address_level3'],
        address_level4 = ['address_level4'],
        address_line1 = ['address_line1'],
        address_line2 = ['address_line2'],
        address_line3 = ['address_line3'],
        country = ['country'],
        country_name = ['country_name'],
        email = ['email'],
        family_name = ['family_name'],
        given_name = ['given_name'],
        postal_code = ['postal_code'],
        street_address = ['street_address'],
        tel = ['tel'],
        tel_area_code = ['tel_area_code'],
        tel_country_code = ['tel_country_code'],
        tel_local = ['tel_local'],
        tel_local_prefix = ['tel_local_prefix'],
        tel_local_suffix = ['tel_local_suffix'],
        tel_national = ['tel_national'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def blocked_profiles_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/blocked_profiles.json"])

    df = parse_json(data,
        row_path=["$.relationships_blocked_users"],
        col_paths=dict(
        href = ['string_list_data.href'],
        timestamp = ['string_list_data.timestamp'],
        title = ['title'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def bookmark_and_app_settings_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/bookmark_and_app_settings.json"])

    df = parse_json(data,
        row_path=["$.timestamp"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def browser_cookies_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/browser_cookies.json"])

    df = parse_json(data,
        row_path=["$.datr_stats_v2"],
        col_paths=dict(
        _0Fo____________________ = ['-0Fo********************'],
        _3ZP____________________ = ['-3ZP********************'],
        _1k95____________________ = ['1k95********************'],
        _2kt5____________________ = ['2kt5********************'],
        _2qxu____________________ = ['2qxu********************'],
        _9Ws_____________________ = ['9Ws-********************'],
        _9vRp____________________ = ['9vRp********************'],
        BDiW____________________ = ['BDiW********************'],
        Fvbc____________________ = ['Fvbc********************'],
        IL4G____________________ = ['IL4G********************'],
        K38o____________________ = ['K38o********************'],
        NUJ5____________________ = ['NUJ5********************'],
        R5de____________________ = ['R5de********************'],
        Rr0R____________________ = ['Rr0R********************'],
        Vtdg____________________ = ['Vtdg********************'],
        Y0U8____________________ = ['Y0U8********************'],
        aZn9____________________ = ['aZn9********************'],
        hJ9e____________________ = ['hJ9e********************'],
        l6Fv____________________ = ['l6Fv********************'],
        lRsu____________________ = ['lRsu********************'],
        mf5e____________________ = ['mf5e********************'],
        q7f3____________________ = ['q7f3********************'],
        ufsK____________________ = ['ufsK********************'],
        vF55____________________ = ['vF55********************'],
        w6oG____________________ = ['w6oG********************'],
        wNaZ____________________ = ['wNaZ********************'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def browser_push_notifications_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/browser_push_notifications.json"])

    df = parse_json(data,
        row_path=["$.timestamp"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def camera_information_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/camera_information.json"])

    df = parse_json(data,
        row_path=["$.devices_camera"],
        col_paths=dict(
        media_map_data = ['media_map_data'],
        href = ['string_map_data.Supported SDK Versions.href'],
        timestamp = ['string_map_data.Supported SDK Versions.timestamp'],
        value = ['string_map_data.Supported SDK Versions.value'],
        title = ['title'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def check_ins_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/check-ins.json"])

    df = parse_json(data,
        row_path=["$.timestamp"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def cities_you_have_checked_into_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/cities_you_have_checked_into.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def close_friends_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/close_friends.json"])

    df = parse_json(data,
        row_path=["$.relationships_close_friends"],
        col_paths=dict(
        media_list_data = ['media_list_data'],
        href = ['string_list_data.href'],
        timestamp = ['string_list_data.timestamp'],
        value = ['string_list_data.value'],
        title = ['title'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def comments_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/comments.json"])

    df = parse_json(data,
        row_path=["$.comments_v2"],
        col_paths=dict(
        author = ['data.comment.author'],
        comment = ['data.comment.comment'],
        timestamp = ['timestamp'],
        title = ['title'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def comments_allowed_from_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/comments_allowed_from.json"])

    df = parse_json(data,
        row_path=["$.settings_allow_comments_from"],
        col_paths=dict(
        media_map_data = ['media_map_data'],
        href = ['string_map_data.Comments Allowed From.href'],
        timestamp = ['string_map_data.Comments Allowed From.timestamp'],
        value = ['string_map_data.Comments Allowed From.value'],
        title = ['title'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def connected_apps_and_websites_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/connected_apps_and_websites.json"])

    df = parse_json(data,
        row_path=["$.installed_apps_v2"],
        col_paths=dict(
        added_timestamp = ['added_timestamp'],
        category = ['category'],
        name = ['name'],
        removed_timestamp = ['removed_timestamp'],
        user_app_scoped_id = ['user_app_scoped_id'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def consent_for_combining_facebook_and_messenger_data_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/consent_for_combining_facebook_and_messenger_data.json"])

    df = parse_json(data,
        row_path=["$.timestamp"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def consents_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/consents.json"])

    df = parse_json(data,
        row_path=["$.timestamp"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def contacts_sync_settings_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/contacts_sync_settings.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def controls_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/controls.json"])

    df = parse_json(data,
        row_path=["$.controls"],
        col_paths=dict(
        description = ['description'],
        entries = ['entries'],
        name = ['name'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def conversations_you_had_as_a_buyer_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/conversations_you_had_as_a_buyer.json"])

    df = parse_json(data,
        row_path=["$.timestamp"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def detected_hardware_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/detected_hardware.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def device_location_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/device_location.json"])

    df = parse_json(data,
        row_path=["$.phone_number_location_v2"],
        col_paths=dict(
        country_code = ['country_code'],
        spn = ['spn'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def device_login_cookies_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/device_login_cookies.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def device_navigation_bar_information_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/device_navigation_bar_information.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def devices_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/devices.json"])

    df = parse_json(data,
        row_path=["$.devices_devices"],
        col_paths=dict(
        media_map_data = ['media_map_data'],
        href = ['string_map_data.User Agent.href'],
        timestamp = ['string_map_data.User Agent.timestamp'],
        value = ['string_map_data.User Agent.value'],
        title = ['title'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def eligibility_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/eligibility.json"])

    df = parse_json(data,
        row_path=["$.monetization_eligibility"],
        col_paths=dict(
        media_map_data = ['media_map_data'],
        href = ['string_map_data.Reason.href'],
        timestamp = ['string_map_data.Reason.timestamp'],
        value = ['string_map_data.Reason.value'],
        title = ['title'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def email_address_verifications_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/email_address_verifications.json"])

    df = parse_json(data,
        row_path=["$.contact_verifications_v2"],
        col_paths=dict(
        contact = ['contact'],
        contact_type = ['contact_type'],
        verification_time = ['verification_time'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def emails_we_sent_you_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/emails_we_sent_you.json"])

    df = parse_json(data,
        row_path=["$.title"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def emoji_sliders_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/emoji_sliders.json"])

    df = parse_json(data,
        row_path=["$.story_activities_emoji_sliders"],
        col_paths=dict(
        timestamp = ['string_list_data.timestamp'],
        value = ['string_list_data.value'],
        title = ['title'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def event_invitations_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/event_invitations.json"])

    df = parse_json(data,
        row_path=["$.events_invited_v2"],
        col_paths=dict(
        end_timestamp = ['end_timestamp'],
        name = ['name'],
        start_timestamp = ['start_timestamp'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def events_interactions_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/events_interactions.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def events_you_ve_hidden_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/events_you've_hidden.json"])

    df = parse_json(data,
        row_path=["$.events_hidden_v2"],
        col_paths=dict(
        data = ['data'],
        timestamp = ['timestamp'],
        title = ['title'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def facebook_lite_notification_settings_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/facebook_lite_notification_settings.json"])

    df = parse_json(data,
        row_path=["$.timestamp"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def facebook_new_user_guide_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/facebook_new_user_guide.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def facebook_reels_usage_information_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/facebook_reels_usage_information.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def feed_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/feed.json"])

    df = parse_json(data,
        row_path=["$.people_and_friends_v2"],
        col_paths=dict(
        description = ['description'],
        name = ['name'],
        uri = ['entries.data.uri'],
        timestamp = ['entries.timestamp'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def follow_requests_you_ve_received_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/follow_requests_you've_received.json"])

    df = parse_json(data,
        row_path=["$.relationships_follow_requests_received"],
        col_paths=dict(
        media_list_data = ['media_list_data'],
        href = ['string_list_data.href'],
        timestamp = ['string_list_data.timestamp'],
        value = ['string_list_data.value'],
        title = ['title'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def followers_1_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/followers_1.json"])

    df = parse_json(data,
        row_path=["$.title"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def following_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/following.json"])

    df = parse_json(data,
        row_path=["$.relationships_following"],
        col_paths=dict(
        media_list_data = ['media_list_data'],
        href = ['string_list_data.href'],
        timestamp = ['string_list_data.timestamp'],
        value = ['string_list_data.value'],
        title = ['title'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def following_hashtags_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/following_hashtags.json"])

    df = parse_json(data,
        row_path=["$.relationships_following_hashtags"],
        col_paths=dict(
        media_list_data = ['media_list_data'],
        href = ['string_list_data.href'],
        timestamp = ['string_list_data.timestamp'],
        value = ['string_list_data.value'],
        title = ['title'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def for_sale_group_preferences_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/for-sale_group_preferences.json"])

    df = parse_json(data,
        row_path=["$.timestamp"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def fundraiser_posts_you_likely_viewed_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/fundraiser_posts_you_likely_viewed.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def gaming_tab_notifications_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/gaming_tab_notifications.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def group_posts_and_comments_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/group_posts_and_comments.json"])

    df = parse_json(data,
        row_path=["$.group_posts_v2"],
        col_paths=dict(
        creation_timestamp = ['attachments.data.media.creation_timestamp'],
        description = ['attachments.data.media.description'],
        photo_metadata = ['attachments.data.media.media_metadata.photo_metadata'],
        uri = ['attachments.data.media.uri'],
        post = ['data.post'],
        timestamp = ['timestamp'],
        title = ['title'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def how_active_we_think_you_are_on_marketplace_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/how_active_we_think_you_are_on_marketplace.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def id_verification_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/id_verification.json"])

    df = parse_json(data,
        row_path=["$.timestamp"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def in_app_browser_autofill_settings_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/in-app_browser_autofill_settings.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def information_about_your_last_login_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/information_about_your_last_login.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def information_you_ve_submitted_to_advertisers_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/information_you've_submitted_to_advertisers.json"])

    df = parse_json(data,
        row_path=["$.ig_lead_gen_info"],
        col_paths=dict(
        label = ['label'],
        value = ['value'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def instagram_profile_information_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/instagram_profile_information.json"])

    df = parse_json(data,
        row_path=["$.profile_account_insights"],
        col_paths=dict(
        media_map_data = ['media_map_data'],
        href = ['string_map_data.Last Story Time.href'],
        timestamp = ['string_map_data.Last Story Time.timestamp'],
        value = ['string_map_data.Last Story Time.value'],
        title = ['title'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def instagram_signup_details_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/instagram_signup_details.json"])

    df = parse_json(data,
        row_path=["$.account_history_registration_info"],
        col_paths=dict(
        media_map_data = ['media_map_data'],
        href = ['string_map_data.Username.href'],
        timestamp = ['string_map_data.Username.timestamp'],
        value = ['string_map_data.Username.value'],
        title = ['title'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def ip_address_activity_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/ip_address_activity.json"])

    df = parse_json(data,
        row_path=["$.used_ip_address_v2"],
        col_paths=dict(
        action = ['action'],
        ip = ['ip'],
        timestamp = ['timestamp'],
        user_agent = ['user_agent'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def language_and_locale_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/language_and_locale.json"])

    df = parse_json(data,
        row_path=["$.language_and_locale_v2"],
        col_paths=dict(
        description = ['description'],
        value = ['children.entries.data.value'],
        name = ['name'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def language_settings_history_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/language_settings_history.json"])

    df = parse_json(data,
        row_path=["$.timestamp"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def last_known_location_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/last_known_location.json"])

    df = parse_json(data,
        row_path=["$.account_history_imprecise_last_known_location"],
        col_paths=dict(
        media_map_data = ['media_map_data'],
        href = ['string_map_data.Precise Longitude.href'],
        timestamp = ['string_map_data.Precise Longitude.timestamp'],
        value = ['string_map_data.Precise Longitude.value'],
        title = ['title'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def liked_comments_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/liked_comments.json"])

    df = parse_json(data,
        row_path=["$.likes_comment_likes"],
        col_paths=dict(
        href = ['string_list_data.href'],
        timestamp = ['string_list_data.timestamp'],
        value = ['string_list_data.value'],
        title = ['title'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def liked_posts_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/liked_posts.json"])

    df = parse_json(data,
        row_path=["$.likes_media_likes"],
        col_paths=dict(
        href = ['string_list_data.href'],
        timestamp = ['string_list_data.timestamp'],
        value = ['string_list_data.value'],
        title = ['title'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def likes_and_reactions_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/likes_and_reactions.json"])

    df = parse_json(data,
        row_path=["$.timestamp"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def likes_and_reactions_1_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/likes_and_reactions_1.json"])

    df = parse_json(data,
        row_path=["$.timestamp"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def linked_meta_accounts_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/linked_meta_accounts.json"])

    df = parse_json(data,
        row_path=["$.timestamp"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def locations_of_interest_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/locations_of_interest.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def login_activity_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/login_activity.json"])

    df = parse_json(data,
        row_path=["$.account_history_login_history"],
        col_paths=dict(
        media_map_data = ['media_map_data'],
        href = ['string_map_data.User Agent.href'],
        timestamp = ['string_map_data.User Agent.timestamp'],
        value = ['string_map_data.User Agent.value'],
        title = ['title'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def login_alerts_settings_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/login_alerts_settings.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def login_protection_data_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/login_protection_data.json"])

    df = parse_json(data,
        row_path=["$.login_protection_data_v2"],
        col_paths=dict(
        name = ['name'],
        created_timestamp = ['session.created_timestamp'],
        ip_address = ['session.ip_address'],
        updated_timestamp = ['session.updated_timestamp'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def logins_and_logouts_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/logins_and_logouts.json"])

    df = parse_json(data,
        row_path=["$.account_accesses_v2"],
        col_paths=dict(
        action = ['action'],
        ip_address = ['ip_address'],
        site = ['site'],
        timestamp = ['timestamp'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def message_1_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/message_1.json"])

    df = parse_json(data,
        row_path=["$.participants"],
        col_paths=dict(
        name = ['name'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def meta_privacy_policy_update_notifications_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/meta_privacy_policy_update_notifications.json"])

    df = parse_json(data,
        row_path=["$.timestamp"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def milestone_notifications_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/milestone_notifications.json"])

    df = parse_json(data,
        row_path=["$.timestamp"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def mobile_devices_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/mobile_devices.json"])

    df = parse_json(data,
        row_path=["$.devices_v2"],
        col_paths=dict(
        advertiser_id = ['advertiser_id'],
        device_locale = ['device_locale'],
        family_device_id = ['family_device_id'],
        os = ['os'],
        app_version = ['push_tokens.app_version'],
        client_update_time = ['push_tokens.client_update_time'],
        creation_time = ['push_tokens.creation_time'],
        device_id = ['push_tokens.device_id'],
        disabled = ['push_tokens.disabled'],
        locale = ['push_tokens.locale'],
        os_version = ['push_tokens.os_version'],
        token = ['push_tokens.token'],
        redact_tokens = ['redact_tokens'],
        type = ['type'],
        udid = ['udid'],
        update_time = ['update_time'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def navigation_bar_shortcut_history_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/navigation_bar_shortcut_history.json"])

    df = parse_json(data,
        row_path=["$.timestamp"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def note_interactions_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/note_interactions.json"])

    df = parse_json(data,
        row_path=["$.profile_note_interactions"],
        col_paths=dict(
        media_map_data = ['media_map_data'],
        href = ['string_map_data.Last Notes Seen Time.href'],
        timestamp = ['string_map_data.Last Notes Seen Time.timestamp'],
        value = ['string_map_data.Last Notes Seen Time.value'],
        title = ['title'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def notification_of_meta_privacy_policy_update_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/notification_of_meta_privacy_policy_update.json"])

    df = parse_json(data,
        row_path=["$.notification_meta_privacy_policy_update"],
        col_paths=dict(
        consent_state = ['consent_state'],
        impression_time = ['impression_time'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def notification_of_privacy_policy_updates_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/notification_of_privacy_policy_updates.json"])

    df = parse_json(data,
        row_path=["$.policy_updates_and_permissions_notification_of_privacy_policy_updates"],
        col_paths=dict(
        value = ['string_map_data.Impression Time.value'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def notification_preferences_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/notification_preferences.json"])

    df = parse_json(data,
        row_path=["$.settings_notification_preferences"],
        col_paths=dict(
        value = ['string_map_data.Value.value'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def notification_settings_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/notification_settings.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def notification_tab_display_information_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/notification_tab_display_information.json"])

    df = parse_json(data,
        row_path=["$.timestamp"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def notifications_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/notifications.json"])

    df = parse_json(data,
        row_path=["$.notifications_v2"],
        col_paths=dict(
        href = ['href'],
        text = ['text'],
        timestamp = ['timestamp'],
        unread = ['unread'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def notifications_about_new_users_joining_facebook_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/notifications_about_new_users_joining_facebook.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def other_categories_used_to_reach_you_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/other_categories_used_to_reach_you.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def pages_and_profiles_you_ve_recommended_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/pages_and_profiles_you've_recommended.json"])

    df = parse_json(data,
        row_path=["$.recommended_pages_v2"],
        col_paths=dict(
        name = ['name'],
        timestamp = ['timestamp'],
        url = ['url'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def pages_and_profiles_you_follow_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/pages_and_profiles_you_follow.json"])

    df = parse_json(data,
        row_path=["$.pages_followed_v2"],
        col_paths=dict(
        name = ['data.name'],
        timestamp = ['timestamp'],
        title = ['title'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def pages_you_ve_liked_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/pages_you've_liked.json"])

    df = parse_json(data,
        row_path=["$.page_likes_v2"],
        col_paths=dict(
        name = ['name'],
        timestamp = ['timestamp'],
        url = ['url'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def password_change_activity_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/password_change_activity.json"])

    df = parse_json(data,
        row_path=["$.account_history_password_change_history"],
        col_paths=dict(
        media_map_data = ['media_map_data'],
        href = ['string_map_data.Time.href'],
        timestamp = ['string_map_data.Time.timestamp'],
        value = ['string_map_data.Time.value'],
        title = ['title'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def payment_history_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/payment_history.json"])

    df = parse_json(data,
        row_path=["$.payments_v2"],
        col_paths=dict(
        payments = ['payments'],
        preferred_currency = ['preferred_currency'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def pending_follow_requests_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/pending_follow_requests.json"])

    df = parse_json(data,
        row_path=["$.relationships_follow_requests_sent"],
        col_paths=dict(
        media_list_data = ['media_list_data'],
        href = ['string_list_data.href'],
        timestamp = ['string_list_data.timestamp'],
        value = ['string_list_data.value'],
        title = ['title'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def people_and_friends_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/people_and_friends.json"])

    df = parse_json(data,
        row_path=["$.timestamp"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def people_you_may_know_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/people_you_may_know.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def permissions_you_have_granted_to_apps_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/permissions_you_have_granted_to_apps.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def personal_information_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/personal_information.json"])

    df = parse_json(data,
        row_path=["$.profile_user"],
        col_paths=dict(
        backup_uri = ['media_map_data.Profile Photo.backup_uri'],
        creation_timestamp = ['media_map_data.Profile Photo.creation_timestamp'],
        source_app = ['media_map_data.Profile Photo.cross_post_source.source_app'],
        has_camera_metadata = ['media_map_data.Profile Photo.media_metadata.camera_metadata.has_camera_metadata'],
        title = ['title'],
        uri = ['media_map_data.Profile Photo.uri'],
        href = ['string_map_data.Username.href'],
        timestamp = ['string_map_data.Username.timestamp'],
        value = ['string_map_data.Username.value'],
        media_map_data = ['media_map_data'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def places_you_have_been_tagged_in_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/places_you_have_been_tagged_in.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def pokes_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/pokes.json"])

    df = parse_json(data,
        row_path=["$.pokes_v2"],
        col_paths=dict(
        pokee = ['pokee'],
        poker = ['poker'],
        rank = ['rank'],
        timestamp = ['timestamp'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def polls_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/polls.json"])

    df = parse_json(data,
        row_path=["$.story_activities_polls"],
        col_paths=dict(
        timestamp = ['string_list_data.timestamp'],
        value = ['string_list_data.value'],
        title = ['title'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def polls_you_voted_on_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/polls_you_voted_on.json"])

    df = parse_json(data,
        row_path=["$.poll_votes_v2"],
        col_paths=dict(
        option = ['attachments.data.poll.options.option'],
        voted = ['attachments.data.poll.options.voted'],
        timestamp = ['timestamp'],
        title = ['title'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def possible_emails_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/possible_emails.json"])

    df = parse_json(data,
        row_path=["$.inferred_data_inferred_emails"],
        col_paths=dict(
        media_list_data = ['media_list_data'],
        href = ['string_list_data.href'],
        timestamp = ['string_list_data.timestamp'],
        value = ['string_list_data.value'],
        title = ['title'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def post_comments_1_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/post_comments_1.json"])

    df = parse_json(data,
        row_path=["$.media_list_data"],
        col_paths=dict(
        uri = ['uri'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def posts_1_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/posts_1.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
        creation_timestamp = ['creation_timestamp'],
        source_app = ['cross_post_source.source_app'],
        has_camera_metadata = ['media_metadata.camera_metadata.has_camera_metadata'],
        title = ['title'],
        uri = ['uri'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def posts_on_other_pages_and_profiles_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/posts_on_other_pages_and_profiles.json"])

    df = parse_json(data,
        row_path=["$.timestamp"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def posts_viewed_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/posts_viewed.json"])

    df = parse_json(data,
        row_path=["$.impressions_history_posts_seen"],
        col_paths=dict(
        value = ['string_map_data.Author.value'],
        timestamp = ['string_map_data.Time.timestamp'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def posts_you_re_not_interested_in_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/posts_you're_not_interested_in.json"])

    df = parse_json(data,
        row_path=["$.impressions_history_posts_not_interested"],
        col_paths=dict(
        href = ['string_list_data.href'],
        value = ['string_list_data.value'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def predicted_languages_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/predicted_languages.json"])

    df = parse_json(data,
        row_path=["$.timestamp"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def primary_location_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/primary_location.json"])

    df = parse_json(data,
        row_path=["$.primary_location_v2"],
        col_paths=dict(
        city_region_pairs = ['city_region_pairs'],
        zipcode = ['zipcode'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def primary_public_location_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/primary_public_location.json"])

    df = parse_json(data,
        row_path=["$.primary_public_location_v2"],
        col_paths=dict(
        city = ['city'],
        country = ['country'],
        region = ['region'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def privacy_settings_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/privacy_settings.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def professional_information_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/professional_information.json"])

    df = parse_json(data,
        row_path=["$.profile_business"],
        col_paths=dict(
        media_map_data = ['media_map_data'],
        string_map_data = ['string_map_data'],
        title = ['title'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def profile_based_in_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/profile_based_in.json"])

    df = parse_json(data,
        row_path=["$.inferred_data_primary_location"],
        col_paths=dict(
        media_map_data = ['media_map_data'],
        href = ['string_map_data.City Name.href'],
        timestamp = ['string_map_data.City Name.timestamp'],
        value = ['string_map_data.City Name.value'],
        title = ['title'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def profile_changes_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/profile_changes.json"])

    df = parse_json(data,
        row_path=["$.profile_profile_change"],
        col_paths=dict(
        media_map_data = ['media_map_data'],
        href = ['string_map_data.Previous Value.href'],
        timestamp = ['string_map_data.Previous Value.timestamp'],
        value = ['string_map_data.Previous Value.value'],
        title = ['title'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def profile_information_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/profile_information.json"])

    df = parse_json(data,
        row_path=["$.profile_v2"],
        col_paths=dict(
        day = ['birthday.day'],
        month = ['birthday.month'],
        year = ['birthday.year'],
        name = ['screen_names.names.name'],
        timestamp = ['screen_names.names.timestamp'],
        concentrations = ['education_experiences.concentrations'],
        description = ['education_experiences.description'],
        end_timestamp = ['education_experiences.end_timestamp'],
        graduated = ['education_experiences.graduated'],
        school_type = ['education_experiences.school_type'],
        start_timestamp = ['education_experiences.start_timestamp'],
        ad_account_emails = ['emails.ad_account_emails'],
        emails = ['emails.emails'],
        pending_emails = ['emails.pending_emails'],
        previous_emails = ['emails.previous_emails'],
        favorite_quotes = ['favorite_quotes'],
        gender_option = ['gender.gender_option'],
        pronoun = ['gender.pronoun'],
        first_name = ['name.first_name'],
        full_name = ['name.full_name'],
        last_name = ['name.last_name'],
        middle_name = ['name.middle_name'],
        other_names = ['other_names'],
        creation_time = ['phone_numbers.creation_time'],
        phone_number = ['phone_numbers.phone_number'],
        phone_type = ['phone_numbers.phone_type'],
        verified = ['phone_numbers.verified'],
        previous_names = ['previous_names'],
        profile_uri = ['profile_uri'],
        registration_timestamp = ['registration_timestamp'],
        status = ['relationship.status'],
        service_name = ['screen_names.service_name'],
        websites = ['websites'],
        work_experiences = ['work_experiences'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def profile_photos_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/profile_photos.json"])

    df = parse_json(data,
        row_path=["$.ig_profile_picture"],
        col_paths=dict(
        creation_timestamp = ['creation_timestamp'],
        source_app = ['cross_post_source.source_app'],
        has_camera_metadata = ['media_metadata.camera_metadata.has_camera_metadata'],
        title = ['title'],
        uri = ['uri'],
        backup_uri = ['backup_uri'],
        is_profile_picture = ['is_profile_picture'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def profile_privacy_changes_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/profile_privacy_changes.json"])

    df = parse_json(data,
        row_path=["$.account_history_account_privacy_history"],
        col_paths=dict(
        media_map_data = ['media_map_data'],
        href = ['string_map_data.Time.href'],
        timestamp = ['string_map_data.Time.timestamp'],
        value = ['string_map_data.Time.value'],
        title = ['title'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def profile_searches_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/profile_searches.json"])

    df = parse_json(data,
        row_path=["$.searches_user"],
        col_paths=dict(
        media_map_data = ['media_map_data'],
        href = ['string_map_data.Time.href'],
        timestamp = ['string_map_data.Time.timestamp'],
        value = ['string_map_data.Time.value'],
        title = ['title'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def profile_status_changes_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/profile_status_changes.json"])

    df = parse_json(data,
        row_path=["$.account_history_account_active_status_changes"],
        col_paths=dict(
        media_map_data = ['media_map_data'],
        href = ['string_map_data.Time.href'],
        timestamp = ['string_map_data.Time.timestamp'],
        value = ['string_map_data.Time.value'],
        title = ['title'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def profile_update_history_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/profile_update_history.json"])

    df = parse_json(data,
        row_path=["$.profile_updates_v2"],
        col_paths=dict(
        timestamp = ['timestamp'],
        title = ['title'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def profiles_you_re_not_interested_in_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/profiles_you're_not_interested_in.json"])

    df = parse_json(data,
        row_path=["$.impressions_history_recs_hidden_authors"],
        col_paths=dict(
        media_map_data = ['media_map_data'],
        href = ['string_map_data.Username.href'],
        timestamp = ['string_map_data.Username.timestamp'],
        value = ['string_map_data.Username.value'],
        title = ['title'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def questions_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/questions.json"])

    df = parse_json(data,
        row_path=["$.story_activities_questions"],
        col_paths=dict(
        media_list_data = ['media_list_data'],
        href = ['string_list_data.href'],
        timestamp = ['string_list_data.timestamp'],
        value = ['string_list_data.value'],
        title = ['title'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def quizzes_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/quizzes.json"])

    df = parse_json(data,
        row_path=["$.story_activities_quizzes"],
        col_paths=dict(
        timestamp = ['string_list_data.timestamp'],
        value = ['string_list_data.value'],
        title = ['title'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def recent_follow_requests_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/recent_follow_requests.json"])

    df = parse_json(data,
        row_path=["$.relationships_permanent_follow_requests"],
        col_paths=dict(
        media_list_data = ['media_list_data'],
        href = ['string_list_data.href'],
        timestamp = ['string_list_data.timestamp'],
        value = ['string_list_data.value'],
        title = ['title'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def recently_deleted_content_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/recently_deleted_content.json"])

    df = parse_json(data,
        row_path=["$.ig_recently_deleted_media"],
        col_paths=dict(
        media = ['media'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def recently_unfollowed_profiles_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/recently_unfollowed_profiles.json"])

    df = parse_json(data,
        row_path=["$.relationships_unfollowed_users"],
        col_paths=dict(
        media_list_data = ['media_list_data'],
        href = ['string_list_data.href'],
        timestamp = ['string_list_data.timestamp'],
        value = ['string_list_data.value'],
        title = ['title'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def recently_viewed_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/recently_viewed.json"])

    df = parse_json(data,
        row_path=["$.recently_viewed"],
        col_paths=dict(
        description = ['description'],
        name = ['name'],
        uri = ['children.entries.data.uri'],
        watch_time = ['children.entries.data.watch_time'],
        timestamp = ['children.entries.timestamp'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def recently_visited_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/recently_visited.json"])

    df = parse_json(data,
        row_path=["$.visited_things_v2"],
        col_paths=dict(
        description = ['description'],
        name = ['name'],
        uri = ['entries.data.uri'],
        timestamp = ['entries.timestamp'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def recognized_devices_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/recognized_devices.json"])

    df = parse_json(data,
        row_path=["$.recognized_devices_v2"],
        col_paths=dict(
        created_timestamp = ['created_timestamp'],
        datr_cookie = ['datr_cookie'],
        ip_address = ['ip_address'],
        name = ['name'],
        user_agent = ['user_agent'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def recommended_topics_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/recommended_topics.json"])

    df = parse_json(data,
        row_path=["$.topics_your_topics"],
        col_paths=dict(
        media_map_data = ['media_map_data'],
        href = ['string_map_data.Name.href'],
        timestamp = ['string_map_data.Name.timestamp'],
        value = ['string_map_data.Name.value'],
        title = ['title'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def record_details_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/record_details.json"])

    df = parse_json(data,
        row_path=["$.admin_records_v2"],
        col_paths=dict(
        event = ['event'],
        created_timestamp = ['session.created_timestamp'],
        datr_cookie = ['session.datr_cookie'],
        ip_address = ['session.ip_address'],
        user_agent = ['session.user_agent'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def reels_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/reels.json"])

    df = parse_json(data,
        row_path=["$.ig_reels_media"],
        col_paths=dict(
        creation_timestamp = ['media.creation_timestamp'],
        source_app = ['media.cross_post_source.source_app'],
        dubbing_info = ['media.dubbing_info'],
        has_camera_metadata = ['media.media_metadata.camera_metadata.has_camera_metadata'],
        camera_position = ['media.media_metadata.video_metadata.exif_data.camera_position'],
        device_id = ['media.media_metadata.video_metadata.exif_data.device_id'],
        source_type = ['media.media_metadata.video_metadata.exif_data.source_type'],
        music_genre = ['media.media_metadata.video_metadata.music_genre'],
        media_variants = ['media.media_variants'],
        title = ['media.title'],
        uri = ['media.uri'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def reels_comments_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/reels_comments.json"])

    df = parse_json(data,
        row_path=["$.comments_reels_comments"],
        col_paths=dict(
        value = ['string_map_data.Media Owner.value'],
        timestamp = ['string_map_data.Time.timestamp'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def reels_preferences_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/reels_preferences.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def rejected_friend_requests_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/rejected_friend_requests.json"])

    df = parse_json(data,
        row_path=["$.rejected_requests_v2"],
        col_paths=dict(
        name = ['name'],
        timestamp = ['timestamp'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def removed_friends_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/removed_friends.json"])

    df = parse_json(data,
        row_path=["$.deleted_friends_v2"],
        col_paths=dict(
        name = ['name'],
        timestamp = ['timestamp'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def removed_suggestions_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/removed_suggestions.json"])

    df = parse_json(data,
        row_path=["$.relationships_dismissed_suggested_users"],
        col_paths=dict(
        media_list_data = ['media_list_data'],
        href = ['string_list_data.href'],
        timestamp = ['string_list_data.timestamp'],
        value = ['string_list_data.value'],
        title = ['title'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def reshare_education_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/reshare_education.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def saved_collections_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/saved_collections.json"])

    df = parse_json(data,
        row_path=["$.saved_saved_collections"],
        col_paths=dict(
        timestamp = ['string_map_data.Update Time.timestamp'],
        value = ['string_map_data.Name.value'],
        title = ['title'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def saved_posts_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/saved_posts.json"])

    df = parse_json(data,
        row_path=["$.saved_saved_media"],
        col_paths=dict(
        href = ['string_map_data.Saved on.href'],
        timestamp = ['string_map_data.Saved on.timestamp'],
        title = ['title'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def secret_conversations_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/secret_conversations.json"])

    df = parse_json(data,
        row_path=["$.ig_secret_conversations"],
        col_paths=dict(
        device_manufacturer = ['armadillo_devices.device_manufacturer'],
        device_model = ['armadillo_devices.device_model'],
        device_os_version = ['armadillo_devices.device_os_version'],
        device_type = ['armadillo_devices.device_type'],
        last_active_time = ['armadillo_devices.last_active_time'],
        last_connected_ip = ['armadillo_devices.last_connected_ip'],
        calls = ['calls'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def sent_friend_requests_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/sent_friend_requests.json"])

    df = parse_json(data,
        row_path=["$.sent_requests_v2"],
        col_paths=dict(
        name = ['name'],
        timestamp = ['timestamp'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def settings_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/settings.json"])

    df = parse_json(data,
        row_path=["$.timestamp"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def show_exclusive_story_promo_setting_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/show_exclusive_story_promo_setting.json"])

    df = parse_json(data,
        row_path=["$.subscriptions_show_story_teaser_setting"],
        col_paths=dict(
        media_map_data = ['media_map_data'],
        href = ['string_map_data.Exclusive Story Promo Setting.href'],
        timestamp = ['string_map_data.Exclusive Story Promo Setting.timestamp'],
        value = ['string_map_data.Exclusive Story Promo Setting.value'],
        title = ['title'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def signup_details_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/signup_details.json"])

    df = parse_json(data,
        row_path=["$.account_history_registration_info"],
        col_paths=dict(
        media_map_data = ['media_map_data'],
        href = ['string_map_data.Username.href'],
        timestamp = ['string_map_data.Username.timestamp'],
        value = ['string_map_data.Username.value'],
        title = ['title'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def stories_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/stories.json"])

    df = parse_json(data,
        row_path=["$.ig_stories"],
        col_paths=dict(
        creation_timestamp = ['creation_timestamp'],
        source_app = ['cross_post_source.source_app'],
        dubbing_info = ['dubbing_info'],
        has_camera_metadata = ['media_metadata.camera_metadata.has_camera_metadata'],
        camera_position = ['media_metadata.video_metadata.exif_data.camera_position'],
        date_time_original = ['media_metadata.video_metadata.exif_data.date_time_original'],
        device_id = ['media_metadata.video_metadata.exif_data.device_id'],
        source_type = ['media_metadata.video_metadata.exif_data.source_type'],
        media_variants = ['media_variants'],
        title = ['title'],
        uri = ['uri'],
        backup_uri = ['backup_uri'],
        music_genre = ['media_metadata.video_metadata.music_genre'],
        aperture = ['media_metadata.video_metadata.exif_data.aperture'],
        date_time_digitized = ['media_metadata.video_metadata.exif_data.date_time_digitized'],
        focal_length = ['media_metadata.video_metadata.exif_data.focal_length'],
        iso = ['media_metadata.video_metadata.exif_data.iso'],
        lens_make = ['media_metadata.video_metadata.exif_data.lens_make'],
        lens_model = ['media_metadata.video_metadata.exif_data.lens_model'],
        metering_mode = ['media_metadata.video_metadata.exif_data.metering_mode'],
        scene_type = ['media_metadata.video_metadata.exif_data.scene_type'],
        shutter_speed = ['media_metadata.video_metadata.exif_data.shutter_speed'],
        software = ['media_metadata.video_metadata.exif_data.software'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def story_likes_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/story_likes.json"])

    df = parse_json(data,
        row_path=["$.story_activities_story_likes"],
        col_paths=dict(
        timestamp = ['string_list_data.timestamp'],
        title = ['title'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def subscription_for_no_ads_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/subscription_for_no_ads.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def suggested_friends_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/suggested_friends.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def suggested_profiles_viewed_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/suggested_profiles_viewed.json"])

    df = parse_json(data,
        row_path=["$.impressions_history_chaining_seen"],
        col_paths=dict(
        timestamp = ['string_map_data.Time.timestamp'],
        value = ['string_map_data.Username.value'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def synced_contacts_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/synced_contacts.json"])

    df = parse_json(data,
        row_path=["$.contacts_contact_info"],
        col_paths=dict(
        media_map_data = ['media_map_data'],
        href = ['string_map_data.Last Name.href'],
        timestamp = ['string_map_data.Last Name.timestamp'],
        value = ['string_map_data.Last Name.value'],
        title = ['title'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def synced_contacts_from_instagram_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/synced_contacts_from_instagram.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def the_ways_we_can_send_you_notifications_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/the_ways_we_can_send_you_notifications.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def time_spent_on_facebook_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/time_spent_on_facebook.json"])

    df = parse_json(data,
        row_path=["$.timestamp"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def time_spent_on_instagram_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/time_spent_on_instagram.json"])

    df = parse_json(data,
        row_path=["$.timestamp"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def timezone_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/timezone.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def trusting_frequently_used_devices_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/trusting_frequently_used_devices.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def two_factor_authentication_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/two-factor_authentication.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def unfollowed_profiles_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/unfollowed_profiles.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def use_cross_app_messaging_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/use_cross-app_messaging.json"])

    df = parse_json(data,
        row_path=["$.settings_upgraded_to_cross_app_messaging"],
        col_paths=dict(
        media_map_data = ['media_map_data'],
        href = ['string_map_data.Upgraded To Cross-App Messaging.href'],
        timestamp = ['string_map_data.Upgraded To Cross-App Messaging.timestamp'],
        value = ['string_map_data.Upgraded To Cross-App Messaging.value'],
        title = ['title'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def videos_watched_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/videos_watched.json"])

    df = parse_json(data,
        row_path=["$.impressions_history_videos_watched"],
        col_paths=dict(
        value = ['string_map_data.Author.value'],
        timestamp = ['string_map_data.Time.timestamp'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def voting_location_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/voting_location.json"])

    df = parse_json(data,
        row_path=["$.voting_location_v2"],
        col_paths=dict(
        voting_location = ['voting_location'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def voting_reminders_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/voting_reminders.json"])

    df = parse_json(data,
        row_path=["$.voting_reminders_v2"],
        col_paths=dict(
        voting_reminders = ['voting_reminders'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def weather_forecast_settings_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/weather_forecast_settings.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def where_you_re_logged_in_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/where_you're_logged_in.json"])

    df = parse_json(data,
        row_path=["$.active_sessions_v2"],
        col_paths=dict(
        app = ['app'],
        created_timestamp = ['created_timestamp'],
        datr_cookie = ['datr_cookie'],
        device = ['device'],
        ip_address = ['ip_address'],
        location = ['location'],
        name = ['name'],
        session_type = ['session_type'],
        updated_timestamp = ['updated_timestamp'],
        user_agent = ['user_agent'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def who_you_ve_followed_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/who_you've_followed.json"])

    df = parse_json(data,
        row_path=["$.following_v3"],
        col_paths=dict(
        name = ['name'],
        timestamp = ['timestamp'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def word_or_phrase_searches_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/word_or_phrase_searches.json"])

    df = parse_json(data,
        row_path=["$.searches_keyword"],
        col_paths=dict(
        media_map_data = ['media_map_data'],
        href = ['string_map_data.Time.href'],
        timestamp = ['string_map_data.Time.timestamp'],
        value = ['string_map_data.Time.value'],
        title = ['title'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def your_account_password_information_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/your_account_password_information.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def your_activity_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/your_activity.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def your_activity_off_meta_technologies_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/your_activity_off_meta_technologies.json"])

    df = parse_json(data,
        row_path=["$.apps_and_websites_off_meta_activity"],
        col_paths=dict(
        id = ['events.id'],
        timestamp = ['events.timestamp'],
        type = ['events.type'],
        name = ['name'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def your_activity_off_meta_technologies_settings_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/your_activity_off_meta_technologies_settings.json"])

    df = parse_json(data,
        row_path=["$.timestamp"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def your_apps_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/your_apps.json"])

    df = parse_json(data,
        row_path=["$.admined_apps_v2"],
        col_paths=dict(
        added_timestamp = ['added_timestamp'],
        name = ['name'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def your_badges_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/your_badges.json"])

    df = parse_json(data,
        row_path=["$.group_badges_v2"],
        col_paths=dict(
        International_Space_Camp_2009 = ['International Space Camp 2009'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def your_comment_edits_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/your_comment_edits.json"])

    df = parse_json(data,
        row_path=["$.timestamp"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def your_comments_in_groups_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/your_comments_in_groups.json"])

    df = parse_json(data,
        row_path=["$.group_comments_v2"],
        col_paths=dict(
        author = ['data.comment.author'],
        comment = ['data.comment.comment'],
        group = ['data.comment.group'],
        timestamp = ['timestamp'],
        title = ['title'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def your_consent_settings_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/your_consent_settings.json"])

    df = parse_json(data,
        row_path=["$.timestamp"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def your_content_visibility_notification_history_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/your_content_visibility_notification_history.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def your_device_push_settings_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/your_device_push_settings.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def your_devices_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/your_devices.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def your_document_revision_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/your_document_revision.json"])

    df = parse_json(data,
        row_path=["$.timestamp"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def your_educational_notification_interactions_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/your_educational_notification_interactions.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def your_event_invitation_links_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/your_event_invitation_links.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def your_event_responses_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/your_event_responses.json"])

    df = parse_json(data,
        row_path=["$.event_responses_v2"],
        col_paths=dict(
        end_timestamp = ['events_joined.end_timestamp'],
        name = ['events_joined.name'],
        start_timestamp = ['events_joined.start_timestamp'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def your_events_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/your_events.json"])

    df = parse_json(data,
        row_path=["$.your_events_v2"],
        col_paths=dict(
        create_timestamp = ['create_timestamp'],
        description = ['description'],
        end_timestamp = ['end_timestamp'],
        name = ['place.name'],
        address = ['place.address'],
        latitude = ['place.coordinate.latitude'],
        longitude = ['place.coordinate.longitude'],
        start_timestamp = ['start_timestamp'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def your_experiences_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/your_experiences.json"])

    df = parse_json(data,
        row_path=["$.timestamp"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def your_facebook_activity_history_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/your_facebook_activity_history.json"])

    df = parse_json(data,
        row_path=["$.last_activity_v2"],
        col_paths=dict(
        activity_by_day = ['last_activity_time.Website.activity_by_day'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def your_facebook_story_preferences_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/your_facebook_story_preferences.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def your_facebook_watch_activity_in_the_last_28_days_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/your_facebook_watch_activity_in_the_last_28_days.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def your_friends_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/your_friends.json"])

    df = parse_json(data,
        row_path=["$.friends_v2"],
        col_paths=dict(
        name = ['name'],
        timestamp = ['timestamp'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def your_fundraiser_donations_information_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/your_fundraiser_donations_information.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def your_fundraiser_settings_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/your_fundraiser_settings.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def your_group_membership_activity_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/your_group_membership_activity.json"])

    df = parse_json(data,
        row_path=["$.groups_joined_v2"],
        col_paths=dict(
        name = ['data.name'],
        timestamp = ['timestamp'],
        title = ['title'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def your_group_shortcuts_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/your_group_shortcuts.json"])

    df = parse_json(data,
        row_path=["$.timestamp"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def your_groups_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/your_groups.json"])

    df = parse_json(data,
        row_path=["$.groups_admined_v2"],
        col_paths=dict(
        name = ['name'],
        timestamp = ['timestamp'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def your_in_app_messages_interactions_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/your_in-app_messages_interactions.json"])

    df = parse_json(data,
        row_path=["$.timestamp"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def your_information_download_requests_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/your_information_download_requests.json"])

    df = parse_json(data,
        row_path=["$.timestamp"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def your_marketplace_assistant_settings_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/your_marketplace_assistant_settings.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def your_marketplace_device_history_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/your_marketplace_device_history.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def your_media_permissions_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/your_media_permissions.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def your_meta_business_suite_guidance_interactions_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/your_meta_business_suite_guidance_interactions.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def your_muted_story_teaser_creators_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/your_muted_story_teaser_creators.json"])

    df = parse_json(data,
        row_path=["$.subscriptions_muted_story_teaser_creators"],
        col_paths=dict(
        media_map_data = ['media_map_data'],
        href = ['string_map_data.Muted Creators.href'],
        timestamp = ['string_map_data.Muted Creators.timestamp'],
        value = ['string_map_data.Muted Creators.value'],
        title = ['title'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def your_notification_status_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/your_notification_status.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def your_notifications_tab_activity_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/your_notifications_tab_activity.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def your_pages_mentions_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/your_pages_mentions.json"])

    df = parse_json(data,
        row_path=["$.timestamp"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def your_payment_account_activity_history_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/your_payment_account_activity_history.json"])

    df = parse_json(data,
        row_path=["$.timestamp"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def your_poll_votes_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/your_poll_votes.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def your_post_audiences_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/your_post_audiences.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def your_post_composer_settings_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/your_post_composer_settings.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def your_posts__check_ins__photos_and_videos_1_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/your_posts__check_ins__photos_and_videos_1.json"])

    df = parse_json(data,
        row_path=["$.timestamp"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def your_privacy_jurisdiction_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/your_privacy_jurisdiction.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def your_recent_account_recovery_successes_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/your_recent_account_recovery_successes.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def your_recently_followed_history_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/your_recently_followed_history.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def your_recently_used_emojis_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/your_recently_used_emojis.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def your_sampled_locations_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/your_sampled_locations.json"])

    df = parse_json(data,
        row_path=["$.timestamp"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def your_saved_items_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/your_saved_items.json"])

    df = parse_json(data,
        row_path=["$.saves_v2"],
        col_paths=dict(
        timestamp = ['timestamp'],
        title = ['title'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def your_search_history_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/your_search_history.json"])

    df = parse_json(data,
        row_path=["$.searches_v2"],
        col_paths=dict(
        text = ['data.text'],
        timestamp = ['timestamp'],
        title = ['title'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def your_settings_for_groups_tab_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/your_settings_for_groups_tab.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def your_story_highlights_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/your_story_highlights.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def your_tab_notifications_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/your_tab_notifications.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def your_topics_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/your_topics.json"])

    df = parse_json(data,
        row_path=["$.topics_your_topics"],
        col_paths=dict(
        media_map_data = ['media_map_data'],
        href = ['string_map_data.Name.href'],
        timestamp = ['string_map_data.Name.timestamp'],
        value = ['string_map_data.Name.value'],
        title = ['title'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def your_transaction_survey_information_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/your_transaction_survey_information.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def your_uncategorized_photos_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/your_uncategorized_photos.json"])

    df = parse_json(data,
        row_path=["$.other_photos_v2"],
        col_paths=dict(
        creation_timestamp = ['creation_timestamp'],
        description = ['description'],
        upload_ip = ['media_metadata.photo_metadata.exif_data.upload_ip'],
        uri = ['uri'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def your_videos_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/your_videos.json"])

    df = parse_json(data,
        row_path=["$.videos_v2"],
        col_paths=dict(
        creation_timestamp = ['creation_timestamp'],
        description = ['description'],
        dubbing_info = ['dubbing_info'],
        upload_ip = ['media_metadata.video_metadata.exif_data.upload_ip'],
        upload_timestamp = ['media_metadata.video_metadata.exif_data.upload_timestamp'],
        media_variants = ['media_variants'],
        title = ['title'],
        uri = ['uri'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def your_watch_settings_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/your_watch_settings.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def create_donation_flow(file_input: list[str]):
    """
    Creates a donation flow for Instagram data, explicitly trying each extractor function.
    Only creates tables for data that's available in the provided files.
    """
    tables = []
    #print(file_input)

    # _0
    try:
        _0_table = donation_table(
            name="_0",
            df=_0_df(file_input),
            title={"en": "_0", "nl": "_0"},
        )
        tables.append(_0_table)
    except Exception as e:
        #print(f"Skipping _0: {e}")
        pass

    # _1
    try:
        _1_table = donation_table(
            name="_1",
            df=_1_df(file_input),
            title={"en": "_1", "nl": "_1"},
        )
        tables.append(_1_table)
    except Exception as e:
        #print(f"Skipping _1: {e}")
        pass

    # _2
    try:
        _2_table = donation_table(
            name="_2",
            df=_2_df(file_input),
            title={"en": "_2", "nl": "_2"},
        )
        tables.append(_2_table)
    except Exception as e:
        #print(f"Skipping _2: {e}")
        pass

    # _3
    try:
        _3_table = donation_table(
            name="_3",
            df=_3_df(file_input),
            title={"en": "_3", "nl": "_3"},
        )
        tables.append(_3_table)
    except Exception as e:
        #print(f"Skipping _3: {e}")
        pass

    # _4
    try:
        _4_table = donation_table(
            name="_4",
            df=_4_df(file_input),
            title={"en": "_4", "nl": "_4"},
        )
        tables.append(_4_table)
    except Exception as e:
        #print(f"Skipping _4: {e}")
        pass

    # _5
    try:
        _5_table = donation_table(
            name="_5",
            df=_5_df(file_input),
            title={"en": "_5", "nl": "_5"},
        )
        tables.append(_5_table)
    except Exception as e:
        #print(f"Skipping _5: {e}")
        pass

    # _6
    try:
        _6_table = donation_table(
            name="_6",
            df=_6_df(file_input),
            title={"en": "_6", "nl": "_6"},
        )
        tables.append(_6_table)
    except Exception as e:
        #print(f"Skipping _6: {e}")
        pass

    # _7
    try:
        _7_table = donation_table(
            name="_7",
            df=_7_df(file_input),
            title={"en": "_7", "nl": "_7"},
        )
        tables.append(_7_table)
    except Exception as e:
        #print(f"Skipping _7: {e}")
        pass

    # _8
    try:
        _8_table = donation_table(
            name="_8",
            df=_8_df(file_input),
            title={"en": "_8", "nl": "_8"},
        )
        tables.append(_8_table)
    except Exception as e:
        #print(f"Skipping _8: {e}")
        pass

    # account_activity
    try:
        account_activity_table = donation_table(
            name="account_activity",
            df=account_activity_df(file_input),
            title={"en": "account_activity", "nl": "account_activity"},
        )
        tables.append(account_activity_table)
    except Exception as e:
        #print(f"Skipping account_activity: {e}")
        pass

    # ad_preferences
    try:
        ad_preferences_table = donation_table(
            name="ad_preferences",
            df=ad_preferences_df(file_input),
            title={"en": "ad_preferences", "nl": "ad_preferences"},
        )
        tables.append(ad_preferences_table)
    except Exception as e:
        #print(f"Skipping ad_preferences: {e}")
        pass

    # ads_about_meta
    try:
        ads_about_meta_table = donation_table(
            name="ads_about_meta",
            df=ads_about_meta_df(file_input),
            title={"en": "ads_about_meta", "nl": "ads_about_meta"},
        )
        tables.append(ads_about_meta_table)
    except Exception as e:
        #print(f"Skipping ads_about_meta: {e}")
        pass

    # ads_clicked
    try:
        ads_clicked_table = donation_table(
            name="ads_clicked",
            df=ads_clicked_df(file_input),
            title={"en": "ads_clicked", "nl": "ads_clicked"},
        )
        tables.append(ads_clicked_table)
    except Exception as e:
        #print(f"Skipping ads_clicked: {e}")
        pass

    # ads_interests
    try:
        ads_interests_table = donation_table(
            name="ads_interests",
            df=ads_interests_df(file_input),
            title={"en": "ads_interests", "nl": "ads_interests"},
        )
        tables.append(ads_interests_table)
    except Exception as e:
        #print(f"Skipping ads_interests: {e}")
        pass

    # ads_personalization_consent
    try:
        ads_personalization_consent_table = donation_table(
            name="ads_personalization_consent",
            df=ads_personalization_consent_df(file_input),
            title={"en": "ads_personalization_consent", "nl": "ads_personalization_consent"},
        )
        tables.append(ads_personalization_consent_table)
    except Exception as e:
        #print(f"Skipping ads_personalization_consent: {e}")
        pass

    # ads_viewed
    try:
        ads_viewed_table = donation_table(
            name="ads_viewed",
            df=ads_viewed_df(file_input),
            title={"en": "ads_viewed", "nl": "ads_viewed"},
        )
        tables.append(ads_viewed_table)
    except Exception as e:
        #print(f"Skipping ads_viewed: {e}")
        pass

    # advertisers_using_your_activity_or_information
    try:
        advertisers_using_your_activity_or_information_table = donation_table(
            name="advertisers_using_your_activity_or_information",
            df=advertisers_using_your_activity_or_information_df(file_input),
            title={"en": "advertisers_using_your_activity_or_information", "nl": "advertisers_using_your_activity_or_information"},
        )
        tables.append(advertisers_using_your_activity_or_information_table)
    except Exception as e:
        #print(f"Skipping advertisers_using_your_activity_or_information: {e}")
        pass

    # autofill_information
    try:
        autofill_information_table = donation_table(
            name="autofill_information",
            df=autofill_information_df(file_input),
            title={"en": "autofill_information", "nl": "autofill_information"},
        )
        tables.append(autofill_information_table)
    except Exception as e:
        #print(f"Skipping autofill_information: {e}")
        pass

    # blocked_profiles
    try:
        blocked_profiles_table = donation_table(
            name="blocked_profiles",
            df=blocked_profiles_df(file_input),
            title={"en": "blocked_profiles", "nl": "blocked_profiles"},
        )
        tables.append(blocked_profiles_table)
    except Exception as e:
        #print(f"Skipping blocked_profiles: {e}")
        pass

    # bookmark_and_app_settings
    try:
        bookmark_and_app_settings_table = donation_table(
            name="bookmark_and_app_settings",
            df=bookmark_and_app_settings_df(file_input),
            title={"en": "bookmark_and_app_settings", "nl": "bookmark_and_app_settings"},
        )
        tables.append(bookmark_and_app_settings_table)
    except Exception as e:
        #print(f"Skipping bookmark_and_app_settings: {e}")
        pass

    # browser_cookies
    try:
        browser_cookies_table = donation_table(
            name="browser_cookies",
            df=browser_cookies_df(file_input),
            title={"en": "browser_cookies", "nl": "browser_cookies"},
        )
        tables.append(browser_cookies_table)
    except Exception as e:
        #print(f"Skipping browser_cookies: {e}")
        pass

    # browser_push_notifications
    try:
        browser_push_notifications_table = donation_table(
            name="browser_push_notifications",
            df=browser_push_notifications_df(file_input),
            title={"en": "browser_push_notifications", "nl": "browser_push_notifications"},
        )
        tables.append(browser_push_notifications_table)
    except Exception as e:
        #print(f"Skipping browser_push_notifications: {e}")
        pass

    # camera_information
    try:
        camera_information_table = donation_table(
            name="camera_information",
            df=camera_information_df(file_input),
            title={"en": "camera_information", "nl": "camera_information"},
        )
        tables.append(camera_information_table)
    except Exception as e:
        #print(f"Skipping camera_information: {e}")
        pass

    # check_ins
    try:
        check_ins_table = donation_table(
            name="check_ins",
            df=check_ins_df(file_input),
            title={"en": "check_ins", "nl": "check_ins"},
        )
        tables.append(check_ins_table)
    except Exception as e:
        #print(f"Skipping check_ins: {e}")
        pass

    # cities_you_have_checked_into
    try:
        cities_you_have_checked_into_table = donation_table(
            name="cities_you_have_checked_into",
            df=cities_you_have_checked_into_df(file_input),
            title={"en": "cities_you_have_checked_into", "nl": "cities_you_have_checked_into"},
        )
        tables.append(cities_you_have_checked_into_table)
    except Exception as e:
        #print(f"Skipping cities_you_have_checked_into: {e}")
        pass

    # close_friends
    try:
        close_friends_table = donation_table(
            name="close_friends",
            df=close_friends_df(file_input),
            title={"en": "close_friends", "nl": "close_friends"},
        )
        tables.append(close_friends_table)
    except Exception as e:
        #print(f"Skipping close_friends: {e}")
        pass

    # comments
    try:
        comments_table = donation_table(
            name="comments",
            df=comments_df(file_input),
            title={"en": "comments", "nl": "comments"},
        )
        tables.append(comments_table)
    except Exception as e:
        #print(f"Skipping comments: {e}")
        pass

    # comments_allowed_from
    try:
        comments_allowed_from_table = donation_table(
            name="comments_allowed_from",
            df=comments_allowed_from_df(file_input),
            title={"en": "comments_allowed_from", "nl": "comments_allowed_from"},
        )
        tables.append(comments_allowed_from_table)
    except Exception as e:
        #print(f"Skipping comments_allowed_from: {e}")
        pass

    # connected_apps_and_websites
    try:
        connected_apps_and_websites_table = donation_table(
            name="connected_apps_and_websites",
            df=connected_apps_and_websites_df(file_input),
            title={"en": "connected_apps_and_websites", "nl": "connected_apps_and_websites"},
        )
        tables.append(connected_apps_and_websites_table)
    except Exception as e:
        #print(f"Skipping connected_apps_and_websites: {e}")
        pass

    # consent_for_combining_facebook_and_messenger_data
    try:
        consent_for_combining_facebook_and_messenger_data_table = donation_table(
            name="consent_for_combining_facebook_and_messenger_data",
            df=consent_for_combining_facebook_and_messenger_data_df(file_input),
            title={"en": "consent_for_combining_facebook_and_messenger_data", "nl": "consent_for_combining_facebook_and_messenger_data"},
        )
        tables.append(consent_for_combining_facebook_and_messenger_data_table)
    except Exception as e:
        #print(f"Skipping consent_for_combining_facebook_and_messenger_data: {e}")
        pass

    # consents
    try:
        consents_table = donation_table(
            name="consents",
            df=consents_df(file_input),
            title={"en": "consents", "nl": "consents"},
        )
        tables.append(consents_table)
    except Exception as e:
        #print(f"Skipping consents: {e}")
        pass

    # contacts_sync_settings
    try:
        contacts_sync_settings_table = donation_table(
            name="contacts_sync_settings",
            df=contacts_sync_settings_df(file_input),
            title={"en": "contacts_sync_settings", "nl": "contacts_sync_settings"},
        )
        tables.append(contacts_sync_settings_table)
    except Exception as e:
        #print(f"Skipping contacts_sync_settings: {e}")
        pass

    # controls
    try:
        controls_table = donation_table(
            name="controls",
            df=controls_df(file_input),
            title={"en": "controls", "nl": "controls"},
        )
        tables.append(controls_table)
    except Exception as e:
        #print(f"Skipping controls: {e}")
        pass

    # conversations_you_had_as_a_buyer
    try:
        conversations_you_had_as_a_buyer_table = donation_table(
            name="conversations_you_had_as_a_buyer",
            df=conversations_you_had_as_a_buyer_df(file_input),
            title={"en": "conversations_you_had_as_a_buyer", "nl": "conversations_you_had_as_a_buyer"},
        )
        tables.append(conversations_you_had_as_a_buyer_table)
    except Exception as e:
        #print(f"Skipping conversations_you_had_as_a_buyer: {e}")
        pass

    # detected_hardware
    try:
        detected_hardware_table = donation_table(
            name="detected_hardware",
            df=detected_hardware_df(file_input),
            title={"en": "detected_hardware", "nl": "detected_hardware"},
        )
        tables.append(detected_hardware_table)
    except Exception as e:
        #print(f"Skipping detected_hardware: {e}")
        pass

    # device_location
    try:
        device_location_table = donation_table(
            name="device_location",
            df=device_location_df(file_input),
            title={"en": "device_location", "nl": "device_location"},
        )
        tables.append(device_location_table)
    except Exception as e:
        #print(f"Skipping device_location: {e}")
        pass

    # device_login_cookies
    try:
        device_login_cookies_table = donation_table(
            name="device_login_cookies",
            df=device_login_cookies_df(file_input),
            title={"en": "device_login_cookies", "nl": "device_login_cookies"},
        )
        tables.append(device_login_cookies_table)
    except Exception as e:
        #print(f"Skipping device_login_cookies: {e}")
        pass

    # device_navigation_bar_information
    try:
        device_navigation_bar_information_table = donation_table(
            name="device_navigation_bar_information",
            df=device_navigation_bar_information_df(file_input),
            title={"en": "device_navigation_bar_information", "nl": "device_navigation_bar_information"},
        )
        tables.append(device_navigation_bar_information_table)
    except Exception as e:
        #print(f"Skipping device_navigation_bar_information: {e}")
        pass

    # devices
    try:
        devices_table = donation_table(
            name="devices",
            df=devices_df(file_input),
            title={"en": "devices", "nl": "devices"},
        )
        tables.append(devices_table)
    except Exception as e:
        #print(f"Skipping devices: {e}")
        pass

    # eligibility
    try:
        eligibility_table = donation_table(
            name="eligibility",
            df=eligibility_df(file_input),
            title={"en": "eligibility", "nl": "eligibility"},
        )
        tables.append(eligibility_table)
    except Exception as e:
        #print(f"Skipping eligibility: {e}")
        pass

    # email_address_verifications
    try:
        email_address_verifications_table = donation_table(
            name="email_address_verifications",
            df=email_address_verifications_df(file_input),
            title={"en": "email_address_verifications", "nl": "email_address_verifications"},
        )
        tables.append(email_address_verifications_table)
    except Exception as e:
        #print(f"Skipping email_address_verifications: {e}")
        pass

    # emails_we_sent_you
    try:
        emails_we_sent_you_table = donation_table(
            name="emails_we_sent_you",
            df=emails_we_sent_you_df(file_input),
            title={"en": "emails_we_sent_you", "nl": "emails_we_sent_you"},
        )
        tables.append(emails_we_sent_you_table)
    except Exception as e:
        #print(f"Skipping emails_we_sent_you: {e}")
        pass

    # emoji_sliders
    try:
        emoji_sliders_table = donation_table(
            name="emoji_sliders",
            df=emoji_sliders_df(file_input),
            title={"en": "emoji_sliders", "nl": "emoji_sliders"},
        )
        tables.append(emoji_sliders_table)
    except Exception as e:
        #print(f"Skipping emoji_sliders: {e}")
        pass

    # event_invitations
    try:
        event_invitations_table = donation_table(
            name="event_invitations",
            df=event_invitations_df(file_input),
            title={"en": "event_invitations", "nl": "event_invitations"},
        )
        tables.append(event_invitations_table)
    except Exception as e:
        #print(f"Skipping event_invitations: {e}")
        pass

    # events_interactions
    try:
        events_interactions_table = donation_table(
            name="events_interactions",
            df=events_interactions_df(file_input),
            title={"en": "events_interactions", "nl": "events_interactions"},
        )
        tables.append(events_interactions_table)
    except Exception as e:
        #print(f"Skipping events_interactions: {e}")
        pass

    # events_you_ve_hidden
    try:
        events_you_ve_hidden_table = donation_table(
            name="events_you_ve_hidden",
            df=events_you_ve_hidden_df(file_input),
            title={"en": "events_you_ve_hidden", "nl": "events_you_ve_hidden"},
        )
        tables.append(events_you_ve_hidden_table)
    except Exception as e:
        #print(f"Skipping events_you_ve_hidden: {e}")
        pass

    # facebook_lite_notification_settings
    try:
        facebook_lite_notification_settings_table = donation_table(
            name="facebook_lite_notification_settings",
            df=facebook_lite_notification_settings_df(file_input),
            title={"en": "facebook_lite_notification_settings", "nl": "facebook_lite_notification_settings"},
        )
        tables.append(facebook_lite_notification_settings_table)
    except Exception as e:
        #print(f"Skipping facebook_lite_notification_settings: {e}")
        pass

    # facebook_new_user_guide
    try:
        facebook_new_user_guide_table = donation_table(
            name="facebook_new_user_guide",
            df=facebook_new_user_guide_df(file_input),
            title={"en": "facebook_new_user_guide", "nl": "facebook_new_user_guide"},
        )
        tables.append(facebook_new_user_guide_table)
    except Exception as e:
        #print(f"Skipping facebook_new_user_guide: {e}")
        pass

    # facebook_reels_usage_information
    try:
        facebook_reels_usage_information_table = donation_table(
            name="facebook_reels_usage_information",
            df=facebook_reels_usage_information_df(file_input),
            title={"en": "facebook_reels_usage_information", "nl": "facebook_reels_usage_information"},
        )
        tables.append(facebook_reels_usage_information_table)
    except Exception as e:
        #print(f"Skipping facebook_reels_usage_information: {e}")
        pass

    # feed
    try:
        feed_table = donation_table(
            name="feed",
            df=feed_df(file_input),
            title={"en": "feed", "nl": "feed"},
        )
        tables.append(feed_table)
    except Exception as e:
        #print(f"Skipping feed: {e}")
        pass

    # follow_requests_you_ve_received
    try:
        follow_requests_you_ve_received_table = donation_table(
            name="follow_requests_you_ve_received",
            df=follow_requests_you_ve_received_df(file_input),
            title={"en": "follow_requests_you_ve_received", "nl": "follow_requests_you_ve_received"},
        )
        tables.append(follow_requests_you_ve_received_table)
    except Exception as e:
        #print(f"Skipping follow_requests_you_ve_received: {e}")
        pass

    # followers_1
    try:
        followers_1_table = donation_table(
            name="followers_1",
            df=followers_1_df(file_input),
            title={"en": "followers_1", "nl": "followers_1"},
        )
        tables.append(followers_1_table)
    except Exception as e:
        #print(f"Skipping followers_1: {e}")
        pass

    # following
    try:
        following_table = donation_table(
            name="following",
            df=following_df(file_input),
            title={"en": "following", "nl": "following"},
        )
        tables.append(following_table)
    except Exception as e:
        #print(f"Skipping following: {e}")
        pass

    # following_hashtags
    try:
        following_hashtags_table = donation_table(
            name="following_hashtags",
            df=following_hashtags_df(file_input),
            title={"en": "following_hashtags", "nl": "following_hashtags"},
        )
        tables.append(following_hashtags_table)
    except Exception as e:
        #print(f"Skipping following_hashtags: {e}")
        pass

    # for_sale_group_preferences
    try:
        for_sale_group_preferences_table = donation_table(
            name="for_sale_group_preferences",
            df=for_sale_group_preferences_df(file_input),
            title={"en": "for_sale_group_preferences", "nl": "for_sale_group_preferences"},
        )
        tables.append(for_sale_group_preferences_table)
    except Exception as e:
        #print(f"Skipping for_sale_group_preferences: {e}")
        pass

    # fundraiser_posts_you_likely_viewed
    try:
        fundraiser_posts_you_likely_viewed_table = donation_table(
            name="fundraiser_posts_you_likely_viewed",
            df=fundraiser_posts_you_likely_viewed_df(file_input),
            title={"en": "fundraiser_posts_you_likely_viewed", "nl": "fundraiser_posts_you_likely_viewed"},
        )
        tables.append(fundraiser_posts_you_likely_viewed_table)
    except Exception as e:
        #print(f"Skipping fundraiser_posts_you_likely_viewed: {e}")
        pass

    # gaming_tab_notifications
    try:
        gaming_tab_notifications_table = donation_table(
            name="gaming_tab_notifications",
            df=gaming_tab_notifications_df(file_input),
            title={"en": "gaming_tab_notifications", "nl": "gaming_tab_notifications"},
        )
        tables.append(gaming_tab_notifications_table)
    except Exception as e:
        #print(f"Skipping gaming_tab_notifications: {e}")
        pass

    # group_posts_and_comments
    try:
        group_posts_and_comments_table = donation_table(
            name="group_posts_and_comments",
            df=group_posts_and_comments_df(file_input),
            title={"en": "group_posts_and_comments", "nl": "group_posts_and_comments"},
        )
        tables.append(group_posts_and_comments_table)
    except Exception as e:
        #print(f"Skipping group_posts_and_comments: {e}")
        pass

    # how_active_we_think_you_are_on_marketplace
    try:
        how_active_we_think_you_are_on_marketplace_table = donation_table(
            name="how_active_we_think_you_are_on_marketplace",
            df=how_active_we_think_you_are_on_marketplace_df(file_input),
            title={"en": "how_active_we_think_you_are_on_marketplace", "nl": "how_active_we_think_you_are_on_marketplace"},
        )
        tables.append(how_active_we_think_you_are_on_marketplace_table)
    except Exception as e:
        #print(f"Skipping how_active_we_think_you_are_on_marketplace: {e}")
        pass

    # id_verification
    try:
        id_verification_table = donation_table(
            name="id_verification",
            df=id_verification_df(file_input),
            title={"en": "id_verification", "nl": "id_verification"},
        )
        tables.append(id_verification_table)
    except Exception as e:
        #print(f"Skipping id_verification: {e}")
        pass

    # in_app_browser_autofill_settings
    try:
        in_app_browser_autofill_settings_table = donation_table(
            name="in_app_browser_autofill_settings",
            df=in_app_browser_autofill_settings_df(file_input),
            title={"en": "in_app_browser_autofill_settings", "nl": "in_app_browser_autofill_settings"},
        )
        tables.append(in_app_browser_autofill_settings_table)
    except Exception as e:
        #print(f"Skipping in_app_browser_autofill_settings: {e}")
        pass

    # information_about_your_last_login
    try:
        information_about_your_last_login_table = donation_table(
            name="information_about_your_last_login",
            df=information_about_your_last_login_df(file_input),
            title={"en": "information_about_your_last_login", "nl": "information_about_your_last_login"},
        )
        tables.append(information_about_your_last_login_table)
    except Exception as e:
        #print(f"Skipping information_about_your_last_login: {e}")
        pass

    # information_you_ve_submitted_to_advertisers
    try:
        information_you_ve_submitted_to_advertisers_table = donation_table(
            name="information_you_ve_submitted_to_advertisers",
            df=information_you_ve_submitted_to_advertisers_df(file_input),
            title={"en": "information_you_ve_submitted_to_advertisers", "nl": "information_you_ve_submitted_to_advertisers"},
        )
        tables.append(information_you_ve_submitted_to_advertisers_table)
    except Exception as e:
        #print(f"Skipping information_you_ve_submitted_to_advertisers: {e}")
        pass

    # instagram_profile_information
    try:
        instagram_profile_information_table = donation_table(
            name="instagram_profile_information",
            df=instagram_profile_information_df(file_input),
            title={"en": "instagram_profile_information", "nl": "instagram_profile_information"},
        )
        tables.append(instagram_profile_information_table)
    except Exception as e:
        #print(f"Skipping instagram_profile_information: {e}")
        pass

    # instagram_signup_details
    try:
        instagram_signup_details_table = donation_table(
            name="instagram_signup_details",
            df=instagram_signup_details_df(file_input),
            title={"en": "instagram_signup_details", "nl": "instagram_signup_details"},
        )
        tables.append(instagram_signup_details_table)
    except Exception as e:
        #print(f"Skipping instagram_signup_details: {e}")
        pass

    # ip_address_activity
    try:
        ip_address_activity_table = donation_table(
            name="ip_address_activity",
            df=ip_address_activity_df(file_input),
            title={"en": "ip_address_activity", "nl": "ip_address_activity"},
        )
        tables.append(ip_address_activity_table)
    except Exception as e:
        #print(f"Skipping ip_address_activity: {e}")
        pass

    # language_and_locale
    try:
        language_and_locale_table = donation_table(
            name="language_and_locale",
            df=language_and_locale_df(file_input),
            title={"en": "language_and_locale", "nl": "language_and_locale"},
        )
        tables.append(language_and_locale_table)
    except Exception as e:
        #print(f"Skipping language_and_locale: {e}")
        pass

    # language_settings_history
    try:
        language_settings_history_table = donation_table(
            name="language_settings_history",
            df=language_settings_history_df(file_input),
            title={"en": "language_settings_history", "nl": "language_settings_history"},
        )
        tables.append(language_settings_history_table)
    except Exception as e:
        #print(f"Skipping language_settings_history: {e}")
        pass

    # last_known_location
    try:
        last_known_location_table = donation_table(
            name="last_known_location",
            df=last_known_location_df(file_input),
            title={"en": "last_known_location", "nl": "last_known_location"},
        )
        tables.append(last_known_location_table)
    except Exception as e:
        #print(f"Skipping last_known_location: {e}")
        pass

    # liked_comments
    try:
        liked_comments_table = donation_table(
            name="liked_comments",
            df=liked_comments_df(file_input),
            title={"en": "liked_comments", "nl": "liked_comments"},
        )
        tables.append(liked_comments_table)
    except Exception as e:
        #print(f"Skipping liked_comments: {e}")
        pass

    # liked_posts
    try:
        liked_posts_table = donation_table(
            name="liked_posts",
            df=liked_posts_df(file_input),
            title={"en": "liked_posts", "nl": "liked_posts"},
        )
        tables.append(liked_posts_table)
    except Exception as e:
        #print(f"Skipping liked_posts: {e}")
        pass

    # likes_and_reactions
    try:
        likes_and_reactions_table = donation_table(
            name="likes_and_reactions",
            df=likes_and_reactions_df(file_input),
            title={"en": "likes_and_reactions", "nl": "likes_and_reactions"},
        )
        tables.append(likes_and_reactions_table)
    except Exception as e:
        #print(f"Skipping likes_and_reactions: {e}")
        pass

    # likes_and_reactions_1
    try:
        likes_and_reactions_1_table = donation_table(
            name="likes_and_reactions_1",
            df=likes_and_reactions_1_df(file_input),
            title={"en": "likes_and_reactions_1", "nl": "likes_and_reactions_1"},
        )
        tables.append(likes_and_reactions_1_table)
    except Exception as e:
        #print(f"Skipping likes_and_reactions_1: {e}")
        pass

    # linked_meta_accounts
    try:
        linked_meta_accounts_table = donation_table(
            name="linked_meta_accounts",
            df=linked_meta_accounts_df(file_input),
            title={"en": "linked_meta_accounts", "nl": "linked_meta_accounts"},
        )
        tables.append(linked_meta_accounts_table)
    except Exception as e:
        #print(f"Skipping linked_meta_accounts: {e}")
        pass

    # locations_of_interest
    try:
        locations_of_interest_table = donation_table(
            name="locations_of_interest",
            df=locations_of_interest_df(file_input),
            title={"en": "locations_of_interest", "nl": "locations_of_interest"},
        )
        tables.append(locations_of_interest_table)
    except Exception as e:
        #print(f"Skipping locations_of_interest: {e}")
        pass

    # login_activity
    try:
        login_activity_table = donation_table(
            name="login_activity",
            df=login_activity_df(file_input),
            title={"en": "login_activity", "nl": "login_activity"},
        )
        tables.append(login_activity_table)
    except Exception as e:
        #print(f"Skipping login_activity: {e}")
        pass

    # login_alerts_settings
    try:
        login_alerts_settings_table = donation_table(
            name="login_alerts_settings",
            df=login_alerts_settings_df(file_input),
            title={"en": "login_alerts_settings", "nl": "login_alerts_settings"},
        )
        tables.append(login_alerts_settings_table)
    except Exception as e:
        #print(f"Skipping login_alerts_settings: {e}")
        pass

    # login_protection_data
    try:
        login_protection_data_table = donation_table(
            name="login_protection_data",
            df=login_protection_data_df(file_input),
            title={"en": "login_protection_data", "nl": "login_protection_data"},
        )
        tables.append(login_protection_data_table)
    except Exception as e:
        #print(f"Skipping login_protection_data: {e}")
        pass

    # logins_and_logouts
    try:
        logins_and_logouts_table = donation_table(
            name="logins_and_logouts",
            df=logins_and_logouts_df(file_input),
            title={"en": "logins_and_logouts", "nl": "logins_and_logouts"},
        )
        tables.append(logins_and_logouts_table)
    except Exception as e:
        #print(f"Skipping logins_and_logouts: {e}")
        pass

    # message_1
    try:
        message_1_table = donation_table(
            name="message_1",
            df=message_1_df(file_input),
            title={"en": "message_1", "nl": "message_1"},
        )
        tables.append(message_1_table)
    except Exception as e:
        #print(f"Skipping message_1: {e}")
        pass

    # meta_privacy_policy_update_notifications
    try:
        meta_privacy_policy_update_notifications_table = donation_table(
            name="meta_privacy_policy_update_notifications",
            df=meta_privacy_policy_update_notifications_df(file_input),
            title={"en": "meta_privacy_policy_update_notifications", "nl": "meta_privacy_policy_update_notifications"},
        )
        tables.append(meta_privacy_policy_update_notifications_table)
    except Exception as e:
        #print(f"Skipping meta_privacy_policy_update_notifications: {e}")
        pass

    # milestone_notifications
    try:
        milestone_notifications_table = donation_table(
            name="milestone_notifications",
            df=milestone_notifications_df(file_input),
            title={"en": "milestone_notifications", "nl": "milestone_notifications"},
        )
        tables.append(milestone_notifications_table)
    except Exception as e:
        #print(f"Skipping milestone_notifications: {e}")
        pass

    # mobile_devices
    try:
        mobile_devices_table = donation_table(
            name="mobile_devices",
            df=mobile_devices_df(file_input),
            title={"en": "mobile_devices", "nl": "mobile_devices"},
        )
        tables.append(mobile_devices_table)
    except Exception as e:
        #print(f"Skipping mobile_devices: {e}")
        pass

    # navigation_bar_shortcut_history
    try:
        navigation_bar_shortcut_history_table = donation_table(
            name="navigation_bar_shortcut_history",
            df=navigation_bar_shortcut_history_df(file_input),
            title={"en": "navigation_bar_shortcut_history", "nl": "navigation_bar_shortcut_history"},
        )
        tables.append(navigation_bar_shortcut_history_table)
    except Exception as e:
        #print(f"Skipping navigation_bar_shortcut_history: {e}")
        pass

    # note_interactions
    try:
        note_interactions_table = donation_table(
            name="note_interactions",
            df=note_interactions_df(file_input),
            title={"en": "note_interactions", "nl": "note_interactions"},
        )
        tables.append(note_interactions_table)
    except Exception as e:
        #print(f"Skipping note_interactions: {e}")
        pass

    # notification_of_meta_privacy_policy_update
    try:
        notification_of_meta_privacy_policy_update_table = donation_table(
            name="notification_of_meta_privacy_policy_update",
            df=notification_of_meta_privacy_policy_update_df(file_input),
            title={"en": "notification_of_meta_privacy_policy_update", "nl": "notification_of_meta_privacy_policy_update"},
        )
        tables.append(notification_of_meta_privacy_policy_update_table)
    except Exception as e:
        #print(f"Skipping notification_of_meta_privacy_policy_update: {e}")
        pass

    # notification_of_privacy_policy_updates
    try:
        notification_of_privacy_policy_updates_table = donation_table(
            name="notification_of_privacy_policy_updates",
            df=notification_of_privacy_policy_updates_df(file_input),
            title={"en": "notification_of_privacy_policy_updates", "nl": "notification_of_privacy_policy_updates"},
        )
        tables.append(notification_of_privacy_policy_updates_table)
    except Exception as e:
        #print(f"Skipping notification_of_privacy_policy_updates: {e}")
        pass

    # notification_preferences
    try:
        notification_preferences_table = donation_table(
            name="notification_preferences",
            df=notification_preferences_df(file_input),
            title={"en": "notification_preferences", "nl": "notification_preferences"},
        )
        tables.append(notification_preferences_table)
    except Exception as e:
        #print(f"Skipping notification_preferences: {e}")
        pass

    # notification_settings
    try:
        notification_settings_table = donation_table(
            name="notification_settings",
            df=notification_settings_df(file_input),
            title={"en": "notification_settings", "nl": "notification_settings"},
        )
        tables.append(notification_settings_table)
    except Exception as e:
        #print(f"Skipping notification_settings: {e}")
        pass

    # notification_tab_display_information
    try:
        notification_tab_display_information_table = donation_table(
            name="notification_tab_display_information",
            df=notification_tab_display_information_df(file_input),
            title={"en": "notification_tab_display_information", "nl": "notification_tab_display_information"},
        )
        tables.append(notification_tab_display_information_table)
    except Exception as e:
        #print(f"Skipping notification_tab_display_information: {e}")
        pass

    # notifications
    try:
        notifications_table = donation_table(
            name="notifications",
            df=notifications_df(file_input),
            title={"en": "notifications", "nl": "notifications"},
        )
        tables.append(notifications_table)
    except Exception as e:
        #print(f"Skipping notifications: {e}")
        pass

    # notifications_about_new_users_joining_facebook
    try:
        notifications_about_new_users_joining_facebook_table = donation_table(
            name="notifications_about_new_users_joining_facebook",
            df=notifications_about_new_users_joining_facebook_df(file_input),
            title={"en": "notifications_about_new_users_joining_facebook", "nl": "notifications_about_new_users_joining_facebook"},
        )
        tables.append(notifications_about_new_users_joining_facebook_table)
    except Exception as e:
        #print(f"Skipping notifications_about_new_users_joining_facebook: {e}")
        pass

    # other_categories_used_to_reach_you
    try:
        other_categories_used_to_reach_you_table = donation_table(
            name="other_categories_used_to_reach_you",
            df=other_categories_used_to_reach_you_df(file_input),
            title={"en": "other_categories_used_to_reach_you", "nl": "other_categories_used_to_reach_you"},
        )
        tables.append(other_categories_used_to_reach_you_table)
    except Exception as e:
        #print(f"Skipping other_categories_used_to_reach_you: {e}")
        pass

    # pages_and_profiles_you_ve_recommended
    try:
        pages_and_profiles_you_ve_recommended_table = donation_table(
            name="pages_and_profiles_you_ve_recommended",
            df=pages_and_profiles_you_ve_recommended_df(file_input),
            title={"en": "pages_and_profiles_you_ve_recommended", "nl": "pages_and_profiles_you_ve_recommended"},
        )
        tables.append(pages_and_profiles_you_ve_recommended_table)
    except Exception as e:
        #print(f"Skipping pages_and_profiles_you_ve_recommended: {e}")
        pass

    # pages_and_profiles_you_follow
    try:
        pages_and_profiles_you_follow_table = donation_table(
            name="pages_and_profiles_you_follow",
            df=pages_and_profiles_you_follow_df(file_input),
            title={"en": "pages_and_profiles_you_follow", "nl": "pages_and_profiles_you_follow"},
        )
        tables.append(pages_and_profiles_you_follow_table)
    except Exception as e:
        #print(f"Skipping pages_and_profiles_you_follow: {e}")
        pass

    # pages_you_ve_liked
    try:
        pages_you_ve_liked_table = donation_table(
            name="pages_you_ve_liked",
            df=pages_you_ve_liked_df(file_input),
            title={"en": "pages_you_ve_liked", "nl": "pages_you_ve_liked"},
        )
        tables.append(pages_you_ve_liked_table)
    except Exception as e:
        #print(f"Skipping pages_you_ve_liked: {e}")
        pass

    # password_change_activity
    try:
        password_change_activity_table = donation_table(
            name="password_change_activity",
            df=password_change_activity_df(file_input),
            title={"en": "password_change_activity", "nl": "password_change_activity"},
        )
        tables.append(password_change_activity_table)
    except Exception as e:
        #print(f"Skipping password_change_activity: {e}")
        pass

    # payment_history
    try:
        payment_history_table = donation_table(
            name="payment_history",
            df=payment_history_df(file_input),
            title={"en": "payment_history", "nl": "payment_history"},
        )
        tables.append(payment_history_table)
    except Exception as e:
        #print(f"Skipping payment_history: {e}")
        pass

    # pending_follow_requests
    try:
        pending_follow_requests_table = donation_table(
            name="pending_follow_requests",
            df=pending_follow_requests_df(file_input),
            title={"en": "pending_follow_requests", "nl": "pending_follow_requests"},
        )
        tables.append(pending_follow_requests_table)
    except Exception as e:
        #print(f"Skipping pending_follow_requests: {e}")
        pass

    # people_and_friends
    try:
        people_and_friends_table = donation_table(
            name="people_and_friends",
            df=people_and_friends_df(file_input),
            title={"en": "people_and_friends", "nl": "people_and_friends"},
        )
        tables.append(people_and_friends_table)
    except Exception as e:
        #print(f"Skipping people_and_friends: {e}")
        pass

    # people_you_may_know
    try:
        people_you_may_know_table = donation_table(
            name="people_you_may_know",
            df=people_you_may_know_df(file_input),
            title={"en": "people_you_may_know", "nl": "people_you_may_know"},
        )
        tables.append(people_you_may_know_table)
    except Exception as e:
        #print(f"Skipping people_you_may_know: {e}")
        pass

    # permissions_you_have_granted_to_apps
    try:
        permissions_you_have_granted_to_apps_table = donation_table(
            name="permissions_you_have_granted_to_apps",
            df=permissions_you_have_granted_to_apps_df(file_input),
            title={"en": "permissions_you_have_granted_to_apps", "nl": "permissions_you_have_granted_to_apps"},
        )
        tables.append(permissions_you_have_granted_to_apps_table)
    except Exception as e:
        #print(f"Skipping permissions_you_have_granted_to_apps: {e}")
        pass

    # personal_information
    try:
        personal_information_table = donation_table(
            name="personal_information",
            df=personal_information_df(file_input),
            title={"en": "personal_information", "nl": "personal_information"},
        )
        tables.append(personal_information_table)
    except Exception as e:
        #print(f"Skipping personal_information: {e}")
        pass

    # places_you_have_been_tagged_in
    try:
        places_you_have_been_tagged_in_table = donation_table(
            name="places_you_have_been_tagged_in",
            df=places_you_have_been_tagged_in_df(file_input),
            title={"en": "places_you_have_been_tagged_in", "nl": "places_you_have_been_tagged_in"},
        )
        tables.append(places_you_have_been_tagged_in_table)
    except Exception as e:
        #print(f"Skipping places_you_have_been_tagged_in: {e}")
        pass

    # pokes
    try:
        pokes_table = donation_table(
            name="pokes",
            df=pokes_df(file_input),
            title={"en": "pokes", "nl": "pokes"},
        )
        tables.append(pokes_table)
    except Exception as e:
        #print(f"Skipping pokes: {e}")
        pass

    # polls
    try:
        polls_table = donation_table(
            name="polls",
            df=polls_df(file_input),
            title={"en": "polls", "nl": "polls"},
        )
        tables.append(polls_table)
    except Exception as e:
        #print(f"Skipping polls: {e}")
        pass

    # polls_you_voted_on
    try:
        polls_you_voted_on_table = donation_table(
            name="polls_you_voted_on",
            df=polls_you_voted_on_df(file_input),
            title={"en": "polls_you_voted_on", "nl": "polls_you_voted_on"},
        )
        tables.append(polls_you_voted_on_table)
    except Exception as e:
        #print(f"Skipping polls_you_voted_on: {e}")
        pass

    # possible_emails
    try:
        possible_emails_table = donation_table(
            name="possible_emails",
            df=possible_emails_df(file_input),
            title={"en": "possible_emails", "nl": "possible_emails"},
        )
        tables.append(possible_emails_table)
    except Exception as e:
        #print(f"Skipping possible_emails: {e}")
        pass

    # post_comments_1
    try:
        post_comments_1_table = donation_table(
            name="post_comments_1",
            df=post_comments_1_df(file_input),
            title={"en": "post_comments_1", "nl": "post_comments_1"},
        )
        tables.append(post_comments_1_table)
    except Exception as e:
        #print(f"Skipping post_comments_1: {e}")
        pass

    # posts_1
    try:
        posts_1_table = donation_table(
            name="posts_1",
            df=posts_1_df(file_input),
            title={"en": "posts_1", "nl": "posts_1"},
        )
        tables.append(posts_1_table)
    except Exception as e:
        #print(f"Skipping posts_1: {e}")
        pass

    # posts_on_other_pages_and_profiles
    try:
        posts_on_other_pages_and_profiles_table = donation_table(
            name="posts_on_other_pages_and_profiles",
            df=posts_on_other_pages_and_profiles_df(file_input),
            title={"en": "posts_on_other_pages_and_profiles", "nl": "posts_on_other_pages_and_profiles"},
        )
        tables.append(posts_on_other_pages_and_profiles_table)
    except Exception as e:
        #print(f"Skipping posts_on_other_pages_and_profiles: {e}")
        pass

    # posts_viewed
    try:
        posts_viewed_table = donation_table(
            name="posts_viewed",
            df=posts_viewed_df(file_input),
            title={"en": "posts_viewed", "nl": "posts_viewed"},
        )
        tables.append(posts_viewed_table)
    except Exception as e:
        #print(f"Skipping posts_viewed: {e}")
        pass

    # posts_you_re_not_interested_in
    try:
        posts_you_re_not_interested_in_table = donation_table(
            name="posts_you_re_not_interested_in",
            df=posts_you_re_not_interested_in_df(file_input),
            title={"en": "posts_you_re_not_interested_in", "nl": "posts_you_re_not_interested_in"},
        )
        tables.append(posts_you_re_not_interested_in_table)
    except Exception as e:
        #print(f"Skipping posts_you_re_not_interested_in: {e}")
        pass

    # predicted_languages
    try:
        predicted_languages_table = donation_table(
            name="predicted_languages",
            df=predicted_languages_df(file_input),
            title={"en": "predicted_languages", "nl": "predicted_languages"},
        )
        tables.append(predicted_languages_table)
    except Exception as e:
        #print(f"Skipping predicted_languages: {e}")
        pass

    # primary_location
    try:
        primary_location_table = donation_table(
            name="primary_location",
            df=primary_location_df(file_input),
            title={"en": "primary_location", "nl": "primary_location"},
        )
        tables.append(primary_location_table)
    except Exception as e:
        #print(f"Skipping primary_location: {e}")
        pass

    # primary_public_location
    try:
        primary_public_location_table = donation_table(
            name="primary_public_location",
            df=primary_public_location_df(file_input),
            title={"en": "primary_public_location", "nl": "primary_public_location"},
        )
        tables.append(primary_public_location_table)
    except Exception as e:
        #print(f"Skipping primary_public_location: {e}")
        pass

    # privacy_settings
    try:
        privacy_settings_table = donation_table(
            name="privacy_settings",
            df=privacy_settings_df(file_input),
            title={"en": "privacy_settings", "nl": "privacy_settings"},
        )
        tables.append(privacy_settings_table)
    except Exception as e:
        #print(f"Skipping privacy_settings: {e}")
        pass

    # professional_information
    try:
        professional_information_table = donation_table(
            name="professional_information",
            df=professional_information_df(file_input),
            title={"en": "professional_information", "nl": "professional_information"},
        )
        tables.append(professional_information_table)
    except Exception as e:
        #print(f"Skipping professional_information: {e}")
        pass

    # profile_based_in
    try:
        profile_based_in_table = donation_table(
            name="profile_based_in",
            df=profile_based_in_df(file_input),
            title={"en": "profile_based_in", "nl": "profile_based_in"},
        )
        tables.append(profile_based_in_table)
    except Exception as e:
        #print(f"Skipping profile_based_in: {e}")
        pass

    # profile_changes
    try:
        profile_changes_table = donation_table(
            name="profile_changes",
            df=profile_changes_df(file_input),
            title={"en": "profile_changes", "nl": "profile_changes"},
        )
        tables.append(profile_changes_table)
    except Exception as e:
        #print(f"Skipping profile_changes: {e}")
        pass

    # profile_information
    try:
        profile_information_table = donation_table(
            name="profile_information",
            df=profile_information_df(file_input),
            title={"en": "profile_information", "nl": "profile_information"},
        )
        tables.append(profile_information_table)
    except Exception as e:
        #print(f"Skipping profile_information: {e}")
        pass

    # profile_photos
    try:
        profile_photos_table = donation_table(
            name="profile_photos",
            df=profile_photos_df(file_input),
            title={"en": "profile_photos", "nl": "profile_photos"},
        )
        tables.append(profile_photos_table)
    except Exception as e:
        #print(f"Skipping profile_photos: {e}")
        pass

    # profile_privacy_changes
    try:
        profile_privacy_changes_table = donation_table(
            name="profile_privacy_changes",
            df=profile_privacy_changes_df(file_input),
            title={"en": "profile_privacy_changes", "nl": "profile_privacy_changes"},
        )
        tables.append(profile_privacy_changes_table)
    except Exception as e:
        #print(f"Skipping profile_privacy_changes: {e}")
        pass

    # profile_searches
    try:
        profile_searches_table = donation_table(
            name="profile_searches",
            df=profile_searches_df(file_input),
            title={"en": "profile_searches", "nl": "profile_searches"},
        )
        tables.append(profile_searches_table)
    except Exception as e:
        #print(f"Skipping profile_searches: {e}")
        pass

    # profile_status_changes
    try:
        profile_status_changes_table = donation_table(
            name="profile_status_changes",
            df=profile_status_changes_df(file_input),
            title={"en": "profile_status_changes", "nl": "profile_status_changes"},
        )
        tables.append(profile_status_changes_table)
    except Exception as e:
        #print(f"Skipping profile_status_changes: {e}")
        pass

    # profile_update_history
    try:
        profile_update_history_table = donation_table(
            name="profile_update_history",
            df=profile_update_history_df(file_input),
            title={"en": "profile_update_history", "nl": "profile_update_history"},
        )
        tables.append(profile_update_history_table)
    except Exception as e:
        #print(f"Skipping profile_update_history: {e}")
        pass

    # profiles_you_re_not_interested_in
    try:
        profiles_you_re_not_interested_in_table = donation_table(
            name="profiles_you_re_not_interested_in",
            df=profiles_you_re_not_interested_in_df(file_input),
            title={"en": "profiles_you_re_not_interested_in", "nl": "profiles_you_re_not_interested_in"},
        )
        tables.append(profiles_you_re_not_interested_in_table)
    except Exception as e:
        #print(f"Skipping profiles_you_re_not_interested_in: {e}")
        pass

    # questions
    try:
        questions_table = donation_table(
            name="questions",
            df=questions_df(file_input),
            title={"en": "questions", "nl": "questions"},
        )
        tables.append(questions_table)
    except Exception as e:
        #print(f"Skipping questions: {e}")
        pass

    # quizzes
    try:
        quizzes_table = donation_table(
            name="quizzes",
            df=quizzes_df(file_input),
            title={"en": "quizzes", "nl": "quizzes"},
        )
        tables.append(quizzes_table)
    except Exception as e:
        #print(f"Skipping quizzes: {e}")
        pass

    # recent_follow_requests
    try:
        recent_follow_requests_table = donation_table(
            name="recent_follow_requests",
            df=recent_follow_requests_df(file_input),
            title={"en": "recent_follow_requests", "nl": "recent_follow_requests"},
        )
        tables.append(recent_follow_requests_table)
    except Exception as e:
        #print(f"Skipping recent_follow_requests: {e}")
        pass

    # recently_deleted_content
    try:
        recently_deleted_content_table = donation_table(
            name="recently_deleted_content",
            df=recently_deleted_content_df(file_input),
            title={"en": "recently_deleted_content", "nl": "recently_deleted_content"},
        )
        tables.append(recently_deleted_content_table)
    except Exception as e:
        #print(f"Skipping recently_deleted_content: {e}")
        pass

    # recently_unfollowed_profiles
    try:
        recently_unfollowed_profiles_table = donation_table(
            name="recently_unfollowed_profiles",
            df=recently_unfollowed_profiles_df(file_input),
            title={"en": "recently_unfollowed_profiles", "nl": "recently_unfollowed_profiles"},
        )
        tables.append(recently_unfollowed_profiles_table)
    except Exception as e:
        #print(f"Skipping recently_unfollowed_profiles: {e}")
        pass

    # recently_viewed
    try:
        recently_viewed_table = donation_table(
            name="recently_viewed",
            df=recently_viewed_df(file_input),
            title={"en": "recently_viewed", "nl": "recently_viewed"},
        )
        tables.append(recently_viewed_table)
    except Exception as e:
        #print(f"Skipping recently_viewed: {e}")
        pass

    # recently_visited
    try:
        recently_visited_table = donation_table(
            name="recently_visited",
            df=recently_visited_df(file_input),
            title={"en": "recently_visited", "nl": "recently_visited"},
        )
        tables.append(recently_visited_table)
    except Exception as e:
        #print(f"Skipping recently_visited: {e}")
        pass

    # recognized_devices
    try:
        recognized_devices_table = donation_table(
            name="recognized_devices",
            df=recognized_devices_df(file_input),
            title={"en": "recognized_devices", "nl": "recognized_devices"},
        )
        tables.append(recognized_devices_table)
    except Exception as e:
        #print(f"Skipping recognized_devices: {e}")
        pass

    # recommended_topics
    try:
        recommended_topics_table = donation_table(
            name="recommended_topics",
            df=recommended_topics_df(file_input),
            title={"en": "recommended_topics", "nl": "recommended_topics"},
        )
        tables.append(recommended_topics_table)
    except Exception as e:
        #print(f"Skipping recommended_topics: {e}")
        pass

    # record_details
    try:
        record_details_table = donation_table(
            name="record_details",
            df=record_details_df(file_input),
            title={"en": "record_details", "nl": "record_details"},
        )
        tables.append(record_details_table)
    except Exception as e:
        #print(f"Skipping record_details: {e}")
        pass

    # reels
    try:
        reels_table = donation_table(
            name="reels",
            df=reels_df(file_input),
            title={"en": "reels", "nl": "reels"},
        )
        tables.append(reels_table)
    except Exception as e:
        #print(f"Skipping reels: {e}")
        pass

    # reels_comments
    try:
        reels_comments_table = donation_table(
            name="reels_comments",
            df=reels_comments_df(file_input),
            title={"en": "reels_comments", "nl": "reels_comments"},
        )
        tables.append(reels_comments_table)
    except Exception as e:
        #print(f"Skipping reels_comments: {e}")
        pass

    # reels_preferences
    try:
        reels_preferences_table = donation_table(
            name="reels_preferences",
            df=reels_preferences_df(file_input),
            title={"en": "reels_preferences", "nl": "reels_preferences"},
        )
        tables.append(reels_preferences_table)
    except Exception as e:
        #print(f"Skipping reels_preferences: {e}")
        pass

    # rejected_friend_requests
    try:
        rejected_friend_requests_table = donation_table(
            name="rejected_friend_requests",
            df=rejected_friend_requests_df(file_input),
            title={"en": "rejected_friend_requests", "nl": "rejected_friend_requests"},
        )
        tables.append(rejected_friend_requests_table)
    except Exception as e:
        #print(f"Skipping rejected_friend_requests: {e}")
        pass

    # removed_friends
    try:
        removed_friends_table = donation_table(
            name="removed_friends",
            df=removed_friends_df(file_input),
            title={"en": "removed_friends", "nl": "removed_friends"},
        )
        tables.append(removed_friends_table)
    except Exception as e:
        #print(f"Skipping removed_friends: {e}")
        pass

    # removed_suggestions
    try:
        removed_suggestions_table = donation_table(
            name="removed_suggestions",
            df=removed_suggestions_df(file_input),
            title={"en": "removed_suggestions", "nl": "removed_suggestions"},
        )
        tables.append(removed_suggestions_table)
    except Exception as e:
        #print(f"Skipping removed_suggestions: {e}")
        pass

    # reshare_education
    try:
        reshare_education_table = donation_table(
            name="reshare_education",
            df=reshare_education_df(file_input),
            title={"en": "reshare_education", "nl": "reshare_education"},
        )
        tables.append(reshare_education_table)
    except Exception as e:
        #print(f"Skipping reshare_education: {e}")
        pass

    # saved_collections
    try:
        saved_collections_table = donation_table(
            name="saved_collections",
            df=saved_collections_df(file_input),
            title={"en": "saved_collections", "nl": "saved_collections"},
        )
        tables.append(saved_collections_table)
    except Exception as e:
        #print(f"Skipping saved_collections: {e}")
        pass

    # saved_posts
    try:
        saved_posts_table = donation_table(
            name="saved_posts",
            df=saved_posts_df(file_input),
            title={"en": "saved_posts", "nl": "saved_posts"},
        )
        tables.append(saved_posts_table)
    except Exception as e:
        #print(f"Skipping saved_posts: {e}")
        pass

    # secret_conversations
    try:
        secret_conversations_table = donation_table(
            name="secret_conversations",
            df=secret_conversations_df(file_input),
            title={"en": "secret_conversations", "nl": "secret_conversations"},
        )
        tables.append(secret_conversations_table)
    except Exception as e:
        #print(f"Skipping secret_conversations: {e}")
        pass

    # sent_friend_requests
    try:
        sent_friend_requests_table = donation_table(
            name="sent_friend_requests",
            df=sent_friend_requests_df(file_input),
            title={"en": "sent_friend_requests", "nl": "sent_friend_requests"},
        )
        tables.append(sent_friend_requests_table)
    except Exception as e:
        #print(f"Skipping sent_friend_requests: {e}")
        pass

    # settings
    try:
        settings_table = donation_table(
            name="settings",
            df=settings_df(file_input),
            title={"en": "settings", "nl": "settings"},
        )
        tables.append(settings_table)
    except Exception as e:
        #print(f"Skipping settings: {e}")
        pass

    # show_exclusive_story_promo_setting
    try:
        show_exclusive_story_promo_setting_table = donation_table(
            name="show_exclusive_story_promo_setting",
            df=show_exclusive_story_promo_setting_df(file_input),
            title={"en": "show_exclusive_story_promo_setting", "nl": "show_exclusive_story_promo_setting"},
        )
        tables.append(show_exclusive_story_promo_setting_table)
    except Exception as e:
        #print(f"Skipping show_exclusive_story_promo_setting: {e}")
        pass

    # signup_details
    try:
        signup_details_table = donation_table(
            name="signup_details",
            df=signup_details_df(file_input),
            title={"en": "signup_details", "nl": "signup_details"},
        )
        tables.append(signup_details_table)
    except Exception as e:
        #print(f"Skipping signup_details: {e}")
        pass

    # stories
    try:
        stories_table = donation_table(
            name="stories",
            df=stories_df(file_input),
            title={"en": "stories", "nl": "stories"},
        )
        tables.append(stories_table)
    except Exception as e:
        #print(f"Skipping stories: {e}")
        pass

    # story_likes
    try:
        story_likes_table = donation_table(
            name="story_likes",
            df=story_likes_df(file_input),
            title={"en": "story_likes", "nl": "story_likes"},
        )
        tables.append(story_likes_table)
    except Exception as e:
        #print(f"Skipping story_likes: {e}")
        pass

    # subscription_for_no_ads
    try:
        subscription_for_no_ads_table = donation_table(
            name="subscription_for_no_ads",
            df=subscription_for_no_ads_df(file_input),
            title={"en": "subscription_for_no_ads", "nl": "subscription_for_no_ads"},
        )
        tables.append(subscription_for_no_ads_table)
    except Exception as e:
        #print(f"Skipping subscription_for_no_ads: {e}")
        pass

    # suggested_friends
    try:
        suggested_friends_table = donation_table(
            name="suggested_friends",
            df=suggested_friends_df(file_input),
            title={"en": "suggested_friends", "nl": "suggested_friends"},
        )
        tables.append(suggested_friends_table)
    except Exception as e:
        #print(f"Skipping suggested_friends: {e}")
        pass

    # suggested_profiles_viewed
    try:
        suggested_profiles_viewed_table = donation_table(
            name="suggested_profiles_viewed",
            df=suggested_profiles_viewed_df(file_input),
            title={"en": "suggested_profiles_viewed", "nl": "suggested_profiles_viewed"},
        )
        tables.append(suggested_profiles_viewed_table)
    except Exception as e:
        #print(f"Skipping suggested_profiles_viewed: {e}")
        pass

    # synced_contacts
    try:
        synced_contacts_table = donation_table(
            name="synced_contacts",
            df=synced_contacts_df(file_input),
            title={"en": "synced_contacts", "nl": "synced_contacts"},
        )
        tables.append(synced_contacts_table)
    except Exception as e:
        #print(f"Skipping synced_contacts: {e}")
        pass

    # synced_contacts_from_instagram
    try:
        synced_contacts_from_instagram_table = donation_table(
            name="synced_contacts_from_instagram",
            df=synced_contacts_from_instagram_df(file_input),
            title={"en": "synced_contacts_from_instagram", "nl": "synced_contacts_from_instagram"},
        )
        tables.append(synced_contacts_from_instagram_table)
    except Exception as e:
        #print(f"Skipping synced_contacts_from_instagram: {e}")
        pass

    # the_ways_we_can_send_you_notifications
    try:
        the_ways_we_can_send_you_notifications_table = donation_table(
            name="the_ways_we_can_send_you_notifications",
            df=the_ways_we_can_send_you_notifications_df(file_input),
            title={"en": "the_ways_we_can_send_you_notifications", "nl": "the_ways_we_can_send_you_notifications"},
        )
        tables.append(the_ways_we_can_send_you_notifications_table)
    except Exception as e:
        #print(f"Skipping the_ways_we_can_send_you_notifications: {e}")
        pass

    # time_spent_on_facebook
    try:
        time_spent_on_facebook_table = donation_table(
            name="time_spent_on_facebook",
            df=time_spent_on_facebook_df(file_input),
            title={"en": "time_spent_on_facebook", "nl": "time_spent_on_facebook"},
        )
        tables.append(time_spent_on_facebook_table)
    except Exception as e:
        #print(f"Skipping time_spent_on_facebook: {e}")
        pass

    # time_spent_on_instagram
    try:
        time_spent_on_instagram_table = donation_table(
            name="time_spent_on_instagram",
            df=time_spent_on_instagram_df(file_input),
            title={"en": "time_spent_on_instagram", "nl": "time_spent_on_instagram"},
        )
        tables.append(time_spent_on_instagram_table)
    except Exception as e:
        #print(f"Skipping time_spent_on_instagram: {e}")
        pass

    # timezone
    try:
        timezone_table = donation_table(
            name="timezone",
            df=timezone_df(file_input),
            title={"en": "timezone", "nl": "timezone"},
        )
        tables.append(timezone_table)
    except Exception as e:
        #print(f"Skipping timezone: {e}")
        pass

    # trusting_frequently_used_devices
    try:
        trusting_frequently_used_devices_table = donation_table(
            name="trusting_frequently_used_devices",
            df=trusting_frequently_used_devices_df(file_input),
            title={"en": "trusting_frequently_used_devices", "nl": "trusting_frequently_used_devices"},
        )
        tables.append(trusting_frequently_used_devices_table)
    except Exception as e:
        #print(f"Skipping trusting_frequently_used_devices: {e}")
        pass

    # two_factor_authentication
    try:
        two_factor_authentication_table = donation_table(
            name="two_factor_authentication",
            df=two_factor_authentication_df(file_input),
            title={"en": "two_factor_authentication", "nl": "two_factor_authentication"},
        )
        tables.append(two_factor_authentication_table)
    except Exception as e:
        #print(f"Skipping two_factor_authentication: {e}")
        pass

    # unfollowed_profiles
    try:
        unfollowed_profiles_table = donation_table(
            name="unfollowed_profiles",
            df=unfollowed_profiles_df(file_input),
            title={"en": "unfollowed_profiles", "nl": "unfollowed_profiles"},
        )
        tables.append(unfollowed_profiles_table)
    except Exception as e:
        #print(f"Skipping unfollowed_profiles: {e}")
        pass

    # use_cross_app_messaging
    try:
        use_cross_app_messaging_table = donation_table(
            name="use_cross_app_messaging",
            df=use_cross_app_messaging_df(file_input),
            title={"en": "use_cross_app_messaging", "nl": "use_cross_app_messaging"},
        )
        tables.append(use_cross_app_messaging_table)
    except Exception as e:
        #print(f"Skipping use_cross_app_messaging: {e}")
        pass

    # videos_watched
    try:
        videos_watched_table = donation_table(
            name="videos_watched",
            df=videos_watched_df(file_input),
            title={"en": "videos_watched", "nl": "videos_watched"},
        )
        tables.append(videos_watched_table)
    except Exception as e:
        #print(f"Skipping videos_watched: {e}")
        pass

    # voting_location
    try:
        voting_location_table = donation_table(
            name="voting_location",
            df=voting_location_df(file_input),
            title={"en": "voting_location", "nl": "voting_location"},
        )
        tables.append(voting_location_table)
    except Exception as e:
        #print(f"Skipping voting_location: {e}")
        pass

    # voting_reminders
    try:
        voting_reminders_table = donation_table(
            name="voting_reminders",
            df=voting_reminders_df(file_input),
            title={"en": "voting_reminders", "nl": "voting_reminders"},
        )
        tables.append(voting_reminders_table)
    except Exception as e:
        #print(f"Skipping voting_reminders: {e}")
        pass

    # weather_forecast_settings
    try:
        weather_forecast_settings_table = donation_table(
            name="weather_forecast_settings",
            df=weather_forecast_settings_df(file_input),
            title={"en": "weather_forecast_settings", "nl": "weather_forecast_settings"},
        )
        tables.append(weather_forecast_settings_table)
    except Exception as e:
        #print(f"Skipping weather_forecast_settings: {e}")
        pass

    # where_you_re_logged_in
    try:
        where_you_re_logged_in_table = donation_table(
            name="where_you_re_logged_in",
            df=where_you_re_logged_in_df(file_input),
            title={"en": "where_you_re_logged_in", "nl": "where_you_re_logged_in"},
        )
        tables.append(where_you_re_logged_in_table)
    except Exception as e:
        #print(f"Skipping where_you_re_logged_in: {e}")
        pass

    # who_you_ve_followed
    try:
        who_you_ve_followed_table = donation_table(
            name="who_you_ve_followed",
            df=who_you_ve_followed_df(file_input),
            title={"en": "who_you_ve_followed", "nl": "who_you_ve_followed"},
        )
        tables.append(who_you_ve_followed_table)
    except Exception as e:
        #print(f"Skipping who_you_ve_followed: {e}")
        pass

    # word_or_phrase_searches
    try:
        word_or_phrase_searches_table = donation_table(
            name="word_or_phrase_searches",
            df=word_or_phrase_searches_df(file_input),
            title={"en": "word_or_phrase_searches", "nl": "word_or_phrase_searches"},
        )
        tables.append(word_or_phrase_searches_table)
    except Exception as e:
        #print(f"Skipping word_or_phrase_searches: {e}")
        pass

    # your_account_password_information
    try:
        your_account_password_information_table = donation_table(
            name="your_account_password_information",
            df=your_account_password_information_df(file_input),
            title={"en": "your_account_password_information", "nl": "your_account_password_information"},
        )
        tables.append(your_account_password_information_table)
    except Exception as e:
        #print(f"Skipping your_account_password_information: {e}")
        pass

    # your_activity
    try:
        your_activity_table = donation_table(
            name="your_activity",
            df=your_activity_df(file_input),
            title={"en": "your_activity", "nl": "your_activity"},
        )
        tables.append(your_activity_table)
    except Exception as e:
        #print(f"Skipping your_activity: {e}")
        pass

    # your_activity_off_meta_technologies
    try:
        your_activity_off_meta_technologies_table = donation_table(
            name="your_activity_off_meta_technologies",
            df=your_activity_off_meta_technologies_df(file_input),
            title={"en": "your_activity_off_meta_technologies", "nl": "your_activity_off_meta_technologies"},
        )
        tables.append(your_activity_off_meta_technologies_table)
    except Exception as e:
        #print(f"Skipping your_activity_off_meta_technologies: {e}")
        pass

    # your_activity_off_meta_technologies_settings
    try:
        your_activity_off_meta_technologies_settings_table = donation_table(
            name="your_activity_off_meta_technologies_settings",
            df=your_activity_off_meta_technologies_settings_df(file_input),
            title={"en": "your_activity_off_meta_technologies_settings", "nl": "your_activity_off_meta_technologies_settings"},
        )
        tables.append(your_activity_off_meta_technologies_settings_table)
    except Exception as e:
        #print(f"Skipping your_activity_off_meta_technologies_settings: {e}")
        pass

    # your_apps
    try:
        your_apps_table = donation_table(
            name="your_apps",
            df=your_apps_df(file_input),
            title={"en": "your_apps", "nl": "your_apps"},
        )
        tables.append(your_apps_table)
    except Exception as e:
        #print(f"Skipping your_apps: {e}")
        pass

    # your_badges
    try:
        your_badges_table = donation_table(
            name="your_badges",
            df=your_badges_df(file_input),
            title={"en": "your_badges", "nl": "your_badges"},
        )
        tables.append(your_badges_table)
    except Exception as e:
        #print(f"Skipping your_badges: {e}")
        pass

    # your_comment_edits
    try:
        your_comment_edits_table = donation_table(
            name="your_comment_edits",
            df=your_comment_edits_df(file_input),
            title={"en": "your_comment_edits", "nl": "your_comment_edits"},
        )
        tables.append(your_comment_edits_table)
    except Exception as e:
        #print(f"Skipping your_comment_edits: {e}")
        pass

    # your_comments_in_groups
    try:
        your_comments_in_groups_table = donation_table(
            name="your_comments_in_groups",
            df=your_comments_in_groups_df(file_input),
            title={"en": "your_comments_in_groups", "nl": "your_comments_in_groups"},
        )
        tables.append(your_comments_in_groups_table)
    except Exception as e:
        #print(f"Skipping your_comments_in_groups: {e}")
        pass

    # your_consent_settings
    try:
        your_consent_settings_table = donation_table(
            name="your_consent_settings",
            df=your_consent_settings_df(file_input),
            title={"en": "your_consent_settings", "nl": "your_consent_settings"},
        )
        tables.append(your_consent_settings_table)
    except Exception as e:
        #print(f"Skipping your_consent_settings: {e}")
        pass

    # your_content_visibility_notification_history
    try:
        your_content_visibility_notification_history_table = donation_table(
            name="your_content_visibility_notification_history",
            df=your_content_visibility_notification_history_df(file_input),
            title={"en": "your_content_visibility_notification_history", "nl": "your_content_visibility_notification_history"},
        )
        tables.append(your_content_visibility_notification_history_table)
    except Exception as e:
        #print(f"Skipping your_content_visibility_notification_history: {e}")
        pass

    # your_device_push_settings
    try:
        your_device_push_settings_table = donation_table(
            name="your_device_push_settings",
            df=your_device_push_settings_df(file_input),
            title={"en": "your_device_push_settings", "nl": "your_device_push_settings"},
        )
        tables.append(your_device_push_settings_table)
    except Exception as e:
        #print(f"Skipping your_device_push_settings: {e}")
        pass

    # your_devices
    try:
        your_devices_table = donation_table(
            name="your_devices",
            df=your_devices_df(file_input),
            title={"en": "your_devices", "nl": "your_devices"},
        )
        tables.append(your_devices_table)
    except Exception as e:
        #print(f"Skipping your_devices: {e}")
        pass

    # your_document_revision
    try:
        your_document_revision_table = donation_table(
            name="your_document_revision",
            df=your_document_revision_df(file_input),
            title={"en": "your_document_revision", "nl": "your_document_revision"},
        )
        tables.append(your_document_revision_table)
    except Exception as e:
        #print(f"Skipping your_document_revision: {e}")
        pass

    # your_educational_notification_interactions
    try:
        your_educational_notification_interactions_table = donation_table(
            name="your_educational_notification_interactions",
            df=your_educational_notification_interactions_df(file_input),
            title={"en": "your_educational_notification_interactions", "nl": "your_educational_notification_interactions"},
        )
        tables.append(your_educational_notification_interactions_table)
    except Exception as e:
        #print(f"Skipping your_educational_notification_interactions: {e}")
        pass

    # your_event_invitation_links
    try:
        your_event_invitation_links_table = donation_table(
            name="your_event_invitation_links",
            df=your_event_invitation_links_df(file_input),
            title={"en": "your_event_invitation_links", "nl": "your_event_invitation_links"},
        )
        tables.append(your_event_invitation_links_table)
    except Exception as e:
        #print(f"Skipping your_event_invitation_links: {e}")
        pass

    # your_event_responses
    try:
        your_event_responses_table = donation_table(
            name="your_event_responses",
            df=your_event_responses_df(file_input),
            title={"en": "your_event_responses", "nl": "your_event_responses"},
        )
        tables.append(your_event_responses_table)
    except Exception as e:
        #print(f"Skipping your_event_responses: {e}")
        pass

    # your_events
    try:
        your_events_table = donation_table(
            name="your_events",
            df=your_events_df(file_input),
            title={"en": "your_events", "nl": "your_events"},
        )
        tables.append(your_events_table)
    except Exception as e:
        #print(f"Skipping your_events: {e}")
        pass

    # your_experiences
    try:
        your_experiences_table = donation_table(
            name="your_experiences",
            df=your_experiences_df(file_input),
            title={"en": "your_experiences", "nl": "your_experiences"},
        )
        tables.append(your_experiences_table)
    except Exception as e:
        #print(f"Skipping your_experiences: {e}")
        pass

    # your_facebook_activity_history
    try:
        your_facebook_activity_history_table = donation_table(
            name="your_facebook_activity_history",
            df=your_facebook_activity_history_df(file_input),
            title={"en": "your_facebook_activity_history", "nl": "your_facebook_activity_history"},
        )
        tables.append(your_facebook_activity_history_table)
    except Exception as e:
        #print(f"Skipping your_facebook_activity_history: {e}")
        pass

    # your_facebook_story_preferences
    try:
        your_facebook_story_preferences_table = donation_table(
            name="your_facebook_story_preferences",
            df=your_facebook_story_preferences_df(file_input),
            title={"en": "your_facebook_story_preferences", "nl": "your_facebook_story_preferences"},
        )
        tables.append(your_facebook_story_preferences_table)
    except Exception as e:
        #print(f"Skipping your_facebook_story_preferences: {e}")
        pass

    # your_facebook_watch_activity_in_the_last_28_days
    try:
        your_facebook_watch_activity_in_the_last_28_days_table = donation_table(
            name="your_facebook_watch_activity_in_the_last_28_days",
            df=your_facebook_watch_activity_in_the_last_28_days_df(file_input),
            title={"en": "your_facebook_watch_activity_in_the_last_28_days", "nl": "your_facebook_watch_activity_in_the_last_28_days"},
        )
        tables.append(your_facebook_watch_activity_in_the_last_28_days_table)
    except Exception as e:
        #print(f"Skipping your_facebook_watch_activity_in_the_last_28_days: {e}")
        pass

    # your_friends
    try:
        your_friends_table = donation_table(
            name="your_friends",
            df=your_friends_df(file_input),
            title={"en": "your_friends", "nl": "your_friends"},
        )
        tables.append(your_friends_table)
    except Exception as e:
        #print(f"Skipping your_friends: {e}")
        pass

    # your_fundraiser_donations_information
    try:
        your_fundraiser_donations_information_table = donation_table(
            name="your_fundraiser_donations_information",
            df=your_fundraiser_donations_information_df(file_input),
            title={"en": "your_fundraiser_donations_information", "nl": "your_fundraiser_donations_information"},
        )
        tables.append(your_fundraiser_donations_information_table)
    except Exception as e:
        #print(f"Skipping your_fundraiser_donations_information: {e}")
        pass

    # your_fundraiser_settings
    try:
        your_fundraiser_settings_table = donation_table(
            name="your_fundraiser_settings",
            df=your_fundraiser_settings_df(file_input),
            title={"en": "your_fundraiser_settings", "nl": "your_fundraiser_settings"},
        )
        tables.append(your_fundraiser_settings_table)
    except Exception as e:
        #print(f"Skipping your_fundraiser_settings: {e}")
        pass

    # your_group_membership_activity
    try:
        your_group_membership_activity_table = donation_table(
            name="your_group_membership_activity",
            df=your_group_membership_activity_df(file_input),
            title={"en": "your_group_membership_activity", "nl": "your_group_membership_activity"},
        )
        tables.append(your_group_membership_activity_table)
    except Exception as e:
        #print(f"Skipping your_group_membership_activity: {e}")
        pass

    # your_group_shortcuts
    try:
        your_group_shortcuts_table = donation_table(
            name="your_group_shortcuts",
            df=your_group_shortcuts_df(file_input),
            title={"en": "your_group_shortcuts", "nl": "your_group_shortcuts"},
        )
        tables.append(your_group_shortcuts_table)
    except Exception as e:
        #print(f"Skipping your_group_shortcuts: {e}")
        pass

    # your_groups
    try:
        your_groups_table = donation_table(
            name="your_groups",
            df=your_groups_df(file_input),
            title={"en": "your_groups", "nl": "your_groups"},
        )
        tables.append(your_groups_table)
    except Exception as e:
        #print(f"Skipping your_groups: {e}")
        pass

    # your_in_app_messages_interactions
    try:
        your_in_app_messages_interactions_table = donation_table(
            name="your_in_app_messages_interactions",
            df=your_in_app_messages_interactions_df(file_input),
            title={"en": "your_in_app_messages_interactions", "nl": "your_in_app_messages_interactions"},
        )
        tables.append(your_in_app_messages_interactions_table)
    except Exception as e:
        #print(f"Skipping your_in_app_messages_interactions: {e}")
        pass

    # your_information_download_requests
    try:
        your_information_download_requests_table = donation_table(
            name="your_information_download_requests",
            df=your_information_download_requests_df(file_input),
            title={"en": "your_information_download_requests", "nl": "your_information_download_requests"},
        )
        tables.append(your_information_download_requests_table)
    except Exception as e:
        #print(f"Skipping your_information_download_requests: {e}")
        pass

    # your_marketplace_assistant_settings
    try:
        your_marketplace_assistant_settings_table = donation_table(
            name="your_marketplace_assistant_settings",
            df=your_marketplace_assistant_settings_df(file_input),
            title={"en": "your_marketplace_assistant_settings", "nl": "your_marketplace_assistant_settings"},
        )
        tables.append(your_marketplace_assistant_settings_table)
    except Exception as e:
        #print(f"Skipping your_marketplace_assistant_settings: {e}")
        pass

    # your_marketplace_device_history
    try:
        your_marketplace_device_history_table = donation_table(
            name="your_marketplace_device_history",
            df=your_marketplace_device_history_df(file_input),
            title={"en": "your_marketplace_device_history", "nl": "your_marketplace_device_history"},
        )
        tables.append(your_marketplace_device_history_table)
    except Exception as e:
        #print(f"Skipping your_marketplace_device_history: {e}")
        pass

    # your_media_permissions
    try:
        your_media_permissions_table = donation_table(
            name="your_media_permissions",
            df=your_media_permissions_df(file_input),
            title={"en": "your_media_permissions", "nl": "your_media_permissions"},
        )
        tables.append(your_media_permissions_table)
    except Exception as e:
        #print(f"Skipping your_media_permissions: {e}")
        pass

    # your_meta_business_suite_guidance_interactions
    try:
        your_meta_business_suite_guidance_interactions_table = donation_table(
            name="your_meta_business_suite_guidance_interactions",
            df=your_meta_business_suite_guidance_interactions_df(file_input),
            title={"en": "your_meta_business_suite_guidance_interactions", "nl": "your_meta_business_suite_guidance_interactions"},
        )
        tables.append(your_meta_business_suite_guidance_interactions_table)
    except Exception as e:
        #print(f"Skipping your_meta_business_suite_guidance_interactions: {e}")
        pass

    # your_muted_story_teaser_creators
    try:
        your_muted_story_teaser_creators_table = donation_table(
            name="your_muted_story_teaser_creators",
            df=your_muted_story_teaser_creators_df(file_input),
            title={"en": "your_muted_story_teaser_creators", "nl": "your_muted_story_teaser_creators"},
        )
        tables.append(your_muted_story_teaser_creators_table)
    except Exception as e:
        #print(f"Skipping your_muted_story_teaser_creators: {e}")
        pass

    # your_notification_status
    try:
        your_notification_status_table = donation_table(
            name="your_notification_status",
            df=your_notification_status_df(file_input),
            title={"en": "your_notification_status", "nl": "your_notification_status"},
        )
        tables.append(your_notification_status_table)
    except Exception as e:
        #print(f"Skipping your_notification_status: {e}")
        pass

    # your_notifications_tab_activity
    try:
        your_notifications_tab_activity_table = donation_table(
            name="your_notifications_tab_activity",
            df=your_notifications_tab_activity_df(file_input),
            title={"en": "your_notifications_tab_activity", "nl": "your_notifications_tab_activity"},
        )
        tables.append(your_notifications_tab_activity_table)
    except Exception as e:
        #print(f"Skipping your_notifications_tab_activity: {e}")
        pass

    # your_pages_mentions
    try:
        your_pages_mentions_table = donation_table(
            name="your_pages_mentions",
            df=your_pages_mentions_df(file_input),
            title={"en": "your_pages_mentions", "nl": "your_pages_mentions"},
        )
        tables.append(your_pages_mentions_table)
    except Exception as e:
        #print(f"Skipping your_pages_mentions: {e}")
        pass

    # your_payment_account_activity_history
    try:
        your_payment_account_activity_history_table = donation_table(
            name="your_payment_account_activity_history",
            df=your_payment_account_activity_history_df(file_input),
            title={"en": "your_payment_account_activity_history", "nl": "your_payment_account_activity_history"},
        )
        tables.append(your_payment_account_activity_history_table)
    except Exception as e:
        #print(f"Skipping your_payment_account_activity_history: {e}")
        pass

    # your_poll_votes
    try:
        your_poll_votes_table = donation_table(
            name="your_poll_votes",
            df=your_poll_votes_df(file_input),
            title={"en": "your_poll_votes", "nl": "your_poll_votes"},
        )
        tables.append(your_poll_votes_table)
    except Exception as e:
        #print(f"Skipping your_poll_votes: {e}")
        pass

    # your_post_audiences
    try:
        your_post_audiences_table = donation_table(
            name="your_post_audiences",
            df=your_post_audiences_df(file_input),
            title={"en": "your_post_audiences", "nl": "your_post_audiences"},
        )
        tables.append(your_post_audiences_table)
    except Exception as e:
        #print(f"Skipping your_post_audiences: {e}")
        pass

    # your_post_composer_settings
    try:
        your_post_composer_settings_table = donation_table(
            name="your_post_composer_settings",
            df=your_post_composer_settings_df(file_input),
            title={"en": "your_post_composer_settings", "nl": "your_post_composer_settings"},
        )
        tables.append(your_post_composer_settings_table)
    except Exception as e:
        #print(f"Skipping your_post_composer_settings: {e}")
        pass

    # your_posts__check_ins__photos_and_videos_1
    try:
        your_posts__check_ins__photos_and_videos_1_table = donation_table(
            name="your_posts__check_ins__photos_and_videos_1",
            df=your_posts__check_ins__photos_and_videos_1_df(file_input),
            title={"en": "your_posts__check_ins__photos_and_videos_1", "nl": "your_posts__check_ins__photos_and_videos_1"},
        )
        tables.append(your_posts__check_ins__photos_and_videos_1_table)
    except Exception as e:
        #print(f"Skipping your_posts__check_ins__photos_and_videos_1: {e}")
        pass

    # your_privacy_jurisdiction
    try:
        your_privacy_jurisdiction_table = donation_table(
            name="your_privacy_jurisdiction",
            df=your_privacy_jurisdiction_df(file_input),
            title={"en": "your_privacy_jurisdiction", "nl": "your_privacy_jurisdiction"},
        )
        tables.append(your_privacy_jurisdiction_table)
    except Exception as e:
        #print(f"Skipping your_privacy_jurisdiction: {e}")
        pass

    # your_recent_account_recovery_successes
    try:
        your_recent_account_recovery_successes_table = donation_table(
            name="your_recent_account_recovery_successes",
            df=your_recent_account_recovery_successes_df(file_input),
            title={"en": "your_recent_account_recovery_successes", "nl": "your_recent_account_recovery_successes"},
        )
        tables.append(your_recent_account_recovery_successes_table)
    except Exception as e:
        #print(f"Skipping your_recent_account_recovery_successes: {e}")
        pass

    # your_recently_followed_history
    try:
        your_recently_followed_history_table = donation_table(
            name="your_recently_followed_history",
            df=your_recently_followed_history_df(file_input),
            title={"en": "your_recently_followed_history", "nl": "your_recently_followed_history"},
        )
        tables.append(your_recently_followed_history_table)
    except Exception as e:
        #print(f"Skipping your_recently_followed_history: {e}")
        pass

    # your_recently_used_emojis
    try:
        your_recently_used_emojis_table = donation_table(
            name="your_recently_used_emojis",
            df=your_recently_used_emojis_df(file_input),
            title={"en": "your_recently_used_emojis", "nl": "your_recently_used_emojis"},
        )
        tables.append(your_recently_used_emojis_table)
    except Exception as e:
        #print(f"Skipping your_recently_used_emojis: {e}")
        pass

    # your_sampled_locations
    try:
        your_sampled_locations_table = donation_table(
            name="your_sampled_locations",
            df=your_sampled_locations_df(file_input),
            title={"en": "your_sampled_locations", "nl": "your_sampled_locations"},
        )
        tables.append(your_sampled_locations_table)
    except Exception as e:
        #print(f"Skipping your_sampled_locations: {e}")
        pass

    # your_saved_items
    try:
        your_saved_items_table = donation_table(
            name="your_saved_items",
            df=your_saved_items_df(file_input),
            title={"en": "your_saved_items", "nl": "your_saved_items"},
        )
        tables.append(your_saved_items_table)
    except Exception as e:
        #print(f"Skipping your_saved_items: {e}")
        pass

    # your_search_history
    try:
        your_search_history_table = donation_table(
            name="your_search_history",
            df=your_search_history_df(file_input),
            title={"en": "your_search_history", "nl": "your_search_history"},
        )
        tables.append(your_search_history_table)
    except Exception as e:
        #print(f"Skipping your_search_history: {e}")
        pass

    # your_settings_for_groups_tab
    try:
        your_settings_for_groups_tab_table = donation_table(
            name="your_settings_for_groups_tab",
            df=your_settings_for_groups_tab_df(file_input),
            title={"en": "your_settings_for_groups_tab", "nl": "your_settings_for_groups_tab"},
        )
        tables.append(your_settings_for_groups_tab_table)
    except Exception as e:
        #print(f"Skipping your_settings_for_groups_tab: {e}")
        pass

    # your_story_highlights
    try:
        your_story_highlights_table = donation_table(
            name="your_story_highlights",
            df=your_story_highlights_df(file_input),
            title={"en": "your_story_highlights", "nl": "your_story_highlights"},
        )
        tables.append(your_story_highlights_table)
    except Exception as e:
        #print(f"Skipping your_story_highlights: {e}")
        pass

    # your_tab_notifications
    try:
        your_tab_notifications_table = donation_table(
            name="your_tab_notifications",
            df=your_tab_notifications_df(file_input),
            title={"en": "your_tab_notifications", "nl": "your_tab_notifications"},
        )
        tables.append(your_tab_notifications_table)
    except Exception as e:
        #print(f"Skipping your_tab_notifications: {e}")
        pass

    # your_topics
    try:
        your_topics_table = donation_table(
            name="your_topics",
            df=your_topics_df(file_input),
            title={"en": "your_topics", "nl": "your_topics"},
        )
        tables.append(your_topics_table)
    except Exception as e:
        #print(f"Skipping your_topics: {e}")
        pass

    # your_transaction_survey_information
    try:
        your_transaction_survey_information_table = donation_table(
            name="your_transaction_survey_information",
            df=your_transaction_survey_information_df(file_input),
            title={"en": "your_transaction_survey_information", "nl": "your_transaction_survey_information"},
        )
        tables.append(your_transaction_survey_information_table)
    except Exception as e:
        #print(f"Skipping your_transaction_survey_information: {e}")
        pass

    # your_uncategorized_photos
    try:
        your_uncategorized_photos_table = donation_table(
            name="your_uncategorized_photos",
            df=your_uncategorized_photos_df(file_input),
            title={"en": "your_uncategorized_photos", "nl": "your_uncategorized_photos"},
        )
        tables.append(your_uncategorized_photos_table)
    except Exception as e:
        #print(f"Skipping your_uncategorized_photos: {e}")
        pass

    # your_videos
    try:
        your_videos_table = donation_table(
            name="your_videos",
            df=your_videos_df(file_input),
            title={"en": "your_videos", "nl": "your_videos"},
        )
        tables.append(your_videos_table)
    except Exception as e:
        #print(f"Skipping your_videos: {e}")
        pass

    # your_watch_settings
    try:
        your_watch_settings_table = donation_table(
            name="your_watch_settings",
            df=your_watch_settings_df(file_input),
            title={"en": "your_watch_settings", "nl": "your_watch_settings"},
        )
        tables.append(your_watch_settings_table)
    except Exception as e:
        #print(f"Skipping your_watch_settings: {e}")
        pass

    # Only create the donation flow if we have at least one table
    if tables:
        return donation_flow(
            id="instagram",
            tables=tables
        )
    else:
        #print("No tables could be generated from the provided files")
        return None