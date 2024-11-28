"""
Facebook

This module contains an example flow of a Facebook data donation study
"""
import logging

import pandas as pd

from pathlib import Path
from typing import Any

import port.api.props as props
import port.helpers.extraction_helpers as eh
import port.helpers.port_helpers as ph
import port.helpers.validate as validate

from port.helpers.validate import (
    DDPCategory,
    DDPFiletype,
    Language,
)

logger = logging.getLogger(__name__)

DDP_CATEGORIES = [
    DDPCategory(
        id="json_en",
        ddp_filetype=DDPFiletype.JSON,
        language=Language.EN,
        known_files=[
            "events_interactions.json",
            "group_interactions.json",
            "people_and_friends.json",
            "advertisers_using_your_activity_or_information.json",
            "advertisers_you've_interacted_with.json",
            "apps_and_websites.json",
            "your_off-facebook_activity.json",
            "comments.json",
            "posts_and_comments.json",
            "event_invitations.json",
            "your_event_responses.json",
            "accounts_center.json",
            "marketplace_notifications.json",
            "payment_history.json",
            "controls.json",
            "reduce.json",
            "friend_requests_received.json",
            "friend_requests_sent.json",
            "friends.json",
            "rejected_friend_requests.json",
            "removed_friends.json",
            "who_you_follow.json",
            "your_comments_in_groups.json",
            "your_group_membership_activity.json",
            "your_posts_in_groups.json",
            "primary_location.json",
            "primary_public_location.json",
            "timezone.json",
            "notifications.json",
            "pokes.json",
            "ads_interests.json",
            "friend_peer_group.json",
            "pages_and_profiles_you_follow.json",
            "pages_and_profiles_you've_recommended.json",
            "pages_and_profiles_you've_unfollowed.json",
            "pages_you've_liked.json",
            "polls_you_voted_on.json",
            "your_uncategorized_photos.json",
            "your_videos.json",
            "language_and_locale.json",
            "live_video_subscriptions.json",
            "profile_information.json",
            "profile_update_history.json",
            "your_local_lists.json",
            "your_saved_items.json",
            "your_search_history.json",
            "account_activity.json",
            "authorized_logins.json",
            "browser_cookies.json",
            "email_address_verifications.json",
            "ip_address_activity.json",
            "login_protection_data.json",
            "logins_and_logouts.json",
            "mobile_devices.json",
            "record_details.json",
            "where_you're_logged_in.json",
            "your_facebook_activity_history.json",
            "archived_stories.json",
            "location.json",
            "recently_viewed.json",
            "recently_visited.json",
            "your_topics.json",
        ],
    )
]


def group_interactions_to_df(facebook_zip: str) -> pd.DataFrame:

    b = eh.extract_file_from_zip(facebook_zip, "group_interactions.json")
    d = eh.read_json_from_bytes(b)

    out = pd.DataFrame()
    datapoints = []

    try:
        items = d["group_interactions_v2"][0]["entries"]
        for item in items:
            datapoints.append((
                item.get("data", {}).get("name", None),
                item.get("data", {}).get("value", '').split(" ")[0],
                item.get("data", {}).get("uri", None)
            ))
        out = pd.DataFrame(datapoints, columns=["Group name", "Times Interacted", "Group Link"])
        out = out.sort_values(by="Times Interacted", ascending=False)

    except Exception as e:
        logger.error("Exception caught: %s", e)

    return out


def comments_to_df(facebook_zip: str) -> pd.DataFrame:

    b = eh.extract_file_from_zip(facebook_zip, "comments.json")
    d = eh.read_json_from_bytes(b)

    out = pd.DataFrame()
    datapoints = []

    try:
        items = d["comments_v2"]
        for item in items:
            datapoints.append((
                item.get("title", ""),
                item["data"][0].get("comment", {}).get("comment", ""),
                eh.epoch_to_iso(item.get("timestamp", {}))
            ))
        out = pd.DataFrame(datapoints, columns=["Action", "Comment", "Date"])

    except Exception as e:
        logger.error("Exception caught: %s", e)

    return out



def likes_and_reactions_to_df(facebook_zip: str) -> pd.DataFrame:

    b = eh.extract_file_from_zip(facebook_zip, "likes_and_reactions_1.json")
    d = eh.read_json_from_bytes(b)

    out = pd.DataFrame()
    datapoints = []

    try:
        for item in d:
            datapoints.append((
                item.get("title", ""),
                item["data"][0].get("reaction", {}).get("reaction", ""),
                eh.epoch_to_iso(item.get("timestamp", {}))
            ))
        out = pd.DataFrame(datapoints, columns=["Action", "Reaction", "Date"])

    except Exception as e:
        logger.error("Exception caught: %s", e)

    return out


def your_badges_to_df(facebook_zip: str) -> pd.DataFrame:

    b = eh.extract_file_from_zip(facebook_zip, "your_badges.json")
    d = eh.read_json_from_bytes(b)

    out = pd.DataFrame()
    datapoints = []

    try:
        for k, v in d["group_badges_v2"].items():
            datapoints.append((
                k,
                ', '.join(v),
                len(v)
            ))
        out = pd.DataFrame(datapoints, columns=["Group name", "Badges", "Number of badges"])
        out = out.sort_values(by="Number of badges", ascending=False)

    except Exception as e:
        logger.error("Exception caught: %s", e)

    return out


def find_items(d: dict[Any, Any],  key_to_match: str) -> str:
    """
    d is a denested dict
    match all keys in d that contain key_to_match

    return the value beloning to that key that are the least nested
    In case of no match return empty string

    example:
    key_to_match = asd

    asd-asd-asd-asd-asd-asd: 1
    asd-asd: 2
    qwe: 3

    returns 2

    This function is needed because your_posts_1.json contains a wide variety of nestedness per post
    """
    out = ""
    pattern = r"{}".format(f"^.*{key_to_match}.*$")
    depth = math.inf

    try:
        for k, v in d.items():
            if re.match(pattern, k):
                depth_current_match = k.count("-")
                if depth_current_match < depth:
                    depth = depth_current_match
                    out = str(v)
    except Exception as e:
        logger.error("bork bork: %s", e)

    return out



def your_posts_to_df(facebook_zip: str) -> pd.DataFrame:

    b = eh.extract_file_from_zip(facebook_zip, "your_posts_1.json")
    d = eh.read_json_from_bytes(b)
    if isinstance(d, dict) == True:
        d = [d]

    out = pd.DataFrame()
    datapoints = []

    try:
        for item in d:
            denested_dict = eh.dict_denester(item)

            datapoints.append((
                find_items(denested_dict, "title"),
                find_items(denested_dict, "post"),
                eh.epoch_to_iso(find_items(denested_dict, "timestamp")),
                find_items(denested_dict, "url"),
            ))

        out = pd.DataFrame(datapoints, columns=["Title", "Post", "Date", "Url"])
    except Exception as e:
        logger.error("Exception caught: %s", e)

    return out


def your_posts_check_ins_photos_and_videos_1_to_df(facebook_zip: str) -> pd.DataFrame:

    b = eh.extract_file_from_zip(facebook_zip, "your_posts__check_ins__photos_and_videos_1.json")
    d = eh.read_json_from_bytes(b)

    out = pd.DataFrame()
    datapoints = []

    try:
        for item in d:
            denested_dict = eh.dict_denester(item)

            datapoints.append((
                find_items(denested_dict, "title"),
                find_items(denested_dict, "post"),
                eh.epoch_to_iso(find_items(denested_dict, "timestamp")),
                find_items(denested_dict, "url"),
            ))

        out = pd.DataFrame(datapoints, columns=["Title", "Post", "Date", "Url"])
    except Exception as e:
        logger.error("Exception caught: %s", e)

    return out


def your_search_history_to_df(facebook_zip: str) -> pd.DataFrame:

    b = eh.extract_file_from_zip(facebook_zip, "your_search_history.json")
    d = eh.read_json_from_bytes(b)

    out = pd.DataFrame()
    datapoints = []

    try:
        items = d["searches_v2"]
        for item in items:
            datapoints.append((
                item["data"][0].get("text", ""),
                eh.epoch_to_iso(item.get("timestamp", {}))
            ))

        out = pd.DataFrame(datapoints, columns=["Search Term", "Date"])
    except Exception as e:
        logger.error("Exception caught: %s", e)

    return out


def recently_viewed_to_df(facebook_zip: str) -> pd.DataFrame:
    b = eh.extract_file_from_zip(facebook_zip, "recently_viewed.json")
    d = eh.read_json_from_bytes(b)

    out = pd.DataFrame()
    datapoints = []

    try:
        items = d["recently_viewed"]
        for item in items:

            if "entries" in item:
                for entry in item["entries"]:
                    datapoints.append((
                        item.get("name", ""),
                        entry.get("data", {}).get("name", ""),
                        entry.get("data", {}).get("uri", ""),
                        eh.epoch_to_iso(entry.get("timestamp"))
                    ))

            # The nesting goes deeper
            if "children" in item:
                for child in item["children"]:
                    for entry in child["entries"]:
                        datapoints.append((
                            child.get("name", ""),
                            entry.get("data", {}).get("name", ""),
                            entry.get("data", {}).get("uri", ""),
                            eh.epoch_to_iso(entry.get("timestamp"))
                        ))

        out = pd.DataFrame(datapoints, columns=["Watched", "Name", "Link", "Date"])
        out = out.sort_values(by="Date", key=eh.sort_isotimestamp_empty_timestamp_last)

    except Exception as e:
        logger.error("Exception caught: %s", e)

    return out



def recently_visited_to_df(facebook_zip: str) -> pd.DataFrame:
    b = eh.extract_file_from_zip(facebook_zip, "recently_visited.json")
    d = eh.read_json_from_bytes(b)

    out = pd.DataFrame()
    datapoints = []

    try:
        items = d["visited_things_v2"]
        for item in items:
            if "entries" in item:
                for entry in item["entries"]:
                    datapoints.append((
                        item.get("name", ""),
                        entry.get("data", {}).get("name", ""),
                        entry.get("data", {}).get("uri", ""),
                        eh.epoch_to_iso(entry.get("timestamp"))
                    ))
        out = pd.DataFrame(datapoints, columns=["Watched", "Name", "Link", "Date"])
        out = out.sort_values(by="Date", key=eh.sort_isotimestamp_empty_timestamp_last)

    except Exception as e:
        logger.error("Exception caught: %s", e)

    return out


def feed_to_df(facebook_zip: str) -> pd.DataFrame:
    b = eh.extract_file_from_zip(facebook_zip, "feed.json")
    d = eh.read_json_from_bytes(b)

    out = pd.DataFrame()
    datapoints = []

    try:
        items = d["people_and_friends_v2"]
        for item in items:
            if "entries" in item:
                for entry in item["entries"]:
                    datapoints.append((
                        item.get("name", ""),
                        entry.get("data", {}).get("name", ""),
                        entry.get("data", {}).get("uri", ""),
                        eh.epoch_to_iso(entry.get("timestamp"))
                    ))
        out = pd.DataFrame(datapoints, columns=["Category", "Name", "Link", "Date"])
        out = out.sort_values(by="Date", key=eh.sort_isotimestamp_empty_timestamp_last)

    except Exception as e:
        logger.error("Exception caught: %s", e)

    return out


def controls_to_df(facebook_zip: str) -> pd.DataFrame:
    b = eh.extract_file_from_zip(facebook_zip, "controls.json")
    d = eh.read_json_from_bytes(b)

    out = pd.DataFrame()
    datapoints = []

    try:
        items = d["controls"]
        for item in items:
            if "entries" in item:
                for entry in item["entries"]:
                    datapoints.append((
                        item.get("name", ""),
                        entry.get("data", {}).get("name", ""),
                        entry.get("data", {}).get("uri", ""),
                        eh.epoch_to_iso(entry.get("timestamp"))
                    ))
        out = pd.DataFrame(datapoints, columns=["Category", "Name", "Link", "Date"])
        out = out.sort_values(by="Date", key=eh.sort_isotimestamp_empty_timestamp_last)

    except Exception as e:
        logger.error("Exception caught: %s", e)

    return out


def group_posts_and_comments_to_df(facebook_zip: str) -> pd.DataFrame:

    b = eh.extract_file_from_zip(facebook_zip, "group_posts_and_comments.json")
    d = eh.read_json_from_bytes(b)

    if not d:
        b = eh.extract_file_from_zip(facebook_zip, "your_posts_in_groups.json")
        d = eh.read_json_from_bytes(b)

    out = pd.DataFrame()
    datapoints = []

    try:
        l = d["group_posts_v2"]
        for item in l:
            denested_dict = eh.dict_denester(item)

            datapoints.append((
                find_items(denested_dict, "title"),
                find_items(denested_dict, "post"),
                find_items(denested_dict, "comment"), # There are no comments in my test data, this is a guess!!
                eh.epoch_to_iso(find_items(denested_dict, "timestamp")),
                find_items(denested_dict, "url"),
            ))

        out = pd.DataFrame(datapoints, columns=["Title", "Post", "Comment", "Date", "Url"])
    except Exception as e:
        logger.error("Exception caught: %s", e)

    return out


def extraction(facebook_zip : str) -> list[props.PropsUIPromptConsentFormTable]:
    tables_to_render = []

    df = group_interactions_to_df(facebook_zip)
    if not df.empty:
        table_title = props.Translatable({
            "en": "Group Interactions",
            "nl": "Groepsinteracties"
        })
        table = props.PropsUIPromptConsentFormTable("group_interactions", table_title, df)
        tables_to_render.append(table)

    df = comments_to_df(facebook_zip)
    if not df.empty:
        table_title = props.Translatable({
            "en": "Comments",
            "nl": "Reacties"
        })
        table = props.PropsUIPromptConsentFormTable("comments", table_title, df)
        tables_to_render.append(table)


    df = likes_and_reactions_to_df(facebook_zip)
    if not df.empty:
        table_title = props.Translatable({
            "en": "Likes and Reactions",
            "nl": "Likes en reacties",
        })
        table_description = props.Translatable({
           "en": "This table shows the likes and reactions you yourself have given to posts and comments.",
           "nl": "Deze tabel toont de likes en reacties die je hebt gegeven aan berichten en reacties."
        })
        table = props.PropsUIPromptConsentFormTable("likes_and_reactions", table_title, df, table_description)
        tables_to_render.append(table)

    # df = your_badges_to_df(facebook_zip)

    # df = your_posts_to_df(facebook_zip)

    # df = your_posts_check_ins_photos_and_videos_1_to_df(facebook_zip)

    df = your_search_history_to_df(facebook_zip)
    if not df.empty:
        table_title = props.Translatable({
            "en": "Search History",
            "nl": "Zoekgeschiedenis"
        })
        table_description = props.Translatable({
            "en": "This table shows your search history on Facebook, including the search terms and the dates they were searched.",
            "nl": "Deze tabel toont uw zoekgeschiedenis op Facebook, inclusief de zoektermen en de datums waarop ze zijn gezocht."
        })
        table = props.PropsUIPromptConsentFormTable("search_history", table_title, df)
        tables_to_render.append(table)

    # df = recently_viewed_to_df(facebook_zip)

    # df = recently_visited_to_df(facebook_zip)

    df = feed_to_df(facebook_zip)
    if not df.empty:
        table_title = props.Translatable({
            "en": "Feed",
            "nl": "Feed"
        })
        table = props.PropsUIPromptConsentFormTable("feed", table_title, df)
        tables_to_render.append(table)

    # df = controls_to_df(facebook_zip)

    df = group_posts_and_comments_to_df(facebook_zip)
    if not df.empty:
        table_title = props.Translatable({
            "en": "Group Posts and Comments",
            "nl": "Groepsberichten en reacties"
        })
        table = props.PropsUIPromptConsentFormTable("group_posts_and_comments", table_title, df)
        tables_to_render.append(table)

    return tables_to_render


# TEXTS
SUBMIT_FILE_HEADER = props.Translatable({
    "en": "Select your Facebook file",
    "nl": "Selecteer uw Facebook bestand"
})

REVIEW_DATA_HEADER = props.Translatable({
    "en": "Your Facebook data",
    "nl": "Uw Facebook gegevens"
})

RETRY_HEADER = props.Translatable({
    "en": "Try again",
    "nl": "Probeer opnieuw"
})

REVIEW_DATA_DESCRIPTION = props.Translatable({
   "en": "This is a demo for what the donation interface looks like. We extract data from the zip file, and participants first get to see all the data we extracted. Only the data that is visible to them will be donated, and they can optionally delete data they do not want to donate.",
   "nl": "Dit is een demo voor hoe de donatie-interface eruit ziet. We extraheren gegevens uit het zip-bestand en deelnemers krijgen eerst alle gegevens te zien die we hebben geëxtraheerd. Alleen de gegevens die voor hen zichtbaar zijn, worden gedoneerd en ze kunnen optioneel gegevens verwijderen die ze niet willen doneren."
})


def process(session_id: int):
    platform_name = "Facebook"

    table_list = None
    while True:
        logger.info("Prompt for file for %s", platform_name)

        file_prompt = ph.generate_file_prompt("application/zip")
        file_result = yield ph.render_page(SUBMIT_FILE_HEADER, file_prompt)

        if file_result.__type__ == "PayloadString":
            validation = validate.validate_zip(DDP_CATEGORIES, file_result.value)

            # Happy flow: Valid DDP
            if validation.get_status_code_id() == 0:
                logger.info("Payload for %s", platform_name)
                extraction_result = extraction(file_result.value)
                table_list = extraction_result
                break

            # Enter retry flow, reason: if DDP was not a Facebook DDP
            if validation.get_status_code_id() != 0:
                logger.info("Not a valid %s zip; No payload; prompt retry_confirmation", platform_name)
                retry_prompt = ph.generate_retry_prompt(platform_name)
                retry_result = yield ph.render_page(RETRY_HEADER, retry_prompt)

                if retry_result.__type__ == "PayloadTrue":
                    continue
                else:
                    logger.info("Skipped during retry flow")
                    break

        else:
            logger.info("Skipped at file selection ending flow")
            break

    if table_list is not None:
        logger.info("Prompt consent; %s", platform_name)
        review_data_prompt = ph.generate_review_data_prompt(f"{session_id}-facebook", REVIEW_DATA_DESCRIPTION, table_list)
        yield ph.render_page(REVIEW_DATA_HEADER, review_data_prompt)

    yield ph.exit(0, "Success")
    yield ph.render_end_page()
