
# Auto-generated Facebook extractors

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


def _6179754102079646_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/6179754102079646.json"])

    df = parse_json(data,
        row_path=["$.thread_name"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def _6452840174763366_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/6452840174763366.json"])

    df = parse_json(data,
        row_path=["$.thread_name"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def _6477893372272082_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/6477893372272082.json"])

    df = parse_json(data,
        row_path=["$.thread_name"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def _6798433430245173_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/6798433430245173.json"])

    df = parse_json(data,
        row_path=["$.thread_name"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def account_activity_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/account_activity.json"])

    print(data)

    df = parse_json(data,
        row_path=["$.account_activity_v2"],
        col_paths=dict(
        action = ['action'],
        city = ['city'],
        country = ['country'],
        ip_address = ['ip_address'],
        port = ['port'],
        region = ['region'],
        site_name = ['site_name'],
        timestamp = ['timestamp'],
        user_agent = ['user_agent'],
        datr_cookie = ['datr_cookie'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def account_recoveries_without_password_changes_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/account_recoveries_without_password_changes.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def activity_summary_about_a_page_or_profile_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/activity_summary_about_a_page_or_profile.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
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


def admin_activity_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/admin_activity.json"])

    df = parse_json(data,
        row_path=["$.timestamp"],
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


def ads_feedback_activity_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/ads_feedback_activity.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
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
        row_path=["$.media"],
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


def advertisers_you_ve_interacted_with_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/advertisers_you've_interacted_with.json"])

    df = parse_json(data,
        row_path=["$.history_v2"],
        col_paths=dict(
        action = ['action'],
        timestamp = ['timestamp'],
        title = ['title'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def archived_stories_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/archived_stories.json"])

    df = parse_json(data,
        row_path=["$.archived_stories_v2"],
        col_paths=dict(
        creation_timestamp = ['attachments.data.media.creation_timestamp'],
        description = ['attachments.data.media.description'],
        dubbing_info = ['attachments.data.media.dubbing_info'],
        video_metadata = ['attachments.data.media.media_metadata.video_metadata'],
        media_variants = ['attachments.data.media.media_variants'],
        title = ['title'],
        uri = ['attachments.data.media.uri'],
        data = ['data'],
        timestamp = ['timestamp'],
        photo_metadata = ['attachments.data.media.media_metadata.photo_metadata'],
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
        COMPANY_NAME = ['COMPANY_NAME'],
        COUNTRY = ['COUNTRY'],
        EMAIL = ['EMAIL'],
        FIRST_NAME = ['FIRST_NAME'],
        FULL_NAME = ['FULL_NAME'],
        GENDER = ['GENDER'],
        JOB_TITLE = ['JOB_TITLE'],
        LAST_NAME = ['LAST_NAME'],
        PHONE = ['PHONE'],
        SLIDER = ['SLIDER'],
        WORK_EMAIL = ['WORK_EMAIL'],
        WORK_PHONE = ['WORK_PHONE'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def avatar_items_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/avatar_items.json"])

    df = parse_json(data,
        row_path=["$.avatar_marketplace_avatar_items"],
        col_paths=dict(
        acquisition_time = ['acquisition_time'],
        item = ['item'],
        type = ['type'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def birthday_media_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/birthday_media.json"])

    df = parse_json(data,
        row_path=["$.timestamp"],
        col_paths=dict(
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
        _T9h____________________ = ['-T9h********************'],
        _2EXn____________________ = ['2EXn********************'],
        _2Yx_____________________ = ['2Yx-********************'],
        _4VrW____________________ = ['4VrW********************'],
        _6XVG____________________ = ['6XVG********************'],
        _7zHx____________________ = ['7zHx********************'],
        _9EXn____________________ = ['9EXn********************'],
        Amjj____________________ = ['Amjj********************'],
        DlJc____________________ = ['DlJc********************'],
        GUaJ____________________ = ['GUaJ********************'],
        Jm9g____________________ = ['Jm9g********************'],
        KQme____________________ = ['KQme********************'],
        LRU_____________________ = ['LRU-********************'],
        URP_____________________ = ['URP-********************'],
        YBle____________________ = ['YBle********************'],
        _Rkn____________________ = ['_Rkn********************'],
        aNdM____________________ = ['aNdM********************'],
        aZGi____________________ = ['aZGi********************'],
        bZaj____________________ = ['bZaj********************'],
        btzT____________________ = ['btzT********************'],
        v5Wj____________________ = ['v5Wj********************'],
        x0Xn____________________ = ['x0Xn********************'],
        zygo____________________ = ['zygo********************'],
        _4KuC____________________ = ['4KuC********************'],
        F_DI____________________ = ['F_DI********************'],
        Nf_T____________________ = ['Nf-T********************'],
        Qrjl____________________ = ['Qrjl********************'],
        S3EK____________________ = ['S3EK********************'],
        eAJa____________________ = ['eAJa********************'],
        iDMA____________________ = ['iDMA********************'],
        yLaM____________________ = ['yLaM********************'],
        _18Z_____________________ = ['18Z_********************'],
        _5DJY____________________ = ['5DJY********************'],
        _6YCp____________________ = ['6YCp********************'],
        _6k_e____________________ = ['6k-e********************'],
        _7AFV____________________ = ['7AFV********************'],
        _7YnB____________________ = ['7YnB********************'],
        _7ehR____________________ = ['7ehR********************'],
        _9c8d____________________ = ['9c8d********************'],
        CAZd____________________ = ['CAZd********************'],
        CX1V____________________ = ['CX1V********************'],
        EyxH____________________ = ['EyxH********************'],
        G6cZ____________________ = ['G6cZ********************'],
        HvPC____________________ = ['HvPC********************'],
        J8ju____________________ = ['J8ju********************'],
        JePr____________________ = ['JePr********************'],
        LM9M____________________ = ['LM9M********************'],
        O2JW____________________ = ['O2JW********************'],
        RNYF____________________ = ['RNYF********************'],
        RUJV____________________ = ['RUJV********************'],
        S1FX____________________ = ['S1FX********************'],
        TG04____________________ = ['TG04********************'],
        TNor____________________ = ['TNor********************'],
        TfVW____________________ = ['TfVW********************'],
        UetU____________________ = ['UetU********************'],
        W6Zg____________________ = ['W6Zg********************'],
        XjHL____________________ = ['XjHL********************'],
        Z_xU____________________ = ['Z_xU********************'],
        __a7____________________ = ['_-a7********************'],
        _bA3____________________ = ['_bA3********************'],
        asU_____________________ = ['asU-********************'],
        azOd____________________ = ['azOd********************'],
        dxFh____________________ = ['dxFh********************'],
        ebWd____________________ = ['ebWd********************'],
        gZ______________________ = ['gZ__********************'],
        hQ8P____________________ = ['hQ8P********************'],
        i1AE____________________ = ['i1AE********************'],
        kQrh____________________ = ['kQrh********************'],
        lI36____________________ = ['lI36********************'],
        lzVQ____________________ = ['lzVQ********************'],
        pORU____________________ = ['pORU********************'],
        sBFO____________________ = ['sBFO********************'],
        u5Se____________________ = ['u5Se********************'],
        zCJo____________________ = ['zCJo********************'],
        zTff____________________ = ['zTff********************'],
        ZmLB____________________ = ['ZmLB********************'],
        nQ2i____________________ = ['nQ2i********************'],
        q76Q____________________ = ['q76Q********************'],
        _3vuC____________________ = ['3vuC********************'],
        _5gPw____________________ = ['5gPw********************'],
        Fl02____________________ = ['Fl02********************'],
        sJMS____________________ = ['sJMS********************'],
        wrzL____________________ = ['wrzL********************'],
        _0R_r____________________ = ['0R-r********************'],
        _4Ktb____________________ = ['4Ktb********************'],
        _4_2q____________________ = ['4_2q********************'],
        _5ZPD____________________ = ['5ZPD********************'],
        _6DYQ____________________ = ['6DYQ********************'],
        _7mWs____________________ = ['7mWs********************'],
        _7zYg____________________ = ['7zYg********************'],
        _9CWj____________________ = ['9CWj********************'],
        _9Kd0____________________ = ['9Kd0********************'],
        _9P3R____________________ = ['9P3R********************'],
        _9YrK____________________ = ['9YrK********************'],
        A_C1____________________ = ['A-C1********************'],
        AjLr____________________ = ['AjLr********************'],
        Brtu____________________ = ['Brtu********************'],
        DyHB____________________ = ['DyHB********************'],
        Fl_T____________________ = ['Fl-T********************'],
        Imus____________________ = ['Imus********************'],
        L9uh____________________ = ['L9uh********************'],
        N0wo____________________ = ['N0wo********************'],
        Ojv0____________________ = ['Ojv0********************'],
        Osgw____________________ = ['Osgw********************'],
        OvnT____________________ = ['OvnT********************'],
        PedU____________________ = ['PedU********************'],
        Pf4x____________________ = ['Pf4x********************'],
        Qyyn____________________ = ['Qyyn********************'],
        RYTG____________________ = ['RYTG********************'],
        U4bP____________________ = ['U4bP********************'],
        UP______________________ = ['UP-_********************'],
        UQSS____________________ = ['UQSS********************'],
        WQLx____________________ = ['WQLx********************'],
        Y8K9____________________ = ['Y8K9********************'],
        YvP_____________________ = ['YvP_********************'],
        ZSZy____________________ = ['ZSZy********************'],
        bedU____________________ = ['bedU********************'],
        dRfk____________________ = ['dRfk********************'],
        e6Kc____________________ = ['e6Kc********************'],
        eQXd____________________ = ['eQXd********************'],
        hCPp____________________ = ['hCPp********************'],
        jE2b____________________ = ['jE2b********************'],
        k67A____________________ = ['k67A********************'],
        kK7A____________________ = ['kK7A********************'],
        kk4N____________________ = ['kk4N********************'],
        ky69____________________ = ['ky69********************'],
        pXm5____________________ = ['pXm5********************'],
        phvv____________________ = ['phvv********************'],
        rHKi____________________ = ['rHKi********************'],
        tNv9____________________ = ['tNv9********************'],
        woOG____________________ = ['woOG********************'],
        x8Mo____________________ = ['x8Mo********************'],
        yXfX____________________ = ['yXfX********************'],
        zDqd____________________ = ['zDqd********************'],
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


def chat_invites_received_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/chat_invites_received.json"])

    df = parse_json(data,
        row_path=["$.title"],
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


def collections_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/collections.json"])

    df = parse_json(data,
        row_path=["$.timestamp"],
        col_paths=dict(
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


def community_chat_settings_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/community_chat_settings.json"])

    df = parse_json(data,
        row_path=["$.title"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def community_chats_settings_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/community_chats_settings.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
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


def contacts_uploaded_before_2021_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/contacts_uploaded_before_2021.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def content_sharing_links_you_have_created_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/content_sharing_links_you_have_created.json"])

    df = parse_json(data,
        row_path=["$.timestamp"],
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
        uri = ['entries.data.uri'],
        timestamp = ['entries.timestamp'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def dark_mode_settings_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/dark_mode_settings.json"])

    df = parse_json(data,
        row_path=["$.media"],
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


def edits_you_made_to_posts_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/edits_you_made_to_posts.json"])

    df = parse_json(data,
        row_path=["$.timestamp"],
        col_paths=dict(
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


def facebook_editor_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/facebook_editor.json"])

    df = parse_json(data,
        row_path=["$.facebook_editor"],
        col_paths=dict(
        question_type = ['responses.question_type'],
        timestamp = ['responses.timestamp'],
        title = ['responses.title'],
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


def fundraisers_donated_to_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/fundraisers_donated_to.json"])

    df = parse_json(data,
        row_path=["$.fundraisers_donated_to_v2"],
        col_paths=dict(
        donated_amount = ['attachments.data.fundraiser.donated_amount'],
        title = ['attachments.data.fundraiser.title'],
        timestamp = ['timestamp'],
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


def global_navigation_bar_information_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/global_navigation_bar_information.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def group_invites_you_ve_received_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/group_invites_you've_received.json"])

    df = parse_json(data,
        row_path=["$.timestamp"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def group_invites_you_ve_sent_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/group_invites_you've_sent.json"])

    df = parse_json(data,
        row_path=["$.timestamp"],
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
        post = ['data.post'],
        timestamp = ['timestamp'],
        title = ['title'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def groups_you_ve_visited_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/groups_you've_visited.json"])

    df = parse_json(data,
        row_path=["$.timestamp"],
        col_paths=dict(
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


def information_about_your_devices_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/information_about_your_devices.json"])

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
        row_path=["$.lead_gen_info_v2"],
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


def instant_games_usage_data_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/instant_games_usage_data.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def interactions_with_marketplace_ads_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/interactions_with_marketplace_ads.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
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


def items_sold_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/items_sold.json"])

    df = parse_json(data,
        row_path=["$.items_selling_v2"],
        col_paths=dict(
        category = ['category'],
        created_timestamp = ['created_timestamp'],
        description = ['description'],
        latitude = ['location.coordinate.latitude'],
        longitude = ['location.coordinate.longitude'],
        marketplace = ['marketplace'],
        price = ['price'],
        seller = ['seller'],
        title = ['title'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def join_requests_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/join_requests.json"])

    df = parse_json(data,
        row_path=["$.timestamp"],
        col_paths=dict(
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


def likes_and_reactions_2_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/likes_and_reactions_2.json"])

    df = parse_json(data,
        row_path=["$.timestamp"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def likes_and_reactions_3_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/likes_and_reactions_3.json"])

    df = parse_json(data,
        row_path=["$.timestamp"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def likes_and_reactions_4_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/likes_and_reactions_4.json"])

    df = parse_json(data,
        row_path=["$.timestamp"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def likes_and_reactions_5_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/likes_and_reactions_5.json"])

    df = parse_json(data,
        row_path=["$.timestamp"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def likes_and_reactions_6_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/likes_and_reactions_6.json"])

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


def marketplace_notifications_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/marketplace_notifications.json"])

    df = parse_json(data,
        row_path=["$.marketplace_notifications_v2"],
        col_paths=dict(
        dismissed_28d = ['dismissed_28d'],
        opened_28d = ['opened_28d'],
        sent_28d = ['sent_28d'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def media_used_for_memories_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/media_used_for_memories.json"])

    df = parse_json(data,
        row_path=["$.timestamp"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def memorialization_settings_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/memorialization_settings.json"])

    df = parse_json(data,
        row_path=["$.timestamp"],
        col_paths=dict(
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


def message_2_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/message_2.json"])

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


def messaging_settings_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/messaging_settings.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def messenger_active_status_platform_settings_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/messenger_active_status_platform_settings.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def messenger_active_status_settings_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/messenger_active_status_settings.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def messenger_threads_you_started_by_clicking_on_an_ad_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/messenger_threads_you_started_by_clicking_on_an_ad.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def messenger_ui_settings_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/messenger_ui_settings.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def meta_ad_library_accounts_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/meta_ad_library_accounts.json"])

    df = parse_json(data,
        row_path=["$.timestamp"],
        col_paths=dict(
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
        type = ['type'],
        udid = ['udid'],
        update_time = ['update_time'],
        app_version = ['push_tokens.app_version'],
        client_update_time = ['push_tokens.client_update_time'],
        creation_time = ['push_tokens.creation_time'],
        device_id = ['push_tokens.device_id'],
        disabled = ['push_tokens.disabled'],
        locale = ['push_tokens.locale'],
        os_version = ['push_tokens.os_version'],
        token = ['push_tokens.token'],
        redact_tokens = ['redact_tokens'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def navigation_bar_activity_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/navigation_bar_activity.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
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
        row_path=["$.timestamp"],
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


def pages_and_profiles_you_ve_unfollowed_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/pages_and_profiles_you've_unfollowed.json"])

    df = parse_json(data,
        row_path=["$.pages_unfollowed_v2"],
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


def payment_addresses_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/payment_addresses.json"])

    df = parse_json(data,
        row_path=["$.title"],
        col_paths=dict(
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
        amount = ['payments.amount'],
        created_timestamp = ['payments.created_timestamp'],
        currency = ['payments.currency'],
        ip = ['payments.ip'],
        payment_method = ['payments.payment_method'],
        receiver = ['payments.receiver'],
        sender = ['payments.sender'],
        status = ['payments.status'],
        type = ['payments.type'],
        fees = ['payments.payment_data.p2p_payment.fees'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def payments_you_have_made_as_a_buyer_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/payments_you_have_made_as_a_buyer.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def people_and_friends_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/people_and_friends.json"])

    df = parse_json(data,
        row_path=["$.people_interactions_v2"],
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


def people_we_think_you_should_follow_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/people_we_think_you_should_follow.json"])

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
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def places_you_ve_created_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/places_you've_created.json"])

    df = parse_json(data,
        row_path=["$.timestamp"],
        col_paths=dict(
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
        question = ['attachments.data.poll.question'],
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
        row_path=["primary_public_location_v2"],
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


def profile_information_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/profile_information.json"])

    df = parse_json(data,
        row_path=["$.profile_v2"],
        col_paths=dict(
        day = ['birthday.day'],
        month = ['birthday.month'],
        year = ['birthday.year'],
        name = ['hometown.name'],
        timestamp = ['work_experiences.timestamp'],
        concentrations = ['education_experiences.concentrations'],
        end_timestamp = ['education_experiences.end_timestamp'],
        graduated = ['education_experiences.graduated'],
        school_type = ['education_experiences.school_type'],
        ad_account_emails = ['emails.ad_account_emails'],
        emails = ['emails.emails'],
        pending_emails = ['emails.pending_emails'],
        previous_emails = ['emails.previous_emails'],
        relation = ['family_members.relation'],
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
        websites = ['websites'],
        employer = ['work_experiences.employer'],
        location = ['work_experiences.location'],
        title = ['work_experiences.title'],
        description = ['work_experiences.description'],
        start_timestamp = ['work_experiences.start_timestamp'],
        phone_numbers = ['phone_numbers'],
        address = ['websites.address'],
        work_experiences = ['work_experiences'],
        place = ['places_lived.place'],
        blood_donor_status = ['blood_info.blood_donor_status'],
        degree = ['education_experiences.degree'],
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


def profile_update_history_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/profile_update_history.json"])

    df = parse_json(data,
        row_path=["$.profile_updates_v2"],
        col_paths=dict(
        timestamp = ['timestamp'],
        title = ['title'],
        creation_timestamp = ['attachments.data.media.creation_timestamp'],
        photo_metadata = ['attachments.data.media.media_metadata.photo_metadata'],
        uri = ['attachments.data.media.uri'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def profiles_you_visited_in_the_past_7_days_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/profiles_you_visited_in_the_past_7_days.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
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


def received_friend_requests_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/received_friend_requests.json"])

    df = parse_json(data,
        row_path=["$.received_requests_v2"],
        col_paths=dict(
        name = ['name'],
        timestamp = ['timestamp'],
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
        value = ['children.entries.data.value'],
        name = ['name'],
        uri = ['entries.data.uri'],
        watch_time = ['children.entries.data.watch_time'],
        timestamp = ['entries.timestamp'],
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
        updated_timestamp = ['updated_timestamp'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def recommended_bookmark_info_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/recommended_bookmark_info.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
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
        new_email = ['extra_info.new_email'],
        new_name = ['extra_info.new_name'],
        new_number = ['extra_info.new_number'],
        new_vanity = ['extra_info.new_vanity'],
        old_email = ['extra_info.old_email'],
        old_name = ['extra_info.old_name'],
        old_number = ['extra_info.old_number'],
        old_vanity = ['extra_info.old_vanity'],
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


def rising_fan_badges_you_ve_received_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/rising_fan_badges_you've_received.json"])

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
        row_path=["$.secret_conversations_v2"],
        col_paths=dict(
        device_manufacturer = ['armadillo_devices.device_manufacturer'],
        device_model = ['armadillo_devices.device_model'],
        device_os_version = ['armadillo_devices.device_os_version'],
        device_type = ['armadillo_devices.device_type'],
        last_active_time = ['armadillo_devices.last_active_time'],
        last_connected_ip = ['armadillo_devices.last_connected_ip'],
        calls = ['calls'],
        tincan_devices = ['tincan_devices'],
        has_received_message = ['has_received_message'],
        has_sent_message = ['has_sent_message'],
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


def snooze_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/snooze.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
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


def story_reactions_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/story_reactions.json"])

    df = parse_json(data,
        row_path=["$.stories_feedback_v2"],
        col_paths=dict(
        title = ['title'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def story_views_in_past_7_days_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/story_views_in_past_7_days.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
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


def support_messages_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/support_messages.json"])

    df = parse_json(data,
        row_path=["$.support_messages"],
        col_paths=dict(
        from_ = ['8752122044910884.messages.from'],
        message = ['8752122044910884.messages.message'],
        subject = ['8752122044910884.subject'],
        timestamp = ['8752122044910884.timestamp'],
        to = ['8752122044910884.messages.to'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def surveys_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/surveys.json"])

    df = parse_json(data,
        row_path=["$.timestamp"],
        col_paths=dict(
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


def top_fan_badges_you_ve_received_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/top_fan_badges_you've_received.json"])

    df = parse_json(data,
        row_path=["$.timestamp"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def top_fan_information_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/top_fan_information.json"])

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


def video_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/video.json"])

    df = parse_json(data,
        row_path=["$.watch_videos_v2"],
        col_paths=dict(
        action_time = ['action_time'],
        feedback_collection = ['feedback_collection'],
        user_action = ['user_action'],
        video_title = ['video_title'],
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


def weekly_engagement_list_activity_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/weekly_engagement_list_activity.json"])

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
        session_type = ['session_type'],
        user_agent = ['user_agent'],
        updated_timestamp = ['updated_timestamp'],
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


def your_actions_on_violating_content_in_your_groups_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/your_actions_on_violating_content_in_your_groups.json"])

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


def your_anonymous_mode_status_in_groups_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/your_anonymous_mode_status_in_groups.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def your_answers_to_membership_questions_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/your_answers_to_membership_questions.json"])

    df = parse_json(data,
        row_path=["$.group_membership_questions_answers_v2"],
        col_paths=dict(
        answer = ['group_answers.answers.answer'],
        question = ['group_answers.answers.question'],
        timestamp = ['group_answers.answers.timestamp'],
        group_name = ['group_answers.group_name'],
        rules_agreement = ['group_answers.rules_agreement'],
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


def your_autofill_settings_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/your_autofill_settings.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
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
        Cap_d_Any_Girona_2013_2014 = ["Cap d'Any Girona 2013-2014"],
        Foto_s_barcalonaaa = ["Foto's barcalonaaa"],
        _2022_2023_Research_Methods_master = ['2022-2023_Research_Methods_master'],
        _2023_2024_Research_Methods = ['2023_2024_Research_Methods'],
        Doctorat___Metode_de_cercetare_cantitativa_2024_2025 = ['Doctorat - Metode de cercetare cantitativa 2024-2025'],
        Doctorat_Metode_de_cercetare_cantitativa_2023_2024 = ['Doctorat Metode de cercetare cantitativa 2023-2024'],
        ECREA_Political_Communication_Section = ['ECREA Political Communication Section'],
        Licenta_2018_2019 = ['Licenta 2018-2019'],
        Licenta_Disertatie_2019_2020 = ['Licenta-Disertatie 2019-2020'],
        Metode_de_cercetare_PhD_2020_2021 = ['Metode de cercetare PhD 2020-2021'],
        Metode_de_cercetare_cantitativa_2022_2023 = ['Metode de cercetare cantitativa 2022-2023'],
        Metode_de_cercetare_cantitative___Doctorat_2021_2022 = ['Metode de cercetare cantitative - Doctorat 2021-2022'],
        PhD_SNSPA = ['PhD SNSPA'],
        Research_Methods__master__2021_2022 = ['Research Methods _master_ 2021/2022'],
        Research_Methods_master_2020_2021 = ['Research Methods/master 2020/2021'],
        SNSPA___Scoala_Doctorala_FCRP___2019 = ['SNSPA - Scoala Doctorala FCRP - 2019'],
        Absolvire_2017___2018 = ['Absolvire 2017 - 2018'],
        Absolvire_2019_2020 = ['Absolvire 2019-2020'],
        Cercetare_FCRP = ['Cercetare_FCRP'],
        FCRP_MMS_2016_2017 = ['FCRP_MMS_2016-2017'],
        FCRP_MMS_2017_2018 = ['FCRP_MMS_2017-2018'],
        FCRP_Metode_si_tehnici_de_elaborare_a_lucrarii_de_absolvire = ['FCRP_Metode si tehnici de elaborare a lucrarii de absolvire'],
        FCRP_Metode_si_tehnici_17_18 = ['FCRP_Metode si tehnici_17-18'],
        Lucrare_absolvire = ['Lucrare absolvire'],
        Mass_media_and_society__Emerging_media = ['Mass media and society. Emerging media'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def your_basic_mode_opt_in_status_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/your_basic_mode_opt-in_status.json"])

    df = parse_json(data,
        row_path=["$.timestamp"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def your_comment_active_days_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/your_comment_active_days.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
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


def your_contributions_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/your_contributions.json"])

    df = parse_json(data,
        row_path=["$.title"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def your_cross_app_messaging_settings_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/your_cross-app_messaging_settings.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def your_crowdsourcing_edits_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/your_crowdsourcing_edits.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def your_daily_limit_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/your_daily_limit.json"])

    df = parse_json(data,
        row_path=["$.timestamp"],
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


def your_end_to_end_encryption_enabled_messenger_device_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/your_end-to-end_encryption_enabled_messenger_device.json"])

    df = parse_json(data,
        row_path=["$.timestamp"],
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
        name = ['name'],
        start_timestamp = ['start_timestamp'],
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


def your_group_post_tags_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/your_group_post_tags.json"])

    df = parse_json(data,
        row_path=["$.timestamp"],
        col_paths=dict(
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


def your_imported_contacts_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/your_imported_contacts.json"])

    df = parse_json(data,
        row_path=["$.timestamp"],
        col_paths=dict(
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


def your_inferred_language_preferences_for_videos_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/your_inferred_language_preferences_for_videos.json"])

    df = parse_json(data,
        row_path=["$.media"],
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


def your_instant_games_tournament_information_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/your_instant_games_tournament_information.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def your_language_translation_settings_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/your_language_translation_settings.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def your_locations_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/your_locations.json"])

    df = parse_json(data,
        row_path=["$.news_your_locations_v2"],
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


def your_marketplace_cart_information_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/your_marketplace_cart_information.json"])

    df = parse_json(data,
        row_path=["$.timestamp"],
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


def your_marketplace_listing_history_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/your_marketplace_listing_history.json"])

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


def your_mentions_settings_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/your_mentions_settings.json"])

    df = parse_json(data,
        row_path=["$.timestamp"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def your_messenger_app_install_information_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/your_messenger_app_install_information.json"])

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


def your_page_or_groups_badges_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/your_page_or_groups_badges.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def your_pages_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/your_pages.json"])

    df = parse_json(data,
        row_path=["$.pages_v2"],
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


def your_participation_requests_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/your_participation_requests.json"])

    df = parse_json(data,
        row_path=["$.media"],
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


def your_pending_posts_in_groups_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/your_pending_posts_in_groups.json"])

    df = parse_json(data,
        row_path=["$.pending_posts_v2"],
        col_paths=dict(
        post = ['data.post'],
        timestamp = ['timestamp'],
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


def your_recent_reported_conversions_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/your_recent_reported_conversions.json"])

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


def your_recently_viewed_products_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/your_recently_viewed_products.json"])

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
        name = ['attachments.data.external_context.name'],
        source = ['attachments.data.external_context.source'],
        url = ['attachments.data.external_context.url'],
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
        camera_make = ['media_metadata.photo_metadata.exif_data.camera_make'],
        camera_model = ['media_metadata.photo_metadata.exif_data.camera_model'],
        exposure = ['media_metadata.photo_metadata.exif_data.exposure'],
        f_stop = ['media_metadata.photo_metadata.exif_data.f_stop'],
        focal_length = ['media_metadata.photo_metadata.exif_data.focal_length'],
        iso = ['media_metadata.photo_metadata.exif_data.iso'],
        latitude = ['media_metadata.photo_metadata.exif_data.latitude'],
        longitude = ['media_metadata.photo_metadata.exif_data.longitude'],
        modified_timestamp = ['media_metadata.photo_metadata.exif_data.modified_timestamp'],
        orientation = ['media_metadata.photo_metadata.exif_data.orientation'],
        taken_timestamp = ['media_metadata.photo_metadata.exif_data.taken_timestamp'],
        upload_ip = ['media_metadata.photo_metadata.exif_data.upload_ip'],
        uri = ['uri'],
        description = ['description'],
        backup_uri = ['backup_uri'],
        )
    )

    if "time" in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")

    return df


def your_video_consumption_summary_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/your_video_consumption_summary.json"])

    df = parse_json(data,
        row_path=["$.media"],
        col_paths=dict(
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
    Creates a donation flow for Facebook data, explicitly trying each extractor function.
    Only creates tables for data that's available in the provided files.
    """
    tables = []
    #print(file_input)
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


    # Only create the donation flow if we have at least one table
    if tables:
        return donation_flow(
            id="facebook",
            tables=tables
        )
    else:
        #print("No tables could be generated from the provided files")
        return None
