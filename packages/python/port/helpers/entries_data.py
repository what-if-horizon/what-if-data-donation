"""
Donation file structure data for takeout flows

This file contains a list of Entries for each platform.
Each Entry represents a table to be generated from the appropriate file.

To generate this file, please run structure/flow_generation/generate_entries.py
which will use the Merged_structures_*.csv to determine the required entries.
"""

from port.helpers.parsers import Entry, Node

TIKTOK_ENTRIES: dict[str, list[Entry]] = {
    'Activity': [
        Entry(table='Activity', filename=None, static_fields={'videosWatchedToTheEndSinceAccountRegistration': ('Activity', 'Activity Summary', 'ActivitySummaryMap', 'videosWatchedToTheEndSinceAccountRegistration'), 'videosSharedSinceAccountRegistration': ('Activity', 'Activity Summary', 'ActivitySummaryMap', 'videosSharedSinceAccountRegistration'), 'videosCommentedOnSinceAccountRegistration': ('Activity', 'Activity Summary', 'ActivitySummaryMap', 'videosCommentedOnSinceAccountRegistration')}, tree=Node(columns={}, children={'Activity': Node(columns={}, children={'Like List': Node(columns={}, children={'ItemFavoriteList': Node(columns={'link': ('link',), 'date': ('date',)}, children={})}), 'Follower List': Node(columns={}, children={'FansList': Node(columns={'UserName': ('UserName',), 'Date': ('Date',)}, children={})}), 'Following List': Node(columns={}, children={'Following': Node(columns={'UserName': ('UserName',), 'Date': ('Date',)}, children={})}), 'Search History': Node(columns={}, children={'SearchList': Node(columns={'SearchTerm': ('SearchTerm',), 'Date': ('Date',)}, children={})}), 'Video Browsing History': Node(columns={}, children={'VideoList': Node(columns={'Link': ('Link',), 'Date': ('Date',)}, children={})}), 'Share History': Node(columns={}, children={'ShareHistoryList': Node(columns={'Link': ('Link',), 'Date': ('Date',)}, children={})}), 'Favorite Videos': Node(columns={}, children={'FavoriteVideoList': Node(columns={'Link': ('Link',), 'Date': ('Date',)}, children={})}), 'Hashtag': Node(columns={}, children={'HashtagList': Node(columns={'HashtagName': ('HashtagName',), 'HashtagLink': ('HashtagLink',)}, children={})})})})),
    ],
    'Ads And Data': [
        Entry(table='Ads And Data', filename=None, static_fields={'ResponsesList': ('Ads and data', 'Instant Form Ads Responses', 'ResponsesList'), 'AdInterestCategories': ('Ads and data', 'Ad Interests', 'AdInterestCategories')}, tree=Node(columns={}, children={})),
    ],
    'App Settings': [
        Entry(table='App Settings', filename=None, static_fields={'Who Can View Videos I Liked': ('App Settings', 'Settings', 'SettingsMap', 'Who Can View Videos I Liked'), 'Who Can Stitch with your videos': ('App Settings', 'Settings', 'SettingsMap', 'Who Can Stitch with your videos'), 'Who Can Send Me Message': ('App Settings', 'Settings', 'SettingsMap', 'Who Can Send Me Message'), 'Who Can Post Comments': ('App Settings', 'Settings', 'SettingsMap', 'Who Can Post Comments'), 'Who Can Duet With Me': ('App Settings', 'Settings', 'SettingsMap', 'Who Can Duet With Me'), 'Web Language': ('App Settings', 'Settings', 'SettingsMap', 'Web Language'), 'Private Account': ('App Settings', 'Settings', 'SettingsMap', 'Private Account'), 'Personalized Ads': ('App Settings', 'Settings', 'SettingsMap', 'Personalized Ads'), 'Interests': ('App Settings', 'Settings', 'SettingsMap', 'Interests'), 'Filter Comments': ('App Settings', 'Settings', 'SettingsMap', 'Filter Comments'), 'Video Languages Preferences': ('App Settings', 'Settings', 'SettingsMap', 'Content Preferences', 'Video Languages Preferences'), 'Keyword filters for videos in For You feed': ('App Settings', 'Settings', 'SettingsMap', 'Content Preferences', 'Keyword filters for videos in For You feed'), 'Keyword filters for videos in Following feed': ('App Settings', 'Settings', 'SettingsMap', 'Content Preferences', 'Keyword filters for videos in Following feed'), 'App Language': ('App Settings', 'Settings', 'SettingsMap', 'App Language'), 'BlockList': ('App Settings', 'Block List', 'BlockList')}, tree=Node(columns={}, children={'App Settings': Node(columns={}, children={'Block': Node(columns={}, children={'BlockList': Node(columns={'UserName': ('UserName',), 'Date': ('Date',)}, children={})})})})),
    ],
    'Comment': [
        Entry(table='Comment', filename=None, static_fields={'CommentsList': ('Comment', 'Comments', 'CommentsList')}, tree=Node(columns={}, children={'Comment': Node(columns={}, children={'Comments': Node(columns={}, children={'CommentsList': Node(columns={'url': ('url',), 'photo': ('photo',), 'date': ('date',), 'comment': ('comment',)}, children={})})})})),
    ],
    'Post': [
        Entry(table='Post', filename=None, static_fields={'VideoList': ('Post', 'Posts', 'VideoList')}, tree=Node(columns={}, children={'Post': Node(columns={}, children={'Posts': Node(columns={}, children={'VideoList': Node(columns={'WhoCanView': ('WhoCanView',), 'Title': ('Title',), 'Sound': ('Sound',), 'Location': ('Location',), 'Link': ('Link',), 'Likes': ('Likes',), 'Date': ('Date',), 'ContentDisclosure': ('ContentDisclosure',), 'AllowStitches': ('AllowStitches',), 'AllowStickers': ('AllowStickers',), 'AllowSharingToStory': ('AllowSharingToStory',), 'AllowDuets': ('AllowDuets',), 'AllowComments': ('AllowComments',), 'AddYoursText': ('AddYoursText',), 'AIGeneratedContent': ('AIGeneratedContent',)}, children={})})})})),
    ],
    'Profile': [
        Entry(table='Profile', filename=None, static_fields={'userName': ('Profile', 'Profile Info', 'ProfileMap', 'userName'), 'likesReceived': ('Profile', 'Profile Info', 'ProfileMap', 'likesReceived')}, tree=Node(columns={}, children={})),
    ],
    'Tiktok Live': [
        Entry(table='Tiktok Live', filename=None, static_fields={'Show your username and gift information in features with ranking lists': ('Tiktok Live', 'Go Live Settings', 'SettingsMap', 'Show your username and gift information in features with ranking lists'), 'People you assigned to moderate your LIVE': ('Tiktok Live', 'Go Live Settings', 'SettingsMap', 'People you assigned to moderate your LIVE'), 'Hide potential spam or offensive comments from your LIVE': ('Tiktok Live', 'Go Live Settings', 'SettingsMap', 'Hide potential spam or offensive comments from your LIVE'), 'Hide comments that contain the following keywords from your LIVE': ('Tiktok Live', 'Go Live Settings', 'SettingsMap', 'Hide comments that contain the following keywords from your LIVE'), 'Allow viewers to send you gifts during your LIVE': ('Tiktok Live', 'Go Live Settings', 'SettingsMap', 'Allow viewers to send you gifts during your LIVE'), 'Allow viewers to see and send questions and answers in your LIVE': ('Tiktok Live', 'Go Live Settings', 'SettingsMap', 'Allow viewers to see and send questions and answers in your LIVE'), 'Allow viewers to request to go LIVE with you': ('Tiktok Live', 'Go Live Settings', 'SettingsMap', 'Allow viewers to request to go LIVE with you'), 'Allow suggested LIVE hosts to invite you to co-host in LIVE': ('Tiktok Live', 'Go Live Settings', 'SettingsMap', 'Allow suggested LIVE hosts to invite you to co-host in LIVE'), 'Allow people to send and receive comments during your LIVE': ('Tiktok Live', 'Go Live Settings', 'SettingsMap', 'Allow people to send and receive comments during your LIVE'), 'Allow others to invite you to co-host in LIVE': ('Tiktok Live', 'Go Live Settings', 'SettingsMap', 'Allow others to invite you to co-host in LIVE'), 'Allow agencies to find and invite you': ('Tiktok Live', 'Go Live Settings', 'SettingsMap', 'Allow agencies to find and invite you'), 'GoLiveList': ('Tiktok Live', 'Go Live History', 'GoLiveList')}, tree=Node(columns={}, children={'Tiktok Live': Node(columns={}, children={'Go Live Settings': Node(columns={}, children={'SettingsMap': Node(columns={}, children={'People you assigned to moderate your LIVE': Node(columns={'People you assigned to moderate your LIVE': ()}, children={}), 'Hide comments that contain the following keywords from your LIVE': Node(columns={'Hide comments that contain the following keywords from your LIVE': ()}, children={})})})})})),
    ],
    'Video': [
        Entry(table='Video', filename=None, static_fields={}, tree=Node(columns={}, children={'Video': Node(columns={}, children={'Videos': Node(columns={}, children={'VideoList': Node(columns={'WhoCanView': ('WhoCanView',), 'Title': ('Title',), 'Sound': ('Sound',), 'Location': ('Location',), 'Link': ('Link',), 'Likes': ('Likes',), 'Date': ('Date',), 'ContentDisclosure': ('ContentDisclosure',), 'AllowStitches': ('AllowStitches',), 'AllowStickers': ('AllowStickers',), 'AllowSharingToStory': ('AllowSharingToStory',), 'AllowDuets': ('AllowDuets',), 'AllowComments': ('AllowComments',), 'AddYoursText': ('AddYoursText',), 'AIGeneratedContent': ('AIGeneratedContent',)}, children={})})})})),
    ],
    'Your Activity': [
        Entry(table='Your Activity', filename=None, static_fields={'ShareHistoryList': ('Your Activity', 'Share History', 'ShareHistoryList'), 'ItemFavoriteList': ('Your Activity', 'Like List', 'ItemFavoriteList'), 'HashtagList': ('Your Activity', 'Hashtag', 'HashtagList'), 'Following': ('Your Activity', 'Following', 'Following'), 'FansList': ('Your Activity', 'Follower', 'FansList'), 'FavoriteVideoList': ('Your Activity', 'Favorite Videos', 'FavoriteVideoList'), 'FavoriteSoundList': ('Your Activity', 'Favorite Sounds', 'FavoriteSoundList'), 'FavoriteHashtagList': ('Your Activity', 'Favorite Hashtags', 'FavoriteHashtagList'), 'FavoriteEffectsList': ('Your Activity', 'Favorite Effects', 'FavoriteEffectsList'), 'videosWatchedToTheEndSinceAccountRegistration': ('Your Activity', 'Activity Summary', 'ActivitySummaryMap', 'videosWatchedToTheEndSinceAccountRegistration'), 'videosSharedSinceAccountRegistration': ('Your Activity', 'Activity Summary', 'ActivitySummaryMap', 'videosSharedSinceAccountRegistration'), 'videosCommentedOnSinceAccountRegistration': ('Your Activity', 'Activity Summary', 'ActivitySummaryMap', 'videosCommentedOnSinceAccountRegistration')}, tree=Node(columns={}, children={'Your Activity': Node(columns={}, children={'Like List': Node(columns={}, children={'ItemFavoriteList': Node(columns={'link': ('link',), 'date': ('date',)}, children={})}), 'Follower': Node(columns={}, children={'FansList': Node(columns={'UserName': ('UserName',), 'Date': ('Date',)}, children={})}), 'Following': Node(columns={}, children={'Following': Node(columns={'UserName': ('UserName',), 'Date': ('Date',)}, children={})}), 'Searches': Node(columns={}, children={'SearchList': Node(columns={'SearchTerm': ('SearchTerm',), 'Date': ('Date',)}, children={})}), 'Watch History': Node(columns={}, children={'VideoList': Node(columns={'Link': ('Link',), 'Date': ('Date',)}, children={})}), 'Favorite Sounds': Node(columns={}, children={'FavoriteSoundList': Node(columns={'Link': ('Link',), 'Date': ('Date',)}, children={})}), 'Favorite Videos': Node(columns={}, children={'FavoriteVideoList': Node(columns={'Link': ('Link',), 'Date': ('Date',)}, children={})}), 'Hashtag': Node(columns={}, children={'HashtagList': Node(columns={'HashtagName': ('HashtagName',), 'HashtagLink': ('HashtagLink',)}, children={})}), 'Favorite Effects': Node(columns={}, children={'FavoriteEffectsList': Node(columns={'EffectLink': ('EffectLink',), 'Date': ('Date',)}, children={})})})})),
    ],
}

X_ENTRIES: dict[str, list[Entry]] = {
    'Account': [
        Entry(table='Account', filename='data/account.js', static_fields={'accountId': ('account', 'accountId'), 'createdAt': ('account', 'createdAt')}, tree=Node(columns={}, children={})),
    ],
    'Account-Suspension': [
        Entry(table='Account-Suspension', filename='data/account-suspension.js', static_fields={}, tree=Node(columns={}, children={})),
    ],
    'Ad-Engagements': [
        Entry(table='Ad-Engagements', filename='data/ad-engagements.js', static_fields={}, tree=Node(columns={}, children={'ad': Node(columns={}, children={'adsUserData': Node(columns={}, children={'adEngagements': Node(columns={}, children={'engagements': Node(columns={'displayLocation': ('impressionAttributes', 'displayLocation'), 'impressionTime': ('impressionAttributes', 'impressionTime'), 'tweetId': ('impressionAttributes', 'promotedTweetInfo', 'tweetId'), 'tweetText': ('impressionAttributes', 'promotedTweetInfo', 'tweetText'), 'urls': ('impressionAttributes', 'promotedTweetInfo', 'urls'), 'mediaUrls': ('impressionAttributes', 'promotedTweetInfo', 'mediaUrls'), 'advertiserName': ('impressionAttributes', 'advertiserInfo', 'advertiserName'), 'screenName': ('impressionAttributes', 'publisherInfo', 'screenName'), 'trendId': ('impressionAttributes', 'promotedTrendInfo', 'trendId'), 'name': ('impressionAttributes', 'promotedTrendInfo', 'name'), 'description': ('impressionAttributes', 'promotedTrendInfo', 'description'), 'publisherName': ('impressionAttributes', 'publisherInfo', 'publisherName')}, children={'engagementAttributes': Node(columns={'engagementTime': ('engagementTime',), 'engagementType': ('engagementType',)}, children={}), 'impressionAttributes': Node(columns={}, children={'matchedTargetingCriteria': Node(columns={'targetingType': ('targetingType',), 'targetingValue': ('targetingValue',)}, children={})})})})})})})),
    ],
    'Ad-Impressions': [
        Entry(table='Ad-Impressions', filename='data/ad-impressions.js', static_fields={}, tree=Node(columns={}, children={})),
    ],
    'Ad-Mobile-Conversions-Attributed': [
        Entry(table='Ad-Mobile-Conversions-Attributed', filename='data/ad-mobile-conversions-attributed.js', static_fields={}, tree=Node(columns={}, children={})),
    ],
    'Ad-Mobile-Conversions-Unattributed': [
        Entry(table='Ad-Mobile-Conversions-Unattributed', filename='data/ad-mobile-conversions-unattributed.js', static_fields={}, tree=Node(columns={}, children={})),
    ],
    'Ad-Online-Conversions-Attributed': [
        Entry(table='Ad-Online-Conversions-Attributed', filename='data/ad-online-conversions-attributed.js', static_fields={}, tree=Node(columns={}, children={})),
    ],
    'Ad-Online-Conversions-Unattributed': [
        Entry(table='Ad-Online-Conversions-Unattributed', filename='data/ad-online-conversions-unattributed.js', static_fields={}, tree=Node(columns={}, children={})),
    ],
    'Article': [
        Entry(table='Article', filename='data/article.js', static_fields={}, tree=Node(columns={}, children={})),
    ],
    'Article-Metadata': [
        Entry(table='Article-Metadata', filename='data/article-metadata.js', static_fields={}, tree=Node(columns={}, children={})),
    ],
    'Block': [
        Entry(table='Block', filename='data/block.js', static_fields={}, tree=Node(columns={}, children={})),
    ],
    'Community-Note': [
        Entry(table='Community-Note', filename='data/community-note.js', static_fields={}, tree=Node(columns={}, children={})),
    ],
    'Community-Note-Batsignal': [
        Entry(table='Community-Note-Batsignal', filename='data/community-note-batsignal.js', static_fields={}, tree=Node(columns={}, children={})),
    ],
    'Community-Note-Rating': [
        Entry(table='Community-Note-Rating', filename='data/community-note-rating.js', static_fields={'noteId': ('communityNoteRating', 'noteId'), 'helpfulnessLevel': ('communityNoteRating', 'helpfulnessLevel'), 'createdAt': ('communityNoteRating', 'createdAt'), 'userId': ('communityNoteRating', 'userId'), 'helpfulTags': ('communityNoteRating', 'helpfulTags')}, tree=Node(columns={}, children={})),
    ],
    'Community-Note-Tombstone': [
        Entry(table='Community-Note-Tombstone', filename='data/community-note-tombstone.js', static_fields={}, tree=Node(columns={}, children={})),
    ],
    'Community-Tweet': [
        Entry(table='Community-Tweet', filename='data/community-tweet.js', static_fields={}, tree=Node(columns={}, children={})),
    ],
    'Follower': [
        Entry(table='Follower', filename='data/follower.js', static_fields={'accountId': ('follower', 'accountId'), 'userLink': ('follower', 'userLink')}, tree=Node(columns={}, children={})),
    ],
    'Following': [
        Entry(table='Following', filename='data/following.js', static_fields={'accountId': ('following', 'accountId'), 'userLink': ('following', 'userLink')}, tree=Node(columns={}, children={})),
    ],
    'Grok-Chat-Item': [
        Entry(table='Grok-Chat-Item', filename='data/grok-chat-item.js', static_fields={}, tree=Node(columns={}, children={})),
    ],
    'Like': [
        Entry(table='Like', filename='data/like.js', static_fields={'tweetId': ('like', 'tweetId'), 'fullText': ('like', 'fullText'), 'expandedUrl': ('like', 'expandedUrl')}, tree=Node(columns={}, children={})),
    ],
    'Lists-Created': [
        Entry(table='Lists-Created', filename='data/lists-created.js', static_fields={'url': ('userListInfo', 'url')}, tree=Node(columns={}, children={})),
    ],
    'Lists-Member': [
        Entry(table='Lists-Member', filename='data/lists-member.js', static_fields={'url': ('userListInfo', 'url')}, tree=Node(columns={}, children={})),
    ],
    'Lists-Subscribed': [
        Entry(table='Lists-Subscribed', filename='data/lists-subscribed.js', static_fields={'url': ('userListInfo', 'url')}, tree=Node(columns={}, children={})),
    ],
    'Manifest': [
        Entry(table='Manifest', filename='data/manifest.js', static_fields={'generationDate': ('archiveInfo', 'generationDate')}, tree=Node(columns={}, children={})),
    ],
    'Moment': [
        Entry(table='Moment', filename='data/moment.js', static_fields={}, tree=Node(columns={}, children={})),
    ],
    'Mute': [
        Entry(table='Mute', filename='data/mute.js', static_fields={}, tree=Node(columns={}, children={})),
    ],
    'Note-Tweet': [
        Entry(table='Note-Tweet', filename='data/note-tweet.js', static_fields={}, tree=Node(columns={}, children={})),
    ],
    'Personalization': [
        Entry(table='Personalization', filename='data/personalization.js', static_fields={'shows': ('p13nData', 'interests', 'shows'), 'age': ('p13nData', 'inferredAgeInfo', 'age'), 'birthDate': ('p13nData', 'inferredAgeInfo', 'birthDate'), 'gender': ('p13nData', 'demographics', 'genderInfo', 'gender'), 'lookalikeAdvertisers': ('p13nData', 'interests', 'audienceAndAdvertisers', 'lookalikeAdvertisers'), 'advertisers': ('p13nData', 'interests', 'audienceAndAdvertisers', 'advertisers'), 'numAudiences': ('p13nData', 'interests', 'audienceAndAdvertisers', 'numAudiences')}, tree=Node(columns={}, children={'p13nData': Node(columns={}, children={'demographics': Node(columns={}, children={'languages': Node(columns={'language': ('language',), 'isDisabled': ('isDisabled',)}, children={})}), 'interests': Node(columns={}, children={'interests': Node(columns={'name': ('name',), 'isDisabled': ('isDisabled',)}, children={})})})})),
    ],
    'Professional-Data': [
        Entry(table='Professional-Data', filename='data/professional-data.js', static_fields={}, tree=Node(columns={}, children={})),
    ],
    'Protected-History': [
        Entry(table='Protected-History', filename='data/protected-history.js', static_fields={}, tree=Node(columns={}, children={})),
    ],
    'Reply-Prompt': [
        Entry(table='Reply-Prompt', filename='data/reply-prompt.js', static_fields={}, tree=Node(columns={}, children={})),
    ],
    'Saved-Search': [
        Entry(table='Saved-Search', filename='data/saved-search.js', static_fields={'savedSearchId': ('savedSearch', 'savedSearchId'), 'query': ('savedSearch', 'query')}, tree=Node(columns={}, children={})),
    ],
    'Smartblock': [
        Entry(table='Smartblock', filename='data/smartblock.js', static_fields={}, tree=Node(columns={}, children={})),
    ],
    'Spaces-Metadata': [
        Entry(table='Spaces-Metadata', filename='data/spaces-metadata.js', static_fields={}, tree=Node(columns={}, children={})),
    ],
    'Tweet-Headers': [
        Entry(table='Tweet-Headers', filename='data/tweet-headers.js', static_fields={'user_id': ('tweet', 'user_id')}, tree=Node(columns={}, children={})),
    ],
    'Tweetdeck': [
        Entry(table='Tweetdeck', filename='data/tweetdeck.js', static_fields={}, tree=Node(columns={}, children={})),
    ],
    'Tweets': [
        Entry(table='Tweets', filename='data/tweets.js', static_fields={'retweeted': ('tweet', 'retweeted'), 'source': ('tweet', 'source'), 'display_text_range': ('tweet', 'display_text_range'), 'favorite_count': ('tweet', 'favorite_count'), 'id_str': ('tweet', 'id_str'), 'truncated': ('tweet', 'truncated'), 'retweet_count': ('tweet', 'retweet_count'), 'id': ('tweet', 'id'), 'possibly_sensitive': ('tweet', 'possibly_sensitive'), 'created_at': ('tweet', 'created_at'), 'favorited': ('tweet', 'favorited'), 'full_text': ('tweet', 'full_text'), 'lang': ('tweet', 'lang'), 'in_reply_to_status_id_str': ('tweet', 'in_reply_to_status_id_str'), 'in_reply_to_user_id': ('tweet', 'in_reply_to_user_id'), 'in_reply_to_status_id': ('tweet', 'in_reply_to_status_id'), 'in_reply_to_screen_name': ('tweet', 'in_reply_to_screen_name'), 'in_reply_to_user_id_str': ('tweet', 'in_reply_to_user_id_str'), 'editTweetIds': ('tweet', 'edit_info', 'initial', 'editTweetIds'), 'editableUntil': ('tweet', 'edit_info', 'initial', 'editableUntil'), 'editsRemaining': ('tweet', 'edit_info', 'initial', 'editsRemaining'), 'isEditEligible': ('tweet', 'edit_info', 'initial', 'isEditEligible')}, tree=Node(columns={}, children={'tweet': Node(columns={}, children={'entities': Node(columns={}, children={'urls': Node(columns={'url': ('url',), 'expanded_url': ('expanded_url',), 'display_url': ('display_url',), 'indices': ('indices',)}, children={}), 'user_mentions': Node(columns={'name': ('name',), 'screen_name': ('screen_name',), 'indices': ('indices',), 'id_str': ('id_str',), 'id': ('id',)}, children={}), 'hashtags': Node(columns={'text': ('text',), 'indices': ('indices',)}, children={}), 'media': Node(columns={'media_url_https': ('media_url_https',), 'source_status_id_str': ('source_status_id_str',)}, children={})})})})),
    ],
    'User-Link-Clicks': [
        Entry(table='User-Link-Clicks', filename='data/user-link-clicks.js', static_fields={}, tree=Node(columns={}, children={})),
    ],
    'Verified': [
        Entry(table='Verified', filename='data/verified.js', static_fields={'verified': ('verified', 'verified')}, tree=Node(columns={}, children={})),
    ],
}

IG_ENTRIES: dict[str, list[Entry]] = {
    'Ads About Meta': [
        Entry(table='Ads About Meta', filename='ads_information/instagram_ads_and_businesses/ads_about_meta.json', static_fields={'media': ('media',), 'fbid': ('fbid',), 'ent_name': ('ent_name',)}, tree=Node(columns={}, children={'label_values': Node(columns={'ent_field_name': ('ent_field_name',), 'label': ('label',), 'value': ('value',), 'timestamp_value': ('timestamp_value',)}, children={})})),
    ],
    'Ads Clicked': [
        Entry(table='Ads Clicked', filename='ads_information/ads_and_topics/ads_clicked.json', static_fields={}, tree=Node(columns={}, children={'impressions_history_ads_clicked': Node(columns={'title': ('title',)}, children={'string_list_data': Node(columns={'timestamp': ('timestamp',)}, children={})})})),
    ],
    'Ads Viewed': [
        Entry(table='Ads Viewed', filename='ads_information/ads_and_topics/ads_viewed.json', static_fields={}, tree=Node(columns={}, children={'impressions_history_ads_seen': Node(columns={'value': ('string_map_data', 'Author', 'value'), 'timestamp': ('string_map_data', 'Time', 'timestamp')}, children={})})),
    ],
    'Advertisers Using Your Activity Or Information': [
        Entry(table='Advertisers Using Your Activity Or Information', filename='ads_information/instagram_ads_and_businesses/advertisers_using_your_activity_or_information.json', static_fields={}, tree=Node(columns={}, children={'ig_custom_audiences_all_types': Node(columns={'advertiser_name': ('advertiser_name',), 'has_data_file_custom_audience': ('has_data_file_custom_audience',), 'has_remarketing_custom_audience': ('has_remarketing_custom_audience',), 'has_in_person_store_visit': ('has_in_person_store_visit',)}, children={})})),
    ],
    'Blocked Profiles': [
        Entry(table='Blocked Profiles', filename='connections/followers_and_following/blocked_profiles.json', static_fields={}, tree=Node(columns={}, children={'relationships_blocked_users': Node(columns={'title': ('title',)}, children={'string_list_data': Node(columns={'href': ('href',), 'timestamp': ('timestamp',)}, children={})})})),
    ],
    'Close Friends': [
        Entry(table='Close Friends', filename='connections/followers_and_following/close_friends.json', static_fields={}, tree=Node(columns={}, children={'relationships_close_friends': Node(columns={'title': ('title',), 'media_list_data': ('media_list_data',)}, children={'string_list_data': Node(columns={'href': ('href',), 'value': ('value',), 'timestamp': ('timestamp',)}, children={})})})),
    ],
    'Comments Allowed From': [
        Entry(table='Comments Allowed From', filename='preferences/media_settings/comments_allowed_from.json', static_fields={}, tree=Node(columns={}, children={'settings_allow_comments_from': Node(columns={'title': ('title',), 'href': ('string_map_data', 'Comments Allowed From', 'href'), 'value': ('string_map_data', 'Comments Allowed From', 'value'), 'timestamp': ('string_map_data', 'Comments Allowed From', 'timestamp')}, children={})})),
        Entry(table='Comments Allowed From', filename='preferences/settings/comments_allowed_from.json', static_fields={}, tree=Node(columns={}, children={'settings_allow_comments_from': Node(columns={'title': ('title',), 'href': ('string_map_data', 'Comments Allowed From', 'href'), 'value': ('string_map_data', 'Comments Allowed From', 'value'), 'timestamp': ('string_map_data', 'Comments Allowed From', 'timestamp')}, children={})})),
    ],
    'Consents': [
        Entry(table='Consents', filename='preferences/media_settings/consents.json', static_fields={'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',), 'ent_name': ('ent_name',)}, tree=Node(columns={}, children={'label_values': Node(columns={'ent_field_name': ('ent_field_name',), 'label': ('label',), 'timestamp_value': ('timestamp_value',)}, children={})})),
        Entry(table='Consents', filename='preferences/settings/consents.json', static_fields={'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',), 'ent_name': ('ent_name',)}, tree=Node(columns={}, children={'label_values': Node(columns={'ent_field_name': ('ent_field_name',), 'label': ('label',), 'timestamp_value': ('timestamp_value',)}, children={})})),
    ],
    'Emoji Sliders': [
        Entry(table='Emoji Sliders', filename='your_instagram_activity/story_sticker_interactions/emoji_sliders.json', static_fields={}, tree=Node(columns={}, children={'story_activities_emoji_sliders': Node(columns={'title': ('title',)}, children={'string_list_data': Node(columns={'value': ('value',), 'timestamp': ('timestamp',)}, children={})})})),
    ],
    "Follow Requests You'Ve Received": [
        Entry(table="Follow Requests You'Ve Received", filename="connections/followers_and_following/follow_requests_you've_received.json", static_fields={}, tree=Node(columns={}, children={'relationships_follow_requests_received': Node(columns={'title': ('title',), 'media_list_data': ('media_list_data',)}, children={'string_list_data': Node(columns={'href': ('href',), 'value': ('value',), 'timestamp': ('timestamp',)}, children={})})})),
    ],
    'Followers 1': [
        Entry(table='Followers 1', filename='connections/followers_and_following/followers_1.json', static_fields={'title': ('title',), 'media_list_data': ('media_list_data',)}, tree=Node(columns={'title': ('title',), 'media_list_data': ('media_list_data',)}, children={'string_list_data': Node(columns={'href': ('href',), 'value': ('value',), 'timestamp': ('timestamp',)}, children={})})),
    ],
    'Following': [
        Entry(table='Following', filename='connections/followers_and_following/following.json', static_fields={}, tree=Node(columns={}, children={'relationships_following': Node(columns={'title': ('title',), 'media_list_data': ('media_list_data',)}, children={'string_list_data': Node(columns={'href': ('href',), 'value': ('value',), 'timestamp': ('timestamp',)}, children={})})})),
    ],
    'Following Hashtags': [
        Entry(table='Following Hashtags', filename='connections/followers_and_following/following_hashtags.json', static_fields={}, tree=Node(columns={}, children={'relationships_following_hashtags': Node(columns={'title': ('title',), 'media_list_data': ('media_list_data',)}, children={'string_list_data': Node(columns={'href': ('href',), 'value': ('value',), 'timestamp': ('timestamp',)}, children={})})})),
    ],
    'Instagram Signup Details': [
        Entry(table='Instagram Signup Details', filename='security_and_login_information/login_and_profile_creation/instagram_signup_details.json', static_fields={}, tree=Node(columns={}, children={'account_history_registration_info': Node(columns={'timestamp': ('string_map_data', 'Time', 'timestamp')}, children={})})),
    ],
    'Liked Comments': [
        Entry(table='Liked Comments', filename='your_instagram_activity/likes/liked_comments.json', static_fields={}, tree=Node(columns={}, children={'likes_comment_likes': Node(columns={'title': ('title',)}, children={'string_list_data': Node(columns={'href': ('href',), 'value': ('value',), 'timestamp': ('timestamp',)}, children={})})})),
    ],
    'Liked Posts': [
        Entry(table='Liked Posts', filename='your_instagram_activity/likes/liked_posts.json', static_fields={}, tree=Node(columns={}, children={'likes_media_likes': Node(columns={'title': ('title',)}, children={'string_list_data': Node(columns={'href': ('href',), 'value': ('value',), 'timestamp': ('timestamp',)}, children={})})})),
    ],
    'Other Categories Used To Reach You': [
        Entry(table='Other Categories Used To Reach You', filename='ads_information/instagram_ads_and_businesses/other_categories_used_to_reach_you.json', static_fields={'media': ('media',), 'fbid': ('fbid',), 'ent_name': ('ent_name',)}, tree=Node(columns={}, children={'label_values': Node(columns={'ent_field_name': ('ent_field_name',), 'label': ('label',)}, children={'vec': Node(columns={'value': ('value',)}, children={})})})),
    ],
    'Personal Information': [
        Entry(table='Personal Information', filename='personal_information/personal_information/personal_information.json', static_fields={}, tree=Node(columns={}, children={'profile_user': Node(columns={'href': ('string_map_data', 'Private Account', 'href'), 'value': ('string_map_data', 'Private Account', 'value'), 'timestamp': ('string_map_data', 'Private Account', 'timestamp')}, children={})})),
    ],
    'Polls': [
        Entry(table='Polls', filename='your_instagram_activity/story_interactions/polls.json', static_fields={}, tree=Node(columns={}, children={'story_activities_polls': Node(columns={'title': ('title',)}, children={'string_list_data': Node(columns={'value': ('value',), 'timestamp': ('timestamp',)}, children={})})})),
        Entry(table='Polls', filename='your_instagram_activity/story_sticker_interactions/polls.json', static_fields={}, tree=Node(columns={}, children={'story_activities_polls': Node(columns={'title': ('title',)}, children={'string_list_data': Node(columns={'value': ('value',), 'timestamp': ('timestamp',)}, children={})})})),
    ],
    'Post Comments 1': [
        Entry(table='Post Comments 1', filename='your_instagram_activity/comments/post_comments_1.json', static_fields={'value': ('string_map_data', 'Media Owner', 'value'), 'timestamp': ('string_map_data', 'Time', 'timestamp')}, tree=Node(columns={'value': ('string_map_data', 'Media Owner', 'value'), 'timestamp': ('string_map_data', 'Time', 'timestamp')}, children={'media_list_data': Node(columns={'uri': ('uri',)}, children={})})),
    ],
    'Posts 1': [
        Entry(table='Posts 1', filename='your_instagram_activity/content/posts_1.json', static_fields={'title': ('title',), 'creation_timestamp': ('creation_timestamp',)}, tree=Node(columns={}, children={'media': Node(columns={'uri': ('uri',), 'creation_timestamp': ('creation_timestamp',), 'title': ('title',), 'source_app': ('cross_post_source', 'source_app'), 'has_camera_metadata': ('media_metadata', 'camera_metadata', 'has_camera_metadata')}, children={})})),
        Entry(table='Posts 1', filename='your_instagram_activity/media/posts_1.json', static_fields={}, tree=Node(columns={'title': ('title',), 'creation_timestamp': ('creation_timestamp',)}, children={'media': Node(columns={'uri': ('uri',), 'creation_timestamp': ('creation_timestamp',), 'title': ('title',), 'source_app': ('cross_post_source', 'source_app')}, children={})})),
    ],
    'Posts Viewed': [
        Entry(table='Posts Viewed', filename='ads_information/ads_and_topics/posts_viewed.json', static_fields={}, tree=Node(columns={}, children={'impressions_history_posts_seen': Node(columns={'value': ('string_map_data', 'Author', 'value'), 'timestamp': ('string_map_data', 'Time', 'timestamp')}, children={})})),
    ],
    "Posts You'Re Not Interested In": [
        Entry(table="Posts You'Re Not Interested In", filename="ads_information/ads_and_topics/posts_you're_not_interested_in.json", static_fields={}, tree=Node(columns={}, children={'impressions_history_posts_not_interested': Node(columns={}, children={'string_list_data': Node(columns={'href': ('href',), 'value': ('value',)}, children={})})})),
    ],
    'Profile Privacy Changes': [
        Entry(table='Profile Privacy Changes', filename='security_and_login_information/login_and_profile_creation/profile_privacy_changes.json', static_fields={}, tree=Node(columns={}, children={'account_history_account_privacy_history': Node(columns={'title': ('title',), 'href': ('string_map_data', 'Time', 'href'), 'value': ('string_map_data', 'Time', 'value'), 'timestamp': ('string_map_data', 'Time', 'timestamp')}, children={})})),
    ],
    'Profile Searches': [
        Entry(table='Profile Searches', filename='logged_information/recent_searches/profile_searches.json', static_fields={}, tree=Node(columns={}, children={'searches_user': Node(columns={'title': ('title',), 'href': ('string_map_data', 'Time', 'href'), 'value': ('string_map_data', 'Time', 'value'), 'timestamp': ('string_map_data', 'Time', 'timestamp')}, children={})})),
    ],
    "Profiles You'Re Not Interested In": [
        Entry(table="Profiles You'Re Not Interested In", filename="ads_information/ads_and_topics/profiles_you're_not_interested_in.json", static_fields={}, tree=Node(columns={}, children={'impressions_history_recs_hidden_authors': Node(columns={'title': ('title',), 'href': ('string_map_data', 'Time', 'href'), 'value': ('string_map_data', 'Time', 'value'), 'timestamp': ('string_map_data', 'Time', 'timestamp')}, children={})})),
    ],
    'Questions': [
        Entry(table='Questions', filename='your_instagram_activity/story_interactions/questions.json', static_fields={}, tree=Node(columns={}, children={'story_activities_questions': Node(columns={'title': ('title',), 'media_list_data': ('media_list_data',)}, children={'string_list_data': Node(columns={'href': ('href',), 'value': ('value',), 'timestamp': ('timestamp',)}, children={})})})),
    ],
    'Quizzes': [
        Entry(table='Quizzes', filename='your_instagram_activity/story_sticker_interactions/quizzes.json', static_fields={}, tree=Node(columns={}, children={'story_activities_quizzes': Node(columns={'title': ('title',)}, children={'string_list_data': Node(columns={'value': ('value',), 'timestamp': ('timestamp',)}, children={})})})),
    ],
    'Recommended Topics': [
        Entry(table='Recommended Topics', filename='preferences/your_topics/recommended_topics.json', static_fields={}, tree=Node(columns={}, children={'topics_your_topics': Node(columns={'title': ('title',), 'href': ('string_map_data', 'Name', 'href'), 'value': ('string_map_data', 'Name', 'value'), 'timestamp': ('string_map_data', 'Name', 'timestamp')}, children={})})),
    ],
    'Reels': [
        Entry(table='Reels', filename='your_instagram_activity/media/reels.json', static_fields={}, tree=Node(columns={}, children={'ig_reels_media': Node(columns={}, children={'media': Node(columns={'uri': ('uri',), 'creation_timestamp': ('creation_timestamp',), 'title': ('title',), 'dubbing_info': ('dubbing_info',), 'media_variants': ('media_variants',), 'source_app': ('cross_post_source', 'source_app'), 'music_genre': ('media_metadata', 'video_metadata', 'music_genre')}, children={'media_metadata': Node(columns={}, children={'video_metadata': Node(columns={}, children={'exif_data': Node(columns={'source_type': ('source_type',)}, children={})})})})})})),
    ],
    'Reels Comments': [
        Entry(table='Reels Comments', filename='your_instagram_activity/comments/reels_comments.json', static_fields={}, tree=Node(columns={}, children={'comments_reels_comments': Node(columns={'value': ('string_map_data', 'Media Owner', 'value'), 'timestamp': ('string_map_data', 'Time', 'timestamp')}, children={})})),
    ],
    'Removed Suggestions': [
        Entry(table='Removed Suggestions', filename='connections/followers_and_following/removed_suggestions.json', static_fields={}, tree=Node(columns={}, children={'relationships_dismissed_suggested_users': Node(columns={'title': ('title',), 'media_list_data': ('media_list_data',)}, children={'string_list_data': Node(columns={'href': ('href',), 'value': ('value',), 'timestamp': ('timestamp',)}, children={})})})),
    ],
    'Saved Collections': [
        Entry(table='Saved Collections', filename='your_instagram_activity/saved/saved_collections.json', static_fields={}, tree=Node(columns={}, children={'saved_saved_collections': Node(columns={'title': ('title',), 'value': ('string_map_data', 'Name', 'value'), 'timestamp': ('string_map_data', 'Added Time', 'timestamp'), 'href': ('string_map_data', 'Name', 'href')}, children={})})),
    ],
    'Saved Posts': [
        Entry(table='Saved Posts', filename='your_instagram_activity/saved/saved_posts.json', static_fields={}, tree=Node(columns={}, children={'saved_saved_media': Node(columns={'title': ('title',), 'href': ('string_map_data', 'Saved on', 'href'), 'timestamp': ('string_map_data', 'Saved on', 'timestamp')}, children={})})),
    ],
    'Signup Details': [
        Entry(table='Signup Details', filename='security_and_login_information/login_and_profile_creation/signup_details.json', static_fields={}, tree=Node(columns={}, children={'account_history_registration_info': Node(columns={'timestamp': ('string_map_data', 'Time', 'timestamp')}, children={})})),
    ],
    'Stories': [
        Entry(table='Stories', filename='your_instagram_activity/content/stories.json', static_fields={}, tree=Node(columns={}, children={'ig_stories': Node(columns={'uri': ('uri',), 'creation_timestamp': ('creation_timestamp',), 'title': ('title',), 'dubbing_info': ('dubbing_info',), 'media_variants': ('media_variants',), 'backup_uri': ('backup_uri',), 'source_app': ('cross_post_source', 'source_app'), 'music_genre': ('media_metadata', 'video_metadata', 'music_genre')}, children={'media_metadata': Node(columns={}, children={'video_metadata': Node(columns={}, children={'exif_data': Node(columns={'date_time_digitized': ('date_time_digitized',), 'date_time_original': ('date_time_original',), 'source_type': ('source_type',)}, children={})}), 'photo_metadata': Node(columns={}, children={'exif_data': Node(columns={'source_type': ('source_type',), 'date_time_digitized': ('date_time_digitized',), 'date_time_original': ('date_time_original',)}, children={})})})})})),
        Entry(table='Stories', filename='your_instagram_activity/media/stories.json', static_fields={}, tree=Node(columns={}, children={'ig_stories': Node(columns={'uri': ('uri',), 'creation_timestamp': ('creation_timestamp',), 'title': ('title',), 'dubbing_info': ('dubbing_info',), 'media_variants': ('media_variants',), 'source_app': ('cross_post_source', 'source_app')}, children={'media_metadata': Node(columns={}, children={'video_metadata': Node(columns={}, children={'exif_data': Node(columns={'date_time_digitized': ('date_time_digitized',), 'date_time_original': ('date_time_original',), 'source_type': ('source_type',)}, children={})})})})})),
    ],
    'Story Likes': [
        Entry(table='Story Likes', filename='your_instagram_activity/story_interactions/story_likes.json', static_fields={}, tree=Node(columns={}, children={'story_activities_story_likes': Node(columns={'title': ('title',)}, children={'string_list_data': Node(columns={'timestamp': ('timestamp',)}, children={})})})),
        Entry(table='Story Likes', filename='your_instagram_activity/story_sticker_interactions/story_likes.json', static_fields={}, tree=Node(columns={}, children={'story_activities_story_likes': Node(columns={'title': ('title',)}, children={'string_list_data': Node(columns={'timestamp': ('timestamp',)}, children={})})})),
    ],
    'Subscription For No Ads': [
        Entry(table='Subscription For No Ads', filename='ads_information/instagram_ads_and_businesses/subscription_for_no_ads.json', static_fields={'media': ('media',), 'fbid': ('fbid',)}, tree=Node(columns={}, children={'label_values': Node(columns={'label': ('label',), 'value': ('value',)}, children={})})),
    ],
    'Suggested Profiles Viewed': [
        Entry(table='Suggested Profiles Viewed', filename='ads_information/ads_and_topics/suggested_profiles_viewed.json', static_fields={}, tree=Node(columns={}, children={'impressions_history_chaining_seen': Node(columns={'value': ('string_map_data', 'Username', 'value'), 'timestamp': ('string_map_data', 'Time', 'timestamp')}, children={})})),
    ],
    'Time Spent On Instagram': [
        Entry(table='Time Spent On Instagram', filename='your_instagram_activity/other_activity/time_spent_on_instagram.json', static_fields={}, tree=Node(columns={'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',)}, children={'label_values': Node(columns={'label': ('label',)}, children={'vec': Node(columns={}, children={'dict': Node(columns={'label': ('label',), 'timestamp_value': ('timestamp_value',)}, children={})})})})),
    ],
    'Videos Watched': [
        Entry(table='Videos Watched', filename='ads_information/ads_and_topics/videos_watched.json', static_fields={}, tree=Node(columns={}, children={'impressions_history_videos_watched': Node(columns={'value': ('string_map_data', 'Author', 'value'), 'timestamp': ('string_map_data', 'Time', 'timestamp')}, children={})})),
    ],
    'Word Or Phrase Searches': [
        Entry(table='Word Or Phrase Searches', filename='logged_information/recent_searches/word_or_phrase_searches.json', static_fields={}, tree=Node(columns={}, children={'searches_keyword': Node(columns={'title': ('title',), 'href': ('string_map_data', 'Time', 'href'), 'value': ('string_map_data', 'Time', 'value'), 'timestamp': ('string_map_data', 'Time', 'timestamp')}, children={})})),
    ],
    'Your Activity Off Meta Technologies': [
        Entry(table='Your Activity Off Meta Technologies', filename='apps_and_websites_off_of_instagram/apps_and_websites/your_activity_off_meta_technologies.json', static_fields={}, tree=Node(columns={}, children={'apps_and_websites_off_meta_activity': Node(columns={'name': ('name',)}, children={'events': Node(columns={'id': ('id',), 'type': ('type',), 'timestamp': ('timestamp',)}, children={})})})),
    ],
    'Your Information Download Requests': [
        Entry(table='Your Information Download Requests', filename='your_instagram_activity/other_activity/your_information_download_requests.json', static_fields={'timestamp': ('timestamp',)}, tree=Node(columns={'timestamp': ('timestamp',)}, children={'label_values': Node(columns={'timestamp_value': ('timestamp_value',)}, children={})})),
    ],
    'Your Muted Story Teaser Creators': [
        Entry(table='Your Muted Story Teaser Creators', filename='your_instagram_activity/subscriptions/your_muted_story_teaser_creators.json', static_fields={}, tree=Node(columns={}, children={'subscriptions_muted_story_teaser_creators': Node(columns={'title': ('title',), 'href': ('string_map_data', 'Muted Creators', 'href'), 'value': ('string_map_data', 'Muted Creators', 'value'), 'timestamp': ('string_map_data', 'Muted Creators', 'timestamp')}, children={})})),
    ],
    'Your Topics': [
        Entry(table='Your Topics', filename='preferences/your_topics/your_topics.json', static_fields={}, tree=Node(columns={}, children={'topics_your_topics': Node(columns={'title': ('title',), 'href': ('string_map_data', 'Name', 'href'), 'value': ('string_map_data', 'Name', 'value'), 'timestamp': ('string_map_data', 'Name', 'timestamp')}, children={})})),
    ],
}

FB_ENTRIES: dict[str, list[Entry]] = {
    '6179754102079646': [
        Entry(table='6179754102079646', filename='your_facebook_activity/groups/your_group_messages/6179754102079646.json', static_fields={'thread_name': ('thread_name',), 'messages': ('messages',)}, tree=Node(columns={}, children={})),
    ],
    '6452840174763366': [
        Entry(table='6452840174763366', filename='your_facebook_activity/groups/your_group_messages/6452840174763366.json', static_fields={'thread_name': ('thread_name',), 'messages': ('messages',)}, tree=Node(columns={}, children={})),
    ],
    '6477893372272082': [
        Entry(table='6477893372272082', filename='your_facebook_activity/groups/your_group_messages/6477893372272082.json', static_fields={'thread_name': ('thread_name',), 'messages': ('messages',)}, tree=Node(columns={}, children={})),
    ],
    '6798433430245173': [
        Entry(table='6798433430245173', filename='your_facebook_activity/groups/your_group_messages/6798433430245173.json', static_fields={'thread_name': ('thread_name',), 'messages': ('messages',)}, tree=Node(columns={}, children={})),
    ],
    'Ad Preferences': [
        Entry(table='Ad Preferences', filename='ads_information/ad_preferences.json', static_fields={'media': ('media',), 'fbid': ('fbid',), 'ent_name': ('ent_name',)}, tree=Node(columns={}, children={'label_values': Node(columns={'label': ('label',), 'value': ('value',), 'ent_field_name': ('ent_field_name',), 'vec': ('vec',), 'dict': ('dict',), 'title': ('title',)}, children={'dict': Node(columns={'title': ('title',), 'dict': ()}, children={'dict': Node(columns={'ent_field_name': ('ent_field_name',), 'label': ('label',), 'value': ('value',)}, children={})}), 'vec': Node(columns={'vec': ()}, children={})}), 'media': Node(columns={'media': ()}, children={})})),
    ],
    'Admin Activity': [
        Entry(table='Admin Activity', filename='your_facebook_activity/pages/admin_activity.json', static_fields={'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',)}, tree=Node(columns={}, children={'label_values': Node(columns={'label': ('label',), 'value': ('value',), 'href': ('href',)}, children={})})),
    ],
    'Ads About Meta': [
        Entry(table='Ads About Meta', filename='ads_information/ads_about_meta.json', static_fields={'media': ('media',), 'fbid': ('fbid',), 'ent_name': ('ent_name',)}, tree=Node(columns={}, children={'label_values': Node(columns={'label': ('label',), 'value': ('value',), 'ent_field_name': ('ent_field_name',), 'timestamp_value': ('timestamp_value',)}, children={}), 'media': Node(columns={'media': ()}, children={})})),
    ],
    'Ads Feedback Activity': [
        Entry(table='Ads Feedback Activity', filename='ads_information/ads_feedback_activity.json', static_fields={'media': ('media',), 'fbid': ('fbid',)}, tree=Node(columns={}, children={'label_values': Node(columns={'label': ('label',), 'timestamp_value': ('timestamp_value',)}, children={})})),
    ],
    'Ads Interests': [
        Entry(table='Ads Interests', filename='logged_information/other_logged_information/ads_interests.json', static_fields={'topics_v2': ('topics_v2',)}, tree=Node(columns={}, children={'topics_v2': Node(columns={'topics_v2': ()}, children={})})),
    ],
    'Ads Personalization Consent': [
        Entry(table='Ads Personalization Consent', filename='ads_information/ads_personalization_consent.json', static_fields={'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',), 'ent_name': ('ent_name',)}, tree=Node(columns={}, children={'label_values': Node(columns={'label': ('label',), 'timestamp_value': ('timestamp_value',), 'ent_field_name': ('ent_field_name',), 'value': ('value',)}, children={}), 'media': Node(columns={'media': ()}, children={})})),
    ],
    'Ads Viewed': [
        Entry(table='Ads Viewed', filename='ads_information/ads_and_topics/ads_viewed.json', static_fields={}, tree=Node(columns={}, children={'impressions_history_ads_seen': Node(columns={'value': ('string_map_data', 'Author', 'value'), 'timestamp': ('string_map_data', 'Time', 'timestamp')}, children={})})),
    ],
    'Advertisers Using Your Activity Or Information': [
        Entry(table='Advertisers Using Your Activity Or Information', filename='ads_information/advertisers_using_your_activity_or_information.json', static_fields={'media': ('media',), 'fbid': ('fbid',), 'ent_name': ('ent_name',)}, tree=Node(columns={}, children={'label_values': Node(columns={'label': ('label',), 'ent_field_name': ('ent_field_name',)}, children={'vec': Node(columns={'value': ('value',)}, children={})}), 'media': Node(columns={'media': ()}, children={})})),
    ],
    'Advertisers You Ve Interacted With': [
        Entry(table='Advertisers You Ve Interacted With', filename='ads_information/advertisers_you_ve_interacted_with.json', static_fields={}, tree=Node(columns={}, children={'history_v2': Node(columns={'title': ('title',), 'action': ('action',), 'timestamp': ('timestamp',)}, children={})})),
    ],
    "Advertisers You'Ve Interacted With": [
        Entry(table="Advertisers You'Ve Interacted With", filename="ads_information/advertisers_you've_interacted_with.json", static_fields={'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',)}, tree=Node(columns={'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',)}, children={'history_v2': Node(columns={'title': ('title',), 'action': ('action',), 'timestamp': ('timestamp',)}, children={}), 'label_values': Node(columns={'label': ('label',)}, children={})})),
    ],
    'Archived Stories': [
        Entry(table='Archived Stories', filename='your_facebook_activity/stories/archived_stories.json', static_fields={}, tree=Node(columns={}, children={'archived_stories_v2': Node(columns={'timestamp': ('timestamp',), 'title': ('title',)}, children={'attachments': Node(columns={}, children={'data': Node(columns={'uri': ('media', 'uri'), 'creation_timestamp': ('media', 'creation_timestamp'), 'title': ('media', 'title'), 'description': ('media', 'description'), 'dubbing_info': ('media', 'dubbing_info'), 'media_variants': ('media', 'media_variants')}, children={})})})})),
    ],
    'Close Friends': [
        Entry(table='Close Friends', filename='connections/followers_and_following/close_friends.json', static_fields={}, tree=Node(columns={}, children={'relationships_close_friends': Node(columns={'title': ('title',), 'media_list_data': ('media_list_data',)}, children={'string_list_data': Node(columns={'href': ('href',), 'value': ('value',), 'timestamp': ('timestamp',)}, children={})})})),
    ],
    'Collections': [
        Entry(table='Collections', filename='your_facebook_activity/saved_items_and_collections/collections.json', static_fields={'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',)}, tree=Node(columns={}, children={'label_values': Node(columns={'label': ('label',), 'value': ('value',)}, children={})})),
    ],
    'Comments': [
        Entry(table='Comments', filename='personal_information/profile_information/your_facebook_activity/comments_and_reactions/comments.json', static_fields={}, tree=Node(columns={}, children={'comments_v2': Node(columns={'timestamp': ('timestamp',)}, children={'data': Node(columns={'timestamp': ('comment', 'timestamp'), 'comment': ('comment', 'comment')}, children={})})})),
        Entry(table='Comments', filename='your_activity_across_facebook/comments_and_reactions/comments.json', static_fields={}, tree=Node(columns={}, children={'comments_v2': Node(columns={'timestamp': ('timestamp',)}, children={'data': Node(columns={'timestamp': ('comment', 'timestamp'), 'comment': ('comment', 'comment')}, children={})})})),
        Entry(table='Comments', filename='your_facebook_activity/comments_and_reactions/comments.json', static_fields={}, tree=Node(columns={}, children={'comments_v2': Node(columns={'timestamp': ('timestamp',)}, children={'data': Node(columns={'timestamp': ('comment', 'timestamp'), 'comment': ('comment', 'comment')}, children={})})})),
    ],
    'Comments Allowed From': [
        Entry(table='Comments Allowed From', filename='preferences/settings/comments_allowed_from.json', static_fields={}, tree=Node(columns={}, children={'settings_allow_comments_from': Node(columns={'title': ('title',), 'href': ('string_map_data', 'Comments Allowed From', 'href'), 'value': ('string_map_data', 'Comments Allowed From', 'value'), 'timestamp': ('string_map_data', 'Comments Allowed From', 'timestamp')}, children={})})),
    ],
    'Consents': [
        Entry(table='Consents', filename='logged_information/other_logged_information/consents.json', static_fields={'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',), 'ent_name': ('ent_name',)}, tree=Node(columns={}, children={'label_values': Node(columns={'label': ('label',), 'ent_field_name': ('ent_field_name',), 'timestamp_value': ('timestamp_value',)}, children={}), 'media': Node(columns={'media': ()}, children={})})),
    ],
    'Content Sharing Links You Have Created': [
        Entry(table='Content Sharing Links You Have Created', filename='personal_information/profile_information/your_facebook_activity/posts/content_sharing_links_you_have_created.json', static_fields={'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',)}, tree=Node(columns={'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',)}, children={'label_values': Node(columns={'label': ('label',), 'value': ('value',), 'href': ('href',)}, children={})})),
        Entry(table='Content Sharing Links You Have Created', filename='your_facebook_activity/posts/content_sharing_links_you_have_created.json', static_fields={'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',), 'ent_name': ('ent_name',)}, tree=Node(columns={'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',), 'ent_name': ('ent_name',)}, children={'label_values': Node(columns={'label': ('label',), 'value': ('value',), 'href': ('href',), 'ent_field_name': ('ent_field_name',)}, children={}), 'media': Node(columns={'media': ()}, children={})})),
    ],
    'Controls': [
        Entry(table='Controls', filename='personal_information/profile_information/preferences/feed/controls.json', static_fields={}, tree=Node(columns={}, children={'controls': Node(columns={'name': ('name',), 'description': ('description',)}, children={'entries': Node(columns={'timestamp': ('timestamp',), 'name': ('data', 'name'), 'uri': ('data', 'uri')}, children={})})})),
        Entry(table='Controls', filename='preferences/feed/controls.json', static_fields={}, tree=Node(columns={}, children={'controls': Node(columns={'name': ('name',), 'description': ('description',), 'entries': ('entries',)}, children={'entries': Node(columns={'entries': ()}, children={})})})),
    ],
    'Edits You Made To Posts': [
        Entry(table='Edits You Made To Posts', filename='personal_information/profile_information/your_facebook_activity/posts/edits_you_made_to_posts.json', static_fields={'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',)}, tree=Node(columns={'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',)}, children={'label_values': Node(columns={'label': ('label',), 'value': ('value',)}, children={})})),
        Entry(table='Edits You Made To Posts', filename='your_facebook_activity/posts/edits_you_made_to_posts.json', static_fields={'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',)}, tree=Node(columns={'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',)}, children={'label_values': Node(columns={'label': ('label',), 'value': ('value',)}, children={})})),
    ],
    'Emails We Sent You': [
        Entry(table='Emails We Sent You', filename='personal_information/other_personal_information/emails_we_sent_you.json', static_fields={'title': ('title',), 'timestamp': ('timestamp',)}, tree=Node(columns={'title': ('title',), 'timestamp': ('timestamp',)}, children={})),
    ],
    'Facebook Reels Usage Information': [
        Entry(table='Facebook Reels Usage Information', filename='logged_information/other_logged_information/facebook_reels_usage_information.json', static_fields={'media': ('media',), 'fbid': ('fbid',), 'ent_name': ('ent_name',)}, tree=Node(columns={}, children={'label_values': Node(columns={'label': ('label',), 'ent_field_name': ('ent_field_name',)}, children={'dict': Node(columns={'label': ('label',), 'value': ('value',)}, children={})}), 'media': Node(columns={'media': ()}, children={})})),
    ],
    'Feed': [
        Entry(table='Feed', filename='preferences/feed/feed.json', static_fields={}, tree=Node(columns={}, children={'people_and_friends_v2': Node(columns={'name': ('name',), 'description': ('description',)}, children={'entries': Node(columns={'timestamp': ('timestamp',), 'name': ('data', 'name'), 'uri': ('data', 'uri')}, children={})})})),
    ],
    "Follow Requests You'Ve Received": [
        Entry(table="Follow Requests You'Ve Received", filename="connections/followers_and_following/follow_requests_you've_received.json", static_fields={}, tree=Node(columns={}, children={'relationships_follow_requests_received': Node(columns={'title': ('title',), 'media_list_data': ('media_list_data',)}, children={'string_list_data': Node(columns={'href': ('href',), 'value': ('value',), 'timestamp': ('timestamp',)}, children={})})})),
    ],
    'Followers 1': [
        Entry(table='Followers 1', filename='connections/followers_and_following/followers_1.json', static_fields={'title': ('title',), 'media_list_data': ('media_list_data',)}, tree=Node(columns={'title': ('title',), 'media_list_data': ('media_list_data',)}, children={'string_list_data': Node(columns={'href': ('href',), 'value': ('value',), 'timestamp': ('timestamp',)}, children={})})),
    ],
    'Following': [
        Entry(table='Following', filename='connections/followers_and_following/following.json', static_fields={}, tree=Node(columns={}, children={'relationships_following': Node(columns={'title': ('title',), 'media_list_data': ('media_list_data',)}, children={'string_list_data': Node(columns={'href': ('href',), 'value': ('value',), 'timestamp': ('timestamp',)}, children={})})})),
    ],
    'Fundraiser Posts You Likely Viewed': [
        Entry(table='Fundraiser Posts You Likely Viewed', filename='personal_information/profile_information/your_facebook_activity/fundraisers/fundraiser_posts_you_likely_viewed.json', static_fields={'media': ('media',), 'fbid': ('fbid',)}, tree=Node(columns={}, children={'label_values': Node(columns={'label': ('label',), 'value': ('value',)}, children={})})),
        Entry(table='Fundraiser Posts You Likely Viewed', filename='your_facebook_activity/fundraisers/fundraiser_posts_you_likely_viewed.json', static_fields={'media': ('media',), 'fbid': ('fbid',), 'ent_name': ('ent_name',)}, tree=Node(columns={}, children={'label_values': Node(columns={'label': ('label',), 'value': ('value',), 'ent_field_name': ('ent_field_name',)}, children={}), 'media': Node(columns={'media': ()}, children={})})),
    ],
    'Fundraisers Donated To': [
        Entry(table='Fundraisers Donated To', filename='your_facebook_activity/fundraisers/fundraisers_donated_to.json', static_fields={}, tree=Node(columns={}, children={'fundraisers_donated_to_v2': Node(columns={'timestamp': ('timestamp',)}, children={'attachments': Node(columns={}, children={'data': Node(columns={'title': ('fundraiser', 'title'), 'donated_amount': ('fundraiser', 'donated_amount')}, children={})})})})),
    ],
    "Group Invites You'Ve Received": [
        Entry(table="Group Invites You'Ve Received", filename="your_facebook_activity/groups/group_invites_you've_received.json", static_fields={'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',)}, tree=Node(columns={'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',)}, children={'label_values': Node(columns={'label': ('label',), 'timestamp_value': ('timestamp_value',)}, children={})})),
    ],
    "Group Invites You'Ve Sent": [
        Entry(table="Group Invites You'Ve Sent", filename="your_facebook_activity/groups/group_invites_you've_sent.json", static_fields={'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',)}, tree=Node(columns={'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',)}, children={'label_values': Node(columns={'label': ('label',), 'value': ('value',)}, children={})})),
    ],
    'Group Posts And Comments': [
        Entry(table='Group Posts And Comments', filename='your_activity_across_facebook/groups/group_posts_and_comments.json', static_fields={}, tree=Node(columns={}, children={'group_posts_v2': Node(columns={'timestamp': ('timestamp',), 'title': ('title',)}, children={'data': Node(columns={'post': ('post',)}, children={})})})),
        Entry(table='Group Posts And Comments', filename='your_facebook_activity/groups/group_posts_and_comments.json', static_fields={}, tree=Node(columns={}, children={'group_posts_v2': Node(columns={'timestamp': ('timestamp',), 'title': ('title',)}, children={'data': Node(columns={'post': ('post',)}, children={})})})),
    ],
    'Groups And Pages That You May Find Engaging': [
        Entry(table='Groups And Pages That You May Find Engaging', filename='your_facebook_activity/groups/groups_and_pages_that_you_may_find_engaging.json', static_fields={'media': ('media',), 'fbid': ('fbid',), 'ent_name': ('ent_name',)}, tree=Node(columns={}, children={'label_values': Node(columns={'ent_field_name': ('ent_field_name',), 'label': ('label',)}, children={'vec': Node(columns={'value': ('value',)}, children={})}), 'media': Node(columns={'media': ()}, children={})})),
    ],
    'Groups You Ve Visited': [
        Entry(table='Groups You Ve Visited', filename='logged_information/your_interactions_on_facebook/groups_you_ve_visited.json', static_fields={'timestamp': ('timestamp',), 'fbid': ('fbid',), 'ent_name': ('ent_name',)}, tree=Node(columns={'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',), 'ent_name': ('ent_name',)}, children={'label_values': Node(columns={'ent_field_name': ('ent_field_name',), 'label': ('label',), 'value': ('value',)}, children={}), 'media': Node(columns={'media': ()}, children={})})),
    ],
    "Groups You'Ve Visited": [
        Entry(table="Groups You'Ve Visited", filename="logged_information/interactions/groups_you've_visited.json", static_fields={'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',)}, tree=Node(columns={'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',)}, children={'label_values': Node(columns={'label': ('label',), 'value': ('value',)}, children={})})),
        Entry(table="Groups You'Ve Visited", filename="logged_information/your_interactions_on_facebook/groups_you've_visited.json", static_fields={'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',)}, tree=Node(columns={'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',)}, children={'label_values': Node(columns={'label': ('label',), 'value': ('value',)}, children={})})),
    ],
    "Information You'Ve Submitted To Advertisers": [
        Entry(table="Information You'Ve Submitted To Advertisers", filename="ads_information/information_you've_submitted_to_advertisers.json", static_fields={}, tree=Node(columns={}, children={'lead_gen_info_v2': Node(columns={'label': ('label',), 'value': ('value',)}, children={})})),
    ],
    'Likes And Reactions': [
        Entry(table='Likes And Reactions', filename='personal_information/profile_information/your_facebook_activity/comments_and_reactions/likes_and_reactions.json', static_fields={'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',)}, tree=Node(columns={'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',)}, children={'label_values': Node(columns={'label': ('label',), 'value': ('value',)}, children={})})),
        Entry(table='Likes And Reactions', filename='your_facebook_activity/comments_and_reactions/likes_and_reactions.json', static_fields={'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',), 'ent_name': ('ent_name',)}, tree=Node(columns={'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',), 'ent_name': ('ent_name',)}, children={'label_values': Node(columns={'label': ('label',), 'value': ('value',), 'ent_field_name': ('ent_field_name',), 'href': ('href',), 'title': ('title',)}, children={'dict': Node(columns={'title': ('title',)}, children={'dict': Node(columns={'ent_field_name': ('ent_field_name',), 'label': ('label',), 'value': ('value',)}, children={})})}), 'media': Node(columns={'media': ()}, children={})})),
    ],
    'Other Categories Used To Reach You': [
        Entry(table='Other Categories Used To Reach You', filename='ads_information/other_categories_used_to_reach_you.json', static_fields={'media': ('media',), 'fbid': ('fbid',), 'ent_name': ('ent_name',), 'bcts': ('bcts',)}, tree=Node(columns={}, children={'label_values': Node(columns={'label': ('label',), 'ent_field_name': ('ent_field_name',)}, children={'vec': Node(columns={'value': ('value',)}, children={})}), 'media': Node(columns={'media': ()}, children={}), 'bcts': Node(columns={'bcts': ()}, children={})})),
    ],
    'Pages And Profiles You Follow': [
        Entry(table='Pages And Profiles You Follow', filename='personal_information/profile_information/your_facebook_activity/pages/pages_and_profiles_you_follow.json', static_fields={}, tree=Node(columns={}, children={'pages_followed_v2': Node(columns={'timestamp': ('timestamp',), 'title': ('title',)}, children={'data': Node(columns={'name': ('name',)}, children={})})})),
        Entry(table='Pages And Profiles You Follow', filename='your_activity_across_facebook/pages/pages_and_profiles_you_follow.json', static_fields={}, tree=Node(columns={}, children={'pages_followed_v2': Node(columns={'timestamp': ('timestamp',), 'title': ('title',)}, children={'data': Node(columns={'name': ('name',)}, children={})})})),
        Entry(table='Pages And Profiles You Follow', filename='your_facebook_activity/pages/pages_and_profiles_you_follow.json', static_fields={}, tree=Node(columns={}, children={'pages_followed_v2': Node(columns={'timestamp': ('timestamp',), 'title': ('title',)}, children={'data': Node(columns={'name': ('name',)}, children={})})})),
    ],
    "Pages And Profiles You'Ve Recommended": [
        Entry(table="Pages And Profiles You'Ve Recommended", filename="your_facebook_activity/pages/pages_and_profiles_you've_recommended.json", static_fields={}, tree=Node(columns={}, children={'recommended_pages_v2': Node(columns={'name': ('name',), 'timestamp': ('timestamp',), 'url': ('url',)}, children={})})),
    ],
    "Pages And Profiles You'Ve Unfollowed": [
        Entry(table="Pages And Profiles You'Ve Unfollowed", filename="your_facebook_activity/pages/pages_and_profiles_you've_unfollowed.json", static_fields={}, tree=Node(columns={}, children={'pages_unfollowed_v2': Node(columns={'timestamp': ('timestamp',), 'title': ('title',)}, children={'data': Node(columns={'name': ('name',)}, children={})})})),
    ],
    'Pages You Ve Liked': [
        Entry(table='Pages You Ve Liked', filename='your_facebook_activity/pages/pages_you_ve_liked.json', static_fields={}, tree=Node(columns={}, children={'page_likes_v2': Node(columns={'name': ('name',), 'timestamp': ('timestamp',), 'url': ('url',)}, children={})})),
    ],
    "Pages You'Ve Liked": [
        Entry(table="Pages You'Ve Liked", filename="personal_information/profile_information/your_facebook_activity/pages/pages_you've_liked.json", static_fields={}, tree=Node(columns={}, children={'page_likes_v2': Node(columns={'name': ('name',), 'timestamp': ('timestamp',), 'url': ('url',)}, children={})})),
        Entry(table="Pages You'Ve Liked", filename="your_activity_across_facebook/pages/pages_you've_liked.json", static_fields={}, tree=Node(columns={}, children={'page_likes_v2': Node(columns={'name': ('name',), 'timestamp': ('timestamp',), 'url': ('url',)}, children={})})),
        Entry(table="Pages You'Ve Liked", filename="your_facebook_activity/pages/pages_you've_liked.json", static_fields={}, tree=Node(columns={}, children={'page_likes_v2': Node(columns={'name': ('name',), 'timestamp': ('timestamp',), 'url': ('url',)}, children={})})),
    ],
    'People And Friends': [
        Entry(table='People And Friends', filename='logged_information/activity_messages/people_and_friends.json', static_fields={'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',)}, tree=Node(columns={'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',)}, children={'people_interactions_v2': Node(columns={'name': ('name',), 'description': ('description',)}, children={'entries': Node(columns={'timestamp': ('timestamp',), 'name': ('data', 'name'), 'uri': ('data', 'uri')}, children={})}), 'label_values': Node(columns={'label': ('label',), 'value': ('value',)}, children={})})),
    ],
    'People We Think You Should Follow': [
        Entry(table='People We Think You Should Follow', filename='logged_information/your_topics/people_we_think_you_should_follow.json', static_fields={'timestamp': ('timestamp',), 'media': ('media',)}, tree=Node(columns={}, children={'label_values': Node(columns={'label': ('label',), 'vec': ('vec',)}, children={})})),
    ],
    'Posts On Other Pages And Profiles': [
        Entry(table='Posts On Other Pages And Profiles', filename='personal_information/profile_information/your_facebook_activity/posts/posts_on_other_pages_and_profiles.json', static_fields={'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',)}, tree=Node(columns={'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',)}, children={'label_values': Node(columns={'label': ('label',), 'value': ('value',)}, children={})})),
        Entry(table='Posts On Other Pages And Profiles', filename='your_facebook_activity/posts/posts_on_other_pages_and_profiles.json', static_fields={'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',)}, tree=Node(columns={'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',)}, children={'label_values': Node(columns={'label': ('label',), 'value': ('value',)}, children={})})),
    ],
    'Posts Viewed': [
        Entry(table='Posts Viewed', filename='ads_information/ads_and_topics/posts_viewed.json', static_fields={}, tree=Node(columns={}, children={'impressions_history_posts_seen': Node(columns={'value': ('string_map_data', 'Author', 'value'), 'timestamp': ('string_map_data', 'Time', 'timestamp')}, children={})})),
    ],
    'Privacy Settings': [
        Entry(table='Privacy Settings', filename='personal_information/profile_information/preferences/preferences/privacy_settings.json', static_fields={'media': ('media',), 'fbid': ('fbid',)}, tree=Node(columns={}, children={'label_values': Node(columns={'label': ('label',)}, children={'dict': Node(columns={'label': ('label',), 'value': ('value',)}, children={})})})),
        Entry(table='Privacy Settings', filename='preferences/preferences/privacy_settings.json', static_fields={'media': ('media',), 'fbid': ('fbid',)}, tree=Node(columns={}, children={'label_values': Node(columns={'label': ('label',)}, children={'dict': Node(columns={'label': ('label',), 'value': ('value',)}, children={})})})),
    ],
    'Recently Viewed': [
        Entry(table='Recently Viewed', filename='logged_information/interactions/recently_viewed.json', static_fields={}, tree=Node(columns={}, children={'recently_viewed': Node(columns={'name': ('name',), 'description': ('description',)}, children={'children': Node(columns={'name': ('name',), 'description': ('description',)}, children={'entries': Node(columns={'timestamp': ('timestamp',), 'name': ('data', 'name'), 'uri': ('data', 'uri'), 'watch_time': ('data', 'watch_time'), 'value': ('data', 'value')}, children={})}), 'entries': Node(columns={'timestamp': ('timestamp',), 'name': ('data', 'name'), 'uri': ('data', 'uri')}, children={})})})),
        Entry(table='Recently Viewed', filename='logged_information/your_interactions_on_facebook/recently_viewed.json', static_fields={}, tree=Node(columns={}, children={'recently_viewed': Node(columns={'name': ('name',), 'description': ('description',)}, children={'entries': Node(columns={'timestamp': ('timestamp',), 'name': ('data', 'name'), 'uri': ('data', 'uri')}, children={}), 'children': Node(columns={'name': ('name',), 'description': ('description',)}, children={'entries': Node(columns={'timestamp': ('timestamp',), 'value': ('data', 'value'), 'name': ('data', 'name'), 'uri': ('data', 'uri'), 'watch_time': ('data', 'watch_time')}, children={})})})})),
    ],
    'Recently Visited': [
        Entry(table='Recently Visited', filename='logged_information/interactions/recently_visited.json', static_fields={}, tree=Node(columns={}, children={'visited_things_v2': Node(columns={'name': ('name',), 'description': ('description',)}, children={'entries': Node(columns={'timestamp': ('timestamp',), 'name': ('data', 'name'), 'uri': ('data', 'uri')}, children={})})})),
        Entry(table='Recently Visited', filename='logged_information/your_interactions_on_facebook/recently_visited.json', static_fields={}, tree=Node(columns={}, children={'visited_things_v2': Node(columns={'name': ('name',), 'description': ('description',)}, children={'entries': Node(columns={'timestamp': ('timestamp',), 'name': ('data', 'name'), 'uri': ('data', 'uri'), 'value': ('data', 'value')}, children={})})})),
    ],
    'Recommended Topics': [
        Entry(table='Recommended Topics', filename='preferences/your_topics/recommended_topics.json', static_fields={}, tree=Node(columns={}, children={'topics_your_topics': Node(columns={'title': ('title',), 'href': ('string_map_data', 'Name', 'href'), 'value': ('string_map_data', 'Name', 'value'), 'timestamp': ('string_map_data', 'Name', 'timestamp')}, children={})})),
    ],
    'Reduce': [
        Entry(table='Reduce', filename='preferences/feed/reduce.json', static_fields={'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',), 'ent_name': ('ent_name',)}, tree=Node(columns={}, children={'label_values': Node(columns={'ent_field_name': ('ent_field_name',), 'label': ('label',), 'value': ('value',), 'timestamp_value': ('timestamp_value',)}, children={}), 'media': Node(columns={'media': ()}, children={})})),
    ],
    'Reels Preferences': [
        Entry(table='Reels Preferences', filename='personal_information/profile_information/preferences/preferences/reels_preferences.json', static_fields={'media': ('media',), 'fbid': ('fbid',)}, tree=Node(columns={}, children={'label_values': Node(columns={'label': ('label',), 'value': ('value',)}, children={})})),
        Entry(table='Reels Preferences', filename='preferences/preferences/reels_preferences.json', static_fields={'media': ('media',), 'fbid': ('fbid',), 'ent_name': ('ent_name',)}, tree=Node(columns={}, children={'label_values': Node(columns={'label': ('label',), 'value': ('value',), 'ent_field_name': ('ent_field_name',), 'vec': ('vec',)}, children={'vec': Node(columns={'vec': ()}, children={})}), 'media': Node(columns={'media': ()}, children={})})),
    ],
    'Registration Information': [
        Entry(table='Registration Information', filename='security_and_login_information/registration_information.json', static_fields={'timestamp': ('timestamp',)}, tree=Node(columns={}, children={})),
    ],
    'Snooze': [
        Entry(table='Snooze', filename='personal_information/profile_information/preferences/feed/snooze.json', static_fields={'media': ('media',), 'fbid': ('fbid',)}, tree=Node(columns={}, children={'label_values': Node(columns={'label': ('label',), 'value': ('value',)}, children={})})),
        Entry(table='Snooze', filename='preferences/feed/snooze.json', static_fields={'media': ('media',), 'fbid': ('fbid',)}, tree=Node(columns={}, children={'label_values': Node(columns={'label': ('label',), 'value': ('value',)}, children={})})),
    ],
    'Story Reactions': [
        Entry(table='Story Reactions', filename='personal_information/profile_information/your_facebook_activity/stories/story_reactions.json', static_fields={}, tree=Node(columns={}, children={'stories_feedback_v2': Node(columns={'title': ('title',)}, children={})})),
        Entry(table='Story Reactions', filename='your_facebook_activity/stories/story_reactions.json', static_fields={}, tree=Node(columns={}, children={'stories_feedback_v2': Node(columns={'title': ('title',)}, children={})})),
    ],
    'Story Views In Past 7 Days': [
        Entry(table='Story Views In Past 7 Days', filename='ads_information/story_views_in_past_7_days.json', static_fields={'media': ('media',), 'fbid': ('fbid',)}, tree=Node(columns={}, children={'label_values': Node(columns={'label': ('label',), 'value': ('value',)}, children={})})),
    ],
    'Subscription For No Ads': [
        Entry(table='Subscription For No Ads', filename='ads_information/subscription_for_no_ads.json', static_fields={'media': ('media',), 'fbid': ('fbid',)}, tree=Node(columns={}, children={'label_values': Node(columns={'label': ('label',), 'value': ('value',)}, children={})})),
    ],
    'Support Messages': [
        Entry(table='Support Messages', filename='personal_information/profile_information/your_facebook_activity/messages/support_messages.json', static_fields={'timestamp': ('support_messages', '7156925894430515', 'timestamp'), 'subject': ('support_messages', '7156925894430515', 'subject')}, tree=Node(columns={}, children={'support_messages': Node(columns={}, children={'8752122044910884': Node(columns={}, children={'messages': Node(columns={'from': ('from',), 'to': ('to',), 'subject': ('subject',), 'message': ('message',), 'timestamp': ('timestamp',)}, children={})}), '7156925894430515': Node(columns={}, children={'messages': Node(columns={'from': ('from',), 'to': ('to',), 'subject': ('subject',), 'message': ('message',), 'timestamp': ('timestamp',)}, children={})})})})),
        Entry(table='Support Messages', filename='your_facebook_activity/messages/support_messages.json', static_fields={'timestamp': ('support_messages', '10223298304470161', 'timestamp'), 'subject': ('support_messages', '10223298304470161', 'subject')}, tree=Node(columns={}, children={'support_messages': Node(columns={}, children={'10230171959787248': Node(columns={}, children={'messages': Node(columns={'from': ('from',), 'to': ('to',), 'subject': ('subject',), 'message': ('message',), 'timestamp': ('timestamp',)}, children={})}), '10223298304470161': Node(columns={}, children={'messages': Node(columns={'from': ('from',), 'to': ('to',), 'subject': ('subject',), 'message': ('message',), 'timestamp': ('timestamp',)}, children={})})})})),
    ],
    'Time Spent On Facebook': [
        Entry(table='Time Spent On Facebook', filename='personal_information/profile_information/your_facebook_activity/other_activity/time_spent_on_facebook.json', static_fields={'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',)}, tree=Node(columns={'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',)}, children={'label_values': Node(columns={'label': ('label',)}, children={'vec': Node(columns={}, children={'dict': Node(columns={'label': ('label',), 'timestamp_value': ('timestamp_value',)}, children={})})})})),
        Entry(table='Time Spent On Facebook', filename='your_facebook_activity/other_activity/time_spent_on_facebook.json', static_fields={'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',), 'ent_name': ('ent_name',)}, tree=Node(columns={'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',)}, children={'label_values': Node(columns={'label': ('label',), 'ent_field_name': ('ent_field_name',), 'timestamp_value': ('timestamp_value',)}, children={'vec': Node(columns={}, children={'dict': Node(columns={'label': ('label',), 'timestamp_value': ('timestamp_value',)}, children={})})}), 'media': Node(columns={'media': ()}, children={})})),
    ],
    'Video': [
        Entry(table='Video', filename='personal_information/profile_information/preferences/preferences/video.json', static_fields={}, tree=Node(columns={}, children={'watch_videos_v2': Node(columns={'video_title': ('video_title',), 'user_action': ('user_action',), 'action_time': ('action_time',), 'feedback_collection': ('feedback_collection',)}, children={})})),
        Entry(table='Video', filename='preferences/preferences/video.json', static_fields={'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',), 'ent_name': ('ent_name',)}, tree=Node(columns={}, children={'watch_videos_v2': Node(columns={'video_title': ('video_title',), 'user_action': ('user_action',), 'action_time': ('action_time',), 'feedback_collection': ('feedback_collection',)}, children={}), 'label_values': Node(columns={'label': ('label',), 'value': ('value',), 'ent_field_name': ('ent_field_name',), 'vec': ('vec',), 'timestamp_value': ('timestamp_value',), 'title': ('title',)}, children={'dict': Node(columns={'title': ('title',)}, children={'dict': Node(columns={'ent_field_name': ('ent_field_name',), 'label': ('label',), 'value': ('value',), 'href': ('href',), 'title': ('title',)}, children={'dict': Node(columns={'title': ('title',)}, children={'dict': Node(columns={'ent_field_name': ('ent_field_name',), 'label': ('label',), 'value': ('value',)}, children={})})})}), 'vec': Node(columns={'vec': ()}, children={})}), 'media': Node(columns={'media': ()}, children={})})),
    ],
    'Videos Watched': [
        Entry(table='Videos Watched', filename='ads_information/ads_and_topics/videos_watched.json', static_fields={}, tree=Node(columns={}, children={'impressions_history_videos_watched': Node(columns={'value': ('string_map_data', 'Author', 'value'), 'timestamp': ('string_map_data', 'Time', 'timestamp')}, children={})})),
    ],
    'Who You Ve Followed': [
        Entry(table='Who You Ve Followed', filename='connections/followers/who_you_ve_followed.json', static_fields={}, tree=Node(columns={}, children={'following_v3': Node(columns={'name': ('name',), 'timestamp': ('timestamp',)}, children={})})),
    ],
    "Who You'Ve Followed": [
        Entry(table="Who You'Ve Followed", filename="connections/followers/who_you've_followed.json", static_fields={}, tree=Node(columns={}, children={'following_v3': Node(columns={'name': ('name',), 'timestamp': ('timestamp',)}, children={})})),
    ],
    'Your Actions On Violating Content In Your Groups': [
        Entry(table='Your Actions On Violating Content In Your Groups', filename='your_facebook_activity/groups/your_actions_on_violating_content_in_your_groups.json', static_fields={'media': ('media',), 'fbid': ('fbid',)}, tree=Node(columns={'media': ('media',), 'fbid': ('fbid',)}, children={'label_values': Node(columns={'label': ('label',)}, children={})})),
    ],
    'Your Activity Off Meta Technologies': [
        Entry(table='Your Activity Off Meta Technologies', filename='apps_and_websites_off_of_facebook/your_activity_off_meta_technologies.json', static_fields={'title': ('title',), 'media': ('media',), 'fbid': ('fbid',)}, tree=Node(columns={'title': ('title',), 'media': ('media',), 'fbid': ('fbid',)}, children={'off_facebook_activity_v2': Node(columns={'name': ('name',)}, children={'events': Node(columns={'id': ('id',), 'type': ('type',), 'timestamp': ('timestamp',)}, children={})}), 'label_values': Node(columns={'label': ('label',)}, children={'vec': Node(columns={}, children={'dict': Node(columns={'label': ('label',), 'value': ('value',)}, children={})})})})),
    ],
    'Your Comment Active Days': [
        Entry(table='Your Comment Active Days', filename='personal_information/profile_information/your_facebook_activity/comments_and_reactions/your_comment_active_days.json', static_fields={'media': ('media',), 'fbid': ('fbid',)}, tree=Node(columns={}, children={'label_values': Node(columns={'label': ('label',), 'value': ('value',)}, children={})})),
        Entry(table='Your Comment Active Days', filename='your_facebook_activity/comments_and_reactions/your_comment_active_days.json', static_fields={'media': ('media',), 'fbid': ('fbid',)}, tree=Node(columns={}, children={'label_values': Node(columns={'label': ('label',), 'value': ('value',)}, children={})})),
    ],
    'Your Comment Edits': [
        Entry(table='Your Comment Edits', filename='personal_information/profile_information/your_facebook_activity/comments_and_reactions/your_comment_edits.json', static_fields={'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',)}, tree=Node(columns={'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',)}, children={'label_values': Node(columns={'label': ('label',), 'value': ('value',)}, children={})})),
        Entry(table='Your Comment Edits', filename='your_facebook_activity/comments_and_reactions/your_comment_edits.json', static_fields={'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',)}, tree=Node(columns={'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',)}, children={'label_values': Node(columns={'label': ('label',), 'value': ('value',)}, children={})})),
    ],
    'Your Comments In Groups': [
        Entry(table='Your Comments In Groups', filename='personal_information/profile_information/your_facebook_activity/groups/your_comments_in_groups.json', static_fields={}, tree=Node(columns={}, children={'group_comments_v2': Node(columns={'timestamp': ('timestamp',)}, children={'data': Node(columns={'timestamp': ('comment', 'timestamp'), 'comment': ('comment', 'comment'), 'group': ('comment', 'group')}, children={})})})),
        Entry(table='Your Comments In Groups', filename='your_activity_across_facebook/groups/your_comments_in_groups.json', static_fields={}, tree=Node(columns={}, children={'group_comments_v2': Node(columns={'timestamp': ('timestamp',)}, children={'data': Node(columns={'timestamp': ('comment', 'timestamp'), 'comment': ('comment', 'comment'), 'group': ('comment', 'group')}, children={})})})),
        Entry(table='Your Comments In Groups', filename='your_facebook_activity/groups/your_comments_in_groups.json', static_fields={}, tree=Node(columns={}, children={'group_comments_v2': Node(columns={'timestamp': ('timestamp',)}, children={'data': Node(columns={'timestamp': ('comment', 'timestamp'), 'comment': ('comment', 'comment'), 'group': ('comment', 'group')}, children={})})})),
    ],
    'Your Consent Settings': [
        Entry(table='Your Consent Settings', filename='ads_information/your_consent_settings.json', static_fields={'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',)}, tree=Node(columns={}, children={'label_values': Node(columns={'label': ('label',), 'timestamp_value': ('timestamp_value',)}, children={})})),
    ],
    'Your Facebook Watch Activity In The Last 28 Days': [
        Entry(table='Your Facebook Watch Activity In The Last 28 Days', filename='logged_information/other_logged_information/your_facebook_watch_activity_in_the_last_28_days.json', static_fields={'media': ('media',), 'fbid': ('fbid',), 'ent_name': ('ent_name',)}, tree=Node(columns={}, children={'label_values': Node(columns={'label': ('label',), 'value': ('value',), 'ent_field_name': ('ent_field_name',)}, children={}), 'media': Node(columns={'media': ()}, children={})})),
    ],
    'Your Friends': [
        Entry(table='Your Friends', filename='connections/friends/your_friends.json', static_fields={}, tree=Node(columns={}, children={'friends_v2': Node(columns={'name': ('name',), 'timestamp': ('timestamp',)}, children={})})),
    ],
    'Your Group Membership Activity': [
        Entry(table='Your Group Membership Activity', filename='personal_information/profile_information/your_facebook_activity/groups/your_group_membership_activity.json', static_fields={}, tree=Node(columns={}, children={'groups_joined_v2': Node(columns={'timestamp': ('timestamp',), 'title': ('title',)}, children={'data': Node(columns={'name': ('name',)}, children={})})})),
        Entry(table='Your Group Membership Activity', filename='your_activity_across_facebook/groups/your_group_membership_activity.json', static_fields={}, tree=Node(columns={}, children={'groups_joined_v2': Node(columns={'timestamp': ('timestamp',), 'title': ('title',)}, children={'data': Node(columns={'name': ('name',)}, children={})})})),
        Entry(table='Your Group Membership Activity', filename='your_facebook_activity/groups/your_group_membership_activity.json', static_fields={}, tree=Node(columns={}, children={'groups_joined_v2': Node(columns={'timestamp': ('timestamp',), 'title': ('title',)}, children={'data': Node(columns={'name': ('name',)}, children={})})})),
    ],
    'Your Groups': [
        Entry(table='Your Groups', filename='your_activity_across_facebook/groups/your_groups.json', static_fields={}, tree=Node(columns={}, children={'groups_admined_v2': Node(columns={'name': ('name',), 'timestamp': ('timestamp',)}, children={})})),
        Entry(table='Your Groups', filename='your_facebook_activity/groups/your_groups.json', static_fields={}, tree=Node(columns={}, children={'groups_admined_v2': Node(columns={'name': ('name',), 'timestamp': ('timestamp',)}, children={})})),
    ],
    'Your Information Download Requests': [
        Entry(table='Your Information Download Requests', filename='personal_information/profile_information/your_facebook_activity/other_activity/your_information_download_requests.json', static_fields={'timestamp': ('timestamp',)}, tree=Node(columns={}, children={})),
        Entry(table='Your Information Download Requests', filename='your_facebook_activity/other_activity/your_information_download_requests.json', static_fields={'timestamp': ('timestamp',)}, tree=Node(columns={'timestamp': ('timestamp',)}, children={})),
    ],
    'Your Pages': [
        Entry(table='Your Pages', filename='your_facebook_activity/pages/your_pages.json', static_fields={}, tree=Node(columns={}, children={'pages_v2': Node(columns={'name': ('name',), 'timestamp': ('timestamp',), 'url': ('url',)}, children={})})),
    ],
    'Your Pages Mentions': [
        Entry(table='Your Pages Mentions', filename='ads_information/your_pages_mentions.json', static_fields={'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',)}, tree=Node(columns={'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',)}, children={'label_values': Node(columns={'label': ('label',), 'vec': ('vec',)}, children={})})),
    ],
    'Your Post Audiences': [
        Entry(table='Your Post Audiences', filename='connections/friends/your_post_audiences.json', static_fields={'media': ('media',), 'fbid': ('fbid',), 'ent_name': ('ent_name',)}, tree=Node(columns={'media': ('media',), 'fbid': ('fbid',), 'ent_name': ('ent_name',)}, children={'label_values': Node(columns={'label': ('label',), 'value': ('value',), 'ent_field_name': ('ent_field_name',), 'dict': ('dict',), 'title': ('title',)}, children={'dict': Node(columns={'dict': ()}, children={})}), 'media': Node(columns={'media': ()}, children={})})),
    ],
    'Your Posts  Check Ins  Photos And Videos 1': [
        Entry(table='Your Posts  Check Ins  Photos And Videos 1', filename='personal_information/profile_information/your_facebook_activity/posts/your_posts__check_ins__photos_and_videos_1.json', static_fields={'timestamp': ('timestamp',), 'title': ('title',)}, tree=Node(columns={'timestamp': ('timestamp',), 'title': ('title',)}, children={'data': Node(columns={'update_timestamp': ('update_timestamp',)}, children={}), 'attachments': Node(columns={}, children={'data': Node(columns={'url': ('external_context', 'url')}, children={})})})),
        Entry(table='Your Posts  Check Ins  Photos And Videos 1', filename='your_activity_across_facebook/posts/your_posts__check_ins__photos_and_videos_1.json', static_fields={'timestamp': ('timestamp',), 'title': ('title',)}, tree=Node(columns={'timestamp': ('timestamp',), 'title': ('title',)}, children={'data': Node(columns={'post': ('post',)}, children={}), 'attachments': Node(columns={}, children={'data': Node(columns={'url': ('external_context', 'url')}, children={})})})),
        Entry(table='Your Posts  Check Ins  Photos And Videos 1', filename='your_facebook_activity/posts/your_posts__check_ins__photos_and_videos_1.json', static_fields={'timestamp': ('timestamp',), 'title': ('title',)}, tree=Node(columns={'timestamp': ('timestamp',), 'title': ('title',)}, children={'data': Node(columns={'update_timestamp': ('update_timestamp',), 'post': ('post',), 'backdated_timestamp': ('backdated_timestamp',)}, children={}), 'attachments': Node(columns={}, children={'data': Node(columns={'url': ('external_context', 'url'), 'name': ('external_context', 'name'), 'source': ('external_context', 'source'), 'title': ('life_event', 'title'), 'year': ('life_event', 'start_date', 'year'), 'month': ('life_event', 'start_date', 'month'), 'day': ('life_event', 'start_date', 'day')}, children={})})})),
    ],
    'Your Preferred Categories': [
        Entry(table='Your Preferred Categories', filename='preferences/preferences/your_preferred_categories.json', static_fields={'media': ('media',), 'fbid': ('fbid',), 'ent_name': ('ent_name',)}, tree=Node(columns={}, children={'label_values': Node(columns={'ent_field_name': ('ent_field_name',), 'label': ('label',)}, children={'vec': Node(columns={'ent_field_name': ('ent_field_name',)}, children={'dict': Node(columns={'ent_field_name': ('ent_field_name',), 'label': ('label',), 'value': ('value',)}, children={})})}), 'media': Node(columns={'media': ()}, children={})})),
    ],
    'Your Recent Reported Conversions': [
        Entry(table='Your Recent Reported Conversions', filename='ads_information/your_recent_reported_conversions.json', static_fields={'media': ('media',), 'fbid': ('fbid',), 'ent_name': ('ent_name',)}, tree=Node(columns={'media': ('media',), 'fbid': ('fbid',), 'ent_name': ('ent_name',)}, children={'label_values': Node(columns={'label': ('label',), 'timestamp_value': ('timestamp_value',), 'ent_field_name': ('ent_field_name',)}, children={}), 'media': Node(columns={'media': ()}, children={})})),
    ],
    'Your Recently Followed History': [
        Entry(table='Your Recently Followed History', filename='personal_information/profile_information/your_facebook_activity/other_activity/your_recently_followed_history.json', static_fields={'media': ('media',), 'fbid': ('fbid',)}, tree=Node(columns={}, children={'label_values': Node(columns={'label': ('label',)}, children={'vec': Node(columns={}, children={'dict': Node(columns={'label': ('label',), 'value': ('value',)}, children={})})})})),
        Entry(table='Your Recently Followed History', filename='your_activity_across_facebook/other_activity/your_recently_followed_history.json', static_fields={'media': ('media',)}, tree=Node(columns={}, children={'label_values': Node(columns={'label': ('label',)}, children={'vec': Node(columns={}, children={'dict': Node(columns={'label': ('label',), 'value': ('value',)}, children={})})})})),
        Entry(table='Your Recently Followed History', filename='your_facebook_activity/other_activity/your_recently_followed_history.json', static_fields={'media': ('media',), 'fbid': ('fbid',), 'ent_name': ('ent_name',)}, tree=Node(columns={}, children={'label_values': Node(columns={'label': ('label',), 'ent_field_name': ('ent_field_name',)}, children={'vec': Node(columns={}, children={'dict': Node(columns={'label': ('label',), 'value': ('value',)}, children={})})}), 'media': Node(columns={'media': ()}, children={})})),
    ],
    'Your Saved Items': [
        Entry(table='Your Saved Items', filename='personal_information/profile_information/your_facebook_activity/saved_items_and_collections/your_saved_items.json', static_fields={}, tree=Node(columns={}, children={'saves_v2': Node(columns={'timestamp': ('timestamp',), 'title': ('title',)}, children={'attachments': Node(columns={}, children={'data': Node(columns={'name': ('external_context', 'name'), 'source': ('external_context', 'source'), 'url': ('external_context', 'url')}, children={})})})})),
        Entry(table='Your Saved Items', filename='your_facebook_activity/saved_items_and_collections/your_saved_items.json', static_fields={}, tree=Node(columns={}, children={'saves_v2': Node(columns={'timestamp': ('timestamp',), 'title': ('title',)}, children={})})),
    ],
    'Your Search History': [
        Entry(table='Your Search History', filename='logged_information/search/your_search_history.json', static_fields={}, tree=Node(columns={}, children={'searches_v2': Node(columns={'timestamp': ('timestamp',), 'title': ('title',)}, children={'data': Node(columns={'text': ('text',)}, children={}), 'attachments': Node(columns={}, children={'data': Node(columns={'text': ('text',)}, children={})})})})),
    ],
    'Your Story Highlights': [
        Entry(table='Your Story Highlights', filename='personal_information/profile_information/preferences/preferences/your_story_highlights.json', static_fields={'media': ('media',), 'fbid': ('fbid',)}, tree=Node(columns={}, children={'label_values': Node(columns={'label': ('label',), 'value': ('value',)}, children={})})),
        Entry(table='Your Story Highlights', filename='preferences/preferences/your_story_highlights.json', static_fields={'media': ('media',), 'fbid': ('fbid',)}, tree=Node(columns={}, children={'label_values': Node(columns={'label': ('label',), 'value': ('value',)}, children={})})),
    ],
    'Your Video Consumption Summary': [
        Entry(table='Your Video Consumption Summary', filename='personal_information/profile_information/your_facebook_activity/other_activity/your_video_consumption_summary.json', static_fields={'media': ('media',), 'fbid': ('fbid',)}, tree=Node(columns={}, children={'label_values': Node(columns={'label': ('label',)}, children={})})),
        Entry(table='Your Video Consumption Summary', filename='your_facebook_activity/other_activity/your_video_consumption_summary.json', static_fields={'media': ('media',), 'fbid': ('fbid',), 'ent_name': ('ent_name',)}, tree=Node(columns={}, children={'label_values': Node(columns={'label': ('label',), 'ent_field_name': ('ent_field_name',), 'value': ('value',)}, children={}), 'media': Node(columns={'media': ()}, children={})})),
    ],
    'Your Videos': [
        Entry(table='Your Videos', filename='personal_information/profile_information/your_facebook_activity/posts/your_videos.json', static_fields={}, tree=Node(columns={}, children={'videos_v2': Node(columns={'uri': ('uri',), 'creation_timestamp': ('creation_timestamp',), 'title': ('title',), 'description': ('description',), 'dubbing_info': ('dubbing_info',), 'media_variants': ('media_variants',)}, children={'media_metadata': Node(columns={}, children={'video_metadata': Node(columns={}, children={'exif_data': Node(columns={'upload_ip': ('upload_ip',), 'upload_timestamp': ('upload_timestamp',)}, children={})})})})})),
        Entry(table='Your Videos', filename='your_facebook_activity/posts/your_videos.json', static_fields={}, tree=Node(columns={}, children={'videos_v2': Node(columns={'uri': ('uri',), 'creation_timestamp': ('creation_timestamp',), 'title': ('title',), 'description': ('description',), 'dubbing_info': ('dubbing_info',), 'media_variants': ('media_variants',)}, children={'media_metadata': Node(columns={}, children={'video_metadata': Node(columns={}, children={'exif_data': Node(columns={'upload_ip': ('upload_ip',), 'upload_timestamp': ('upload_timestamp',)}, children={})})})})})),
    ],
    'Your Watch Settings': [
        Entry(table='Your Watch Settings', filename='personal_information/profile_information/preferences/preferences/your_watch_settings.json', static_fields={'media': ('media',), 'fbid': ('fbid',)}, tree=Node(columns={}, children={'label_values': Node(columns={'label': ('label',), 'value': ('value',)}, children={})})),
        Entry(table='Your Watch Settings', filename='preferences/preferences/your_watch_settings.json', static_fields={'media': ('media',), 'fbid': ('fbid',), 'ent_name': ('ent_name',)}, tree=Node(columns={}, children={'label_values': Node(columns={'label': ('label',), 'value': ('value',), 'ent_field_name': ('ent_field_name',), 'vec': ('vec',), 'timestamp_value': ('timestamp_value',)}, children={'vec': Node(columns={'vec': ()}, children={})}), 'media': Node(columns={'media': ()}, children={})})),
    ],
}

YT_ENTRIES: dict[str, list[Entry]] = {
    'Historial-De-BúSqueda': [
        Entry(table='Historial-De-BúSqueda', filename='historial/historial-de-búsqueda.json', static_fields={}, tree=Node(columns={'header': ('header',), 'title': ('title',), 'titleUrl': ('titleUrl',), 'description': ('description',), 'time': ('time',), 'products': ('products',), 'activityControls': ('activityControls',)}, children={'details': Node(columns={'name': ('name',)}, children={})})),
    ],
    'Historial-De-Búsqueda': [
        Entry(table='Historial-De-Búsqueda', filename='historial/historial-de-búsqueda.json', static_fields={}, tree=Node(columns={'header': ('header',), 'title': ('title',), 'titleUrl': ('titleUrl',), 'time': ('time',), 'products': ('products',), 'activityControls': ('activityControls',)}, children={})),
    ],
    'Historial-De-Reproducciones': [
        Entry(table='Historial-De-Reproducciones', filename='historial/historial-de-reproducciones.json', static_fields={}, tree=Node(columns={'header': ('header',), 'title': ('title',), 'titleUrl': ('titleUrl',), 'time': ('time',), 'products': ('products',), 'activityControls': ('activityControls',)}, children={'subtitles': Node(columns={'name': ('name',), 'url': ('url',)}, children={}), 'details': Node(columns={'name': ('name',)}, children={})})),
    ],
    'Istoricul CăUtăRilor': [
        Entry(table='Istoricul CăUtăRilor', filename='istoric/istoricul căutărilor.json', static_fields={}, tree=Node(columns={'header': ('header',), 'title': ('title',), 'titleUrl': ('titleUrl',), 'description': ('description',), 'time': ('time',), 'products': ('products',), 'activityControls': ('activityControls',)}, children={'details': Node(columns={'name': ('name',)}, children={})})),
    ],
    'Istoricul Căutărilor': [
        Entry(table='Istoricul Căutărilor', filename='istoric/istoricul căutărilor.json', static_fields={}, tree=Node(columns={'header': ('header',), 'title': ('title',), 'titleUrl': ('titleUrl',), 'time': ('time',), 'products': ('products',), 'activityControls': ('activityControls',)}, children={})),
    ],
    'Istoricul-VizionăRilor': [
        Entry(table='Istoricul-VizionăRilor', filename='istoric/istoricul-vizionărilor.json', static_fields={}, tree=Node(columns={'header': ('header',), 'title': ('title',), 'titleUrl': ('titleUrl',), 'time': ('time',), 'products': ('products',), 'activityControls': ('activityControls',)}, children={'subtitles': Node(columns={'name': ('name',), 'url': ('url',)}, children={})})),
    ],
    'Istoricul-Vizionărilor': [
        Entry(table='Istoricul-Vizionărilor', filename='istoric/istoricul-vizionărilor.json', static_fields={}, tree=Node(columns={'header': ('header',), 'title': ('title',), 'titleUrl': ('titleUrl',), 'time': ('time',), 'products': ('products',), 'activityControls': ('activityControls',)}, children={'subtitles': Node(columns={'name': ('name',), 'url': ('url',)}, children={})})),
    ],
    'Kijkgeschiedenis': [
        Entry(table='Kijkgeschiedenis', filename='geschiedenis/kijkgeschiedenis.json', static_fields={}, tree=Node(columns={'header': ('header',), 'title': ('title',), 'titleUrl': ('titleUrl',), 'time': ('time',), 'products': ('products',), 'activityControls': ('activityControls',)}, children={'subtitles': Node(columns={'name': ('name',), 'url': ('url',)}, children={})})),
    ],
    'PaiešKos Istorija': [
        Entry(table='PaiešKos Istorija', filename='istorija/paieškos istorija.json', static_fields={}, tree=Node(columns={'header': ('header',), 'title': ('title',), 'titleUrl': ('titleUrl',), 'description': ('description',), 'time': ('time',), 'products': ('products',), 'activityControls': ('activityControls',)}, children={'details': Node(columns={'name': ('name',)}, children={})})),
    ],
    'Paieškos Istorija': [
        Entry(table='Paieškos Istorija', filename='istorija/paieškos istorija.json', static_fields={}, tree=Node(columns={'header': ('header',), 'title': ('title',), 'titleUrl': ('titleUrl',), 'time': ('time',), 'products': ('products',), 'activityControls': ('activityControls',)}, children={})),
    ],
    'Search-History': [
        Entry(table='Search-History', filename='history/search-history.json', static_fields={}, tree=Node(columns={'header': ('header',), 'title': ('title',), 'titleUrl': ('titleUrl',), 'description': ('description',), 'time': ('time',), 'products': ('products',), 'activityControls': ('activityControls',)}, children={'details': Node(columns={'name': ('name',)}, children={})})),
        Entry(table='Search-History', filename='youtube_takeout/history/search-history.json', static_fields={}, tree=Node(columns={'header': ('header',), 'title': ('title',), 'titleUrl': ('titleUrl',), 'time': ('time',), 'products': ('products',), 'activityControls': ('activityControls',)}, children={})),
    ],
    'Watch-History': [
        Entry(table='Watch-History', filename='history/watch-history.json', static_fields={}, tree=Node(columns={'header': ('header',), 'title': ('title',), 'titleUrl': ('titleUrl',), 'time': ('time',), 'products': ('products',), 'activityControls': ('activityControls',)}, children={'subtitles': Node(columns={'name': ('name',), 'url': ('url',)}, children={}), 'details': Node(columns={'name': ('name',)}, children={})})),
        Entry(table='Watch-History', filename='youtube_takeout/history/watch-history.json', static_fields={}, tree=Node(columns={'header': ('header',), 'title': ('title',), 'time': ('time',), 'products': ('products',), 'activityControls': ('activityControls',)}, children={'details': Node(columns={'name': ('name',)}, children={})})),
    ],
    'Zoekgeschiedenis': [
        Entry(table='Zoekgeschiedenis', filename='geschiedenis/zoekgeschiedenis.json', static_fields={}, tree=Node(columns={'header': ('header',), 'title': ('title',), 'titleUrl': ('titleUrl',), 'time': ('time',), 'products': ('products',), 'activityControls': ('activityControls',), 'description': ('description',)}, children={'details': Node(columns={'name': ('name',)}, children={})})),
    ],
    'ŽIūRėJimo Istorija': [
        Entry(table='ŽIūRėJimo Istorija', filename='istorija/žiūrėjimo istorija.json', static_fields={}, tree=Node(columns={'header': ('header',), 'title': ('title',), 'titleUrl': ('titleUrl',), 'description': ('description',), 'time': ('time',), 'products': ('products',), 'activityControls': ('activityControls',)}, children={'details': Node(columns={'name': ('name',)}, children={})})),
    ],
    'Žiūrėjimo Istorija': [
        Entry(table='Žiūrėjimo Istorija', filename='istorija/žiūrėjimo istorija.json', static_fields={}, tree=Node(columns={'header': ('header',), 'title': ('title',), 'titleUrl': ('titleUrl',), 'time': ('time',), 'products': ('products',), 'activityControls': ('activityControls',)}, children={'subtitles': Node(columns={'name': ('name',), 'url': ('url',)}, children={})})),
    ],
}

YT_CSV_ENTRIES: dict[str, list[Entry]] = {
    'Ajustes_de_moderación_de_la_comunidad_del_canal': [
        Entry(table='Ajustes_de_moderación_de_la_comunidad_del_canal', filename='Ajustes de moderación de la comunidad del canal.csv', static_fields={'ID de canal': ('ID de canal',)}, tree=Node(columns={}, children={})),
    ],
    'Ajustes_de_moderación_de_la_comunidad_del_canal': [
        Entry(table='Ajustes_de_moderación_de_la_comunidad_del_canal', filename='Ajustes de moderación de la comunidad del canal.csv', static_fields={'ID de canal': ('ID de canal',)}, tree=Node(columns={}, children={})),
    ],
    'Favorites-videoclipuri': [
        Entry(table='Favorites-videoclipuri', filename='Favorites-videoclipuri.csv', static_fields={'ID-ul videoclipului': ('ID-ul videoclipului',), 'Marcaj temporal de creare a videoclipului din playlist': ('Marcaj temporal de creare a videoclipului din playlist',)}, tree=Node(columns={}, children={})),
    ],
    'Favorites-videos': [
        Entry(table='Favorites-videos', filename='Favorites-videos.csv', static_fields={'Video ID': ('Video ID',), 'Playlist Video Creation Timestamp': ('Playlist Video Creation Timestamp',), 'Vaizdo įrašo ID': ('Vaizdo įrašo ID',), 'Grojaraščio vaizdo įrašo sukūrimo laiko žymė': ('Grojaraščio vaizdo įrašo sukūrimo laiko žymė',)}, tree=Node(columns={}, children={})),
    ],
    'Favorites-vídeos': [
        Entry(table='Favorites-vídeos', filename='Favorites-vídeos.csv', static_fields={'ID de vídeo': ('ID de vídeo',), 'Marca de tiempo de creación de la lista de reproducción de vídeos': ('Marca de tiempo de creación de la lista de reproducción de vídeos',)}, tree=Node(columns={}, children={})),
    ],
    'Listas_de_reproducción': [
        Entry(table='Listas_de_reproducción', filename='Listas de reproducción.csv', static_fields={'ID de lista de reproducción': ('ID de lista de reproducción',), 'Añadir vídeos nuevos al principio': ('Añadir vídeos nuevos al principio',), 'Título de la lista de reproducción (original)': ('Título de la lista de reproducción (original)',), 'Idioma del título de la lista de reproducción (original)': ('Idioma del título de la lista de reproducción (original)',), 'Marca de tiempo de creación de la lista de reproducción': ('Marca de tiempo de creación de la lista de reproducción',), 'Marca de tiempo de actualización de la lista de reproducción': ('Marca de tiempo de actualización de la lista de reproducción',), 'Orden de vídeos de lista de reproducción': ('Orden de vídeos de lista de reproducción',), 'Visibilidad de la lista de reproducción': ('Visibilidad de la lista de reproducción',)}, tree=Node(columns={}, children={})),
    ],
    'URL-configuraties_van_kanaal': [
        Entry(table='URL-configuraties_van_kanaal', filename='URL-configuraties van kanaal.csv', static_fields={'Kanaal-ID': ('Kanaal-ID',), 'Naam van vanity-URL 1 voor kanaal': ('Naam van vanity-URL 1 voor kanaal',), 'Naam van vanity-URL 2 voor kanaal': ('Naam van vanity-URL 2 voor kanaal',)}, tree=Node(columns={}, children={})),
    ],
    'Video_s_in_Favorites': [
        Entry(table='Video_s_in_Favorites', filename='Video_s in Favorites.csv', static_fields={'Video-ID': ('Video-ID',), 'Tijdstempel voor het maken van een playlistvideo': ('Tijdstempel voor het maken van een playlistvideo',)}, tree=Node(columns={}, children={})),
    ],
    'Video_s_in_Watch_later': [
        Entry(table='Video_s_in_Watch_later', filename='Video_s in Watch later.csv', static_fields={'Video-ID': ('Video-ID',), 'Tijdstempel voor het maken van een playlistvideo': ('Tijdstempel voor het maken van een playlistvideo',)}, tree=Node(columns={}, children={})),
    ],
    'Video_s_in_crochet': [
        Entry(table='Video_s_in_crochet', filename='Video_s in crochet.csv', static_fields={'Video-ID': ('Video-ID',), 'Tijdstempel voor het maken van een playlistvideo': ('Tijdstempel voor het maken van een playlistvideo',)}, tree=Node(columns={}, children={})),
    ],
    'Watch_later-videoclipuri': [
        Entry(table='Watch_later-videoclipuri', filename='Watch later-videoclipuri.csv', static_fields={'ID-ul videoclipului': ('ID-ul videoclipului',), 'Marcaj temporal de creare a videoclipului din playlist': ('Marcaj temporal de creare a videoclipului din playlist',)}, tree=Node(columns={}, children={})),
    ],
    'Watch_later-videos': [
        Entry(table='Watch_later-videos', filename='Watch later-videos.csv', static_fields={'Video ID': ('Video ID',), 'Playlist Video Creation Timestamp': ('Playlist Video Creation Timestamp',), 'Vaizdo įrašo ID': ('Vaizdo įrašo ID',), 'Grojaraščio vaizdo įrašo sukūrimo laiko žymė': ('Grojaraščio vaizdo įrašo sukūrimo laiko žymė',)}, tree=Node(columns={}, children={})),
    ],
    'Watch_later-vídeos': [
        Entry(table='Watch_later-vídeos', filename='Watch later-vídeos.csv', static_fields={'ID de vídeo': ('ID de vídeo',), 'Marca de tiempo de creación de la lista de reproducción de vídeos': ('Marca de tiempo de creación de la lista de reproducción de vídeos',)}, tree=Node(columns={}, children={})),
    ],
    'abonamente': [
        Entry(table='abonamente', filename='abonamente.csv', static_fields={'ID-ul canalului': ('ID-ul canalului',), 'Adresa URL a canalului': ('Adresa URL a canalului',), 'Titlul canalului': ('Titlul canalului',)}, tree=Node(columns={}, children={})),
    ],
    'abonnementen': [
        Entry(table='abonnementen', filename='abonnementen.csv', static_fields={'Kanaal-ID': ('Kanaal-ID',), 'Kanaal-URL': ('Kanaal-URL',), 'Kanaaltitel': ('Kanaaltitel',)}, tree=Node(columns={}, children={})),
    ],
    'canal': [
        Entry(table='canal', filename='canal.csv', static_fields={'ID-ul canalului': ('ID-ul canalului',), 'Titlul canalului (original)': ('Titlul canalului (original)',), 'Vizibilitatea canalului': ('Vizibilitatea canalului',), 'ID de canal': ('ID de canal',), 'Título del canal (original)': ('Título del canal (original)',), 'Visibilidad del canal': ('Visibilidad del canal',)}, tree=Node(columns={}, children={})),
    ],
    'channel': [
        Entry(table='channel', filename='channel.csv', static_fields={'Channel ID': ('Channel ID',), 'Channel Title (Original)': ('Channel Title (Original)',), 'Channel Visibility': ('Channel Visibility',)}, tree=Node(columns={}, children={})),
    ],
    'channel_URL_configs': [
        Entry(table='channel_URL_configs', filename='channel URL configs.csv', static_fields={'Channel ID': ('Channel ID',), 'Channel Vanity URL 1 Name': ('Channel Vanity URL 1 Name',), 'Channel Vanity URL 2 Name': ('Channel Vanity URL 2 Name',)}, tree=Node(columns={}, children={})),
    ],
    'channel_community_moderation_settings': [
        Entry(table='channel_community_moderation_settings', filename='channel community moderation settings.csv', static_fields={'Channel ID': ('Channel ID',)}, tree=Node(columns={}, children={})),
    ],
    'channel_feature_data': [
        Entry(table='channel_feature_data', filename='channel feature data.csv', static_fields={'Channel ID': ('Channel ID',), 'Channel Auto Moderation in Live Chat': ('Channel Auto Moderation in Live Chat',), 'Video Default Allowed Comments Type': ('Video Default Allowed Comments Type',), 'Video Default Targeted Audience': ('Video Default Targeted Audience',), 'Video Default License': ('Video Default License',)}, tree=Node(columns={}, children={})),
    ],
    'channel_page_settings': [
        Entry(table='channel_page_settings', filename='channel page settings.csv', static_fields={'Channel ID': ('Channel ID',)}, tree=Node(columns={}, children={})),
    ],
    'comentarii': [
        Entry(table='comentarii', filename='comentarii.csv', static_fields={'ID-ul comentariului': ('ID-ul comentariului',), 'ID-ul canalului': ('ID-ul canalului',), 'Marcajul temporal de creare a comentariului': ('Marcajul temporal de creare a comentariului',), 'Preț': ('Preț',), 'ID-ul videoclipului': ('ID-ul videoclipului',), 'Textul comentariului': ('Textul comentariului',)}, tree=Node(columns={}, children={})),
    ],
    'comentarios': [
        Entry(table='comentarios', filename='comentarios.csv', static_fields={'ID de comentario': ('ID de comentario',), 'ID de canal': ('ID de canal',), 'Marca de tiempo de creación del comentario': ('Marca de tiempo de creación del comentario',), 'Precio': ('Precio',), 'ID de vídeo': ('ID de vídeo',), 'Texto del comentario': ('Texto del comentario',)}, tree=Node(columns={}, children={})),
    ],
    'comments': [
        Entry(table='comments', filename='comments.csv', static_fields={'Comment ID': ('Comment ID',), 'Channel ID': ('Channel ID',), 'Comment Create Timestamp': ('Comment Create Timestamp',), 'Price': ('Price',), 'Video ID': ('Video ID',), 'Comment Text': ('Comment Text',)}, tree=Node(columns={}, children={})),
    ],
    'configuraciones_de_la_URL_del_canal': [
        Entry(table='configuraciones_de_la_URL_del_canal', filename='configuraciones de la URL del canal.csv', static_fields={'ID de canal': ('ID de canal',), 'Nombre de la URL mnemónica del canal (1)': ('Nombre de la URL mnemónica del canal (1)',), 'Nombre de la URL mnemónica del canal (2)': ('Nombre de la URL mnemónica del canal (2)',)}, tree=Node(columns={}, children={})),
    ],
    'configuración_de_la_página_del_canal': [
        Entry(table='configuración_de_la_página_del_canal', filename='configuración de la página del canal.csv', static_fields={'ID de canal': ('ID de canal',)}, tree=Node(columns={}, children={})),
    ],
    'configuración_de_la_página_del_canal': [
        Entry(table='configuración_de_la_página_del_canal', filename='configuración de la página del canal.csv', static_fields={'ID de canal': ('ID de canal',)}, tree=Node(columns={}, children={})),
    ],
    'configurații_pentru_adresa_URL_a_canalului': [
        Entry(table='configurații_pentru_adresa_URL_a_canalului', filename='configurații pentru adresa URL a canalului.csv', static_fields={'ID-ul canalului': ('ID-ul canalului',), 'Numele adresei URL personalizate a canalului 1': ('Numele adresei URL personalizate a canalului 1',), 'Numele adresei URL personalizate a canalului 2': ('Numele adresei URL personalizate a canalului 2',)}, tree=Node(columns={}, children={})),
    ],
    'configurații_pentru_adresa_URL_a_canalului': [
        Entry(table='configurații_pentru_adresa_URL_a_canalului', filename='configurații pentru adresa URL a canalului.csv', static_fields={'ID-ul canalului': ('ID-ul canalului',), 'Numele adresei URL personalizate a canalului 1': ('Numele adresei URL personalizate a canalului 1',)}, tree=Node(columns={}, children={})),
    ],
    'crochet-videoclipuri': [
        Entry(table='crochet-videoclipuri', filename='crochet-videoclipuri.csv', static_fields={'ID-ul videoclipului': ('ID-ul videoclipului',), 'Marcaj temporal de creare a videoclipului din playlist': ('Marcaj temporal de creare a videoclipului din playlist',)}, tree=Node(columns={}, children={})),
    ],
    'crochet-videos': [
        Entry(table='crochet-videos', filename='crochet-videos.csv', static_fields={'Video ID': ('Video ID',), 'Playlist Video Creation Timestamp': ('Playlist Video Creation Timestamp',), 'Vaizdo įrašo ID': ('Vaizdo įrašo ID',), 'Grojaraščio vaizdo įrašo sukūrimo laiko žymė': ('Grojaraščio vaizdo įrašo sukūrimo laiko žymė',)}, tree=Node(columns={}, children={})),
    ],
    'crochet-vídeos': [
        Entry(table='crochet-vídeos', filename='crochet-vídeos.csv', static_fields={'ID de vídeo': ('ID de vídeo',), 'Marca de tiempo de creación de la lista de reproducción de vídeos': ('Marca de tiempo de creación de la lista de reproducción de vídeos',)}, tree=Node(columns={}, children={})),
    ],
    'date_despre_funcțiile_canalului': [
        Entry(table='date_despre_funcțiile_canalului', filename='date despre funcțiile canalului.csv', static_fields={'ID-ul canalului': ('ID-ul canalului',), 'Moderare automată a canalului în chatul live': ('Moderare automată a canalului în chatul live',), 'Tipul prestabilit de comentarii permise ale videoclipului': ('Tipul prestabilit de comentarii permise ale videoclipului',), 'Publicul vizat prestabilit al videoclipului': ('Publicul vizat prestabilit al videoclipului',), 'Licența prestabilită a videoclipului': ('Licența prestabilită a videoclipului',)}, tree=Node(columns={}, children={})),
    ],
    'date_despre_funcțiile_canalului': [
        Entry(table='date_despre_funcțiile_canalului', filename='date despre funcțiile canalului.csv', static_fields={'ID-ul canalului': ('ID-ul canalului',), 'Moderare automată a canalului în chatul live': ('Moderare automată a canalului în chatul live',), 'Tipul prestabilit de comentarii permise ale videoclipului': ('Tipul prestabilit de comentarii permise ale videoclipului',), 'Publicul vizat prestabilit al videoclipului': ('Publicul vizat prestabilit al videoclipului',), 'Licența prestabilită a videoclipului': ('Licența prestabilită a videoclipului',)}, tree=Node(columns={}, children={})),
    ],
    'datos_de_la_función_del_canal': [
        Entry(table='datos_de_la_función_del_canal', filename='datos de la función del canal.csv', static_fields={'ID de canal': ('ID de canal',), 'Moderación automática del canal en el chat en directo': ('Moderación automática del canal en el chat en directo',), 'Tipo de comentarios permitidos de forma predeterminada en el vídeo': ('Tipo de comentarios permitidos de forma predeterminada en el vídeo',), 'Audiencia objetivo predeterminada del vídeo': ('Audiencia objetivo predeterminada del vídeo',), 'Licencia del vídeo predeterminada': ('Licencia del vídeo predeterminada',)}, tree=Node(columns={}, children={})),
    ],
    'datos_de_la_función_del_canal': [
        Entry(table='datos_de_la_función_del_canal', filename='datos de la función del canal.csv', static_fields={'ID de canal': ('ID de canal',), 'Moderación automática del canal en el chat en directo': ('Moderación automática del canal en el chat en directo',), 'Tipo de comentarios permitidos de forma predeterminada en el vídeo': ('Tipo de comentarios permitidos de forma predeterminada en el vídeo',), 'Audiencia objetivo predeterminada del vídeo': ('Audiencia objetivo predeterminada del vídeo',), 'Licencia del vídeo predeterminada': ('Licencia del vídeo predeterminada',)}, tree=Node(columns={}, children={})),
    ],
    'gegevens_voor_kanaalfunctie': [
        Entry(table='gegevens_voor_kanaalfunctie', filename='gegevens voor kanaalfunctie.csv', static_fields={'Kanaal-ID': ('Kanaal-ID',), 'Automatische moderatie in livechat van kanaal': ('Automatische moderatie in livechat van kanaal',), 'Standaard toegestane reactietype van video': ('Standaard toegestane reactietype van video',), 'Standaard doelgroep van video': ('Standaard doelgroep van video',), 'Standaardlicentie van video': ('Standaardlicentie van video',), 'Automatische moderatie in live chat van kanaal': ('Automatische moderatie in live chat van kanaal',)}, tree=Node(columns={}, children={})),
    ],
    'grojaraščiai': [
        Entry(table='grojaraščiai', filename='grojaraščiai.csv', static_fields={'Grojaraščio ID': ('Grojaraščio ID',), 'Pridėti naujus vaizdo įrašus viršuje': ('Pridėti naujus vaizdo įrašus viršuje',), 'Grojaraščio pavadinimas (originalas)': ('Grojaraščio pavadinimas (originalas)',), 'Grojaraščio pavadinimo (originalo) kalba': ('Grojaraščio pavadinimo (originalo) kalba',), 'Grojaraščio sukūrimo laiko žymė': ('Grojaraščio sukūrimo laiko žymė',), 'Grojaraščio atnaujinimo laiko žymė': ('Grojaraščio atnaujinimo laiko žymė',), 'Grojaraščio vaizdo įrašų tvarka': ('Grojaraščio vaizdo įrašų tvarka',), 'Grojaraščio matomumas': ('Grojaraščio matomumas',)}, tree=Node(columns={}, children={})),
    ],
    'instellingen_voor_het_beheer_van_je_kanaalcommu': [
        Entry(table='instellingen_voor_het_beheer_van_je_kanaalcommu', filename='instellingen voor het beheer van je kanaalcommu.csv', static_fields={'Kanaal-ID': ('Kanaal-ID',)}, tree=Node(columns={}, children={})),
    ],
    'instellingen_voor_kanaalpagina': [
        Entry(table='instellingen_voor_kanaalpagina', filename='instellingen voor kanaalpagina.csv', static_fields={'Kanaal-ID': ('Kanaal-ID',)}, tree=Node(columns={}, children={})),
    ],
    'kanaal': [
        Entry(table='kanaal', filename='kanaal.csv', static_fields={'Kanaal-ID': ('Kanaal-ID',), '(Originele) kanaaltitel': ('(Originele) kanaaltitel',), 'Kanaalzichtbaarheid': ('Kanaalzichtbaarheid',)}, tree=Node(columns={}, children={})),
    ],
    'kanalas': [
        Entry(table='kanalas', filename='kanalas.csv', static_fields={'Kanalo ID': ('Kanalo ID',), 'Kanalo pavadinimas (pradinis)': ('Kanalo pavadinimas (pradinis)',), 'Kanalo matomumas': ('Kanalo matomumas',)}, tree=Node(columns={}, children={})),
    ],
    'kanalo_URL_konfigūracijos': [
        Entry(table='kanalo_URL_konfigūracijos', filename='kanalo URL konfigūracijos.csv', static_fields={'Kanalo ID': ('Kanalo ID',), '1 kanalo reklaminio URL pavadinimas': ('1 kanalo reklaminio URL pavadinimas',), '2 kanalo reklaminio URL pavadinimas': ('2 kanalo reklaminio URL pavadinimas',)}, tree=Node(columns={}, children={})),
    ],
    'kanalo_URL_konfigūracijos': [
        Entry(table='kanalo_URL_konfigūracijos', filename='kanalo URL konfigūracijos.csv', static_fields={'Kanalo ID': ('Kanalo ID',), '1 kanalo reklaminio URL pavadinimas': ('1 kanalo reklaminio URL pavadinimas',)}, tree=Node(columns={}, children={})),
    ],
    'kanalo_bendruomenės_moderavimo_nustatymai': [
        Entry(table='kanalo_bendruomenės_moderavimo_nustatymai', filename='kanalo bendruomenės moderavimo nustatymai.csv', static_fields={'Kanalo ID': ('Kanalo ID',)}, tree=Node(columns={}, children={})),
    ],
    'kanalo_bendruomenės_moderavimo_nustatymai': [
        Entry(table='kanalo_bendruomenės_moderavimo_nustatymai', filename='kanalo bendruomenės moderavimo nustatymai.csv', static_fields={'Kanalo ID': ('Kanalo ID',)}, tree=Node(columns={}, children={})),
    ],
    'kanalo_funkcijų_duomenys': [
        Entry(table='kanalo_funkcijų_duomenys', filename='kanalo funkcijų duomenys.csv', static_fields={'Kanalo ID': ('Kanalo ID',), 'Automatinis kanalo moderavimas tiesioginiame pokalbyje': ('Automatinis kanalo moderavimas tiesioginiame pokalbyje',), 'Numatytasis vaizdo įrašo leidžiamų komentarų tipas': ('Numatytasis vaizdo įrašo leidžiamų komentarų tipas',), 'Numatytoji vaizdo įrašo tikslinė auditorija': ('Numatytoji vaizdo įrašo tikslinė auditorija',), 'Numatytoji vaizdo įrašo licencija': ('Numatytoji vaizdo įrašo licencija',)}, tree=Node(columns={}, children={})),
    ],
    'kanalo_funkcijų_duomenys': [
        Entry(table='kanalo_funkcijų_duomenys', filename='kanalo funkcijų duomenys.csv', static_fields={'Kanalo ID': ('Kanalo ID',), 'Automatinis kanalo moderavimas tiesioginiame pokalbyje': ('Automatinis kanalo moderavimas tiesioginiame pokalbyje',), 'Numatytasis vaizdo įrašo leidžiamų komentarų tipas': ('Numatytasis vaizdo įrašo leidžiamų komentarų tipas',), 'Numatytoji vaizdo įrašo tikslinė auditorija': ('Numatytoji vaizdo įrašo tikslinė auditorija',), 'Numatytoji vaizdo įrašo licencija': ('Numatytoji vaizdo įrašo licencija',)}, tree=Node(columns={}, children={})),
    ],
    'kanalo_puslapio_nustatymai': [
        Entry(table='kanalo_puslapio_nustatymai', filename='kanalo puslapio nustatymai.csv', static_fields={'Kanalo ID': ('Kanalo ID',)}, tree=Node(columns={}, children={})),
    ],
    'komentarai': [
        Entry(table='komentarai', filename='komentarai.csv', static_fields={'Komentaro ID': ('Komentaro ID',), 'Kanalo ID': ('Kanalo ID',), 'Komentaro sukūrimo laiko žymė': ('Komentaro sukūrimo laiko žymė',), 'Kaina': ('Kaina',), 'Vaizdo įrašo ID': ('Vaizdo įrašo ID',), 'Komentuoti tekstą': ('Komentuoti tekstą',)}, tree=Node(columns={}, children={})),
    ],
    'playlists': [
        Entry(table='playlists', filename='playlists.csv', static_fields={'Playlist ID': ('Playlist ID',), 'Add new videos to top': ('Add new videos to top',), 'Playlist Title (Original)': ('Playlist Title (Original)',), 'Playlist Title (Original) Language': ('Playlist Title (Original) Language',), 'Playlist Create Timestamp': ('Playlist Create Timestamp',), 'Playlist Update Timestamp': ('Playlist Update Timestamp',), 'Playlist Video Order': ('Playlist Video Order',), 'Playlist Visibility': ('Playlist Visibility',), 'Playlist-ID': ('Playlist-ID',), "Nieuwe video's bovenaan toevoegen": ("Nieuwe video's bovenaan toevoegen",), 'Playlist-titel (Origineel)': ('Playlist-titel (Origineel)',), '(Originele) taal van playlist-titel': ('(Originele) taal van playlist-titel',), 'Playlist tijdstempel maken': ('Playlist tijdstempel maken',), 'Playlist tijdstempel updaten': ('Playlist tijdstempel updaten',), 'Videovolgorde playlist': ('Videovolgorde playlist',), 'Zichtbaarheid van playlist': ('Zichtbaarheid van playlist',)}, tree=Node(columns={}, children={})),
    ],
    'playlisturi': [
        Entry(table='playlisturi', filename='playlisturi.csv', static_fields={'ID-ul playlistului': ('ID-ul playlistului',), 'Adaugă videoclipuri noi în partea de sus': ('Adaugă videoclipuri noi în partea de sus',), 'Titlul playlistului (original)': ('Titlul playlistului (original)',), 'Limba titlului playlistului (original)': ('Limba titlului playlistului (original)',), 'Playlistul creează marcaj temporal': ('Playlistul creează marcaj temporal',), 'Playlistul actualizează marcajul temporal': ('Playlistul actualizează marcajul temporal',), 'Ordinea videoclipurilor în playlist': ('Ordinea videoclipurilor în playlist',), 'Vizibilitatea playlistului': ('Vizibilitatea playlistului',)}, tree=Node(columns={}, children={})),
    ],
    'prenumeratos': [
        Entry(table='prenumeratos', filename='prenumeratos.csv', static_fields={'Kanalo ID': ('Kanalo ID',), 'Kanalo URL': ('Kanalo URL',), 'Kanalo pavadinimas': ('Kanalo pavadinimas',)}, tree=Node(columns={}, children={})),
    ],
    'reacties': [
        Entry(table='reacties', filename='reacties.csv', static_fields={'Reactie-ID': ('Reactie-ID',), 'Kanaal-ID': ('Kanaal-ID',), 'Aanmaaktijdstempel reactie': ('Aanmaaktijdstempel reactie',), 'Prijs': ('Prijs',), 'Video-ID': ('Video-ID',), 'Reactietekst': ('Reactietekst',)}, tree=Node(columns={}, children={})),
    ],
    'setări_de_moderare_a_comunității_canalului': [
        Entry(table='setări_de_moderare_a_comunității_canalului', filename='setări de moderare a comunității canalului.csv', static_fields={'ID-ul canalului': ('ID-ul canalului',)}, tree=Node(columns={}, children={})),
    ],
    'setările_paginii_de_canal': [
        Entry(table='setările_paginii_de_canal', filename='setările paginii de canal.csv', static_fields={'ID-ul canalului': ('ID-ul canalului',)}, tree=Node(columns={}, children={})),
    ],
    'setări_de_moderare_a_comunității_canalului': [
        Entry(table='setări_de_moderare_a_comunității_canalului', filename='setări de moderare a comunității canalului.csv', static_fields={'ID-ul canalului': ('ID-ul canalului',)}, tree=Node(columns={}, children={})),
    ],
    'setările_paginii_de_canal': [
        Entry(table='setările_paginii_de_canal', filename='setările paginii de canal.csv', static_fields={'ID-ul canalului': ('ID-ul canalului',)}, tree=Node(columns={}, children={})),
    ],
    'subscriptions': [
        Entry(table='subscriptions', filename='subscriptions.csv', static_fields={'Channel Id': ('Channel Id',), 'Channel Url': ('Channel Url',), 'Channel Title': ('Channel Title',)}, tree=Node(columns={}, children={})),
    ],
    'suscripciones': [
        Entry(table='suscripciones', filename='suscripciones.csv', static_fields={'ID del canal': ('ID del canal',), 'URL del canal': ('URL del canal',), 'Título del canal': ('Título del canal',)}, tree=Node(columns={}, children={})),
    ],
    'vaizdo_įrašai': [
        Entry(table='vaizdo_įrašai', filename='vaizdo įrašai.csv', static_fields={'Vaizdo įrašo ID': ('Vaizdo įrašo ID',), 'Apytikrė trukmė (ms)': ('Apytikrė trukmė (ms)',), 'Vaizdo įrašo garso takelio kalba': ('Vaizdo įrašo garso takelio kalba',), 'Vaizdo įrašo kategorija': ('Vaizdo įrašo kategorija',), 'Vaizdo įrašo aprašas (originalas)': ('Vaizdo įrašo aprašas (originalas)',), 'Kanalo ID': ('Kanalo ID',), 'Vaizdo įrašo pavadinimas (originalas)': ('Vaizdo įrašo pavadinimas (originalas)',), 'Privatumas': ('Privatumas',), 'Vaizdo įrašo būsena': ('Vaizdo įrašo būsena',), 'Vaizdo įrašo sukūrimo laiko žymė': ('Vaizdo įrašo sukūrimo laiko žymė',), 'Vaizdo įrašo paskelbimo laiko žymė': ('Vaizdo įrašo paskelbimo laiko žymė',)}, tree=Node(columns={}, children={})),
    ],
    'video_s': [
        Entry(table='video_s', filename='video_s.csv', static_fields={'Video-ID': ('Video-ID',), 'Geschatte duur (ms)': ('Geschatte duur (ms)',), 'Audiotaal van video': ('Audiotaal van video',), 'Videocategorie': ('Videocategorie',), 'Videobeschrijving (origineel)': ('Videobeschrijving (origineel)',), 'Kanaal-ID': ('Kanaal-ID',), 'Videotitel (origineel)': ('Videotitel (origineel)',), 'Privacy': ('Privacy',), 'Videostatus': ('Videostatus',), 'Tijdstempel aanmaaktijd video': ('Tijdstempel aanmaaktijd video',), 'Tijdstempel publicatietijd video': ('Tijdstempel publicatietijd video',)}, tree=Node(columns={}, children={})),
    ],
    'videoclipuri': [
        Entry(table='videoclipuri', filename='videoclipuri.csv', static_fields={'ID-ul videoclipului': ('ID-ul videoclipului',), 'Durată aproximativă (ms)': ('Durată aproximativă (ms)',), 'Limba conținutului audio din videoclip': ('Limba conținutului audio din videoclip',), 'Categorie de videoclipuri': ('Categorie de videoclipuri',), 'Descrierea videoclipului (original)': ('Descrierea videoclipului (original)',), 'ID-ul canalului': ('ID-ul canalului',), 'Titlul videoclipului (original)': ('Titlul videoclipului (original)',), 'Confidențialitate': ('Confidențialitate',), 'Starea videoclipului': ('Starea videoclipului',), 'Marcajul temporal de creare a videoclipului': ('Marcajul temporal de creare a videoclipului',), 'Marcajul temporal de publicare a videoclipului': ('Marcajul temporal de publicare a videoclipului',)}, tree=Node(columns={}, children={})),
    ],
    'videos': [
        Entry(table='videos', filename='videos.csv', static_fields={'Video ID': ('Video ID',), 'Approx Duration (ms)': ('Approx Duration (ms)',), 'Video Audio Language': ('Video Audio Language',), 'Video Category': ('Video Category',), 'Video Description (Original)': ('Video Description (Original)',), 'Channel ID': ('Channel ID',), 'Video Title (Original)': ('Video Title (Original)',), 'Privacy': ('Privacy',), 'Video State': ('Video State',), 'Video Create Timestamp': ('Video Create Timestamp',), 'Video Publish Timestamp': ('Video Publish Timestamp',)}, tree=Node(columns={}, children={})),
    ],
    'vídeos': [
        Entry(table='vídeos', filename='vídeos.csv', static_fields={'ID de vídeo': ('ID de vídeo',), 'Duración aproximada (ms)': ('Duración aproximada (ms)',), 'Idioma del audio del vídeo': ('Idioma del audio del vídeo',), 'Categoría del vídeo': ('Categoría del vídeo',), 'Descripción del vídeo (original)': ('Descripción del vídeo (original)',), 'ID de canal': ('ID de canal',), 'Título del vídeo (original)': ('Título del vídeo (original)',), 'Privacidad': ('Privacidad',), 'Estado del vídeo': ('Estado del vídeo',), 'Marca de tiempo de creación del vídeo': ('Marca de tiempo de creación del vídeo',), 'Marca de tiempo de publicación del vídeo': ('Marca de tiempo de publicación del vídeo',)}, tree=Node(columns={}, children={})),
    ],
}
