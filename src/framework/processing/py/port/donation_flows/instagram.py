from port.helpers.donation_flow import donation_table, donation_flow
from port.helpers.parsers import parse_json
from port.helpers.readers import read_json

import pandas as pd
import json

"""
################

EXAMPLE TEMPLATE

################

def posts_viewed_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/posts_viewed.json"])

    df = parse_json(data,
        row_path = ["$.impressions_history_posts_seen"],
        col_paths = dict(
           name = ["string_map_data.Author.value"],
           time = ["string_map_data.Time.timestamp"]
        )
    )

    df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
    df = df.sort_values("date")

    return df


def ad_preferences_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/ad_preferences.json"])

    df = parse_json(data,
        row_path = ["$.label_values"],
        col_paths = dict(
           label = ["label"],
        )
    )

    return df

def create_donation_flow(file_input: list[str]):
    posts_viewed_table = donation_table(
        name = "followers",
        df = posts_viewed_df(file_input),
        title = {"en": "Example", "nl": "Voorbeeld"}
    )


    return donation_flow(
        id = "facebook",
        tables = [posts_viewed_table],
    )



"""
############################
# level01: ads_information #
############################

## level02: ads_and_topics

# level03: ads_viewed
def ads_viewed_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/ads_viewed.json"])

    df = parse_json(data,
        row_path = ["$.impressions_history_ads_seen"],
        col_paths = dict(
           name = ["string_map_data.Author.value"],
           time = ["string_map_data.Time.timestamp"]
        )
    )

    df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
    df = df.sort_values("date")

    return df

# level03: posts_viewed
def posts_viewed_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/posts_viewed.json"])

    df = parse_json(data,
        row_path = ["$.impressions_history_posts_seen"],
        col_paths = dict(
           name = ["string_map_data.Author.value"],
           time = ["string_map_data.Time.timestamp"]
        )
    )

    df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
    df = df.sort_values("date")

    return df


# level03: videos_watched
def videos_watched_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/videos_watched.json"])

    df = parse_json(data,
        row_path = ["$.impressions_history_videos_watched"],
        col_paths = dict(
           name = ["string_map_data.Author.value"],
           time = ["string_map_data.Time.timestamp"]
        )
    )

    df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
    df = df.sort_values("date")

    return df

## level02: instagram_ads_and_businesses

# level03: ad_preferences


def ad_preferences_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/ad_preferences.json"])

    df = parse_json(data,
        row_path = ["$.label_values"],
        col_paths = dict(
           label = ["label"],
        )
    )

    return df

# level03: advertisers_using_your_activity_or_information


def advertisers_using_your_activity_or_information_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/advertisers_using_your_activity_or_information.json"])

    df = parse_json(data,
        row_path = ["$.ig_custom_audiences_all_types"],
        col_paths = dict(
           advertiser = ["advertiser_name"],
        )
    )

    return df


########################
# level01: connections #
########################

## level02: followers_and_following

# level03: close_friends

def close_friends_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/close_friends.json"])

    df = parse_json(data,
        row_path=["$.relationships_close_friends"],  
        col_paths=dict(
           profile_link=["string_list_data.href"],  
           username=["string_list_data.value"],  
           time=["string_list_data.timestamp"]  
        )
    )

    df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
    df = df.sort_values("date")

    return df

# level03: follow_requests_you've_received

def follow_requests_you_received_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/follow_requests_you've_received.json"])

    df = parse_json(data,
        row_path=["$.relationships_close_friends"],  
        col_paths=dict(
           profile_link=["href"],  
           username=["value"],  
           time=["timestamp"]  
        )
    )

    df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
    df = df.sort_values("date")

    return df

# level03: followers_1

def followers_1_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/string_list_data.json"])

    df = parse_json(data,
        row_path=["$.string_list_data"],  
        col_paths=dict(
           profile_link=["href"],  
           username=["value"],  
           time=["timestamp"]  
        )
    )

    df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
    df = df.sort_values("date")

    return df

# level03: following

def following_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/following"])

    df = parse_json(data,
        row_path=["$.string_list_data"],  
        col_paths=dict(
           profile_link=["href"],  
           username=["value"],  
           time=["timestamp"]  
        )
    )

    df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
    df = df.sort_values("date")

    return df


# level03: following

def recent_follow_requests_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/recent_follow_requests"])

    df = parse_json(data,
        row_path=["$.relationships_permanent_follow_requests"],  
        col_paths=dict(
           profile_link=["string_list_data.href"],  
           username=["string_list_data.value"],  
           time=["string_list_data.timestamp"]  
        )
    )

    df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
    df = df.sort_values("date")

    return df

# level03: recently_unfollowed_profiles

def recently_unfollowed_profiles_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/recently_unfollowed_profiles"])

    df = parse_json(data,
        row_path=["$.relationships_unfollowed_users"],  
        col_paths=dict(
           profile_link=["string_list_data.href"],  
           username=["string_list_data.value"],  
           time=["string_list_data.timestamp"]  
        )
    )

    df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
    df = df.sort_values("date")

    return df

########################
# level01: preferences #
########################

## level02: media_settings

# level03: comments_allowed_from

def comments_allowed_from_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/comments_allowed_from"])

    df = parse_json(data,
        row_path=["$.string_map_data"],  
        col_paths=dict(
           profile_link=["href"],  
           username=["value"],  
           time=["timestamp"]  
        )
    )

    df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
    df = df.sort_values("date")

    return df

## level02: your_topics

# level03: recommended_topics

def recommended_topics_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/recommended_topics"])

    df = parse_json(data,
        row_path=["$.topics_your_topics"],  
        col_paths=dict(
           topic_of_interest=["string_map_data.value"]
        )
    )

    return df

###########################################
# level01: security_and_login_information #
###########################################

## level02: login_and_profile_creation

# level03: instagram_signup_details

def instagram_signup_details_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/instagram_signup_details"])

    df = parse_json(data,
        row_path=["$.account_history_registration_info"],  
        col_paths=dict(
           username_link=["string_map_data.Username.href"],  
           username=["string_map_data.Username.value"],  
           time=["string_map_data.Username.timestamp"],
           email=["string_map_data.Email.value"],
           phone_number=["string_map_data.Phone Number.value"],
           device=["string_map_data.Device.value"],
           
           
        )
    )

    df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
    df = df.sort_values("date")

    return df


# level03: login_activity

def login_activity_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/login_activity"])

    df = parse_json(data,
        row_path=["$.account_history_login_history"],  
        col_paths=dict(
           language=["string_map_data.Language Code.value"],
           time=["string_map_data.Time.value"],
           user_agent=["string_map_data.User Agent.value"] 
           
           
        )
    )

    df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
    df = df.sort_values("date")

    return df


###################################
# level01: your_instagram_activity#
###################################

## level02: comments

# level03: post_comments_1

def post_comments_1_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/post_comments_1"])

    df = parse_json(data,
        row_path=["$.media_list_data"],  
        col_paths=dict(
           comment=["string_map_data.Comment.value"],
           media_owner= ["string_map_data.Media Owner.value"],
           time=["string_map_data.Time.timestamp"]
           
           
        )
    )

    df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
    df = df.sort_values("date")

    return df

## level02: content

# level03: posts_1

def posts_1_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/posts_1"])

    df = parse_json(data,
        row_path=["$.media"],  
        col_paths=dict(
           photo_uri=["uri"],
           time=["creation_timestamp"],
           camera_metadata=["media_metadata.camera_metadata.has_camera_metadata"],
           title=["title"],
           post_shared_on_another_platform=["source_app"]

           
           
        )
    )

    df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
    df = df.sort_values("date")

    return df

# level03: profile_photos

def profile_photos_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/profile_photos"])

    df = parse_json(data,
        row_path=["$.ig_profile_picture"],  
        col_paths=dict(
           photo_uri=["uri"],
           time=["creation_timestamp"],
           camera_metadata=["media_metadata.camera_metadata.has_camera_metadata"],
           title=["title"],
           post_shared_on_another_platform=["source_app"]

           
           
        )
    )

    df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
    df = df.sort_values("date")

    return df

# level03: stories

def stories_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/stories"])

    df = parse_json(data,
        row_path=["$.ig_stories"],  
        col_paths=dict(
           photo_uri=["uri"],
           time=["creation_timestamp"],
           video_device_id=["media_metadata.video_metadata.exif_data.device_id"],
           camera_position=["media_metadata.video_metadata.exif_data.camera_position"],
           date_time_original=["media_metadata.video_metadata.exif_data.date_time_original"],
           type_stories= ["media_metadata.video_metadata.exif_data.source_type"],
           camera_metadata=["camera_metadata.has_camera_metadata"]
           title=["title"],
           post_shared_on_another_platform=["source_app"],
           dubbing_info=["dubbing_info"],
           media_variants=["media_variants"]

           
           
        )
    )

    df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
    df = df.sort_values("date")

    return df

## level02: likes

# level03: liked_posts
def liked_posts_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/likes_media_likes"])

    df = parse_json(data,
        row_path=["$.ig_stories"],  
        col_paths=dict(
           title=["title"],
           post_link=["string_list_data.href"],
           like=["string_list_data.href"]

           
           
        )
    )

    df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
    df = df.sort_values("date")

    return df


## level02: saved

# level03: saved_collections
def saved_collections_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/saved_collections"])

    df = parse_json(data,
        row_path=["$.saved_saved_collections"],  
        col_paths=dict(
           title=["title"],
           name= ["string_map_data.Name.value"],
           time_collection=["Creation Time.timestamp"],
           Update_time_collection=["Update Time.timestamp"],
           profile_link=["string_map_data.Name.href"],
           username=["string_map_data.Name.value"],
           time_added= ["string_map_data.Added Time.timestamp"]


           
           
        )
    )

    df["date"] = pd.to_datetime(df["time_collection"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
    df = df.sort_values("date")

    return df


# level03: saved_posts
def saved_posts_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/saved_posts"])

    df = parse_json(data,
        row_path=["$.saved_saved_media"],  
        col_paths=dict(
           username=["title"],
           post_link=["string_map_data.Saved on.href"],
           time=["string_map_data.Saved on.timestamp"] 

           
           
        )
    )

    df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
    df = df.sort_values("date")

    return df

## level02: story_sticker_interactions

# level03: polls
def polls_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/polls"])

    df = parse_json(data,
        row_path=["$.story_activities_polls"],  
        col_paths=dict(
           username=["title"],
           reply=["string_list_data.value"],
           time=["string_list_data.timestamp"] 

           
           
        )
    )

    df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
    df = df.sort_values("date")

    return df

# level03: quizzes
def polls_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/quizzes"])

    df = parse_json(data,
        row_path=["$.story_activities_quizzes"],  
        col_paths=dict(
           username=["title"],
           reply=["string_list_data.value"],
           time=["string_list_data.timestamp"] 

           
           
        )
    )

    df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
    df = df.sort_values("date")

    return df


# level03: story_likes
def story_likes_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/story_likes"])

    df = parse_json(data,
        row_path=["$.story_activities_quizzes"],  
        col_paths=dict(
           username=["title"],
           time=["string_list_data.timestamp"] 

           
           
        )
    )

    df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
    df = df.sort_values("date")

    return df






############################################################################################
# CREATING THE DATA DONATION FLOW                                                          #
############################################################################################




def create_donation_flow(file_input: list[str]):
    ads_viewed_table = donation_table(
        name = " ads_viewed",
        df =  ads_viewed_df(file_input),
        title = {"en": "Example", "nl": "Voorbeeld"}
    )


    return donation_flow(
        id = "facebook",
        tables = [ads_clicked_table],
    )
