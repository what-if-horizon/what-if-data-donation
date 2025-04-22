# Auto-generated TikTok extractors

import pandas as pd
import logging
import json
from port.helpers.donation_flow import donation_table, donation_flow
from port.helpers.parsers import parse_json

logger = logging.getLogger(__name__)

def Ads_and_data_df(file_input: list[str]) -> pd.DataFrame:
    with open(file_input[0], 'r', encoding='utf-8') as f:
        full_data = json.load(f)
    df = parse_json(full_data,
        row_path=["$.Ads and data"],
        col_paths=dict(
            AdInterestCategories = ['Ad Interests.AdInterestCategories'],
            ResponsesList = ['Instant Form Ads Responses.ResponsesList'],
            OffTikTokActivityDataList = ['Off TikTok Activity.OffTikTokActivityDataList'],
        )
    )
    if 'time' in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")
    return df


def App_Settings_df(file_input: list[str]) -> pd.DataFrame:
    with open(file_input[0], 'r', encoding='utf-8') as f:
        full_data = json.load(f)
    df = parse_json(full_data,
        row_path=["$.App Settings"],
        col_paths=dict(
            App = ['Settings.App'],
            BlockList = ['Block List.BlockList'],
            Allow_DownLoad = ['Settings.SettingsMap.Allow DownLoad'],
            Allow_Others_to_Find_Me = ['Settings.SettingsMap.Allow Others to Find Me'],
            App_Language = ['Settings.SettingsMap.App Language'],
            Keyword_filters_for_videos_in_Following_feed = ['Settings.SettingsMap.Content Preferences.Keyword filters for videos in Following feed'],
            Keyword_filters_for_videos_in_For_You_feed = ['Settings.SettingsMap.Content Preferences.Keyword filters for videos in For You feed'],
            Video_Languages_Preferences = ['Settings.SettingsMap.Content Preferences.Video Languages Preferences'],
            Family_Content_Preferences = ['Settings.SettingsMap.Family Content Preferences'],
            Filter_Comments = ['Settings.SettingsMap.Filter Comments'],
            Interests = ['Settings.SettingsMap.Interests'],
            Private_Account = ['Settings.SettingsMap.Private Account'],
            Desktop_notification = ['Settings.SettingsMap.Push Notification.Desktop notification'],
            New_Comments_on_My_Video = ['Settings.SettingsMap.Push Notification.New Comments on My Video'],
            New_Fans = ['Settings.SettingsMap.Push Notification.New Fans'],
            New_Likes_on_My_Video = ['Settings.SettingsMap.Push Notification.New Likes on My Video'],
            Suggest_your_account_to_Facebook_friends = ['Settings.SettingsMap.Suggest your account to Facebook friends'],
            Suggest_your_account_to_contacts = ['Settings.SettingsMap.Suggest your account to contacts'],
            Suggest_your_account_to_people_who_open_or_send_links_to_you = ['Settings.SettingsMap.Suggest your account to people who open or send links to you'],
            Web_Language = ['Settings.SettingsMap.Web Language'],
            Who_Can_Duet_With_Me = ['Settings.SettingsMap.Who Can Duet With Me'],
            Who_Can_Post_Comments = ['Settings.SettingsMap.Who Can Post Comments'],
            Who_Can_Send_Me_Message = ['Settings.SettingsMap.Who Can Send Me Message'],
            Who_Can_Stitch_with_your_videos = ['Settings.SettingsMap.Who Can Stitch with your videos'],
            Who_Can_View_Videos_I_Liked = ['Settings.SettingsMap.Who Can View Videos I Liked'],
        )
    )
    if 'time' in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")
    return df


def Comment_df(file_input: list[str]) -> pd.DataFrame:
    with open(file_input[0], 'r', encoding='utf-8') as f:
        full_data = json.load(f)
    df = parse_json(full_data,
        row_path=["$.Comment"],
        col_paths=dict(
            App = ['Comments.App'],
            CommentsList = ['Comments.CommentsList'],
        )
    )
    if 'time' in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")
    return df


def Direct_Message_df(file_input: list[str]) -> pd.DataFrame:
    with open(file_input[0], 'r', encoding='utf-8') as f:
        full_data = json.load(f)
    df = parse_json(full_data,
        row_path=["$.Direct Message"],
        col_paths=dict(
            ChatHistory = ['Direct Messages.ChatHistory'],
        )
    )
    if 'time' in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")
    return df


def Income_Plus_Wallet_Transactions_df(file_input: list[str]) -> pd.DataFrame:
    with open(file_input[0], 'r', encoding='utf-8') as f:
        full_data = json.load(f)
    df = parse_json(full_data,
        row_path=["$.Income Plus Wallet Transactions"],
        col_paths=dict(
            TransactionsList = ['Transaction History.TransactionsList'],
        )
    )
    if 'time' in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")
    return df


def Location_Review_df(file_input: list[str]) -> pd.DataFrame:
    with open(file_input[0], 'r', encoding='utf-8') as f:
        full_data = json.load(f)
    df = parse_json(full_data,
        row_path=["$.Location Review"],
        col_paths=dict(
            ReviewsList = ['Location Reviews.ReviewsList'],
        )
    )
    if 'time' in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")
    return df


def Post_df(file_input: list[str]) -> pd.DataFrame:
    with open(file_input[0], 'r', encoding='utf-8') as f:
        full_data = json.load(f)
    df = parse_json(full_data,
        row_path=["$.Post"],
        col_paths=dict(
            VideoList = ['Posts.VideoList'],
            PostList = ['Recently Deleted Posts.PostList'],
        )
    )
    if 'time' in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")
    return df


def Profile_df(file_input: list[str]) -> pd.DataFrame:
    with open(file_input[0], 'r', encoding='utf-8') as f:
        full_data = json.load(f)
    df = parse_json(full_data,
        row_path=["$.Profile"],
        col_paths=dict(
            CreateDate = ['AI-Moji.CreateDate'],
            AIMojiList = ['AI-Moji.AIMojiList'],
            PhoneNumber = ['Autofill.PhoneNumber'],
            Email = ['Autofill.Email'],
            FirstName = ['Autofill.FirstName'],
            LastName = ['Autofill.LastName'],
            Address = ['Autofill.Address'],
            ZipCode = ['Autofill.ZipCode'],
            Unit = ['Autofill.Unit'],
            City = ['Autofill.City'],
            State = ['Autofill.State'],
            Country = ['Autofill.Country'],
            App = ['Profile Info.App'],
            Description = ['Profile Info.ProfileMap.PlatformInfo.Description'],
            Name = ['Profile Info.ProfileMap.PlatformInfo.Name'],
            Platform = ['Profile Info.ProfileMap.PlatformInfo.Platform'],
            Profile_Photo = ['Profile Info.ProfileMap.PlatformInfo.Profile Photo'],
            bioDescription = ['Profile Info.ProfileMap.bioDescription'],
            birthDate = ['Profile Info.ProfileMap.birthDate'],
            emailAddress = ['Profile Info.ProfileMap.emailAddress'],
            likesReceived = ['Profile Info.ProfileMap.likesReceived'],
            profilePhoto = ['Profile Info.ProfileMap.profilePhoto'],
            profileVideo = ['Profile Info.ProfileMap.profileVideo'],
            telephoneNumber = ['Profile Info.ProfileMap.telephoneNumber'],
            userName = ['Profile Info.ProfileMap.userName'],
        )
    )
    if 'time' in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")
    return df


def TikTok_Shop_df(file_input: list[str]) -> pd.DataFrame:
    with open(file_input[0], 'r', encoding='utf-8') as f:
        full_data = json.load(f)
    df = parse_json(full_data,
        row_path=["$.TikTok Shop"],
        col_paths=dict(
            CommunicationHistories = ['Communication With Shops.CommunicationHistories'],
            PayCard = ['Current Payment Information.PayCard'],
            CustomerSupportHistories = ['Customer Support History.CustomerSupportHistories'],
            OrderDisputeHistories = ['Order Dispute History.OrderDisputeHistories'],
            OrderHistories = ['Order History.OrderHistories'],
            ProductBrowsingHistories = ['Product Browsing History.ProductBrowsingHistories'],
            ProductReviewHistories = ['Product Reviews.ProductReviewHistories'],
            ReturnAndRefundHistories = ['Returns and Refunds History.ReturnAndRefundHistories'],
            SavedAddress = ['Saved Address Information.SavedAddress'],
            ShoppingCart = ['Shopping Cart List.ShoppingCart'],
            Vouchers = ['Vouchers.Vouchers'],
        )
    )
    if 'time' in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")
    return df


def Tiktok_Live_df(file_input: list[str]) -> pd.DataFrame:
    with open(file_input[0], 'r', encoding='utf-8') as f:
        full_data = json.load(f)
    df = parse_json(full_data,
        row_path=["$.Tiktok Live"],
        col_paths=dict(
            GoLiveList = ['Go Live History.GoLiveList'],
            Allow_agencies_to_find_and_invite_you = ['Go Live Settings.SettingsMap.Allow agencies to find and invite you'],
            Allow_others_to_invite_you_to_co_host_in_LIVE = ['Go Live Settings.SettingsMap.Allow others to invite you to co-host in LIVE'],
            Allow_people_to_send_and_receive_comments_during_your_LIVE = ['Go Live Settings.SettingsMap.Allow people to send and receive comments during your LIVE'],
            Allow_suggested_LIVE_hosts_to_invite_you_to_co_host_in_LIVE = ['Go Live Settings.SettingsMap.Allow suggested LIVE hosts to invite you to co-host in LIVE'],
            Allow_viewers_to_request_to_go_LIVE_with_you = ['Go Live Settings.SettingsMap.Allow viewers to request to go LIVE with you'],
            Allow_viewers_to_see_and_send_questions_and_answers_in_your_LIVE = ['Go Live Settings.SettingsMap.Allow viewers to see and send questions and answers in your LIVE'],
            Allow_viewers_to_send_you_gifts_during_your_LIVE = ['Go Live Settings.SettingsMap.Allow viewers to send you gifts during your LIVE'],
            Hide_comments_that_contain_the_following_keywords_from_your_LIVE = ['Go Live Settings.SettingsMap.Hide comments that contain the following keywords from your LIVE'],
            Hide_potential_spam_or_offensive_comments_from_your_LIVE = ['Go Live Settings.SettingsMap.Hide potential spam or offensive comments from your LIVE'],
            People_you_assigned_to_moderate_your_LIVE = ['Go Live Settings.SettingsMap.People you assigned to moderate your LIVE'],
            Show_your_username_and_gift_information_in_features_with_ranking_lists = ['Go Live Settings.SettingsMap.Show your username and gift information in features with ranking lists'],
            WatchLiveMap = ['Watch Live History.WatchLiveMap'],
            app = ['Watch Live Settings.WatchLiveSettingsMap.app'],
            web = ['Watch Live Settings.WatchLiveSettingsMap.web'],
            MostRecentModificationTimeInApp = ['Watch Live Settings.MostRecentModificationTimeInApp'],
            MostRecentModificationTimeInWeb = ['Watch Live Settings.MostRecentModificationTimeInWeb'],
        )
    )
    if 'time' in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")
    return df


def Your_Activity_df(file_input: list[str]) -> pd.DataFrame:
    with open(file_input[0], 'r', encoding='utf-8') as f:
        full_data = json.load(f)
    df = parse_json(full_data,
        row_path=["$.Your Activity"],
        col_paths=dict(
            note = ['Activity Summary.ActivitySummaryMap.note'],
            videosCommentedOnSinceAccountRegistration = ['Activity Summary.ActivitySummaryMap.videosCommentedOnSinceAccountRegistration'],
            videosSharedSinceAccountRegistration = ['Activity Summary.ActivitySummaryMap.videosSharedSinceAccountRegistration'],
            videosWatchedToTheEndSinceAccountRegistration = ['Activity Summary.ActivitySummaryMap.videosWatchedToTheEndSinceAccountRegistration'],
            FavoriteEffectsList = ['Favorite Effects.FavoriteEffectsList'],
            FavoriteHashtagList = ['Favorite Hashtags.FavoriteHashtagList'],
            FavoriteSoundList = ['Favorite Sounds.FavoriteSoundList'],
            App = ['Like List.App'],
            FavoriteVideoList = ['Favorite Videos.FavoriteVideoList'],
            IsFastLane = ['Following.IsFastLane'],
            FansList = ['Follower.FansList'],
            Following = ['Following.Following'],
            HashtagList = ['Hashtag.HashtagList'],
            ItemFavoriteList = ['Like List.ItemFavoriteList'],
            LoginHistoryList = ['Login History.LoginHistoryList'],
            Date = ['Watch History.VideoList.Date'],
            GpsData = ['Most Recent Location Data.LocationData.GpsData'],
            LastRegion = ['Most Recent Location Data.LocationData.LastRegion'],
            SendGifts = ['Purchases.SendGifts.SendGifts'],
            BuyGifts = ['Purchases.BuyGifts.BuyGifts'],
            SearchTerm = ['Searches.SearchList.SearchTerm'],
            ShareHistoryList = ['Share History.ShareHistoryList'],
            Resolution = ['Status.Status List.Resolution'],
            App_Version = ['Status.Status List.App Version'],
            IDFA = ['Status.Status List.IDFA'],
            GAID = ['Status.Status List.GAID'],
            Android_ID = ['Status.Status List.Android ID'],
            IDFV = ['Status.Status List.IDFV'],
            Web_ID = ['Status.Status List.Web ID'],
            Link = ['Watch History.VideoList.Link'],
        )
    )
    if 'time' in df.columns:
        df["date"] = pd.to_datetime(df["time"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
        df = df.sort_values("date")
    return df


def create_donation_flow(file_input: list[str]):
    """Creates a donation flow for TikTok data."""
    tables = []

    try:
        Ads_and_data_table = donation_table(
            name="Ads_and_data",
            df=Ads_and_data_df(file_input),
            title={"en": "Ads_and_data", "nl": "Ads_and_data"},
        )
        tables.append(Ads_and_data_table)
    except Exception as e:
        # print(f"Skipping Ads_and_data: {e}")
        pass

    try:
        App_Settings_table = donation_table(
            name="App_Settings",
            df=App_Settings_df(file_input),
            title={"en": "App_Settings", "nl": "App_Settings"},
        )
        tables.append(App_Settings_table)
    except Exception as e:
        # print(f"Skipping App_Settings: {e}")
        pass

    try:
        Comment_table = donation_table(
            name="Comment",
            df=Comment_df(file_input),
            title={"en": "Comment", "nl": "Comment"},
        )
        tables.append(Comment_table)
    except Exception as e:
        # print(f"Skipping Comment: {e}")
        pass

    try:
        Direct_Message_table = donation_table(
            name="Direct_Message",
            df=Direct_Message_df(file_input),
            title={"en": "Direct_Message", "nl": "Direct_Message"},
        )
        tables.append(Direct_Message_table)
    except Exception as e:
        # print(f"Skipping Direct_Message: {e}")
        pass

    try:
        Income_Plus_Wallet_Transactions_table = donation_table(
            name="Income_Plus_Wallet_Transactions",
            df=Income_Plus_Wallet_Transactions_df(file_input),
            title={"en": "Income_Plus_Wallet_Transactions", "nl": "Income_Plus_Wallet_Transactions"},
        )
        tables.append(Income_Plus_Wallet_Transactions_table)
    except Exception as e:
        # print(f"Skipping Income_Plus_Wallet_Transactions: {e}")
        pass

    try:
        Location_Review_table = donation_table(
            name="Location_Review",
            df=Location_Review_df(file_input),
            title={"en": "Location_Review", "nl": "Location_Review"},
        )
        tables.append(Location_Review_table)
    except Exception as e:
        # print(f"Skipping Location_Review: {e}")
        pass

    try:
        Post_table = donation_table(
            name="Post",
            df=Post_df(file_input),
            title={"en": "Post", "nl": "Post"},
        )
        tables.append(Post_table)
    except Exception as e:
        # print(f"Skipping Post: {e}")
        pass

    try:
        Profile_table = donation_table(
            name="Profile",
            df=Profile_df(file_input),
            title={"en": "Profile", "nl": "Profile"},
        )
        tables.append(Profile_table)
    except Exception as e:
        # print(f"Skipping Profile: {e}")
        pass

    try:
        TikTok_Shop_table = donation_table(
            name="TikTok_Shop",
            df=TikTok_Shop_df(file_input),
            title={"en": "TikTok_Shop", "nl": "TikTok_Shop"},
        )
        tables.append(TikTok_Shop_table)
    except Exception as e:
        # print(f"Skipping TikTok_Shop: {e}")
        pass

    try:
        Tiktok_Live_table = donation_table(
            name="Tiktok_Live",
            df=Tiktok_Live_df(file_input),
            title={"en": "Tiktok_Live", "nl": "Tiktok_Live"},
        )
        tables.append(Tiktok_Live_table)
    except Exception as e:
        # print(f"Skipping Tiktok_Live: {e}")
        pass

    try:
        Your_Activity_table = donation_table(
            name="Your_Activity",
            df=Your_Activity_df(file_input),
            title={"en": "Your_Activity", "nl": "Your_Activity"},
        )
        tables.append(Your_Activity_table)
    except Exception as e:
        # print(f"Skipping Your_Activity: {e}")
        pass

    if tables:
        return donation_flow(
            id="tiktok",
            tables=tables
        )
    else:
        return None