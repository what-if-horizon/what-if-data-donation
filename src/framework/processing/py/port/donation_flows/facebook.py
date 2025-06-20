
# Auto-generated Facebook extractors

import pandas as pd
import logging
from port.helpers.donation_flow import donation_table, donation_flow
from port.helpers.readers import read_json
from port.helpers.parsers import parse_json

<<<<<<< HEAD
=======
#from port.structure_extractor_libraries.FB_get_json_structure import structure_from_zip
>>>>>>> 25603eab493806c5cf7add24002c9d16f332766a

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

    # _6179754102079646
    try:
        _6179754102079646_table = donation_table(
            name="_6179754102079646",
            df=_6179754102079646_df(file_input),
            title={"en": "_6179754102079646", "nl": "_6179754102079646"},
        )
        tables.append(_6179754102079646_table)
    except Exception as e:
        #print(f"Skipping _6179754102079646: {e}")
        pass

    # _6452840174763366
    try:
        _6452840174763366_table = donation_table(
            name="_6452840174763366",
            df=_6452840174763366_df(file_input),
            title={"en": "_6452840174763366", "nl": "_6452840174763366"},
        )
        tables.append(_6452840174763366_table)
    except Exception as e:
        #print(f"Skipping _6452840174763366: {e}")
        pass

    # _6477893372272082
    try:
        _6477893372272082_table = donation_table(
            name="_6477893372272082",
            df=_6477893372272082_df(file_input),
            title={"en": "_6477893372272082", "nl": "_6477893372272082"},
        )
        tables.append(_6477893372272082_table)
    except Exception as e:
        #print(f"Skipping _6477893372272082: {e}")
        pass

    # _6798433430245173
    try:
        _6798433430245173_table = donation_table(
            name="_6798433430245173",
            df=_6798433430245173_df(file_input),
            title={"en": "_6798433430245173", "nl": "_6798433430245173"},
        )
        tables.append(_6798433430245173_table)
    except Exception as e:
        #print(f"Skipping _6798433430245173: {e}")
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

    # account_recoveries_without_password_changes
    try:
        account_recoveries_without_password_changes_table = donation_table(
            name="account_recoveries_without_password_changes",
            df=account_recoveries_without_password_changes_df(file_input),
            title={"en": "account_recoveries_without_password_changes", "nl": "account_recoveries_without_password_changes"},
        )
        tables.append(account_recoveries_without_password_changes_table)
    except Exception as e:
        #print(f"Skipping account_recoveries_without_password_changes: {e}")
        pass

    # activity_summary_about_a_page_or_profile
    try:
        activity_summary_about_a_page_or_profile_table = donation_table(
            name="activity_summary_about_a_page_or_profile",
            df=activity_summary_about_a_page_or_profile_df(file_input),
            title={"en": "activity_summary_about_a_page_or_profile", "nl": "activity_summary_about_a_page_or_profile"},
        )
        tables.append(activity_summary_about_a_page_or_profile_table)
    except Exception as e:
        #print(f"Skipping activity_summary_about_a_page_or_profile: {e}")
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

    # admin_activity
    try:
        admin_activity_table = donation_table(
            name="admin_activity",
            df=admin_activity_df(file_input),
            title={"en": "admin_activity", "nl": "admin_activity"},
        )
        tables.append(admin_activity_table)
    except Exception as e:
        #print(f"Skipping admin_activity: {e}")
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

    # ads_feedback_activity
    try:
        ads_feedback_activity_table = donation_table(
            name="ads_feedback_activity",
            df=ads_feedback_activity_df(file_input),
            title={"en": "ads_feedback_activity", "nl": "ads_feedback_activity"},
        )
        tables.append(ads_feedback_activity_table)
    except Exception as e:
        #print(f"Skipping ads_feedback_activity: {e}")
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

    # advertisers_you_ve_interacted_with
    try:
        advertisers_you_ve_interacted_with_table = donation_table(
            name="advertisers_you_ve_interacted_with",
            df=advertisers_you_ve_interacted_with_df(file_input),
            title={"en": "advertisers_you_ve_interacted_with", "nl": "advertisers_you_ve_interacted_with"},
        )
        tables.append(advertisers_you_ve_interacted_with_table)
    except Exception as e:
        #print(f"Skipping advertisers_you_ve_interacted_with: {e}")
        pass

    # archived_stories
    try:
        archived_stories_table = donation_table(
            name="archived_stories",
            df=archived_stories_df(file_input),
            title={"en": "archived_stories", "nl": "archived_stories"},
        )
        tables.append(archived_stories_table)
    except Exception as e:
        #print(f"Skipping archived_stories: {e}")
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

    # avatar_items
    try:
        avatar_items_table = donation_table(
            name="avatar_items",
            df=avatar_items_df(file_input),
            title={"en": "avatar_items", "nl": "avatar_items"},
        )
        tables.append(avatar_items_table)
    except Exception as e:
        #print(f"Skipping avatar_items: {e}")
        pass

    # birthday_media
    try:
        birthday_media_table = donation_table(
            name="birthday_media",
            df=birthday_media_df(file_input),
            title={"en": "birthday_media", "nl": "birthday_media"},
        )
        tables.append(birthday_media_table)
    except Exception as e:
        #print(f"Skipping birthday_media: {e}")
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

    # chat_invites_received
    try:
        chat_invites_received_table = donation_table(
            name="chat_invites_received",
            df=chat_invites_received_df(file_input),
            title={"en": "chat_invites_received", "nl": "chat_invites_received"},
        )
        tables.append(chat_invites_received_table)
    except Exception as e:
        #print(f"Skipping chat_invites_received: {e}")
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

    # collections
    try:
        collections_table = donation_table(
            name="collections",
            df=collections_df(file_input),
            title={"en": "collections", "nl": "collections"},
        )
        tables.append(collections_table)
    except Exception as e:
        #print(f"Skipping collections: {e}")
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

    # community_chat_settings
    try:
        community_chat_settings_table = donation_table(
            name="community_chat_settings",
            df=community_chat_settings_df(file_input),
            title={"en": "community_chat_settings", "nl": "community_chat_settings"},
        )
        tables.append(community_chat_settings_table)
    except Exception as e:
        #print(f"Skipping community_chat_settings: {e}")
        pass

    # community_chats_settings
    try:
        community_chats_settings_table = donation_table(
            name="community_chats_settings",
            df=community_chats_settings_df(file_input),
            title={"en": "community_chats_settings", "nl": "community_chats_settings"},
        )
        tables.append(community_chats_settings_table)
    except Exception as e:
        #print(f"Skipping community_chats_settings: {e}")
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

    # contacts_uploaded_before_2021
    try:
        contacts_uploaded_before_2021_table = donation_table(
            name="contacts_uploaded_before_2021",
            df=contacts_uploaded_before_2021_df(file_input),
            title={"en": "contacts_uploaded_before_2021", "nl": "contacts_uploaded_before_2021"},
        )
        tables.append(contacts_uploaded_before_2021_table)
    except Exception as e:
        #print(f"Skipping contacts_uploaded_before_2021: {e}")
        pass

    # content_sharing_links_you_have_created
    try:
        content_sharing_links_you_have_created_table = donation_table(
            name="content_sharing_links_you_have_created",
            df=content_sharing_links_you_have_created_df(file_input),
            title={"en": "content_sharing_links_you_have_created", "nl": "content_sharing_links_you_have_created"},
        )
        tables.append(content_sharing_links_you_have_created_table)
    except Exception as e:
        #print(f"Skipping content_sharing_links_you_have_created: {e}")
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

    # dark_mode_settings
    try:
        dark_mode_settings_table = donation_table(
            name="dark_mode_settings",
            df=dark_mode_settings_df(file_input),
            title={"en": "dark_mode_settings", "nl": "dark_mode_settings"},
        )
        tables.append(dark_mode_settings_table)
    except Exception as e:
        #print(f"Skipping dark_mode_settings: {e}")
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

    # edits_you_made_to_posts
    try:
        edits_you_made_to_posts_table = donation_table(
            name="edits_you_made_to_posts",
            df=edits_you_made_to_posts_df(file_input),
            title={"en": "edits_you_made_to_posts", "nl": "edits_you_made_to_posts"},
        )
        tables.append(edits_you_made_to_posts_table)
    except Exception as e:
        #print(f"Skipping edits_you_made_to_posts: {e}")
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

    # facebook_editor
    try:
        facebook_editor_table = donation_table(
            name="facebook_editor",
            df=facebook_editor_df(file_input),
            title={"en": "facebook_editor", "nl": "facebook_editor"},
        )
        tables.append(facebook_editor_table)
    except Exception as e:
        #print(f"Skipping facebook_editor: {e}")
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

    # fundraisers_donated_to
    try:
        fundraisers_donated_to_table = donation_table(
            name="fundraisers_donated_to",
            df=fundraisers_donated_to_df(file_input),
            title={"en": "fundraisers_donated_to", "nl": "fundraisers_donated_to"},
        )
        tables.append(fundraisers_donated_to_table)
    except Exception as e:
        #print(f"Skipping fundraisers_donated_to: {e}")
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

    # global_navigation_bar_information
    try:
        global_navigation_bar_information_table = donation_table(
            name="global_navigation_bar_information",
            df=global_navigation_bar_information_df(file_input),
            title={"en": "global_navigation_bar_information", "nl": "global_navigation_bar_information"},
        )
        tables.append(global_navigation_bar_information_table)
    except Exception as e:
        #print(f"Skipping global_navigation_bar_information: {e}")
        pass

    # group_invites_you_ve_received
    try:
        group_invites_you_ve_received_table = donation_table(
            name="group_invites_you_ve_received",
            df=group_invites_you_ve_received_df(file_input),
            title={"en": "group_invites_you_ve_received", "nl": "group_invites_you_ve_received"},
        )
        tables.append(group_invites_you_ve_received_table)
    except Exception as e:
        #print(f"Skipping group_invites_you_ve_received: {e}")
        pass

    # group_invites_you_ve_sent
    try:
        group_invites_you_ve_sent_table = donation_table(
            name="group_invites_you_ve_sent",
            df=group_invites_you_ve_sent_df(file_input),
            title={"en": "group_invites_you_ve_sent", "nl": "group_invites_you_ve_sent"},
        )
        tables.append(group_invites_you_ve_sent_table)
    except Exception as e:
        #print(f"Skipping group_invites_you_ve_sent: {e}")
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

    # groups_you_ve_visited
    try:
        groups_you_ve_visited_table = donation_table(
            name="groups_you_ve_visited",
            df=groups_you_ve_visited_df(file_input),
            title={"en": "groups_you_ve_visited", "nl": "groups_you_ve_visited"},
        )
        tables.append(groups_you_ve_visited_table)
    except Exception as e:
        #print(f"Skipping groups_you_ve_visited: {e}")
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

    # information_about_your_devices
    try:
        information_about_your_devices_table = donation_table(
            name="information_about_your_devices",
            df=information_about_your_devices_df(file_input),
            title={"en": "information_about_your_devices", "nl": "information_about_your_devices"},
        )
        tables.append(information_about_your_devices_table)
    except Exception as e:
        #print(f"Skipping information_about_your_devices: {e}")
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

    # instant_games_usage_data
    try:
        instant_games_usage_data_table = donation_table(
            name="instant_games_usage_data",
            df=instant_games_usage_data_df(file_input),
            title={"en": "instant_games_usage_data", "nl": "instant_games_usage_data"},
        )
        tables.append(instant_games_usage_data_table)
    except Exception as e:
        #print(f"Skipping instant_games_usage_data: {e}")
        pass

    # interactions_with_marketplace_ads
    try:
        interactions_with_marketplace_ads_table = donation_table(
            name="interactions_with_marketplace_ads",
            df=interactions_with_marketplace_ads_df(file_input),
            title={"en": "interactions_with_marketplace_ads", "nl": "interactions_with_marketplace_ads"},
        )
        tables.append(interactions_with_marketplace_ads_table)
    except Exception as e:
        #print(f"Skipping interactions_with_marketplace_ads: {e}")
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

    # items_sold
    try:
        items_sold_table = donation_table(
            name="items_sold",
            df=items_sold_df(file_input),
            title={"en": "items_sold", "nl": "items_sold"},
        )
        tables.append(items_sold_table)
    except Exception as e:
        #print(f"Skipping items_sold: {e}")
        pass

    # join_requests
    try:
        join_requests_table = donation_table(
            name="join_requests",
            df=join_requests_df(file_input),
            title={"en": "join_requests", "nl": "join_requests"},
        )
        tables.append(join_requests_table)
    except Exception as e:
        #print(f"Skipping join_requests: {e}")
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

    # likes_and_reactions_2
    try:
        likes_and_reactions_2_table = donation_table(
            name="likes_and_reactions_2",
            df=likes_and_reactions_2_df(file_input),
            title={"en": "likes_and_reactions_2", "nl": "likes_and_reactions_2"},
        )
        tables.append(likes_and_reactions_2_table)
    except Exception as e:
        #print(f"Skipping likes_and_reactions_2: {e}")
        pass

    # likes_and_reactions_3
    try:
        likes_and_reactions_3_table = donation_table(
            name="likes_and_reactions_3",
            df=likes_and_reactions_3_df(file_input),
            title={"en": "likes_and_reactions_3", "nl": "likes_and_reactions_3"},
        )
        tables.append(likes_and_reactions_3_table)
    except Exception as e:
        #print(f"Skipping likes_and_reactions_3: {e}")
        pass

    # likes_and_reactions_4
    try:
        likes_and_reactions_4_table = donation_table(
            name="likes_and_reactions_4",
            df=likes_and_reactions_4_df(file_input),
            title={"en": "likes_and_reactions_4", "nl": "likes_and_reactions_4"},
        )
        tables.append(likes_and_reactions_4_table)
    except Exception as e:
        #print(f"Skipping likes_and_reactions_4: {e}")
        pass

    # likes_and_reactions_5
    try:
        likes_and_reactions_5_table = donation_table(
            name="likes_and_reactions_5",
            df=likes_and_reactions_5_df(file_input),
            title={"en": "likes_and_reactions_5", "nl": "likes_and_reactions_5"},
        )
        tables.append(likes_and_reactions_5_table)
    except Exception as e:
        #print(f"Skipping likes_and_reactions_5: {e}")
        pass

    # likes_and_reactions_6
    try:
        likes_and_reactions_6_table = donation_table(
            name="likes_and_reactions_6",
            df=likes_and_reactions_6_df(file_input),
            title={"en": "likes_and_reactions_6", "nl": "likes_and_reactions_6"},
        )
        tables.append(likes_and_reactions_6_table)
    except Exception as e:
        #print(f"Skipping likes_and_reactions_6: {e}")
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

    # marketplace_notifications
    try:
        marketplace_notifications_table = donation_table(
            name="marketplace_notifications",
            df=marketplace_notifications_df(file_input),
            title={"en": "marketplace_notifications", "nl": "marketplace_notifications"},
        )
        tables.append(marketplace_notifications_table)
    except Exception as e:
        #print(f"Skipping marketplace_notifications: {e}")
        pass

    # media_used_for_memories
    try:
        media_used_for_memories_table = donation_table(
            name="media_used_for_memories",
            df=media_used_for_memories_df(file_input),
            title={"en": "media_used_for_memories", "nl": "media_used_for_memories"},
        )
        tables.append(media_used_for_memories_table)
    except Exception as e:
        #print(f"Skipping media_used_for_memories: {e}")
        pass

    # memorialization_settings
    try:
        memorialization_settings_table = donation_table(
            name="memorialization_settings",
            df=memorialization_settings_df(file_input),
            title={"en": "memorialization_settings", "nl": "memorialization_settings"},
        )
        tables.append(memorialization_settings_table)
    except Exception as e:
        #print(f"Skipping memorialization_settings: {e}")
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

    # message_2
    try:
        message_2_table = donation_table(
            name="message_2",
            df=message_2_df(file_input),
            title={"en": "message_2", "nl": "message_2"},
        )
        tables.append(message_2_table)
    except Exception as e:
        #print(f"Skipping message_2: {e}")
        pass

    # messaging_settings
    try:
        messaging_settings_table = donation_table(
            name="messaging_settings",
            df=messaging_settings_df(file_input),
            title={"en": "messaging_settings", "nl": "messaging_settings"},
        )
        tables.append(messaging_settings_table)
    except Exception as e:
        #print(f"Skipping messaging_settings: {e}")
        pass

    # messenger_active_status_platform_settings
    try:
        messenger_active_status_platform_settings_table = donation_table(
            name="messenger_active_status_platform_settings",
            df=messenger_active_status_platform_settings_df(file_input),
            title={"en": "messenger_active_status_platform_settings", "nl": "messenger_active_status_platform_settings"},
        )
        tables.append(messenger_active_status_platform_settings_table)
    except Exception as e:
        #print(f"Skipping messenger_active_status_platform_settings: {e}")
        pass

    # messenger_active_status_settings
    try:
        messenger_active_status_settings_table = donation_table(
            name="messenger_active_status_settings",
            df=messenger_active_status_settings_df(file_input),
            title={"en": "messenger_active_status_settings", "nl": "messenger_active_status_settings"},
        )
        tables.append(messenger_active_status_settings_table)
    except Exception as e:
        #print(f"Skipping messenger_active_status_settings: {e}")
        pass

    # messenger_threads_you_started_by_clicking_on_an_ad
    try:
        messenger_threads_you_started_by_clicking_on_an_ad_table = donation_table(
            name="messenger_threads_you_started_by_clicking_on_an_ad",
            df=messenger_threads_you_started_by_clicking_on_an_ad_df(file_input),
            title={"en": "messenger_threads_you_started_by_clicking_on_an_ad", "nl": "messenger_threads_you_started_by_clicking_on_an_ad"},
        )
        tables.append(messenger_threads_you_started_by_clicking_on_an_ad_table)
    except Exception as e:
        #print(f"Skipping messenger_threads_you_started_by_clicking_on_an_ad: {e}")
        pass

    # messenger_ui_settings
    try:
        messenger_ui_settings_table = donation_table(
            name="messenger_ui_settings",
            df=messenger_ui_settings_df(file_input),
            title={"en": "messenger_ui_settings", "nl": "messenger_ui_settings"},
        )
        tables.append(messenger_ui_settings_table)
    except Exception as e:
        #print(f"Skipping messenger_ui_settings: {e}")
        pass

    # meta_ad_library_accounts
    try:
        meta_ad_library_accounts_table = donation_table(
            name="meta_ad_library_accounts",
            df=meta_ad_library_accounts_df(file_input),
            title={"en": "meta_ad_library_accounts", "nl": "meta_ad_library_accounts"},
        )
        tables.append(meta_ad_library_accounts_table)
    except Exception as e:
        #print(f"Skipping meta_ad_library_accounts: {e}")
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

    # navigation_bar_activity
    try:
        navigation_bar_activity_table = donation_table(
            name="navigation_bar_activity",
            df=navigation_bar_activity_df(file_input),
            title={"en": "navigation_bar_activity", "nl": "navigation_bar_activity"},
        )
        tables.append(navigation_bar_activity_table)
    except Exception as e:
        #print(f"Skipping navigation_bar_activity: {e}")
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

    # pages_and_profiles_you_ve_unfollowed
    try:
        pages_and_profiles_you_ve_unfollowed_table = donation_table(
            name="pages_and_profiles_you_ve_unfollowed",
            df=pages_and_profiles_you_ve_unfollowed_df(file_input),
            title={"en": "pages_and_profiles_you_ve_unfollowed", "nl": "pages_and_profiles_you_ve_unfollowed"},
        )
        tables.append(pages_and_profiles_you_ve_unfollowed_table)
    except Exception as e:
        #print(f"Skipping pages_and_profiles_you_ve_unfollowed: {e}")
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

    # payment_addresses
    try:
        payment_addresses_table = donation_table(
            name="payment_addresses",
            df=payment_addresses_df(file_input),
            title={"en": "payment_addresses", "nl": "payment_addresses"},
        )
        tables.append(payment_addresses_table)
    except Exception as e:
        #print(f"Skipping payment_addresses: {e}")
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

    # payments_you_have_made_as_a_buyer
    try:
        payments_you_have_made_as_a_buyer_table = donation_table(
            name="payments_you_have_made_as_a_buyer",
            df=payments_you_have_made_as_a_buyer_df(file_input),
            title={"en": "payments_you_have_made_as_a_buyer", "nl": "payments_you_have_made_as_a_buyer"},
        )
        tables.append(payments_you_have_made_as_a_buyer_table)
    except Exception as e:
        #print(f"Skipping payments_you_have_made_as_a_buyer: {e}")
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

    # people_we_think_you_should_follow
    try:
        people_we_think_you_should_follow_table = donation_table(
            name="people_we_think_you_should_follow",
            df=people_we_think_you_should_follow_df(file_input),
            title={"en": "people_we_think_you_should_follow", "nl": "people_we_think_you_should_follow"},
        )
        tables.append(people_we_think_you_should_follow_table)
    except Exception as e:
        #print(f"Skipping people_we_think_you_should_follow: {e}")
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

    # places_you_ve_created
    try:
        places_you_ve_created_table = donation_table(
            name="places_you_ve_created",
            df=places_you_ve_created_df(file_input),
            title={"en": "places_you_ve_created", "nl": "places_you_ve_created"},
        )
        tables.append(places_you_ve_created_table)
    except Exception as e:
        #print(f"Skipping places_you_ve_created: {e}")
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

    # profiles_you_visited_in_the_past_7_days
    try:
        profiles_you_visited_in_the_past_7_days_table = donation_table(
            name="profiles_you_visited_in_the_past_7_days",
            df=profiles_you_visited_in_the_past_7_days_df(file_input),
            title={"en": "profiles_you_visited_in_the_past_7_days", "nl": "profiles_you_visited_in_the_past_7_days"},
        )
        tables.append(profiles_you_visited_in_the_past_7_days_table)
    except Exception as e:
        #print(f"Skipping profiles_you_visited_in_the_past_7_days: {e}")
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

    # received_friend_requests
    try:
        received_friend_requests_table = donation_table(
            name="received_friend_requests",
            df=received_friend_requests_df(file_input),
            title={"en": "received_friend_requests", "nl": "received_friend_requests"},
        )
        tables.append(received_friend_requests_table)
    except Exception as e:
        #print(f"Skipping received_friend_requests: {e}")
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

    # recommended_bookmark_info
    try:
        recommended_bookmark_info_table = donation_table(
            name="recommended_bookmark_info",
            df=recommended_bookmark_info_df(file_input),
            title={"en": "recommended_bookmark_info", "nl": "recommended_bookmark_info"},
        )
        tables.append(recommended_bookmark_info_table)
    except Exception as e:
        #print(f"Skipping recommended_bookmark_info: {e}")
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

    # rising_fan_badges_you_ve_received
    try:
        rising_fan_badges_you_ve_received_table = donation_table(
            name="rising_fan_badges_you_ve_received",
            df=rising_fan_badges_you_ve_received_df(file_input),
            title={"en": "rising_fan_badges_you_ve_received", "nl": "rising_fan_badges_you_ve_received"},
        )
        tables.append(rising_fan_badges_you_ve_received_table)
    except Exception as e:
        #print(f"Skipping rising_fan_badges_you_ve_received: {e}")
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

    # snooze
    try:
        snooze_table = donation_table(
            name="snooze",
            df=snooze_df(file_input),
            title={"en": "snooze", "nl": "snooze"},
        )
        tables.append(snooze_table)
    except Exception as e:
        #print(f"Skipping snooze: {e}")
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

    # story_reactions
    try:
        story_reactions_table = donation_table(
            name="story_reactions",
            df=story_reactions_df(file_input),
            title={"en": "story_reactions", "nl": "story_reactions"},
        )
        tables.append(story_reactions_table)
    except Exception as e:
        #print(f"Skipping story_reactions: {e}")
        pass

    # story_views_in_past_7_days
    try:
        story_views_in_past_7_days_table = donation_table(
            name="story_views_in_past_7_days",
            df=story_views_in_past_7_days_df(file_input),
            title={"en": "story_views_in_past_7_days", "nl": "story_views_in_past_7_days"},
        )
        tables.append(story_views_in_past_7_days_table)
    except Exception as e:
        #print(f"Skipping story_views_in_past_7_days: {e}")
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

    # support_messages
    try:
        support_messages_table = donation_table(
            name="support_messages",
            df=support_messages_df(file_input),
            title={"en": "support_messages", "nl": "support_messages"},
        )
        tables.append(support_messages_table)
    except Exception as e:
        #print(f"Skipping support_messages: {e}")
        pass

    # surveys
    try:
        surveys_table = donation_table(
            name="surveys",
            df=surveys_df(file_input),
            title={"en": "surveys", "nl": "surveys"},
        )
        tables.append(surveys_table)
    except Exception as e:
        #print(f"Skipping surveys: {e}")
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

    # top_fan_badges_you_ve_received
    try:
        top_fan_badges_you_ve_received_table = donation_table(
            name="top_fan_badges_you_ve_received",
            df=top_fan_badges_you_ve_received_df(file_input),
            title={"en": "top_fan_badges_you_ve_received", "nl": "top_fan_badges_you_ve_received"},
        )
        tables.append(top_fan_badges_you_ve_received_table)
    except Exception as e:
        #print(f"Skipping top_fan_badges_you_ve_received: {e}")
        pass

    # top_fan_information
    try:
        top_fan_information_table = donation_table(
            name="top_fan_information",
            df=top_fan_information_df(file_input),
            title={"en": "top_fan_information", "nl": "top_fan_information"},
        )
        tables.append(top_fan_information_table)
    except Exception as e:
        #print(f"Skipping top_fan_information: {e}")
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

    # video
    try:
        video_table = donation_table(
            name="video",
            df=video_df(file_input),
            title={"en": "video", "nl": "video"},
        )
        tables.append(video_table)
    except Exception as e:
        #print(f"Skipping video: {e}")
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

    # weekly_engagement_list_activity
    try:
        weekly_engagement_list_activity_table = donation_table(
            name="weekly_engagement_list_activity",
            df=weekly_engagement_list_activity_df(file_input),
            title={"en": "weekly_engagement_list_activity", "nl": "weekly_engagement_list_activity"},
        )
        tables.append(weekly_engagement_list_activity_table)
    except Exception as e:
        #print(f"Skipping weekly_engagement_list_activity: {e}")
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

    # your_actions_on_violating_content_in_your_groups
    try:
        your_actions_on_violating_content_in_your_groups_table = donation_table(
            name="your_actions_on_violating_content_in_your_groups",
            df=your_actions_on_violating_content_in_your_groups_df(file_input),
            title={"en": "your_actions_on_violating_content_in_your_groups", "nl": "your_actions_on_violating_content_in_your_groups"},
        )
        tables.append(your_actions_on_violating_content_in_your_groups_table)
    except Exception as e:
        #print(f"Skipping your_actions_on_violating_content_in_your_groups: {e}")
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

    # your_anonymous_mode_status_in_groups
    try:
        your_anonymous_mode_status_in_groups_table = donation_table(
            name="your_anonymous_mode_status_in_groups",
            df=your_anonymous_mode_status_in_groups_df(file_input),
            title={"en": "your_anonymous_mode_status_in_groups", "nl": "your_anonymous_mode_status_in_groups"},
        )
        tables.append(your_anonymous_mode_status_in_groups_table)
    except Exception as e:
        #print(f"Skipping your_anonymous_mode_status_in_groups: {e}")
        pass

    # your_answers_to_membership_questions
    try:
        your_answers_to_membership_questions_table = donation_table(
            name="your_answers_to_membership_questions",
            df=your_answers_to_membership_questions_df(file_input),
            title={"en": "your_answers_to_membership_questions", "nl": "your_answers_to_membership_questions"},
        )
        tables.append(your_answers_to_membership_questions_table)
    except Exception as e:
        #print(f"Skipping your_answers_to_membership_questions: {e}")
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

    # your_autofill_settings
    try:
        your_autofill_settings_table = donation_table(
            name="your_autofill_settings",
            df=your_autofill_settings_df(file_input),
            title={"en": "your_autofill_settings", "nl": "your_autofill_settings"},
        )
        tables.append(your_autofill_settings_table)
    except Exception as e:
        #print(f"Skipping your_autofill_settings: {e}")
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

    # your_basic_mode_opt_in_status
    try:
        your_basic_mode_opt_in_status_table = donation_table(
            name="your_basic_mode_opt_in_status",
            df=your_basic_mode_opt_in_status_df(file_input),
            title={"en": "your_basic_mode_opt_in_status", "nl": "your_basic_mode_opt_in_status"},
        )
        tables.append(your_basic_mode_opt_in_status_table)
    except Exception as e:
        #print(f"Skipping your_basic_mode_opt_in_status: {e}")
        pass

    # your_comment_active_days
    try:
        your_comment_active_days_table = donation_table(
            name="your_comment_active_days",
            df=your_comment_active_days_df(file_input),
            title={"en": "your_comment_active_days", "nl": "your_comment_active_days"},
        )
        tables.append(your_comment_active_days_table)
    except Exception as e:
        #print(f"Skipping your_comment_active_days: {e}")
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

    # your_contributions
    try:
        your_contributions_table = donation_table(
            name="your_contributions",
            df=your_contributions_df(file_input),
            title={"en": "your_contributions", "nl": "your_contributions"},
        )
        tables.append(your_contributions_table)
    except Exception as e:
        #print(f"Skipping your_contributions: {e}")
        pass

    # your_cross_app_messaging_settings
    try:
        your_cross_app_messaging_settings_table = donation_table(
            name="your_cross_app_messaging_settings",
            df=your_cross_app_messaging_settings_df(file_input),
            title={"en": "your_cross_app_messaging_settings", "nl": "your_cross_app_messaging_settings"},
        )
        tables.append(your_cross_app_messaging_settings_table)
    except Exception as e:
        #print(f"Skipping your_cross_app_messaging_settings: {e}")
        pass

    # your_crowdsourcing_edits
    try:
        your_crowdsourcing_edits_table = donation_table(
            name="your_crowdsourcing_edits",
            df=your_crowdsourcing_edits_df(file_input),
            title={"en": "your_crowdsourcing_edits", "nl": "your_crowdsourcing_edits"},
        )
        tables.append(your_crowdsourcing_edits_table)
    except Exception as e:
        #print(f"Skipping your_crowdsourcing_edits: {e}")
        pass

    # your_daily_limit
    try:
        your_daily_limit_table = donation_table(
            name="your_daily_limit",
            df=your_daily_limit_df(file_input),
            title={"en": "your_daily_limit", "nl": "your_daily_limit"},
        )
        tables.append(your_daily_limit_table)
    except Exception as e:
        #print(f"Skipping your_daily_limit: {e}")
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

    # your_end_to_end_encryption_enabled_messenger_device
    try:
        your_end_to_end_encryption_enabled_messenger_device_table = donation_table(
            name="your_end_to_end_encryption_enabled_messenger_device",
            df=your_end_to_end_encryption_enabled_messenger_device_df(file_input),
            title={"en": "your_end_to_end_encryption_enabled_messenger_device", "nl": "your_end_to_end_encryption_enabled_messenger_device"},
        )
        tables.append(your_end_to_end_encryption_enabled_messenger_device_table)
    except Exception as e:
        #print(f"Skipping your_end_to_end_encryption_enabled_messenger_device: {e}")
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

    # your_group_post_tags
    try:
        your_group_post_tags_table = donation_table(
            name="your_group_post_tags",
            df=your_group_post_tags_df(file_input),
            title={"en": "your_group_post_tags", "nl": "your_group_post_tags"},
        )
        tables.append(your_group_post_tags_table)
    except Exception as e:
        #print(f"Skipping your_group_post_tags: {e}")
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

    # your_imported_contacts
    try:
        your_imported_contacts_table = donation_table(
            name="your_imported_contacts",
            df=your_imported_contacts_df(file_input),
            title={"en": "your_imported_contacts", "nl": "your_imported_contacts"},
        )
        tables.append(your_imported_contacts_table)
    except Exception as e:
        #print(f"Skipping your_imported_contacts: {e}")
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

    # your_inferred_language_preferences_for_videos
    try:
        your_inferred_language_preferences_for_videos_table = donation_table(
            name="your_inferred_language_preferences_for_videos",
            df=your_inferred_language_preferences_for_videos_df(file_input),
            title={"en": "your_inferred_language_preferences_for_videos", "nl": "your_inferred_language_preferences_for_videos"},
        )
        tables.append(your_inferred_language_preferences_for_videos_table)
    except Exception as e:
        #print(f"Skipping your_inferred_language_preferences_for_videos: {e}")
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

    # your_instant_games_tournament_information
    try:
        your_instant_games_tournament_information_table = donation_table(
            name="your_instant_games_tournament_information",
            df=your_instant_games_tournament_information_df(file_input),
            title={"en": "your_instant_games_tournament_information", "nl": "your_instant_games_tournament_information"},
        )
        tables.append(your_instant_games_tournament_information_table)
    except Exception as e:
        #print(f"Skipping your_instant_games_tournament_information: {e}")
        pass

    # your_language_translation_settings
    try:
        your_language_translation_settings_table = donation_table(
            name="your_language_translation_settings",
            df=your_language_translation_settings_df(file_input),
            title={"en": "your_language_translation_settings", "nl": "your_language_translation_settings"},
        )
        tables.append(your_language_translation_settings_table)
    except Exception as e:
        #print(f"Skipping your_language_translation_settings: {e}")
        pass

    # your_locations
    try:
        your_locations_table = donation_table(
            name="your_locations",
            df=your_locations_df(file_input),
            title={"en": "your_locations", "nl": "your_locations"},
        )
        tables.append(your_locations_table)
    except Exception as e:
        #print(f"Skipping your_locations: {e}")
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

    # your_marketplace_cart_information
    try:
        your_marketplace_cart_information_table = donation_table(
            name="your_marketplace_cart_information",
            df=your_marketplace_cart_information_df(file_input),
            title={"en": "your_marketplace_cart_information", "nl": "your_marketplace_cart_information"},
        )
        tables.append(your_marketplace_cart_information_table)
    except Exception as e:
        #print(f"Skipping your_marketplace_cart_information: {e}")
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

    # your_marketplace_listing_history
    try:
        your_marketplace_listing_history_table = donation_table(
            name="your_marketplace_listing_history",
            df=your_marketplace_listing_history_df(file_input),
            title={"en": "your_marketplace_listing_history", "nl": "your_marketplace_listing_history"},
        )
        tables.append(your_marketplace_listing_history_table)
    except Exception as e:
        #print(f"Skipping your_marketplace_listing_history: {e}")
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

    # your_mentions_settings
    try:
        your_mentions_settings_table = donation_table(
            name="your_mentions_settings",
            df=your_mentions_settings_df(file_input),
            title={"en": "your_mentions_settings", "nl": "your_mentions_settings"},
        )
        tables.append(your_mentions_settings_table)
    except Exception as e:
        #print(f"Skipping your_mentions_settings: {e}")
        pass

    # your_messenger_app_install_information
    try:
        your_messenger_app_install_information_table = donation_table(
            name="your_messenger_app_install_information",
            df=your_messenger_app_install_information_df(file_input),
            title={"en": "your_messenger_app_install_information", "nl": "your_messenger_app_install_information"},
        )
        tables.append(your_messenger_app_install_information_table)
    except Exception as e:
        #print(f"Skipping your_messenger_app_install_information: {e}")
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

    # your_page_or_groups_badges
    try:
        your_page_or_groups_badges_table = donation_table(
            name="your_page_or_groups_badges",
            df=your_page_or_groups_badges_df(file_input),
            title={"en": "your_page_or_groups_badges", "nl": "your_page_or_groups_badges"},
        )
        tables.append(your_page_or_groups_badges_table)
    except Exception as e:
        #print(f"Skipping your_page_or_groups_badges: {e}")
        pass

    # your_pages
    try:
        your_pages_table = donation_table(
            name="your_pages",
            df=your_pages_df(file_input),
            title={"en": "your_pages", "nl": "your_pages"},
        )
        tables.append(your_pages_table)
    except Exception as e:
        #print(f"Skipping your_pages: {e}")
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

    # your_participation_requests
    try:
        your_participation_requests_table = donation_table(
            name="your_participation_requests",
            df=your_participation_requests_df(file_input),
            title={"en": "your_participation_requests", "nl": "your_participation_requests"},
        )
        tables.append(your_participation_requests_table)
    except Exception as e:
        #print(f"Skipping your_participation_requests: {e}")
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

    # your_pending_posts_in_groups
    try:
        your_pending_posts_in_groups_table = donation_table(
            name="your_pending_posts_in_groups",
            df=your_pending_posts_in_groups_df(file_input),
            title={"en": "your_pending_posts_in_groups", "nl": "your_pending_posts_in_groups"},
        )
        tables.append(your_pending_posts_in_groups_table)
    except Exception as e:
        #print(f"Skipping your_pending_posts_in_groups: {e}")
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

    # your_recent_reported_conversions
    try:
        your_recent_reported_conversions_table = donation_table(
            name="your_recent_reported_conversions",
            df=your_recent_reported_conversions_df(file_input),
            title={"en": "your_recent_reported_conversions", "nl": "your_recent_reported_conversions"},
        )
        tables.append(your_recent_reported_conversions_table)
    except Exception as e:
        #print(f"Skipping your_recent_reported_conversions: {e}")
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

    # your_recently_viewed_products
    try:
        your_recently_viewed_products_table = donation_table(
            name="your_recently_viewed_products",
            df=your_recently_viewed_products_df(file_input),
            title={"en": "your_recently_viewed_products", "nl": "your_recently_viewed_products"},
        )
        tables.append(your_recently_viewed_products_table)
    except Exception as e:
        #print(f"Skipping your_recently_viewed_products: {e}")
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

    # your_video_consumption_summary
    try:
        your_video_consumption_summary_table = donation_table(
            name="your_video_consumption_summary",
            df=your_video_consumption_summary_df(file_input),
            title={"en": "your_video_consumption_summary", "nl": "your_video_consumption_summary"},
        )
        tables.append(your_video_consumption_summary_table)
    except Exception as e:
        #print(f"Skipping your_video_consumption_summary: {e}")
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
            id="facebook",
            tables=tables
        )
    else:
        #print("No tables could be generated from the provided files")
        return None
