"""
Donation file structure data for takeout flows

This file contains a list of Entries for each platform.
Each Entry represents a table to be generated from the appropriate file.

To generate this file, please run structure/flow_generation/generate_entries.py
which will use the Merged_structures_*.csv to determine the required entries.
"""

from port.helpers.parsers import Entry

TIKTOK_ENTRIES: dict[str, list[Entry]] = {
    'Activity (Unchanged)': [
        Entry(table='Activity', filename=None, static_fields={'videosCommentedOnSinceAccountRegistration': ('Activity', 'Activity Summary', 'ActivitySummaryMap', 'videosCommentedOnSinceAccountRegistration'), 'videosSharedSinceAccountRegistration': ('Activity', 'Activity Summary', 'ActivitySummaryMap', 'videosSharedSinceAccountRegistration'), 'videosWatchedToTheEndSinceAccountRegistration': ('Activity', 'Activity Summary', 'ActivitySummaryMap', 'videosWatchedToTheEndSinceAccountRegistration')}, list_blocks={('Activity', 'Favorite Videos', 'FavoriteVideoList'): {'Date': ('Date',), 'Link': ('Link',)}, ('Activity', 'Following List', 'Following'): {'Date': ('Date',), 'UserName': ('UserName',)}, ('Activity', 'Hashtag', 'HashtagList'): {'HashtagName': ('HashtagName',), 'HashtagLink': ('HashtagLink',)}, ('Activity', 'Like List', 'ItemFavoriteList'): {'date': ('date',), 'link': ('link',)}, ('Activity', 'Search History', 'SearchList'): {'Date': ('Date',), 'SearchTerm': ('SearchTerm',)}, ('Activity', 'Share History', 'ShareHistoryList'): {'Date': ('Date',), 'Link': ('Link',)}, ('Activity', 'Video Browsing History', 'VideoList'): {'Date': ('Date',), 'Link': ('Link',)}, ('Activity', 'Follower List', 'FansList'): {'Date': ('Date',), 'UserName': ('UserName',)}}),
    ],
    'Ads And Data (Unchanged)': [
        Entry(table='Ads And Data', filename=None, static_fields={'AdInterestCategories': ('Ads and data', 'Ad Interests', 'AdInterestCategories'), 'ResponsesList': ('Ads and data', 'Instant Form Ads Responses', 'ResponsesList')}, list_blocks={}),
    ],
    'App Settings (Unchanged)': [
        Entry(table='App Settings', filename=None, static_fields={'App Language': ('App Settings', 'Settings', 'SettingsMap', 'App Language'), 'Filter Comments': ('App Settings', 'Settings', 'SettingsMap', 'Filter Comments'), 'Interests': ('App Settings', 'Settings', 'SettingsMap', 'Interests'), 'Private Account': ('App Settings', 'Settings', 'SettingsMap', 'Private Account'), 'Web Language': ('App Settings', 'Settings', 'SettingsMap', 'Web Language'), 'Who Can Duet With Me': ('App Settings', 'Settings', 'SettingsMap', 'Who Can Duet With Me'), 'Who Can Post Comments': ('App Settings', 'Settings', 'SettingsMap', 'Who Can Post Comments'), 'Who Can Send Me Message': ('App Settings', 'Settings', 'SettingsMap', 'Who Can Send Me Message'), 'Who Can Stitch with your videos': ('App Settings', 'Settings', 'SettingsMap', 'Who Can Stitch with your videos'), 'Who Can View Videos I Liked': ('App Settings', 'Settings', 'SettingsMap', 'Who Can View Videos I Liked'), 'BlockList': ('App Settings', 'Block List', 'BlockList'), 'Keyword filters for videos in Following feed': ('App Settings', 'Settings', 'SettingsMap', 'Content Preferences', 'Keyword filters for videos in Following feed'), 'Keyword filters for videos in For You feed': ('App Settings', 'Settings', 'SettingsMap', 'Content Preferences', 'Keyword filters for videos in For You feed'), 'Video Languages Preferences': ('App Settings', 'Settings', 'SettingsMap', 'Content Preferences', 'Video Languages Preferences'), 'Personalized Ads': ('App Settings', 'Settings', 'SettingsMap', 'Personalized Ads')}, list_blocks={('App Settings', 'Block', 'BlockList'): {'Date': ('Date',), 'UserName': ('UserName',)}}),
    ],
    'Comment (Unchanged)': [
        Entry(table='Comment', filename=None, static_fields={'CommentsList': ('Comment', 'Comments', 'CommentsList')}, list_blocks={('Comment', 'Comments', 'CommentsList'): {'date': ('date',), 'comment': ('comment',), 'photo': ('photo',), 'url': ('url',)}}),
    ],
    'Post (Unchanged)': [
        Entry(table='Post', filename=None, static_fields={'VideoList': ('Post', 'Posts', 'VideoList')}, list_blocks={('Post', 'Posts', 'VideoList'): {'Date': ('Date',), 'Link': ('Link',), 'Likes': ('Likes',), 'WhoCanView': ('WhoCanView',), 'AllowComments': ('AllowComments',), 'AllowStitches': ('AllowStitches',), 'AllowDuets': ('AllowDuets',), 'AllowStickers': ('AllowStickers',), 'AllowSharingToStory': ('AllowSharingToStory',), 'ContentDisclosure': ('ContentDisclosure',), 'AIGeneratedContent': ('AIGeneratedContent',), 'Sound': ('Sound',), 'Location': ('Location',), 'Title': ('Title',), 'AddYoursText': ('AddYoursText',)}}),
    ],
    'Profile (Unchanged)': [
        Entry(table='Profile', filename=None, static_fields={'likesReceived': ('Profile', 'Profile Info', 'ProfileMap', 'likesReceived'), 'userName': ('Profile', 'Profile Info', 'ProfileMap', 'userName')}, list_blocks={}),
    ],
    'Tiktok Live (Unchanged)': [
        Entry(table='Tiktok Live', filename=None, static_fields={'Allow agencies to find and invite you': ('Tiktok Live', 'Go Live Settings', 'SettingsMap', 'Allow agencies to find and invite you'), 'Allow others to invite you to co-host in LIVE': ('Tiktok Live', 'Go Live Settings', 'SettingsMap', 'Allow others to invite you to co-host in LIVE'), 'Allow people to send and receive comments during your LIVE': ('Tiktok Live', 'Go Live Settings', 'SettingsMap', 'Allow people to send and receive comments during your LIVE'), 'Allow suggested LIVE hosts to invite you to co-host in LIVE': ('Tiktok Live', 'Go Live Settings', 'SettingsMap', 'Allow suggested LIVE hosts to invite you to co-host in LIVE'), 'Allow viewers to request to go LIVE with you': ('Tiktok Live', 'Go Live Settings', 'SettingsMap', 'Allow viewers to request to go LIVE with you'), 'Allow viewers to see and send questions and answers in your LIVE': ('Tiktok Live', 'Go Live Settings', 'SettingsMap', 'Allow viewers to see and send questions and answers in your LIVE'), 'Allow viewers to send you gifts during your LIVE': ('Tiktok Live', 'Go Live Settings', 'SettingsMap', 'Allow viewers to send you gifts during your LIVE'), 'Hide potential spam or offensive comments from your LIVE': ('Tiktok Live', 'Go Live Settings', 'SettingsMap', 'Hide potential spam or offensive comments from your LIVE'), 'Show your username and gift information in features with ranking lists': ('Tiktok Live', 'Go Live Settings', 'SettingsMap', 'Show your username and gift information in features with ranking lists'), 'GoLiveList': ('Tiktok Live', 'Go Live History', 'GoLiveList'), 'Hide comments that contain the following keywords from your LIVE': ('Tiktok Live', 'Go Live Settings', 'SettingsMap', 'Hide comments that contain the following keywords from your LIVE'), 'People you assigned to moderate your LIVE': ('Tiktok Live', 'Go Live Settings', 'SettingsMap', 'People you assigned to moderate your LIVE')}, list_blocks={('Tiktok Live', 'Go Live Settings', 'SettingsMap', 'Hide comments that contain the following keywords from your LIVE'): {'Hide comments that contain the following keywords from your LIVE': ()}, ('Tiktok Live', 'Go Live Settings', 'SettingsMap', 'People you assigned to moderate your LIVE'): {'People you assigned to moderate your LIVE': ()}}),
    ],
    'Video (Unchanged)': [
        Entry(table='Video', filename=None, static_fields={}, list_blocks={('Video', 'Videos', 'VideoList'): {'Date': ('Date',), 'Link': ('Link',), 'Likes': ('Likes',), 'WhoCanView': ('WhoCanView',), 'AllowComments': ('AllowComments',), 'AllowStitches': ('AllowStitches',), 'AllowDuets': ('AllowDuets',), 'AllowStickers': ('AllowStickers',), 'AllowSharingToStory': ('AllowSharingToStory',), 'ContentDisclosure': ('ContentDisclosure',), 'AIGeneratedContent': ('AIGeneratedContent',), 'Sound': ('Sound',), 'Location': ('Location',), 'Title': ('Title',), 'AddYoursText': ('AddYoursText',)}}),
    ],
    'Your Activity (Unchanged)': [
        Entry(table='Your Activity', filename=None, static_fields={'FavoriteEffectsList': ('Your Activity', 'Favorite Effects', 'FavoriteEffectsList'), 'FavoriteHashtagList': ('Your Activity', 'Favorite Hashtags', 'FavoriteHashtagList'), 'FavoriteSoundList': ('Your Activity', 'Favorite Sounds', 'FavoriteSoundList'), 'FavoriteVideoList': ('Your Activity', 'Favorite Videos', 'FavoriteVideoList'), 'FansList': ('Your Activity', 'Follower', 'FansList'), 'Following': ('Your Activity', 'Following', 'Following'), 'HashtagList': ('Your Activity', 'Hashtag', 'HashtagList'), 'ItemFavoriteList': ('Your Activity', 'Like List', 'ItemFavoriteList'), 'ShareHistoryList': ('Your Activity', 'Share History', 'ShareHistoryList'), 'videosCommentedOnSinceAccountRegistration': ('Your Activity', 'Activity Summary', 'ActivitySummaryMap', 'videosCommentedOnSinceAccountRegistration'), 'videosSharedSinceAccountRegistration': ('Your Activity', 'Activity Summary', 'ActivitySummaryMap', 'videosSharedSinceAccountRegistration'), 'videosWatchedToTheEndSinceAccountRegistration': ('Your Activity', 'Activity Summary', 'ActivitySummaryMap', 'videosWatchedToTheEndSinceAccountRegistration')}, list_blocks={('Your Activity', 'Searches', 'SearchList'): {'Date': ('Date',), 'SearchTerm': ('SearchTerm',)}, ('Your Activity', 'Watch History', 'VideoList'): {'Date': ('Date',), 'Link': ('Link',)}, ('Your Activity', 'Favorite Effects', 'FavoriteEffectsList'): {'Date': ('Date',), 'EffectLink': ('EffectLink',)}, ('Your Activity', 'Favorite Sounds', 'FavoriteSoundList'): {'Date': ('Date',), 'Link': ('Link',)}, ('Your Activity', 'Favorite Videos', 'FavoriteVideoList'): {'Date': ('Date',), 'Link': ('Link',)}, ('Your Activity', 'Follower', 'FansList'): {'Date': ('Date',), 'UserName': ('UserName',)}, ('Your Activity', 'Following', 'Following'): {'Date': ('Date',), 'UserName': ('UserName',)}, ('Your Activity', 'Hashtag', 'HashtagList'): {'HashtagName': ('HashtagName',), 'HashtagLink': ('HashtagLink',)}, ('Your Activity', 'Like List', 'ItemFavoriteList'): {'date': ('date',), 'link': ('link',)}}),
    ],
}

X_ENTRIES: dict[str, list[Entry]] = {
    'Account (Unchanged)': [
        Entry(table='Account', filename='data/account.js', static_fields={'accountId': ('account', 'accountId'), 'createdAt': ('account', 'createdAt')}, list_blocks={}),
    ],
    'Account-Label (Unchanged)': [
        Entry(table='Account-Label', filename='data/account-label.js', static_fields={'accountLabel': ('accountLabel',)}, list_blocks={}),
    ],
    'Account-Suspension (Unchanged)': [
        Entry(table='Account-Suspension', filename='data/account-suspension.js', static_fields={'No data': ('No data',)}, list_blocks={}),
    ],
    'Ad-Engagements (Unchanged)': [
        Entry(table='Ad-Engagements', filename='data/ad-engagements.js', static_fields={'displayLocation': ('ad', 'adsUserData', 'adEngagements', 'engagements', 'impressionAttributes', 'displayLocation'), 'tweetId': ('ad', 'adsUserData', 'adEngagements', 'engagements', 'impressionAttributes', 'promotedTweetInfo', 'tweetId'), 'tweetText': ('ad', 'adsUserData', 'adEngagements', 'engagements', 'impressionAttributes', 'promotedTweetInfo', 'tweetText'), 'advertiserName': ('ad', 'adsUserData', 'adEngagements', 'engagements', 'impressionAttributes', 'advertiserInfo', 'advertiserName'), 'screenName': ('ad', 'adsUserData', 'adEngagements', 'engagements', 'impressionAttributes', 'publisherInfo', 'screenName'), 'targetingType': ('ad', 'adsUserData', 'adEngagements', 'engagements', 'impressionAttributes', 'matchedTargetingCriteria', 'targetingType'), 'targetingValue': ('ad', 'adsUserData', 'adEngagements', 'engagements', 'impressionAttributes', 'matchedTargetingCriteria', 'targetingValue'), 'impressionTime': ('ad', 'adsUserData', 'adEngagements', 'engagements', 'impressionAttributes', 'impressionTime'), 'engagementTime': ('ad', 'adsUserData', 'adEngagements', 'engagements', 'engagementAttributes', 'engagementTime'), 'engagementType': ('ad', 'adsUserData', 'adEngagements', 'engagements', 'engagementAttributes', 'engagementType'), 'trendId': ('ad', 'adsUserData', 'adEngagements', 'engagements', 'impressionAttributes', 'promotedTrendInfo', 'trendId'), 'name': ('ad', 'adsUserData', 'adEngagements', 'engagements', 'impressionAttributes', 'promotedTrendInfo', 'name'), 'description': ('ad', 'adsUserData', 'adEngagements', 'engagements', 'impressionAttributes', 'promotedTrendInfo', 'description'), 'publisherName': ('ad', 'adsUserData', 'adEngagements', 'engagements', 'impressionAttributes', 'publisherInfo', 'publisherName')}, list_blocks={('ad', 'adsUserData', 'adEngagements', 'engagements', 'impressionAttributes', 'promotedTweetInfo'): {'mediaUrls': ('mediaUrls',), 'urls': ('urls',)}}),
    ],
    'Ad-Impressions (Unchanged)': [
        Entry(table='Ad-Impressions', filename='data/ad-impressions.js', static_fields={'No data': ('No data',)}, list_blocks={}),
    ],
    'Ad-Mobile-Conversions-Attributed (Unchanged)': [
        Entry(table='Ad-Mobile-Conversions-Attributed', filename='data/ad-mobile-conversions-attributed.js', static_fields={'No data': ('No data',)}, list_blocks={}),
    ],
    'Ad-Mobile-Conversions-Unattributed (Unchanged)': [
        Entry(table='Ad-Mobile-Conversions-Unattributed', filename='data/ad-mobile-conversions-unattributed.js', static_fields={'No data': ('No data',)}, list_blocks={}),
    ],
    'Ad-Online-Conversions-Attributed (Unchanged)': [
        Entry(table='Ad-Online-Conversions-Attributed', filename='data/ad-online-conversions-attributed.js', static_fields={'No data': ('No data',)}, list_blocks={}),
    ],
    'Ad-Online-Conversions-Unattributed (Unchanged)': [
        Entry(table='Ad-Online-Conversions-Unattributed', filename='data/ad-online-conversions-unattributed.js', static_fields={'No data': ('No data',)}, list_blocks={}),
    ],
    'Article (Unchanged)': [
        Entry(table='Article', filename='data/article.js', static_fields={'No data': ('No data',)}, list_blocks={}),
    ],
    'Article-Metadata (Unchanged)': [
        Entry(table='Article-Metadata', filename='data/article-metadata.js', static_fields={'No data': ('No data',)}, list_blocks={}),
    ],
    'Block (Unchanged)': [
        Entry(table='Block', filename='data/block.js', static_fields={'No data': ('No data',)}, list_blocks={}),
    ],
    'Community-Note (Unchanged)': [
        Entry(table='Community-Note', filename='data/community-note.js', static_fields={'No data': ('No data',)}, list_blocks={}),
    ],
    'Community-Note-Batsignal (Unchanged)': [
        Entry(table='Community-Note-Batsignal', filename='data/community-note-batsignal.js', static_fields={'No data': ('No data',)}, list_blocks={}),
    ],
    'Community-Note-Rating (Unchanged)': [
        Entry(table='Community-Note-Rating', filename='data/community-note-rating.js', static_fields={'noteId': ('communityNoteRating', 'noteId'), 'helpfulnessLevel': ('communityNoteRating', 'helpfulnessLevel'), 'createdAt': ('communityNoteRating', 'createdAt'), 'userId': ('communityNoteRating', 'userId')}, list_blocks={('communityNoteRating',): {'helpfulTags': ('helpfulTags',)}}),
    ],
    'Community-Note-Tombstone (Unchanged)': [
        Entry(table='Community-Note-Tombstone', filename='data/community-note-tombstone.js', static_fields={'No data': ('No data',)}, list_blocks={}),
    ],
    'Community-Tweet (Unchanged)': [
        Entry(table='Community-Tweet', filename='data/community-tweet.js', static_fields={'No data': ('No data',)}, list_blocks={}),
    ],
    'Follower (Unchanged)': [
        Entry(table='Follower', filename='data/follower.js', static_fields={'accountId': ('follower', 'accountId'), 'userLink': ('follower', 'userLink')}, list_blocks={}),
    ],
    'Following (Unchanged)': [
        Entry(table='Following', filename='data/following.js', static_fields={'accountId': ('following', 'accountId'), 'userLink': ('following', 'userLink')}, list_blocks={}),
    ],
    'Grok-Chat-Item (Unchanged)': [
        Entry(table='Grok-Chat-Item', filename='data/grok-chat-item.js', static_fields={'No data': ('No data',)}, list_blocks={}),
    ],
    'Like (Unchanged)': [
        Entry(table='Like', filename='data/like.js', static_fields={'tweetId': ('like', 'tweetId'), 'fullText': ('like', 'fullText'), 'expandedUrl': ('like', 'expandedUrl')}, list_blocks={}),
    ],
    'Lists-Created (Unchanged)': [
        Entry(table='Lists-Created', filename='data/lists-created.js', static_fields={'No data': ('No data',), 'url': ('userListInfo', 'url')}, list_blocks={}),
    ],
    'Lists-Member (Unchanged)': [
        Entry(table='Lists-Member', filename='data/lists-member.js', static_fields={'No data': ('No data',), 'url': ('userListInfo', 'url')}, list_blocks={}),
    ],
    'Lists-Subscribed (Unchanged)': [
        Entry(table='Lists-Subscribed', filename='data/lists-subscribed.js', static_fields={'No data': ('No data',), 'url': ('userListInfo', 'url')}, list_blocks={}),
    ],
    'Manifest (Unchanged)': [
        Entry(table='Manifest', filename='data/manifest.js', static_fields={'generationDate': ('archiveInfo', 'generationDate')}, list_blocks={}),
    ],
    'Moment (Unchanged)': [
        Entry(table='Moment', filename='data/moment.js', static_fields={'No data': ('No data',)}, list_blocks={}),
    ],
    'Mute (Unchanged)': [
        Entry(table='Mute', filename='data/mute.js', static_fields={'No data': ('No data',)}, list_blocks={}),
    ],
    'Note-Tweet (Unchanged)': [
        Entry(table='Note-Tweet', filename='data/note-tweet.js', static_fields={'No data': ('No data',)}, list_blocks={}),
    ],
    'Personalization (Original)': [
        Entry(table='Personalization', filename='data/personalization.js', static_fields={'language': ('p13nData', 'demographics', 'languages', 'language'), 'isDisabled': ('p13nData', 'interests', 'interests', 'isDisabled'), 'gender': ('p13nData', 'demographics', 'genderInfo', 'gender'), 'name': ('p13nData', 'interests', 'interests', 'name'), 'numAudiences': ('p13nData', 'interests', 'audienceAndAdvertisers', 'numAudiences'), 'birthDate': ('p13nData', 'inferredAgeInfo', 'birthDate')}, list_blocks={('p13nData', 'interests', 'audienceAndAdvertisers'): {'lookalikeAdvertisers': ('lookalikeAdvertisers',), 'advertisers': ('advertisers',)}, ('p13nData', 'interests'): {'shows': ('shows',)}, ('p13nData', 'inferredAgeInfo'): {'age': ('age',)}}),
    ],
    'Personalization (Merged)': [
        Entry(table='Personalization', filename='data/personalization.js', static_fields={'language': ('p13nData', 'demographics', 'languages', 'language'), 'isDisabled': ('p13nData', 'interests', 'interests', 'isDisabled'), 'gender': ('p13nData', 'demographics', 'genderInfo', 'gender'), 'name': ('p13nData', 'interests', 'interests', 'name'), 'numAudiences': ('p13nData', 'interests', 'audienceAndAdvertisers', 'numAudiences'), 'birthDate': ('p13nData', 'inferredAgeInfo', 'birthDate')}, list_blocks={('p13nData', 'interests'): {'shows': ('shows',), 'lookalikeAdvertisers': ('audienceAndAdvertisers', 'lookalikeAdvertisers'), 'advertisers': ('audienceAndAdvertisers', 'advertisers')}, ('p13nData', 'inferredAgeInfo'): {'age': ('age',)}}),
    ],
    'Professional-Data (Unchanged)': [
        Entry(table='Professional-Data', filename='data/professional-data.js', static_fields={'No data': ('No data',)}, list_blocks={}),
    ],
    'Protected-History (Unchanged)': [
        Entry(table='Protected-History', filename='data/protected-history.js', static_fields={'No data': ('No data',)}, list_blocks={}),
    ],
    'Reply-Prompt (Unchanged)': [
        Entry(table='Reply-Prompt', filename='data/reply-prompt.js', static_fields={'No data': ('No data',)}, list_blocks={}),
    ],
    'Saved-Search (Unchanged)': [
        Entry(table='Saved-Search', filename='data/saved-search.js', static_fields={'savedSearchId': ('savedSearch', 'savedSearchId'), 'query': ('savedSearch', 'query')}, list_blocks={}),
    ],
    'Smartblock (Unchanged)': [
        Entry(table='Smartblock', filename='data/smartblock.js', static_fields={'No data': ('No data',)}, list_blocks={}),
    ],
    'Spaces-Metadata (Unchanged)': [
        Entry(table='Spaces-Metadata', filename='data/spaces-metadata.js', static_fields={'No data': ('No data',)}, list_blocks={}),
    ],
    'Tweet-Headers (Unchanged)': [
        Entry(table='Tweet-Headers', filename='data/tweet-headers.js', static_fields={'user_id': ('tweet', 'user_id')}, list_blocks={}),
    ],
    'Tweetdeck (Unchanged)': [
        Entry(table='Tweetdeck', filename='data/tweetdeck.js', static_fields={'No data': ('No data',)}, list_blocks={}),
    ],
    'Tweets (Original)': [
        Entry(table='Tweets', filename='data/tweets.js', static_fields={'editableUntil': ('tweet', 'edit_info', 'initial', 'editableUntil'), 'editsRemaining': ('tweet', 'edit_info', 'initial', 'editsRemaining'), 'isEditEligible': ('tweet', 'edit_info', 'initial', 'isEditEligible'), 'retweeted': ('tweet', 'retweeted'), 'source': ('tweet', 'source'), 'url': ('tweet', 'entities', 'urls', 'url'), 'expanded_url': ('tweet', 'entities', 'urls', 'expanded_url'), 'display_url': ('tweet', 'entities', 'urls', 'display_url'), 'favorite_count': ('tweet', 'favorite_count'), 'id_str': ('tweet', 'entities', 'user_mentions', 'id_str'), 'truncated': ('tweet', 'truncated'), 'retweet_count': ('tweet', 'retweet_count'), 'id': ('tweet', 'entities', 'user_mentions', 'id'), 'possibly_sensitive': ('tweet', 'possibly_sensitive'), 'created_at': ('tweet', 'created_at'), 'favorited': ('tweet', 'favorited'), 'full_text': ('tweet', 'full_text'), 'lang': ('tweet', 'lang'), 'name': ('tweet', 'entities', 'user_mentions', 'name'), 'screen_name': ('tweet', 'entities', 'user_mentions', 'screen_name'), 'in_reply_to_status_id_str': ('tweet', 'in_reply_to_status_id_str'), 'in_reply_to_user_id': ('tweet', 'in_reply_to_user_id'), 'in_reply_to_status_id': ('tweet', 'in_reply_to_status_id'), 'in_reply_to_screen_name': ('tweet', 'in_reply_to_screen_name'), 'in_reply_to_user_id_str': ('tweet', 'in_reply_to_user_id_str'), 'text': ('tweet', 'entities', 'hashtags', 'text'), 'media_url_https': ('tweet', 'entities', 'media', 'media_url_https'), 'source_status_id_str': ('tweet', 'entities', 'media', 'source_status_id_str')}, list_blocks={('tweet', 'edit_info', 'initial'): {'editTweetIds': ('editTweetIds',)}, ('tweet', 'entities', 'urls'): {'indices': ('indices',)}, ('tweet',): {'display_text_range': ('display_text_range',)}, ('tweet', 'entities', 'user_mentions'): {'indices': ('indices',)}, ('tweet', 'entities', 'hashtags'): {'indices': ('indices',)}}),
    ],
    'Tweets (Merged)': [
        Entry(table='Tweets', filename='data/tweets.js', static_fields={'editableUntil': ('tweet', 'edit_info', 'initial', 'editableUntil'), 'editsRemaining': ('tweet', 'edit_info', 'initial', 'editsRemaining'), 'isEditEligible': ('tweet', 'edit_info', 'initial', 'isEditEligible'), 'retweeted': ('tweet', 'retweeted'), 'source': ('tweet', 'source'), 'url': ('tweet', 'entities', 'urls', 'url'), 'expanded_url': ('tweet', 'entities', 'urls', 'expanded_url'), 'display_url': ('tweet', 'entities', 'urls', 'display_url'), 'favorite_count': ('tweet', 'favorite_count'), 'id_str': ('tweet', 'entities', 'user_mentions', 'id_str'), 'truncated': ('tweet', 'truncated'), 'retweet_count': ('tweet', 'retweet_count'), 'id': ('tweet', 'entities', 'user_mentions', 'id'), 'possibly_sensitive': ('tweet', 'possibly_sensitive'), 'created_at': ('tweet', 'created_at'), 'favorited': ('tweet', 'favorited'), 'full_text': ('tweet', 'full_text'), 'lang': ('tweet', 'lang'), 'name': ('tweet', 'entities', 'user_mentions', 'name'), 'screen_name': ('tweet', 'entities', 'user_mentions', 'screen_name'), 'in_reply_to_status_id_str': ('tweet', 'in_reply_to_status_id_str'), 'in_reply_to_user_id': ('tweet', 'in_reply_to_user_id'), 'in_reply_to_status_id': ('tweet', 'in_reply_to_status_id'), 'in_reply_to_screen_name': ('tweet', 'in_reply_to_screen_name'), 'in_reply_to_user_id_str': ('tweet', 'in_reply_to_user_id_str'), 'text': ('tweet', 'entities', 'hashtags', 'text'), 'media_url_https': ('tweet', 'entities', 'media', 'media_url_https'), 'source_status_id_str': ('tweet', 'entities', 'media', 'source_status_id_str')}, list_blocks={('tweet',): {'display_text_range': ('display_text_range',), 'editTweetIds': ('edit_info', 'initial', 'editTweetIds'), 'indices': ('entities', 'urls', 'indices'), 'entities.user_mentions.indices': ('entities', 'user_mentions', 'indices'), 'entities.hashtags.indices': ('entities', 'hashtags', 'indices')}}),
    ],
    'User-Link-Clicks (Unchanged)': [
        Entry(table='User-Link-Clicks', filename='data/user-link-clicks.js', static_fields={'No data': ('No data',)}, list_blocks={}),
    ],
    'Verified (Unchanged)': [
        Entry(table='Verified', filename='data/verified.js', static_fields={'verified': ('verified', 'verified')}, list_blocks={}),
    ],
    'Verified-Organization (Unchanged)': [
        Entry(table='Verified-Organization', filename='data/verified-organization.js', static_fields={'verifiedOrganization': ('verifiedOrganization',)}, list_blocks={}),
    ],
}

IG_ENTRIES: dict[str, list[Entry]] = {
    'Ads About Meta (Unchanged)': [
        Entry(table='Ads About Meta', filename='ads_information/instagram_ads_and_businesses/ads_about_meta.json', static_fields={'media': ('media',), 'fbid': ('fbid',), 'ent_name': ('ent_name',)}, list_blocks={('label_values',): {'ent_field_name': ('ent_field_name',), 'label': ('label',), 'value': ('value',), 'timestamp_value': ('timestamp_value',)}}),
    ],
    'Ads Clicked (Original)': [
        Entry(table='Ads Clicked', filename='ads_information/ads_and_topics/ads_clicked.json', static_fields={}, list_blocks={('impressions_history_ads_clicked',): {'title': ('title',)}, ('impressions_history_ads_clicked', 'string_list_data'): {'timestamp': ('timestamp',)}}),
    ],
    'Ads Clicked (Merged)': [
        Entry(table='Ads Clicked', filename='ads_information/ads_and_topics/ads_clicked.json', static_fields={}, list_blocks={('impressions_history_ads_clicked',): {'title': ('title',), 'timestamp': ('string_list_data', 'timestamp')}}),
    ],
    'Ads Viewed (Unchanged)': [
        Entry(table='Ads Viewed', filename='ads_information/ads_and_topics/ads_viewed.json', static_fields={}, list_blocks={('impressions_history_ads_seen',): {'value': ('string_map_data', 'Author', 'value'), 'timestamp': ('string_map_data', 'Time', 'timestamp')}}),
    ],
    'Advertisers Using Your Activity Or Information (Unchanged)': [
        Entry(table='Advertisers Using Your Activity Or Information', filename='ads_information/instagram_ads_and_businesses/advertisers_using_your_activity_or_information.json', static_fields={}, list_blocks={('ig_custom_audiences_all_types',): {'advertiser_name': ('advertiser_name',), 'has_data_file_custom_audience': ('has_data_file_custom_audience',), 'has_remarketing_custom_audience': ('has_remarketing_custom_audience',), 'has_in_person_store_visit': ('has_in_person_store_visit',)}}),
    ],
    'Blocked Profiles (Original)': [
        Entry(table='Blocked Profiles', filename='connections/followers_and_following/blocked_profiles.json', static_fields={}, list_blocks={('relationships_blocked_users',): {'title': ('title',)}, ('relationships_blocked_users', 'string_list_data'): {'href': ('href',), 'timestamp': ('timestamp',)}}),
    ],
    'Blocked Profiles (Merged)': [
        Entry(table='Blocked Profiles', filename='connections/followers_and_following/blocked_profiles.json', static_fields={}, list_blocks={('relationships_blocked_users',): {'title': ('title',), 'href': ('string_list_data', 'href'), 'timestamp': ('string_list_data', 'timestamp')}}),
    ],
    'Close Friends (Original)': [
        Entry(table='Close Friends', filename='connections/followers_and_following/close_friends.json', static_fields={}, list_blocks={('relationships_close_friends',): {'title': ('title',), 'media_list_data': ('media_list_data',)}, ('relationships_close_friends', 'string_list_data'): {'href': ('href',), 'value': ('value',), 'timestamp': ('timestamp',)}}),
    ],
    'Close Friends (Merged)': [
        Entry(table='Close Friends', filename='connections/followers_and_following/close_friends.json', static_fields={}, list_blocks={('relationships_close_friends',): {'title': ('title',), 'media_list_data': ('media_list_data',), 'href': ('string_list_data', 'href'), 'value': ('string_list_data', 'value'), 'timestamp': ('string_list_data', 'timestamp')}}),
    ],
    'Comments Allowed From (Unchanged)': [
        Entry(table='Comments Allowed From', filename='preferences/media_settings/comments_allowed_from.json', static_fields={}, list_blocks={('settings_allow_comments_from',): {'title': ('title',), 'href': ('string_map_data', 'Comments Allowed From', 'href'), 'value': ('string_map_data', 'Comments Allowed From', 'value'), 'timestamp': ('string_map_data', 'Comments Allowed From', 'timestamp')}}),
        Entry(table='Comments Allowed From', filename='preferences/settings/comments_allowed_from.json', static_fields={}, list_blocks={('settings_allow_comments_from',): {'title': ('title',), 'href': ('string_map_data', 'Comments Allowed From', 'href'), 'value': ('string_map_data', 'Comments Allowed From', 'value'), 'timestamp': ('string_map_data', 'Comments Allowed From', 'timestamp')}}),
    ],
    'Consents (Unchanged)': [
        Entry(table='Consents', filename='preferences/media_settings/consents.json', static_fields={'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',), 'ent_name': ('ent_name',)}, list_blocks={('label_values',): {'ent_field_name': ('ent_field_name',), 'label': ('label',), 'timestamp_value': ('timestamp_value',)}}),
        Entry(table='Consents', filename='preferences/settings/consents.json', static_fields={'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',), 'ent_name': ('ent_name',)}, list_blocks={('label_values',): {'ent_field_name': ('ent_field_name',), 'label': ('label',), 'timestamp_value': ('timestamp_value',)}}),
    ],
    'Emoji Sliders (Original)': [
        Entry(table='Emoji Sliders', filename='your_instagram_activity/story_sticker_interactions/emoji_sliders.json', static_fields={}, list_blocks={('story_activities_emoji_sliders',): {'title': ('title',)}, ('story_activities_emoji_sliders', 'string_list_data'): {'value': ('value',), 'timestamp': ('timestamp',)}}),
    ],
    'Emoji Sliders (Merged)': [
        Entry(table='Emoji Sliders', filename='your_instagram_activity/story_sticker_interactions/emoji_sliders.json', static_fields={}, list_blocks={('story_activities_emoji_sliders',): {'title': ('title',), 'value': ('string_list_data', 'value'), 'timestamp': ('string_list_data', 'timestamp')}}),
    ],
    "Follow Requests You'Ve Received (Original)": [
        Entry(table="Follow Requests You'Ve Received", filename="connections/followers_and_following/follow_requests_you've_received.json", static_fields={}, list_blocks={('relationships_follow_requests_received',): {'title': ('title',), 'media_list_data': ('media_list_data',)}, ('relationships_follow_requests_received', 'string_list_data'): {'href': ('href',), 'value': ('value',), 'timestamp': ('timestamp',)}}),
    ],
    "Follow Requests You'Ve Received (Merged)": [
        Entry(table="Follow Requests You'Ve Received", filename="connections/followers_and_following/follow_requests_you've_received.json", static_fields={}, list_blocks={('relationships_follow_requests_received',): {'title': ('title',), 'media_list_data': ('media_list_data',), 'href': ('string_list_data', 'href'), 'value': ('string_list_data', 'value'), 'timestamp': ('string_list_data', 'timestamp')}}),
    ],
    'Followers 1 (Unchanged)': [
        Entry(table='Followers 1', filename='connections/followers_and_following/followers_1.json', static_fields={'title': ('title',), 'media_list_data': ('media_list_data',)}, list_blocks={('string_list_data',): {'href': ('href',), 'value': ('value',), 'timestamp': ('timestamp',)}, (): {'title': ('title',), 'media_list_data': ('media_list_data',)}}),
    ],
    'Following (Original)': [
        Entry(table='Following', filename='connections/followers_and_following/following.json', static_fields={}, list_blocks={('relationships_following',): {'title': ('title',), 'media_list_data': ('media_list_data',)}, ('relationships_following', 'string_list_data'): {'href': ('href',), 'value': ('value',), 'timestamp': ('timestamp',)}}),
    ],
    'Following (Merged)': [
        Entry(table='Following', filename='connections/followers_and_following/following.json', static_fields={}, list_blocks={('relationships_following',): {'title': ('title',), 'media_list_data': ('media_list_data',), 'href': ('string_list_data', 'href'), 'value': ('string_list_data', 'value'), 'timestamp': ('string_list_data', 'timestamp')}}),
    ],
    'Following Hashtags (Original)': [
        Entry(table='Following Hashtags', filename='connections/followers_and_following/following_hashtags.json', static_fields={}, list_blocks={('relationships_following_hashtags',): {'title': ('title',), 'media_list_data': ('media_list_data',)}, ('relationships_following_hashtags', 'string_list_data'): {'href': ('href',), 'value': ('value',), 'timestamp': ('timestamp',)}}),
    ],
    'Following Hashtags (Merged)': [
        Entry(table='Following Hashtags', filename='connections/followers_and_following/following_hashtags.json', static_fields={}, list_blocks={('relationships_following_hashtags',): {'title': ('title',), 'media_list_data': ('media_list_data',), 'href': ('string_list_data', 'href'), 'value': ('string_list_data', 'value'), 'timestamp': ('string_list_data', 'timestamp')}}),
    ],
    'Liked Comments (Original)': [
        Entry(table='Liked Comments', filename='your_instagram_activity/likes/liked_comments.json', static_fields={}, list_blocks={('likes_comment_likes',): {'title': ('title',)}, ('likes_comment_likes', 'string_list_data'): {'href': ('href',), 'value': ('value',), 'timestamp': ('timestamp',)}}),
    ],
    'Liked Comments (Merged)': [
        Entry(table='Liked Comments', filename='your_instagram_activity/likes/liked_comments.json', static_fields={}, list_blocks={('likes_comment_likes',): {'title': ('title',), 'href': ('string_list_data', 'href'), 'value': ('string_list_data', 'value'), 'timestamp': ('string_list_data', 'timestamp')}}),
    ],
    'Liked Posts (Original)': [
        Entry(table='Liked Posts', filename='your_instagram_activity/likes/liked_posts.json', static_fields={}, list_blocks={('likes_media_likes',): {'title': ('title',)}, ('likes_media_likes', 'string_list_data'): {'href': ('href',), 'value': ('value',), 'timestamp': ('timestamp',)}}),
    ],
    'Liked Posts (Merged)': [
        Entry(table='Liked Posts', filename='your_instagram_activity/likes/liked_posts.json', static_fields={}, list_blocks={('likes_media_likes',): {'title': ('title',), 'href': ('string_list_data', 'href'), 'value': ('string_list_data', 'value'), 'timestamp': ('string_list_data', 'timestamp')}}),
    ],
    'Other Categories Used To Reach You (Original)': [
        Entry(table='Other Categories Used To Reach You', filename='ads_information/instagram_ads_and_businesses/other_categories_used_to_reach_you.json', static_fields={'media': ('media',), 'fbid': ('fbid',), 'ent_name': ('ent_name',)}, list_blocks={('label_values',): {'ent_field_name': ('ent_field_name',), 'label': ('label',)}, ('label_values', 'vec'): {'value': ('value',)}}),
    ],
    'Other Categories Used To Reach You (Merged)': [
        Entry(table='Other Categories Used To Reach You', filename='ads_information/instagram_ads_and_businesses/other_categories_used_to_reach_you.json', static_fields={'media': ('media',), 'fbid': ('fbid',), 'ent_name': ('ent_name',)}, list_blocks={('label_values',): {'ent_field_name': ('ent_field_name',), 'label': ('label',), 'value': ('vec', 'value')}}),
    ],
    'Personal Information (Unchanged)': [
        Entry(table='Personal Information', filename='personal_information/personal_information/personal_information.json', static_fields={}, list_blocks={('profile_user',): {'href': ('string_map_data', 'Private Account', 'href'), 'value': ('string_map_data', 'Private Account', 'value'), 'timestamp': ('string_map_data', 'Private Account', 'timestamp')}}),
    ],
    'Polls (Original)': [
        Entry(table='Polls', filename='your_instagram_activity/story_interactions/polls.json', static_fields={}, list_blocks={('story_activities_polls',): {'title': ('title',)}, ('story_activities_polls', 'string_list_data'): {'value': ('value',), 'timestamp': ('timestamp',)}}),
        Entry(table='Polls', filename='your_instagram_activity/story_sticker_interactions/polls.json', static_fields={}, list_blocks={('story_activities_polls',): {'title': ('title',)}, ('story_activities_polls', 'string_list_data'): {'value': ('value',), 'timestamp': ('timestamp',)}}),
    ],
    'Polls (Merged)': [
        Entry(table='Polls', filename='your_instagram_activity/story_interactions/polls.json', static_fields={}, list_blocks={('story_activities_polls',): {'title': ('title',), 'value': ('string_list_data', 'value'), 'timestamp': ('string_list_data', 'timestamp')}}),
        Entry(table='Polls', filename='your_instagram_activity/story_sticker_interactions/polls.json', static_fields={}, list_blocks={('story_activities_polls',): {'title': ('title',), 'value': ('string_list_data', 'value'), 'timestamp': ('string_list_data', 'timestamp')}}),
    ],
    'Post Comments 1 (Unchanged)': [
        Entry(table='Post Comments 1', filename='your_instagram_activity/comments/post_comments_1.json', static_fields={'value': ('string_map_data', 'Media Owner', 'value'), 'timestamp': ('string_map_data', 'Time', 'timestamp')}, list_blocks={('media_list_data',): {'uri': ('uri',)}, (): {'value': ('string_map_data', 'Media Owner', 'value'), 'timestamp': ('string_map_data', 'Time', 'timestamp')}}),
    ],
    'Posts 1 (Unchanged)': [
        Entry(table='Posts 1', filename='your_instagram_activity/content/posts_1.json', static_fields={'title': ('title',), 'creation_timestamp': ('creation_timestamp',)}, list_blocks={('media',): {'uri': ('uri',), 'creation_timestamp': ('creation_timestamp',), 'title': ('title',), 'source_app': ('cross_post_source', 'source_app'), 'has_camera_metadata': ('media_metadata', 'camera_metadata', 'has_camera_metadata')}}),
        Entry(table='Posts 1', filename='your_instagram_activity/media/posts_1.json', static_fields={}, list_blocks={(): {'title': ('title',), 'creation_timestamp': ('creation_timestamp',)}, ('media',): {'uri': ('uri',), 'creation_timestamp': ('creation_timestamp',), 'title': ('title',), 'source_app': ('cross_post_source', 'source_app')}}),
    ],
    'Posts Viewed (Unchanged)': [
        Entry(table='Posts Viewed', filename='ads_information/ads_and_topics/posts_viewed.json', static_fields={}, list_blocks={('impressions_history_posts_seen',): {'value': ('string_map_data', 'Author', 'value'), 'timestamp': ('string_map_data', 'Time', 'timestamp')}}),
    ],
    "Posts You'Re Not Interested In (Unchanged)": [
        Entry(table="Posts You'Re Not Interested In", filename="ads_information/ads_and_topics/posts_you're_not_interested_in.json", static_fields={}, list_blocks={('impressions_history_posts_not_interested', 'string_list_data'): {'href': ('href',), 'value': ('value',)}}),
    ],
    'Profile Privacy Changes (Unchanged)': [
        Entry(table='Profile Privacy Changes', filename='security_and_login_information/login_and_profile_creation/profile_privacy_changes.json', static_fields={}, list_blocks={('account_history_account_privacy_history',): {'title': ('title',), 'href': ('string_map_data', 'Time', 'href'), 'value': ('string_map_data', 'Time', 'value'), 'timestamp': ('string_map_data', 'Time', 'timestamp')}}),
    ],
    'Profile Searches (Unchanged)': [
        Entry(table='Profile Searches', filename='logged_information/recent_searches/profile_searches.json', static_fields={}, list_blocks={('searches_user',): {'title': ('title',), 'href': ('string_map_data', 'Time', 'href'), 'value': ('string_map_data', 'Time', 'value'), 'timestamp': ('string_map_data', 'Time', 'timestamp')}}),
    ],
    "Profiles You'Re Not Interested In (Unchanged)": [
        Entry(table="Profiles You'Re Not Interested In", filename="ads_information/ads_and_topics/profiles_you're_not_interested_in.json", static_fields={}, list_blocks={('impressions_history_recs_hidden_authors',): {'title': ('title',), 'href': ('string_map_data', 'Time', 'href'), 'value': ('string_map_data', 'Time', 'value'), 'timestamp': ('string_map_data', 'Time', 'timestamp')}}),
    ],
    'Questions (Original)': [
        Entry(table='Questions', filename='your_instagram_activity/story_interactions/questions.json', static_fields={}, list_blocks={('story_activities_questions',): {'title': ('title',), 'media_list_data': ('media_list_data',)}, ('story_activities_questions', 'string_list_data'): {'href': ('href',), 'value': ('value',), 'timestamp': ('timestamp',)}}),
    ],
    'Questions (Merged)': [
        Entry(table='Questions', filename='your_instagram_activity/story_interactions/questions.json', static_fields={}, list_blocks={('story_activities_questions',): {'title': ('title',), 'media_list_data': ('media_list_data',), 'href': ('string_list_data', 'href'), 'value': ('string_list_data', 'value'), 'timestamp': ('string_list_data', 'timestamp')}}),
    ],
    'Quizzes (Original)': [
        Entry(table='Quizzes', filename='your_instagram_activity/story_sticker_interactions/quizzes.json', static_fields={}, list_blocks={('story_activities_quizzes',): {'title': ('title',)}, ('story_activities_quizzes', 'string_list_data'): {'value': ('value',), 'timestamp': ('timestamp',)}}),
    ],
    'Quizzes (Merged)': [
        Entry(table='Quizzes', filename='your_instagram_activity/story_sticker_interactions/quizzes.json', static_fields={}, list_blocks={('story_activities_quizzes',): {'title': ('title',), 'value': ('string_list_data', 'value'), 'timestamp': ('string_list_data', 'timestamp')}}),
    ],
    'Recommended Topics (Unchanged)': [
        Entry(table='Recommended Topics', filename='preferences/your_topics/recommended_topics.json', static_fields={}, list_blocks={('topics_your_topics',): {'title': ('title',), 'href': ('string_map_data', 'Name', 'href'), 'value': ('string_map_data', 'Name', 'value'), 'timestamp': ('string_map_data', 'Name', 'timestamp')}}),
    ],
    'Reels (Original)': [
        Entry(table='Reels', filename='your_instagram_activity/media/reels.json', static_fields={}, list_blocks={('ig_reels_media', 'media'): {'uri': ('uri',), 'creation_timestamp': ('creation_timestamp',), 'title': ('title',), 'dubbing_info': ('dubbing_info',), 'media_variants': ('media_variants',), 'source_app': ('cross_post_source', 'source_app'), 'music_genre': ('media_metadata', 'video_metadata', 'music_genre')}, ('ig_reels_media', 'media', 'media_metadata', 'video_metadata', 'exif_data'): {'source_type': ('source_type',)}}),
    ],
    'Reels (Merged)': [
        Entry(table='Reels', filename='your_instagram_activity/media/reels.json', static_fields={}, list_blocks={('ig_reels_media', 'media'): {'uri': ('uri',), 'creation_timestamp': ('creation_timestamp',), 'title': ('title',), 'dubbing_info': ('dubbing_info',), 'media_variants': ('media_variants',), 'source_app': ('cross_post_source', 'source_app'), 'music_genre': ('media_metadata', 'video_metadata', 'music_genre'), 'source_type': ('media_metadata', 'video_metadata', 'exif_data', 'source_type')}}),
    ],
    'Reels Comments (Unchanged)': [
        Entry(table='Reels Comments', filename='your_instagram_activity/comments/reels_comments.json', static_fields={}, list_blocks={('comments_reels_comments',): {'value': ('string_map_data', 'Media Owner', 'value'), 'timestamp': ('string_map_data', 'Time', 'timestamp')}}),
    ],
    'Removed Suggestions (Original)': [
        Entry(table='Removed Suggestions', filename='connections/followers_and_following/removed_suggestions.json', static_fields={}, list_blocks={('relationships_dismissed_suggested_users',): {'title': ('title',), 'media_list_data': ('media_list_data',)}, ('relationships_dismissed_suggested_users', 'string_list_data'): {'href': ('href',), 'value': ('value',), 'timestamp': ('timestamp',)}}),
    ],
    'Removed Suggestions (Merged)': [
        Entry(table='Removed Suggestions', filename='connections/followers_and_following/removed_suggestions.json', static_fields={}, list_blocks={('relationships_dismissed_suggested_users',): {'title': ('title',), 'media_list_data': ('media_list_data',), 'href': ('string_list_data', 'href'), 'value': ('string_list_data', 'value'), 'timestamp': ('string_list_data', 'timestamp')}}),
    ],
    'Saved Collections (Unchanged)': [
        Entry(table='Saved Collections', filename='your_instagram_activity/saved/saved_collections.json', static_fields={}, list_blocks={('saved_saved_collections',): {'title': ('title',), 'value': ('string_map_data', 'Name', 'value'), 'timestamp': ('string_map_data', 'Added Time', 'timestamp'), 'href': ('string_map_data', 'Name', 'href')}}),
    ],
    'Saved Posts (Unchanged)': [
        Entry(table='Saved Posts', filename='your_instagram_activity/saved/saved_posts.json', static_fields={}, list_blocks={('saved_saved_media',): {'title': ('title',), 'href': ('string_map_data', 'Saved on', 'href'), 'timestamp': ('string_map_data', 'Saved on', 'timestamp')}}),
    ],
    'Signup Details (Unchanged)': [
        Entry(table='Signup Details', filename='security_and_login_information/login_and_profile_creation/signup_details.json', static_fields={}, list_blocks={('account_history_registration_info',): {'timestamp': ('string_map_data', 'Time', 'timestamp')}}),
    ],
    'Stories (Original)': [
        Entry(table='Stories', filename='your_instagram_activity/content/stories.json', static_fields={}, list_blocks={('ig_stories',): {'uri': ('uri',), 'creation_timestamp': ('creation_timestamp',), 'title': ('title',), 'dubbing_info': ('dubbing_info',), 'media_variants': ('media_variants',), 'backup_uri': ('backup_uri',), 'source_app': ('cross_post_source', 'source_app'), 'music_genre': ('media_metadata', 'video_metadata', 'music_genre')}, ('ig_stories', 'media_metadata', 'video_metadata', 'exif_data'): {'date_time_digitized': ('date_time_digitized',), 'date_time_original': ('date_time_original',), 'source_type': ('source_type',)}, ('ig_stories', 'media_metadata', 'photo_metadata', 'exif_data'): {'source_type': ('source_type',), 'date_time_digitized': ('date_time_digitized',), 'date_time_original': ('date_time_original',)}}),
        Entry(table='Stories', filename='your_instagram_activity/media/stories.json', static_fields={}, list_blocks={('ig_stories',): {'uri': ('uri',), 'creation_timestamp': ('creation_timestamp',), 'title': ('title',), 'dubbing_info': ('dubbing_info',), 'media_variants': ('media_variants',), 'source_app': ('cross_post_source', 'source_app')}, ('ig_stories', 'media_metadata', 'video_metadata', 'exif_data'): {'date_time_digitized': ('date_time_digitized',), 'date_time_original': ('date_time_original',), 'source_type': ('source_type',)}}),
    ],
    'Stories (Merged)': [
        Entry(table='Stories', filename='your_instagram_activity/content/stories.json', static_fields={}, list_blocks={('ig_stories',): {'uri': ('uri',), 'creation_timestamp': ('creation_timestamp',), 'title': ('title',), 'dubbing_info': ('dubbing_info',), 'media_variants': ('media_variants',), 'backup_uri': ('backup_uri',), 'source_app': ('cross_post_source', 'source_app'), 'music_genre': ('media_metadata', 'video_metadata', 'music_genre'), 'date_time_digitized': ('media_metadata', 'video_metadata', 'exif_data', 'date_time_digitized'), 'date_time_original': ('media_metadata', 'video_metadata', 'exif_data', 'date_time_original'), 'source_type': ('media_metadata', 'video_metadata', 'exif_data', 'source_type'), 'media_metadata.photo_metadata.exif_data.source_type': ('media_metadata', 'photo_metadata', 'exif_data', 'source_type'), 'media_metadata.photo_metadata.exif_data.date_time_digitized': ('media_metadata', 'photo_metadata', 'exif_data', 'date_time_digitized'), 'media_metadata.photo_metadata.exif_data.date_time_original': ('media_metadata', 'photo_metadata', 'exif_data', 'date_time_original')}}),
        Entry(table='Stories', filename='your_instagram_activity/media/stories.json', static_fields={}, list_blocks={('ig_stories',): {'uri': ('uri',), 'creation_timestamp': ('creation_timestamp',), 'title': ('title',), 'dubbing_info': ('dubbing_info',), 'media_variants': ('media_variants',), 'source_app': ('cross_post_source', 'source_app'), 'date_time_digitized': ('media_metadata', 'video_metadata', 'exif_data', 'date_time_digitized'), 'date_time_original': ('media_metadata', 'video_metadata', 'exif_data', 'date_time_original'), 'source_type': ('media_metadata', 'video_metadata', 'exif_data', 'source_type')}}),
    ],
    'Story Likes (Original)': [
        Entry(table='Story Likes', filename='your_instagram_activity/story_interactions/story_likes.json', static_fields={}, list_blocks={('story_activities_story_likes',): {'title': ('title',)}, ('story_activities_story_likes', 'string_list_data'): {'timestamp': ('timestamp',)}}),
        Entry(table='Story Likes', filename='your_instagram_activity/story_sticker_interactions/story_likes.json', static_fields={}, list_blocks={('story_activities_story_likes',): {'title': ('title',)}, ('story_activities_story_likes', 'string_list_data'): {'timestamp': ('timestamp',)}}),
    ],
    'Story Likes (Merged)': [
        Entry(table='Story Likes', filename='your_instagram_activity/story_interactions/story_likes.json', static_fields={}, list_blocks={('story_activities_story_likes',): {'title': ('title',), 'timestamp': ('string_list_data', 'timestamp')}}),
        Entry(table='Story Likes', filename='your_instagram_activity/story_sticker_interactions/story_likes.json', static_fields={}, list_blocks={('story_activities_story_likes',): {'title': ('title',), 'timestamp': ('string_list_data', 'timestamp')}}),
    ],
    'Subscription For No Ads (Unchanged)': [
        Entry(table='Subscription For No Ads', filename='ads_information/instagram_ads_and_businesses/subscription_for_no_ads.json', static_fields={'media': ('media',), 'fbid': ('fbid',)}, list_blocks={('label_values',): {'label': ('label',), 'value': ('value',)}}),
    ],
    'Suggested Profiles Viewed (Unchanged)': [
        Entry(table='Suggested Profiles Viewed', filename='ads_information/ads_and_topics/suggested_profiles_viewed.json', static_fields={}, list_blocks={('impressions_history_chaining_seen',): {'value': ('string_map_data', 'Username', 'value'), 'timestamp': ('string_map_data', 'Time', 'timestamp')}}),
    ],
    'Time Spent On Instagram (Original)': [
        Entry(table='Time Spent On Instagram', filename='your_instagram_activity/other_activity/time_spent_on_instagram.json', static_fields={}, list_blocks={(): {'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',)}, ('label_values',): {'label': ('label',)}, ('label_values', 'vec', 'dict'): {'label': ('label',), 'timestamp_value': ('timestamp_value',)}}),
    ],
    'Time Spent On Instagram (Merged)': [
        Entry(table='Time Spent On Instagram', filename='your_instagram_activity/other_activity/time_spent_on_instagram.json', static_fields={}, list_blocks={(): {'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',)}, ('label_values',): {'label': ('label',), 'vec.dict.label': ('vec', 'dict', 'label'), 'timestamp_value': ('vec', 'dict', 'timestamp_value')}}),
    ],
    'Videos Watched (Unchanged)': [
        Entry(table='Videos Watched', filename='ads_information/ads_and_topics/videos_watched.json', static_fields={}, list_blocks={('impressions_history_videos_watched',): {'value': ('string_map_data', 'Author', 'value'), 'timestamp': ('string_map_data', 'Time', 'timestamp')}}),
    ],
    'Word Or Phrase Searches (Unchanged)': [
        Entry(table='Word Or Phrase Searches', filename='logged_information/recent_searches/word_or_phrase_searches.json', static_fields={}, list_blocks={('searches_keyword',): {'title': ('title',), 'href': ('string_map_data', 'Time', 'href'), 'value': ('string_map_data', 'Time', 'value'), 'timestamp': ('string_map_data', 'Time', 'timestamp')}}),
    ],
    'Your Activity Off Meta Technologies (Original)': [
        Entry(table='Your Activity Off Meta Technologies', filename='apps_and_websites_off_of_instagram/apps_and_websites/your_activity_off_meta_technologies.json', static_fields={}, list_blocks={('apps_and_websites_off_meta_activity',): {'name': ('name',)}, ('apps_and_websites_off_meta_activity', 'events'): {'id': ('id',), 'type': ('type',), 'timestamp': ('timestamp',)}}),
    ],
    'Your Activity Off Meta Technologies (Merged)': [
        Entry(table='Your Activity Off Meta Technologies', filename='apps_and_websites_off_of_instagram/apps_and_websites/your_activity_off_meta_technologies.json', static_fields={}, list_blocks={('apps_and_websites_off_meta_activity',): {'name': ('name',), 'id': ('events', 'id'), 'type': ('events', 'type'), 'timestamp': ('events', 'timestamp')}}),
    ],
    'Your Information Download Requests (Unchanged)': [
        Entry(table='Your Information Download Requests', filename='your_instagram_activity/other_activity/your_information_download_requests.json', static_fields={'timestamp': ('timestamp',)}, list_blocks={(): {'timestamp': ('timestamp',)}, ('label_values',): {'timestamp_value': ('timestamp_value',)}}),
    ],
    'Your Muted Story Teaser Creators (Unchanged)': [
        Entry(table='Your Muted Story Teaser Creators', filename='your_instagram_activity/subscriptions/your_muted_story_teaser_creators.json', static_fields={}, list_blocks={('subscriptions_muted_story_teaser_creators',): {'title': ('title',), 'href': ('string_map_data', 'Muted Creators', 'href'), 'value': ('string_map_data', 'Muted Creators', 'value'), 'timestamp': ('string_map_data', 'Muted Creators', 'timestamp')}}),
    ],
    'Your Topics (Unchanged)': [
        Entry(table='Your Topics', filename='preferences/your_topics/your_topics.json', static_fields={}, list_blocks={('topics_your_topics',): {'title': ('title',), 'href': ('string_map_data', 'Name', 'href'), 'value': ('string_map_data', 'Name', 'value'), 'timestamp': ('string_map_data', 'Name', 'timestamp')}}),
    ],
}

FB_ENTRIES: dict[str, list[Entry]] = {
    '6179754102079646 (Unchanged)': [
        Entry(table='6179754102079646', filename='your_facebook_activity/groups/your_group_messages/6179754102079646.json', static_fields={'thread_name': ('thread_name',), 'messages': ('messages',)}, list_blocks={}),
    ],
    '6452840174763366 (Unchanged)': [
        Entry(table='6452840174763366', filename='your_facebook_activity/groups/your_group_messages/6452840174763366.json', static_fields={'thread_name': ('thread_name',), 'messages': ('messages',)}, list_blocks={}),
    ],
    '6477893372272082 (Unchanged)': [
        Entry(table='6477893372272082', filename='your_facebook_activity/groups/your_group_messages/6477893372272082.json', static_fields={'thread_name': ('thread_name',), 'messages': ('messages',)}, list_blocks={}),
    ],
    '6798433430245173 (Unchanged)': [
        Entry(table='6798433430245173', filename='your_facebook_activity/groups/your_group_messages/6798433430245173.json', static_fields={'thread_name': ('thread_name',), 'messages': ('messages',)}, list_blocks={}),
    ],
    'Ad Preferences (Original)': [
        Entry(table='Ad Preferences', filename='ads_information/ad_preferences.json', static_fields={'media': ('media',), 'fbid': ('fbid',), 'ent_name': ('ent_name',)}, list_blocks={('label_values',): {'label': ('label',), 'value': ('value',), 'ent_field_name': ('ent_field_name',), 'vec': ('vec',), 'dict': ('dict',), 'title': ('title',)}, ('label_values', 'dict'): {'title': ('title',)}, ('label_values', 'dict', 'dict'): {'ent_field_name': ('ent_field_name',), 'label': ('label',), 'value': ('value',)}}),
    ],
    'Ad Preferences (Merged)': [
        Entry(table='Ad Preferences', filename='ads_information/ad_preferences.json', static_fields={'media': ('media',), 'fbid': ('fbid',), 'ent_name': ('ent_name',)}, list_blocks={('label_values',): {'label': ('label',), 'value': ('value',), 'ent_field_name': ('ent_field_name',), 'vec': ('vec',), 'dict': ('dict',), 'title': ('title',), 'dict.title': ('dict', 'title'), 'dict.dict.ent_field_name': ('dict', 'dict', 'ent_field_name'), 'dict.dict.label': ('dict', 'dict', 'label'), 'dict.dict.value': ('dict', 'dict', 'value')}}),
    ],
    'Admin Activity (Unchanged)': [
        Entry(table='Admin Activity', filename='your_facebook_activity/pages/admin_activity.json', static_fields={'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',)}, list_blocks={('label_values',): {'label': ('label',), 'value': ('value',), 'href': ('href',)}}),
    ],
    'Ads About Meta (Unchanged)': [
        Entry(table='Ads About Meta', filename='ads_information/ads_about_meta.json', static_fields={'media': ('media',), 'fbid': ('fbid',), 'ent_name': ('ent_name',)}, list_blocks={('label_values',): {'label': ('label',), 'value': ('value',), 'ent_field_name': ('ent_field_name',), 'timestamp_value': ('timestamp_value',)}}),
    ],
    'Ads Feedback Activity (Unchanged)': [
        Entry(table='Ads Feedback Activity', filename='ads_information/ads_feedback_activity.json', static_fields={'media': ('media',), 'fbid': ('fbid',)}, list_blocks={('label_values',): {'label': ('label',), 'timestamp_value': ('timestamp_value',)}}),
    ],
    'Ads Interests (Unchanged)': [
        Entry(table='Ads Interests', filename='logged_information/other_logged_information/ads_interests.json', static_fields={'topics_v2': ('topics_v2',)}, list_blocks={}),
    ],
    'Ads Personalization Consent (Unchanged)': [
        Entry(table='Ads Personalization Consent', filename='ads_information/ads_personalization_consent.json', static_fields={'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',), 'ent_name': ('ent_name',)}, list_blocks={('label_values',): {'label': ('label',), 'timestamp_value': ('timestamp_value',), 'ent_field_name': ('ent_field_name',), 'value': ('value',)}}),
    ],
    'Ads Viewed (Unchanged)': [
        Entry(table='Ads Viewed', filename='ads_information/ads_and_topics/ads_viewed.json', static_fields={}, list_blocks={('impressions_history_ads_seen',): {'value': ('string_map_data', 'Author', 'value'), 'timestamp': ('string_map_data', 'Time', 'timestamp')}}),
    ],
    'Advertisers Using Your Activity Or Information (Original)': [
        Entry(table='Advertisers Using Your Activity Or Information', filename='ads_information/advertisers_using_your_activity_or_information.json', static_fields={'media': ('media',), 'fbid': ('fbid',), 'ent_name': ('ent_name',)}, list_blocks={('label_values',): {'label': ('label',), 'ent_field_name': ('ent_field_name',)}, ('label_values', 'vec'): {'value': ('value',)}}),
    ],
    'Advertisers Using Your Activity Or Information (Merged)': [
        Entry(table='Advertisers Using Your Activity Or Information', filename='ads_information/advertisers_using_your_activity_or_information.json', static_fields={'media': ('media',), 'fbid': ('fbid',), 'ent_name': ('ent_name',)}, list_blocks={('label_values',): {'label': ('label',), 'ent_field_name': ('ent_field_name',), 'value': ('vec', 'value')}}),
    ],
    'Advertisers You Ve Interacted With (Unchanged)': [
        Entry(table='Advertisers You Ve Interacted With', filename='ads_information/advertisers_you_ve_interacted_with.json', static_fields={}, list_blocks={('history_v2',): {'title': ('title',), 'action': ('action',), 'timestamp': ('timestamp',)}}),
    ],
    "Advertisers You'Ve Interacted With (Unchanged)": [
        Entry(table="Advertisers You'Ve Interacted With", filename="ads_information/advertisers_you've_interacted_with.json", static_fields={}, list_blocks={('history_v2',): {'title': ('title',), 'action': ('action',), 'timestamp': ('timestamp',)}, (): {'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',)}, ('label_values',): {'label': ('label',)}}),
    ],
    'Archived Stories (Original)': [
        Entry(table='Archived Stories', filename='your_facebook_activity/stories/archived_stories.json', static_fields={}, list_blocks={('archived_stories_v2',): {'timestamp': ('timestamp',), 'title': ('title',)}, ('archived_stories_v2', 'attachments', 'data'): {'uri': ('media', 'uri'), 'creation_timestamp': ('media', 'creation_timestamp'), 'title': ('media', 'title'), 'description': ('media', 'description'), 'dubbing_info': ('media', 'dubbing_info'), 'media_variants': ('media', 'media_variants')}}),
    ],
    'Archived Stories (Merged)': [
        Entry(table='Archived Stories', filename='your_facebook_activity/stories/archived_stories.json', static_fields={}, list_blocks={('archived_stories_v2',): {'timestamp': ('timestamp',), 'title': ('title',), 'uri': ('attachments', 'data', 'media', 'uri'), 'creation_timestamp': ('attachments', 'data', 'media', 'creation_timestamp'), 'attachments.data.title': ('attachments', 'data', 'media', 'title'), 'description': ('attachments', 'data', 'media', 'description'), 'dubbing_info': ('attachments', 'data', 'media', 'dubbing_info'), 'media_variants': ('attachments', 'data', 'media', 'media_variants')}}),
    ],
    'Close Friends (Original)': [
        Entry(table='Close Friends', filename='connections/followers_and_following/close_friends.json', static_fields={}, list_blocks={('relationships_close_friends',): {'title': ('title',), 'media_list_data': ('media_list_data',)}, ('relationships_close_friends', 'string_list_data'): {'href': ('href',), 'value': ('value',), 'timestamp': ('timestamp',)}}),
    ],
    'Close Friends (Merged)': [
        Entry(table='Close Friends', filename='connections/followers_and_following/close_friends.json', static_fields={}, list_blocks={('relationships_close_friends',): {'title': ('title',), 'media_list_data': ('media_list_data',), 'href': ('string_list_data', 'href'), 'value': ('string_list_data', 'value'), 'timestamp': ('string_list_data', 'timestamp')}}),
    ],
    'Collections (Unchanged)': [
        Entry(table='Collections', filename='your_facebook_activity/saved_items_and_collections/collections.json', static_fields={'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',)}, list_blocks={('label_values',): {'label': ('label',), 'value': ('value',)}}),
    ],
    'Comments (Original)': [
        Entry(table='Comments', filename='personal_information/profile_information/your_facebook_activity/comments_and_reactions/comments.json', static_fields={}, list_blocks={('comments_v2',): {'timestamp': ('timestamp',)}, ('comments_v2', 'data'): {'timestamp': ('comment', 'timestamp'), 'comment': ('comment', 'comment')}}),
        Entry(table='Comments', filename='your_activity_across_facebook/comments_and_reactions/comments.json', static_fields={}, list_blocks={('comments_v2',): {'timestamp': ('timestamp',)}, ('comments_v2', 'data'): {'timestamp': ('comment', 'timestamp'), 'comment': ('comment', 'comment')}}),
        Entry(table='Comments', filename='your_facebook_activity/comments_and_reactions/comments.json', static_fields={}, list_blocks={('comments_v2',): {'timestamp': ('timestamp',)}, ('comments_v2', 'data'): {'timestamp': ('comment', 'timestamp'), 'comment': ('comment', 'comment')}}),
    ],
    'Comments (Merged)': [
        Entry(table='Comments', filename='personal_information/profile_information/your_facebook_activity/comments_and_reactions/comments.json', static_fields={}, list_blocks={('comments_v2',): {'timestamp': ('timestamp',), 'data.timestamp': ('data', 'comment', 'timestamp'), 'comment': ('data', 'comment', 'comment')}}),
        Entry(table='Comments', filename='your_activity_across_facebook/comments_and_reactions/comments.json', static_fields={}, list_blocks={('comments_v2',): {'timestamp': ('timestamp',), 'data.timestamp': ('data', 'comment', 'timestamp'), 'comment': ('data', 'comment', 'comment')}}),
        Entry(table='Comments', filename='your_facebook_activity/comments_and_reactions/comments.json', static_fields={}, list_blocks={('comments_v2',): {'timestamp': ('timestamp',), 'data.timestamp': ('data', 'comment', 'timestamp'), 'comment': ('data', 'comment', 'comment')}}),
    ],
    'Comments Allowed From (Unchanged)': [
        Entry(table='Comments Allowed From', filename='preferences/settings/comments_allowed_from.json', static_fields={}, list_blocks={('settings_allow_comments_from',): {'title': ('title',), 'href': ('string_map_data', 'Comments Allowed From', 'href'), 'value': ('string_map_data', 'Comments Allowed From', 'value'), 'timestamp': ('string_map_data', 'Comments Allowed From', 'timestamp')}}),
    ],
    'Consents (Unchanged)': [
        Entry(table='Consents', filename='logged_information/other_logged_information/consents.json', static_fields={'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',), 'ent_name': ('ent_name',)}, list_blocks={('label_values',): {'label': ('label',), 'ent_field_name': ('ent_field_name',), 'timestamp_value': ('timestamp_value',)}}),
    ],
    'Content Sharing Links You Have Created (Unchanged)': [
        Entry(table='Content Sharing Links You Have Created', filename='personal_information/profile_information/your_facebook_activity/posts/content_sharing_links_you_have_created.json', static_fields={}, list_blocks={(): {'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',)}, ('label_values',): {'label': ('label',), 'value': ('value',), 'href': ('href',)}}),
        Entry(table='Content Sharing Links You Have Created', filename='your_facebook_activity/posts/content_sharing_links_you_have_created.json', static_fields={}, list_blocks={(): {'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',), 'ent_name': ('ent_name',)}, ('label_values',): {'label': ('label',), 'value': ('value',), 'href': ('href',), 'ent_field_name': ('ent_field_name',)}}),
    ],
    'Controls (Original)': [
        Entry(table='Controls', filename='personal_information/profile_information/preferences/feed/controls.json', static_fields={}, list_blocks={('controls',): {'name': ('name',), 'description': ('description',)}, ('controls', 'entries'): {'timestamp': ('timestamp',), 'name': ('data', 'name'), 'uri': ('data', 'uri')}}),
        Entry(table='Controls', filename='preferences/feed/controls.json', static_fields={}, list_blocks={('controls',): {'name': ('name',), 'description': ('description',), 'entries': ('entries',)}}),
    ],
    'Controls (Merged)': [
        Entry(table='Controls', filename='personal_information/profile_information/preferences/feed/controls.json', static_fields={}, list_blocks={('controls',): {'name': ('name',), 'description': ('description',), 'timestamp': ('entries', 'timestamp'), 'entries.name': ('entries', 'data', 'name'), 'uri': ('entries', 'data', 'uri')}}),
        Entry(table='Controls', filename='preferences/feed/controls.json', static_fields={}, list_blocks={('controls',): {'name': ('name',), 'description': ('description',), 'entries': ('entries',)}}),
    ],
    'Edits You Made To Posts (Unchanged)': [
        Entry(table='Edits You Made To Posts', filename='personal_information/profile_information/your_facebook_activity/posts/edits_you_made_to_posts.json', static_fields={}, list_blocks={(): {'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',)}, ('label_values',): {'label': ('label',), 'value': ('value',)}}),
        Entry(table='Edits You Made To Posts', filename='your_facebook_activity/posts/edits_you_made_to_posts.json', static_fields={}, list_blocks={(): {'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',)}, ('label_values',): {'label': ('label',), 'value': ('value',)}}),
    ],
    'Emails We Sent You (Unchanged)': [
        Entry(table='Emails We Sent You', filename='personal_information/other_personal_information/emails_we_sent_you.json', static_fields={}, list_blocks={(): {'title': ('title',), 'timestamp': ('timestamp',)}}),
    ],
    'Facebook Reels Usage Information (Original)': [
        Entry(table='Facebook Reels Usage Information', filename='logged_information/other_logged_information/facebook_reels_usage_information.json', static_fields={'media': ('media',), 'fbid': ('fbid',), 'ent_name': ('ent_name',)}, list_blocks={('label_values',): {'label': ('label',), 'ent_field_name': ('ent_field_name',)}, ('label_values', 'dict'): {'label': ('label',), 'value': ('value',)}}),
    ],
    'Facebook Reels Usage Information (Merged)': [
        Entry(table='Facebook Reels Usage Information', filename='logged_information/other_logged_information/facebook_reels_usage_information.json', static_fields={'media': ('media',), 'fbid': ('fbid',), 'ent_name': ('ent_name',)}, list_blocks={('label_values',): {'label': ('label',), 'ent_field_name': ('ent_field_name',), 'dict.label': ('dict', 'label'), 'value': ('dict', 'value')}}),
    ],
    'Feed (Original)': [
        Entry(table='Feed', filename='preferences/feed/feed.json', static_fields={}, list_blocks={('people_and_friends_v2',): {'name': ('name',), 'description': ('description',)}, ('people_and_friends_v2', 'entries'): {'timestamp': ('timestamp',), 'name': ('data', 'name'), 'uri': ('data', 'uri')}}),
    ],
    'Feed (Merged)': [
        Entry(table='Feed', filename='preferences/feed/feed.json', static_fields={}, list_blocks={('people_and_friends_v2',): {'name': ('name',), 'description': ('description',), 'timestamp': ('entries', 'timestamp'), 'entries.name': ('entries', 'data', 'name'), 'uri': ('entries', 'data', 'uri')}}),
    ],
    "Follow Requests You'Ve Received (Original)": [
        Entry(table="Follow Requests You'Ve Received", filename="connections/followers_and_following/follow_requests_you've_received.json", static_fields={}, list_blocks={('relationships_follow_requests_received',): {'title': ('title',), 'media_list_data': ('media_list_data',)}, ('relationships_follow_requests_received', 'string_list_data'): {'href': ('href',), 'value': ('value',), 'timestamp': ('timestamp',)}}),
    ],
    "Follow Requests You'Ve Received (Merged)": [
        Entry(table="Follow Requests You'Ve Received", filename="connections/followers_and_following/follow_requests_you've_received.json", static_fields={}, list_blocks={('relationships_follow_requests_received',): {'title': ('title',), 'media_list_data': ('media_list_data',), 'href': ('string_list_data', 'href'), 'value': ('string_list_data', 'value'), 'timestamp': ('string_list_data', 'timestamp')}}),
    ],
    'Followers 1 (Unchanged)': [
        Entry(table='Followers 1', filename='connections/followers_and_following/followers_1.json', static_fields={}, list_blocks={(): {'title': ('title',), 'media_list_data': ('media_list_data',)}, ('string_list_data',): {'href': ('href',), 'value': ('value',), 'timestamp': ('timestamp',)}}),
    ],
    'Following (Original)': [
        Entry(table='Following', filename='connections/followers_and_following/following.json', static_fields={}, list_blocks={('relationships_following',): {'title': ('title',), 'media_list_data': ('media_list_data',)}, ('relationships_following', 'string_list_data'): {'href': ('href',), 'value': ('value',), 'timestamp': ('timestamp',)}}),
    ],
    'Following (Merged)': [
        Entry(table='Following', filename='connections/followers_and_following/following.json', static_fields={}, list_blocks={('relationships_following',): {'title': ('title',), 'media_list_data': ('media_list_data',), 'href': ('string_list_data', 'href'), 'value': ('string_list_data', 'value'), 'timestamp': ('string_list_data', 'timestamp')}}),
    ],
    'Fundraiser Posts You Likely Viewed (Unchanged)': [
        Entry(table='Fundraiser Posts You Likely Viewed', filename='personal_information/profile_information/your_facebook_activity/fundraisers/fundraiser_posts_you_likely_viewed.json', static_fields={'media': ('media',), 'fbid': ('fbid',)}, list_blocks={('label_values',): {'label': ('label',), 'value': ('value',)}}),
        Entry(table='Fundraiser Posts You Likely Viewed', filename='your_facebook_activity/fundraisers/fundraiser_posts_you_likely_viewed.json', static_fields={'media': ('media',), 'fbid': ('fbid',), 'ent_name': ('ent_name',)}, list_blocks={('label_values',): {'label': ('label',), 'value': ('value',), 'ent_field_name': ('ent_field_name',)}}),
    ],
    'Fundraisers Donated To (Original)': [
        Entry(table='Fundraisers Donated To', filename='your_facebook_activity/fundraisers/fundraisers_donated_to.json', static_fields={}, list_blocks={('fundraisers_donated_to_v2',): {'timestamp': ('timestamp',)}, ('fundraisers_donated_to_v2', 'attachments', 'data'): {'title': ('fundraiser', 'title'), 'donated_amount': ('fundraiser', 'donated_amount')}}),
    ],
    'Fundraisers Donated To (Merged)': [
        Entry(table='Fundraisers Donated To', filename='your_facebook_activity/fundraisers/fundraisers_donated_to.json', static_fields={}, list_blocks={('fundraisers_donated_to_v2',): {'timestamp': ('timestamp',), 'title': ('attachments', 'data', 'fundraiser', 'title'), 'donated_amount': ('attachments', 'data', 'fundraiser', 'donated_amount')}}),
    ],
    "Group Invites You'Ve Received (Unchanged)": [
        Entry(table="Group Invites You'Ve Received", filename="your_facebook_activity/groups/group_invites_you've_received.json", static_fields={'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',)}, list_blocks={(): {'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',)}, ('label_values',): {'label': ('label',), 'timestamp_value': ('timestamp_value',)}}),
    ],
    "Group Invites You'Ve Sent (Unchanged)": [
        Entry(table="Group Invites You'Ve Sent", filename="your_facebook_activity/groups/group_invites_you've_sent.json", static_fields={}, list_blocks={(): {'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',)}, ('label_values',): {'label': ('label',), 'value': ('value',)}}),
    ],
    'Group Posts And Comments (Original)': [
        Entry(table='Group Posts And Comments', filename='your_activity_across_facebook/groups/group_posts_and_comments.json', static_fields={}, list_blocks={('group_posts_v2',): {'timestamp': ('timestamp',), 'title': ('title',)}, ('group_posts_v2', 'data'): {'post': ('post',)}}),
        Entry(table='Group Posts And Comments', filename='your_facebook_activity/groups/group_posts_and_comments.json', static_fields={}, list_blocks={('group_posts_v2',): {'timestamp': ('timestamp',), 'title': ('title',)}, ('group_posts_v2', 'data'): {'post': ('post',)}}),
    ],
    'Group Posts And Comments (Merged)': [
        Entry(table='Group Posts And Comments', filename='your_activity_across_facebook/groups/group_posts_and_comments.json', static_fields={}, list_blocks={('group_posts_v2',): {'timestamp': ('timestamp',), 'title': ('title',), 'post': ('data', 'post')}}),
        Entry(table='Group Posts And Comments', filename='your_facebook_activity/groups/group_posts_and_comments.json', static_fields={}, list_blocks={('group_posts_v2',): {'timestamp': ('timestamp',), 'title': ('title',), 'post': ('data', 'post')}}),
    ],
    'Groups And Pages That You May Find Engaging (Original)': [
        Entry(table='Groups And Pages That You May Find Engaging', filename='your_facebook_activity/groups/groups_and_pages_that_you_may_find_engaging.json', static_fields={'media': ('media',), 'fbid': ('fbid',), 'ent_name': ('ent_name',)}, list_blocks={('label_values',): {'ent_field_name': ('ent_field_name',), 'label': ('label',)}, ('label_values', 'vec'): {'value': ('value',)}}),
    ],
    'Groups And Pages That You May Find Engaging (Merged)': [
        Entry(table='Groups And Pages That You May Find Engaging', filename='your_facebook_activity/groups/groups_and_pages_that_you_may_find_engaging.json', static_fields={'media': ('media',), 'fbid': ('fbid',), 'ent_name': ('ent_name',)}, list_blocks={('label_values',): {'ent_field_name': ('ent_field_name',), 'label': ('label',), 'value': ('vec', 'value')}}),
    ],
    'Groups You Ve Visited (Unchanged)': [
        Entry(table='Groups You Ve Visited', filename='logged_information/your_interactions_on_facebook/groups_you_ve_visited.json', static_fields={}, list_blocks={(): {'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',), 'ent_name': ('ent_name',)}, ('label_values',): {'ent_field_name': ('ent_field_name',), 'label': ('label',), 'value': ('value',)}}),
    ],
    "Groups You'Ve Visited (Unchanged)": [
        Entry(table="Groups You'Ve Visited", filename="logged_information/interactions/groups_you've_visited.json", static_fields={}, list_blocks={(): {'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',)}, ('label_values',): {'label': ('label',), 'value': ('value',)}}),
        Entry(table="Groups You'Ve Visited", filename="logged_information/your_interactions_on_facebook/groups_you've_visited.json", static_fields={}, list_blocks={(): {'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',)}, ('label_values',): {'label': ('label',), 'value': ('value',)}}),
    ],
    "Information You'Ve Submitted To Advertisers (Unchanged)": [
        Entry(table="Information You'Ve Submitted To Advertisers", filename="ads_information/information_you've_submitted_to_advertisers.json", static_fields={}, list_blocks={('lead_gen_info_v2',): {'label': ('label',), 'value': ('value',)}}),
    ],
    'Likes And Reactions (Original)': [
        Entry(table='Likes And Reactions', filename='personal_information/profile_information/your_facebook_activity/comments_and_reactions/likes_and_reactions.json', static_fields={}, list_blocks={(): {'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',)}, ('label_values',): {'label': ('label',), 'value': ('value',)}}),
        Entry(table='Likes And Reactions', filename='your_facebook_activity/comments_and_reactions/likes_and_reactions.json', static_fields={}, list_blocks={(): {'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',), 'ent_name': ('ent_name',)}, ('label_values',): {'label': ('label',), 'value': ('value',), 'ent_field_name': ('ent_field_name',), 'href': ('href',), 'title': ('title',)}, ('label_values', 'dict'): {'title': ('title',)}, ('label_values', 'dict', 'dict'): {'ent_field_name': ('ent_field_name',), 'label': ('label',), 'value': ('value',)}}),
    ],
    'Likes And Reactions (Merged)': [
        Entry(table='Likes And Reactions', filename='personal_information/profile_information/your_facebook_activity/comments_and_reactions/likes_and_reactions.json', static_fields={}, list_blocks={(): {'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',)}, ('label_values',): {'label': ('label',), 'value': ('value',)}}),
        Entry(table='Likes And Reactions', filename='your_facebook_activity/comments_and_reactions/likes_and_reactions.json', static_fields={}, list_blocks={(): {'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',), 'ent_name': ('ent_name',)}, ('label_values',): {'label': ('label',), 'value': ('value',), 'ent_field_name': ('ent_field_name',), 'href': ('href',), 'title': ('title',), 'dict.title': ('dict', 'title'), 'dict.dict.ent_field_name': ('dict', 'dict', 'ent_field_name'), 'dict.dict.label': ('dict', 'dict', 'label'), 'dict.dict.value': ('dict', 'dict', 'value')}}),
    ],
    'Other Categories Used To Reach You (Original)': [
        Entry(table='Other Categories Used To Reach You', filename='ads_information/other_categories_used_to_reach_you.json', static_fields={'media': ('media',), 'fbid': ('fbid',), 'ent_name': ('ent_name',), 'bcts': ('bcts',)}, list_blocks={('label_values',): {'label': ('label',), 'ent_field_name': ('ent_field_name',)}, ('label_values', 'vec'): {'value': ('value',)}}),
    ],
    'Other Categories Used To Reach You (Merged)': [
        Entry(table='Other Categories Used To Reach You', filename='ads_information/other_categories_used_to_reach_you.json', static_fields={'media': ('media',), 'fbid': ('fbid',), 'ent_name': ('ent_name',), 'bcts': ('bcts',)}, list_blocks={('label_values',): {'label': ('label',), 'ent_field_name': ('ent_field_name',), 'value': ('vec', 'value')}}),
    ],
    'Pages And Profiles You Follow (Original)': [
        Entry(table='Pages And Profiles You Follow', filename='personal_information/profile_information/your_facebook_activity/pages/pages_and_profiles_you_follow.json', static_fields={}, list_blocks={('pages_followed_v2',): {'timestamp': ('timestamp',), 'title': ('title',)}, ('pages_followed_v2', 'data'): {'name': ('name',)}}),
        Entry(table='Pages And Profiles You Follow', filename='your_activity_across_facebook/pages/pages_and_profiles_you_follow.json', static_fields={}, list_blocks={('pages_followed_v2',): {'timestamp': ('timestamp',), 'title': ('title',)}, ('pages_followed_v2', 'data'): {'name': ('name',)}}),
        Entry(table='Pages And Profiles You Follow', filename='your_facebook_activity/pages/pages_and_profiles_you_follow.json', static_fields={}, list_blocks={('pages_followed_v2',): {'timestamp': ('timestamp',), 'title': ('title',)}, ('pages_followed_v2', 'data'): {'name': ('name',)}}),
    ],
    'Pages And Profiles You Follow (Merged)': [
        Entry(table='Pages And Profiles You Follow', filename='personal_information/profile_information/your_facebook_activity/pages/pages_and_profiles_you_follow.json', static_fields={}, list_blocks={('pages_followed_v2',): {'timestamp': ('timestamp',), 'title': ('title',), 'name': ('data', 'name')}}),
        Entry(table='Pages And Profiles You Follow', filename='your_activity_across_facebook/pages/pages_and_profiles_you_follow.json', static_fields={}, list_blocks={('pages_followed_v2',): {'timestamp': ('timestamp',), 'title': ('title',), 'name': ('data', 'name')}}),
        Entry(table='Pages And Profiles You Follow', filename='your_facebook_activity/pages/pages_and_profiles_you_follow.json', static_fields={}, list_blocks={('pages_followed_v2',): {'timestamp': ('timestamp',), 'title': ('title',), 'name': ('data', 'name')}}),
    ],
    "Pages And Profiles You'Ve Recommended (Unchanged)": [
        Entry(table="Pages And Profiles You'Ve Recommended", filename="your_facebook_activity/pages/pages_and_profiles_you've_recommended.json", static_fields={}, list_blocks={('recommended_pages_v2',): {'name': ('name',), 'timestamp': ('timestamp',), 'url': ('url',)}}),
    ],
    "Pages And Profiles You'Ve Unfollowed (Original)": [
        Entry(table="Pages And Profiles You'Ve Unfollowed", filename="your_facebook_activity/pages/pages_and_profiles_you've_unfollowed.json", static_fields={}, list_blocks={('pages_unfollowed_v2',): {'timestamp': ('timestamp',), 'title': ('title',)}, ('pages_unfollowed_v2', 'data'): {'name': ('name',)}}),
    ],
    "Pages And Profiles You'Ve Unfollowed (Merged)": [
        Entry(table="Pages And Profiles You'Ve Unfollowed", filename="your_facebook_activity/pages/pages_and_profiles_you've_unfollowed.json", static_fields={}, list_blocks={('pages_unfollowed_v2',): {'timestamp': ('timestamp',), 'title': ('title',), 'name': ('data', 'name')}}),
    ],
    'Pages You Ve Liked (Unchanged)': [
        Entry(table='Pages You Ve Liked', filename='your_facebook_activity/pages/pages_you_ve_liked.json', static_fields={}, list_blocks={('page_likes_v2',): {'name': ('name',), 'timestamp': ('timestamp',), 'url': ('url',)}}),
    ],
    "Pages You'Ve Liked (Unchanged)": [
        Entry(table="Pages You'Ve Liked", filename="personal_information/profile_information/your_facebook_activity/pages/pages_you've_liked.json", static_fields={}, list_blocks={('page_likes_v2',): {'name': ('name',), 'timestamp': ('timestamp',), 'url': ('url',)}}),
        Entry(table="Pages You'Ve Liked", filename="your_activity_across_facebook/pages/pages_you've_liked.json", static_fields={}, list_blocks={('page_likes_v2',): {'name': ('name',), 'timestamp': ('timestamp',), 'url': ('url',)}}),
        Entry(table="Pages You'Ve Liked", filename="your_facebook_activity/pages/pages_you've_liked.json", static_fields={}, list_blocks={('page_likes_v2',): {'name': ('name',), 'timestamp': ('timestamp',), 'url': ('url',)}}),
    ],
    'People And Friends (Original)': [
        Entry(table='People And Friends', filename='logged_information/activity_messages/people_and_friends.json', static_fields={}, list_blocks={('people_interactions_v2',): {'name': ('name',), 'description': ('description',)}, ('people_interactions_v2', 'entries'): {'timestamp': ('timestamp',), 'name': ('data', 'name'), 'uri': ('data', 'uri')}, (): {'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',)}, ('label_values',): {'label': ('label',), 'value': ('value',)}}),
    ],
    'People And Friends (Merged)': [
        Entry(table='People And Friends', filename='logged_information/activity_messages/people_and_friends.json', static_fields={}, list_blocks={('people_interactions_v2',): {'name': ('name',), 'description': ('description',), 'timestamp': ('entries', 'timestamp'), 'entries.name': ('entries', 'data', 'name'), 'uri': ('entries', 'data', 'uri')}, (): {'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',)}, ('label_values',): {'label': ('label',), 'value': ('value',)}}),
    ],
    'People We Think You Should Follow (Unchanged)': [
        Entry(table='People We Think You Should Follow', filename='logged_information/your_topics/people_we_think_you_should_follow.json', static_fields={'timestamp': ('timestamp',), 'media': ('media',)}, list_blocks={('label_values',): {'label': ('label',), 'vec': ('vec',)}}),
    ],
    'Posts On Other Pages And Profiles (Unchanged)': [
        Entry(table='Posts On Other Pages And Profiles', filename='personal_information/profile_information/your_facebook_activity/posts/posts_on_other_pages_and_profiles.json', static_fields={}, list_blocks={(): {'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',)}, ('label_values',): {'label': ('label',), 'value': ('value',)}}),
        Entry(table='Posts On Other Pages And Profiles', filename='your_facebook_activity/posts/posts_on_other_pages_and_profiles.json', static_fields={'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',)}, list_blocks={(): {'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',)}, ('label_values',): {'label': ('label',), 'value': ('value',)}}),
    ],
    'Posts Viewed (Unchanged)': [
        Entry(table='Posts Viewed', filename='ads_information/ads_and_topics/posts_viewed.json', static_fields={}, list_blocks={('impressions_history_posts_seen',): {'value': ('string_map_data', 'Author', 'value'), 'timestamp': ('string_map_data', 'Time', 'timestamp')}}),
    ],
    'Privacy Settings (Original)': [
        Entry(table='Privacy Settings', filename='personal_information/profile_information/preferences/preferences/privacy_settings.json', static_fields={'media': ('media',), 'fbid': ('fbid',)}, list_blocks={('label_values',): {'label': ('label',)}, ('label_values', 'dict'): {'label': ('label',), 'value': ('value',)}}),
        Entry(table='Privacy Settings', filename='preferences/preferences/privacy_settings.json', static_fields={'media': ('media',), 'fbid': ('fbid',)}, list_blocks={('label_values',): {'label': ('label',)}, ('label_values', 'dict'): {'label': ('label',), 'value': ('value',)}}),
    ],
    'Privacy Settings (Merged)': [
        Entry(table='Privacy Settings', filename='personal_information/profile_information/preferences/preferences/privacy_settings.json', static_fields={'media': ('media',), 'fbid': ('fbid',)}, list_blocks={('label_values',): {'label': ('label',), 'dict.label': ('dict', 'label'), 'value': ('dict', 'value')}}),
        Entry(table='Privacy Settings', filename='preferences/preferences/privacy_settings.json', static_fields={'media': ('media',), 'fbid': ('fbid',)}, list_blocks={('label_values',): {'label': ('label',), 'dict.label': ('dict', 'label'), 'value': ('dict', 'value')}}),
    ],
    'Recently Viewed (Original)': [
        Entry(table='Recently Viewed', filename='logged_information/interactions/recently_viewed.json', static_fields={}, list_blocks={('recently_viewed',): {'name': ('name',), 'description': ('description',)}, ('recently_viewed', 'children'): {'name': ('name',), 'description': ('description',)}, ('recently_viewed', 'children', 'entries'): {'timestamp': ('timestamp',), 'name': ('data', 'name'), 'uri': ('data', 'uri'), 'watch_time': ('data', 'watch_time'), 'value': ('data', 'value')}, ('recently_viewed', 'entries'): {'timestamp': ('timestamp',), 'name': ('data', 'name'), 'uri': ('data', 'uri')}}),
        Entry(table='Recently Viewed', filename='logged_information/your_interactions_on_facebook/recently_viewed.json', static_fields={}, list_blocks={('recently_viewed',): {'name': ('name',), 'description': ('description',)}, ('recently_viewed', 'entries'): {'timestamp': ('timestamp',), 'name': ('data', 'name'), 'uri': ('data', 'uri')}, ('recently_viewed', 'children'): {'name': ('name',), 'description': ('description',)}, ('recently_viewed', 'children', 'entries'): {'timestamp': ('timestamp',), 'value': ('data', 'value'), 'name': ('data', 'name'), 'uri': ('data', 'uri'), 'watch_time': ('data', 'watch_time')}}),
    ],
    'Recently Viewed (Merged)': [
        Entry(table='Recently Viewed', filename='logged_information/interactions/recently_viewed.json', static_fields={}, list_blocks={('recently_viewed',): {'name': ('name',), 'description': ('description',), 'children.name': ('children', 'name'), 'children.description': ('children', 'description'), 'timestamp': ('children', 'entries', 'timestamp'), 'children.entries.name': ('children', 'entries', 'data', 'name'), 'uri': ('children', 'entries', 'data', 'uri'), 'watch_time': ('children', 'entries', 'data', 'watch_time'), 'value': ('children', 'entries', 'data', 'value'), 'entries.timestamp': ('entries', 'timestamp'), 'entries.name': ('entries', 'data', 'name'), 'entries.uri': ('entries', 'data', 'uri')}}),
        Entry(table='Recently Viewed', filename='logged_information/your_interactions_on_facebook/recently_viewed.json', static_fields={}, list_blocks={('recently_viewed',): {'name': ('name',), 'description': ('description',), 'timestamp': ('entries', 'timestamp'), 'entries.name': ('entries', 'data', 'name'), 'uri': ('entries', 'data', 'uri'), 'children.name': ('children', 'name'), 'children.description': ('children', 'description'), 'children.entries.timestamp': ('children', 'entries', 'timestamp'), 'value': ('children', 'entries', 'data', 'value'), 'children.entries.name': ('children', 'entries', 'data', 'name'), 'children.entries.uri': ('children', 'entries', 'data', 'uri'), 'watch_time': ('children', 'entries', 'data', 'watch_time')}}),
    ],
    'Recently Visited (Original)': [
        Entry(table='Recently Visited', filename='logged_information/interactions/recently_visited.json', static_fields={}, list_blocks={('visited_things_v2',): {'name': ('name',), 'description': ('description',)}, ('visited_things_v2', 'entries'): {'timestamp': ('timestamp',), 'name': ('data', 'name'), 'uri': ('data', 'uri')}}),
        Entry(table='Recently Visited', filename='logged_information/your_interactions_on_facebook/recently_visited.json', static_fields={}, list_blocks={('visited_things_v2',): {'name': ('name',), 'description': ('description',)}, ('visited_things_v2', 'entries'): {'timestamp': ('timestamp',), 'name': ('data', 'name'), 'uri': ('data', 'uri'), 'value': ('data', 'value')}}),
    ],
    'Recently Visited (Merged)': [
        Entry(table='Recently Visited', filename='logged_information/interactions/recently_visited.json', static_fields={}, list_blocks={('visited_things_v2',): {'name': ('name',), 'description': ('description',), 'timestamp': ('entries', 'timestamp'), 'entries.name': ('entries', 'data', 'name'), 'uri': ('entries', 'data', 'uri')}}),
        Entry(table='Recently Visited', filename='logged_information/your_interactions_on_facebook/recently_visited.json', static_fields={}, list_blocks={('visited_things_v2',): {'name': ('name',), 'description': ('description',), 'timestamp': ('entries', 'timestamp'), 'entries.name': ('entries', 'data', 'name'), 'uri': ('entries', 'data', 'uri'), 'value': ('entries', 'data', 'value')}}),
    ],
    'Recommended Topics (Unchanged)': [
        Entry(table='Recommended Topics', filename='preferences/your_topics/recommended_topics.json', static_fields={}, list_blocks={('topics_your_topics',): {'title': ('title',), 'href': ('string_map_data', 'Name', 'href'), 'value': ('string_map_data', 'Name', 'value'), 'timestamp': ('string_map_data', 'Name', 'timestamp')}}),
    ],
    'Reduce (Unchanged)': [
        Entry(table='Reduce', filename='preferences/feed/reduce.json', static_fields={'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',), 'ent_name': ('ent_name',)}, list_blocks={('label_values',): {'ent_field_name': ('ent_field_name',), 'label': ('label',), 'value': ('value',), 'timestamp_value': ('timestamp_value',)}}),
    ],
    'Reels Preferences (Unchanged)': [
        Entry(table='Reels Preferences', filename='personal_information/profile_information/preferences/preferences/reels_preferences.json', static_fields={'media': ('media',), 'fbid': ('fbid',)}, list_blocks={('label_values',): {'label': ('label',), 'value': ('value',)}}),
        Entry(table='Reels Preferences', filename='preferences/preferences/reels_preferences.json', static_fields={'media': ('media',), 'fbid': ('fbid',), 'ent_name': ('ent_name',)}, list_blocks={('label_values',): {'label': ('label',), 'value': ('value',), 'ent_field_name': ('ent_field_name',), 'vec': ('vec',)}}),
    ],
    'Registration Information (Unchanged)': [
        Entry(table='Registration Information', filename='security_and_login_information/registration_information.json', static_fields={'timestamp': ('timestamp',)}, list_blocks={}),
    ],
    'Snooze (Unchanged)': [
        Entry(table='Snooze', filename='personal_information/profile_information/preferences/feed/snooze.json', static_fields={'media': ('media',), 'fbid': ('fbid',)}, list_blocks={('label_values',): {'label': ('label',), 'value': ('value',)}}),
        Entry(table='Snooze', filename='preferences/feed/snooze.json', static_fields={'media': ('media',), 'fbid': ('fbid',)}, list_blocks={('label_values',): {'label': ('label',), 'value': ('value',)}}),
    ],
    'Story Reactions (Unchanged)': [
        Entry(table='Story Reactions', filename='personal_information/profile_information/your_facebook_activity/stories/story_reactions.json', static_fields={}, list_blocks={('stories_feedback_v2',): {'title': ('title',)}}),
        Entry(table='Story Reactions', filename='your_facebook_activity/stories/story_reactions.json', static_fields={}, list_blocks={('stories_feedback_v2',): {'title': ('title',)}}),
    ],
    'Story Views In Past 7 Days (Unchanged)': [
        Entry(table='Story Views In Past 7 Days', filename='ads_information/story_views_in_past_7_days.json', static_fields={'media': ('media',), 'fbid': ('fbid',)}, list_blocks={('label_values',): {'label': ('label',), 'value': ('value',)}}),
    ],
    'Subscription For No Ads (Unchanged)': [
        Entry(table='Subscription For No Ads', filename='ads_information/subscription_for_no_ads.json', static_fields={'media': ('media',), 'fbid': ('fbid',)}, list_blocks={('label_values',): {'label': ('label',), 'value': ('value',)}}),
    ],
    'Support Messages (Unchanged)': [
        Entry(table='Support Messages', filename='personal_information/profile_information/your_facebook_activity/messages/support_messages.json', static_fields={'timestamp': ('support_messages', '7156925894430515', 'timestamp'), 'subject': ('support_messages', '7156925894430515', 'subject')}, list_blocks={('support_messages', '8752122044910884', 'messages'): {'from': ('from',), 'to': ('to',), 'subject': ('subject',), 'message': ('message',), 'timestamp': ('timestamp',)}, ('support_messages', '7156925894430515', 'messages'): {'from': ('from',), 'to': ('to',), 'subject': ('subject',), 'message': ('message',), 'timestamp': ('timestamp',)}}),
        Entry(table='Support Messages', filename='your_facebook_activity/messages/support_messages.json', static_fields={'timestamp': ('support_messages', '10223298304470161', 'timestamp'), 'subject': ('support_messages', '10223298304470161', 'subject')}, list_blocks={('support_messages', '10230171959787248', 'messages'): {'from': ('from',), 'to': ('to',), 'subject': ('subject',), 'message': ('message',), 'timestamp': ('timestamp',)}, ('support_messages', '10223298304470161', 'messages'): {'from': ('from',), 'to': ('to',), 'subject': ('subject',), 'message': ('message',), 'timestamp': ('timestamp',)}}),
    ],
    'Time Spent On Facebook (Original)': [
        Entry(table='Time Spent On Facebook', filename='personal_information/profile_information/your_facebook_activity/other_activity/time_spent_on_facebook.json', static_fields={}, list_blocks={(): {'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',)}, ('label_values',): {'label': ('label',)}, ('label_values', 'vec', 'dict'): {'label': ('label',), 'timestamp_value': ('timestamp_value',)}}),
        Entry(table='Time Spent On Facebook', filename='your_facebook_activity/other_activity/time_spent_on_facebook.json', static_fields={'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',), 'ent_name': ('ent_name',)}, list_blocks={(): {'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',)}, ('label_values',): {'label': ('label',), 'ent_field_name': ('ent_field_name',), 'timestamp_value': ('timestamp_value',)}, ('label_values', 'vec', 'dict'): {'label': ('label',), 'timestamp_value': ('timestamp_value',)}}),
    ],
    'Time Spent On Facebook (Merged)': [
        Entry(table='Time Spent On Facebook', filename='personal_information/profile_information/your_facebook_activity/other_activity/time_spent_on_facebook.json', static_fields={}, list_blocks={(): {'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',)}, ('label_values',): {'label': ('label',), 'vec.dict.label': ('vec', 'dict', 'label'), 'timestamp_value': ('vec', 'dict', 'timestamp_value')}}),
        Entry(table='Time Spent On Facebook', filename='your_facebook_activity/other_activity/time_spent_on_facebook.json', static_fields={'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',), 'ent_name': ('ent_name',)}, list_blocks={(): {'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',)}, ('label_values',): {'label': ('label',), 'ent_field_name': ('ent_field_name',), 'timestamp_value': ('timestamp_value',), 'vec.dict.label': ('vec', 'dict', 'label'), 'vec.dict.timestamp_value': ('vec', 'dict', 'timestamp_value')}}),
    ],
    'Video (Original)': [
        Entry(table='Video', filename='personal_information/profile_information/preferences/preferences/video.json', static_fields={}, list_blocks={('watch_videos_v2',): {'video_title': ('video_title',), 'user_action': ('user_action',), 'action_time': ('action_time',), 'feedback_collection': ('feedback_collection',)}}),
        Entry(table='Video', filename='preferences/preferences/video.json', static_fields={'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',), 'ent_name': ('ent_name',)}, list_blocks={('watch_videos_v2',): {'video_title': ('video_title',), 'user_action': ('user_action',), 'action_time': ('action_time',), 'feedback_collection': ('feedback_collection',)}, ('label_values',): {'label': ('label',), 'value': ('value',), 'ent_field_name': ('ent_field_name',), 'vec': ('vec',), 'timestamp_value': ('timestamp_value',), 'title': ('title',)}, ('label_values', 'dict'): {'title': ('title',)}, ('label_values', 'dict', 'dict'): {'ent_field_name': ('ent_field_name',), 'label': ('label',), 'value': ('value',), 'href': ('href',), 'title': ('title',)}, ('label_values', 'dict', 'dict', 'dict'): {'title': ('title',)}, ('label_values', 'dict', 'dict', 'dict', 'dict'): {'ent_field_name': ('ent_field_name',), 'label': ('label',), 'value': ('value',)}}),
    ],
    'Video (Merged)': [
        Entry(table='Video', filename='personal_information/profile_information/preferences/preferences/video.json', static_fields={}, list_blocks={('watch_videos_v2',): {'video_title': ('video_title',), 'user_action': ('user_action',), 'action_time': ('action_time',), 'feedback_collection': ('feedback_collection',)}}),
        Entry(table='Video', filename='preferences/preferences/video.json', static_fields={'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',), 'ent_name': ('ent_name',)}, list_blocks={('watch_videos_v2',): {'video_title': ('video_title',), 'user_action': ('user_action',), 'action_time': ('action_time',), 'feedback_collection': ('feedback_collection',)}, ('label_values',): {'label': ('label',), 'value': ('value',), 'ent_field_name': ('ent_field_name',), 'vec': ('vec',), 'timestamp_value': ('timestamp_value',), 'title': ('title',), 'dict.title': ('dict', 'title'), 'dict.dict.ent_field_name': ('dict', 'dict', 'ent_field_name'), 'dict.dict.label': ('dict', 'dict', 'label'), 'dict.dict.value': ('dict', 'dict', 'value'), 'href': ('dict', 'dict', 'href'), 'dict.dict.title': ('dict', 'dict', 'title'), 'dict.dict.dict.title': ('dict', 'dict', 'dict', 'title'), 'dict.dict.dict.dict.ent_field_name': ('dict', 'dict', 'dict', 'dict', 'ent_field_name'), 'dict.dict.dict.dict.label': ('dict', 'dict', 'dict', 'dict', 'label'), 'dict.dict.dict.dict.value': ('dict', 'dict', 'dict', 'dict', 'value')}}),
    ],
    'Videos Watched (Unchanged)': [
        Entry(table='Videos Watched', filename='ads_information/ads_and_topics/videos_watched.json', static_fields={}, list_blocks={('impressions_history_videos_watched',): {'value': ('string_map_data', 'Author', 'value'), 'timestamp': ('string_map_data', 'Time', 'timestamp')}}),
    ],
    'Who You Ve Followed (Unchanged)': [
        Entry(table='Who You Ve Followed', filename='connections/followers/who_you_ve_followed.json', static_fields={}, list_blocks={('following_v3',): {'name': ('name',), 'timestamp': ('timestamp',)}}),
    ],
    "Who You'Ve Followed (Unchanged)": [
        Entry(table="Who You'Ve Followed", filename="connections/followers/who_you've_followed.json", static_fields={}, list_blocks={('following_v3',): {'name': ('name',), 'timestamp': ('timestamp',)}}),
    ],
    'Your Actions On Violating Content In Your Groups (Unchanged)': [
        Entry(table='Your Actions On Violating Content In Your Groups', filename='your_facebook_activity/groups/your_actions_on_violating_content_in_your_groups.json', static_fields={'media': ('media',), 'fbid': ('fbid',)}, list_blocks={(): {'media': ('media',), 'fbid': ('fbid',)}, ('label_values',): {'label': ('label',)}}),
    ],
    'Your Activity Off Meta Technologies (Original)': [
        Entry(table='Your Activity Off Meta Technologies', filename='apps_and_websites_off_of_facebook/your_activity_off_meta_technologies.json', static_fields={}, list_blocks={('off_facebook_activity_v2',): {'name': ('name',)}, ('off_facebook_activity_v2', 'events'): {'id': ('id',), 'type': ('type',), 'timestamp': ('timestamp',)}, (): {'title': ('title',), 'media': ('media',), 'fbid': ('fbid',)}, ('label_values',): {'label': ('label',)}, ('label_values', 'vec', 'dict'): {'label': ('label',), 'value': ('value',)}}),
    ],
    'Your Activity Off Meta Technologies (Merged)': [
        Entry(table='Your Activity Off Meta Technologies', filename='apps_and_websites_off_of_facebook/your_activity_off_meta_technologies.json', static_fields={}, list_blocks={('off_facebook_activity_v2',): {'name': ('name',), 'id': ('events', 'id'), 'type': ('events', 'type'), 'timestamp': ('events', 'timestamp')}, (): {'title': ('title',), 'media': ('media',), 'fbid': ('fbid',)}, ('label_values',): {'label': ('label',), 'vec.dict.label': ('vec', 'dict', 'label'), 'value': ('vec', 'dict', 'value')}}),
    ],
    'Your Comment Active Days (Unchanged)': [
        Entry(table='Your Comment Active Days', filename='personal_information/profile_information/your_facebook_activity/comments_and_reactions/your_comment_active_days.json', static_fields={'media': ('media',), 'fbid': ('fbid',)}, list_blocks={('label_values',): {'label': ('label',), 'value': ('value',)}}),
        Entry(table='Your Comment Active Days', filename='your_facebook_activity/comments_and_reactions/your_comment_active_days.json', static_fields={'media': ('media',), 'fbid': ('fbid',)}, list_blocks={('label_values',): {'label': ('label',), 'value': ('value',)}}),
    ],
    'Your Comment Edits (Unchanged)': [
        Entry(table='Your Comment Edits', filename='personal_information/profile_information/your_facebook_activity/comments_and_reactions/your_comment_edits.json', static_fields={}, list_blocks={(): {'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',)}, ('label_values',): {'label': ('label',), 'value': ('value',)}}),
        Entry(table='Your Comment Edits', filename='your_facebook_activity/comments_and_reactions/your_comment_edits.json', static_fields={}, list_blocks={(): {'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',)}, ('label_values',): {'label': ('label',), 'value': ('value',)}}),
    ],
    'Your Comments In Groups (Original)': [
        Entry(table='Your Comments In Groups', filename='personal_information/profile_information/your_facebook_activity/groups/your_comments_in_groups.json', static_fields={}, list_blocks={('group_comments_v2',): {'timestamp': ('timestamp',)}, ('group_comments_v2', 'data'): {'timestamp': ('comment', 'timestamp'), 'comment': ('comment', 'comment'), 'group': ('comment', 'group')}}),
        Entry(table='Your Comments In Groups', filename='your_activity_across_facebook/groups/your_comments_in_groups.json', static_fields={}, list_blocks={('group_comments_v2',): {'timestamp': ('timestamp',)}, ('group_comments_v2', 'data'): {'timestamp': ('comment', 'timestamp'), 'comment': ('comment', 'comment'), 'group': ('comment', 'group')}}),
        Entry(table='Your Comments In Groups', filename='your_facebook_activity/groups/your_comments_in_groups.json', static_fields={}, list_blocks={('group_comments_v2',): {'timestamp': ('timestamp',)}, ('group_comments_v2', 'data'): {'timestamp': ('comment', 'timestamp'), 'comment': ('comment', 'comment'), 'group': ('comment', 'group')}}),
    ],
    'Your Comments In Groups (Merged)': [
        Entry(table='Your Comments In Groups', filename='personal_information/profile_information/your_facebook_activity/groups/your_comments_in_groups.json', static_fields={}, list_blocks={('group_comments_v2',): {'timestamp': ('timestamp',), 'data.timestamp': ('data', 'comment', 'timestamp'), 'comment': ('data', 'comment', 'comment'), 'group': ('data', 'comment', 'group')}}),
        Entry(table='Your Comments In Groups', filename='your_activity_across_facebook/groups/your_comments_in_groups.json', static_fields={}, list_blocks={('group_comments_v2',): {'timestamp': ('timestamp',), 'data.timestamp': ('data', 'comment', 'timestamp'), 'comment': ('data', 'comment', 'comment'), 'group': ('data', 'comment', 'group')}}),
        Entry(table='Your Comments In Groups', filename='your_facebook_activity/groups/your_comments_in_groups.json', static_fields={}, list_blocks={('group_comments_v2',): {'timestamp': ('timestamp',), 'data.timestamp': ('data', 'comment', 'timestamp'), 'comment': ('data', 'comment', 'comment'), 'group': ('data', 'comment', 'group')}}),
    ],
    'Your Consent Settings (Unchanged)': [
        Entry(table='Your Consent Settings', filename='ads_information/your_consent_settings.json', static_fields={'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',)}, list_blocks={('label_values',): {'label': ('label',), 'timestamp_value': ('timestamp_value',)}}),
    ],
    'Your Facebook Watch Activity In The Last 28 Days (Unchanged)': [
        Entry(table='Your Facebook Watch Activity In The Last 28 Days', filename='logged_information/other_logged_information/your_facebook_watch_activity_in_the_last_28_days.json', static_fields={'media': ('media',), 'fbid': ('fbid',), 'ent_name': ('ent_name',)}, list_blocks={('label_values',): {'label': ('label',), 'value': ('value',), 'ent_field_name': ('ent_field_name',)}}),
    ],
    'Your Friends (Unchanged)': [
        Entry(table='Your Friends', filename='connections/friends/your_friends.json', static_fields={}, list_blocks={('friends_v2',): {'name': ('name',), 'timestamp': ('timestamp',)}}),
    ],
    'Your Group Membership Activity (Original)': [
        Entry(table='Your Group Membership Activity', filename='personal_information/profile_information/your_facebook_activity/groups/your_group_membership_activity.json', static_fields={}, list_blocks={('groups_joined_v2',): {'timestamp': ('timestamp',), 'title': ('title',)}, ('groups_joined_v2', 'data'): {'name': ('name',)}}),
        Entry(table='Your Group Membership Activity', filename='your_activity_across_facebook/groups/your_group_membership_activity.json', static_fields={}, list_blocks={('groups_joined_v2',): {'timestamp': ('timestamp',), 'title': ('title',)}, ('groups_joined_v2', 'data'): {'name': ('name',)}}),
        Entry(table='Your Group Membership Activity', filename='your_facebook_activity/groups/your_group_membership_activity.json', static_fields={}, list_blocks={('groups_joined_v2',): {'timestamp': ('timestamp',), 'title': ('title',)}, ('groups_joined_v2', 'data'): {'name': ('name',)}}),
    ],
    'Your Group Membership Activity (Merged)': [
        Entry(table='Your Group Membership Activity', filename='personal_information/profile_information/your_facebook_activity/groups/your_group_membership_activity.json', static_fields={}, list_blocks={('groups_joined_v2',): {'timestamp': ('timestamp',), 'title': ('title',), 'name': ('data', 'name')}}),
        Entry(table='Your Group Membership Activity', filename='your_activity_across_facebook/groups/your_group_membership_activity.json', static_fields={}, list_blocks={('groups_joined_v2',): {'timestamp': ('timestamp',), 'title': ('title',), 'name': ('data', 'name')}}),
        Entry(table='Your Group Membership Activity', filename='your_facebook_activity/groups/your_group_membership_activity.json', static_fields={}, list_blocks={('groups_joined_v2',): {'timestamp': ('timestamp',), 'title': ('title',), 'name': ('data', 'name')}}),
    ],
    'Your Groups (Unchanged)': [
        Entry(table='Your Groups', filename='your_activity_across_facebook/groups/your_groups.json', static_fields={}, list_blocks={('groups_admined_v2',): {'name': ('name',), 'timestamp': ('timestamp',)}}),
        Entry(table='Your Groups', filename='your_facebook_activity/groups/your_groups.json', static_fields={}, list_blocks={('groups_admined_v2',): {'name': ('name',), 'timestamp': ('timestamp',)}}),
    ],
    'Your Information Download Requests (Unchanged)': [
        Entry(table='Your Information Download Requests', filename='personal_information/profile_information/your_facebook_activity/other_activity/your_information_download_requests.json', static_fields={'timestamp': ('timestamp',)}, list_blocks={}),
        Entry(table='Your Information Download Requests', filename='your_facebook_activity/other_activity/your_information_download_requests.json', static_fields={'timestamp': ('timestamp',)}, list_blocks={(): {'timestamp': ('timestamp',)}}),
    ],
    'Your Pages (Unchanged)': [
        Entry(table='Your Pages', filename='your_facebook_activity/pages/your_pages.json', static_fields={}, list_blocks={('pages_v2',): {'name': ('name',), 'timestamp': ('timestamp',), 'url': ('url',)}}),
    ],
    'Your Pages Mentions (Unchanged)': [
        Entry(table='Your Pages Mentions', filename='ads_information/your_pages_mentions.json', static_fields={}, list_blocks={(): {'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',)}, ('label_values',): {'label': ('label',), 'vec': ('vec',)}}),
    ],
    'Your Post Audiences (Unchanged)': [
        Entry(table='Your Post Audiences', filename='connections/friends/your_post_audiences.json', static_fields={}, list_blocks={(): {'media': ('media',), 'fbid': ('fbid',), 'ent_name': ('ent_name',)}, ('label_values',): {'label': ('label',), 'value': ('value',), 'ent_field_name': ('ent_field_name',), 'dict': ('dict',), 'title': ('title',)}}),
    ],
    'Your Posts  Check Ins  Photos And Videos 1 (Unchanged)': [
        Entry(table='Your Posts  Check Ins  Photos And Videos 1', filename='personal_information/profile_information/your_facebook_activity/posts/your_posts__check_ins__photos_and_videos_1.json', static_fields={}, list_blocks={(): {'timestamp': ('timestamp',), 'title': ('title',)}, ('data',): {'update_timestamp': ('update_timestamp',)}, ('attachments', 'data'): {'url': ('external_context', 'url')}}),
        Entry(table='Your Posts  Check Ins  Photos And Videos 1', filename='your_activity_across_facebook/posts/your_posts__check_ins__photos_and_videos_1.json', static_fields={}, list_blocks={(): {'timestamp': ('timestamp',), 'title': ('title',)}, ('data',): {'post': ('post',)}, ('attachments', 'data'): {'url': ('external_context', 'url')}}),
        Entry(table='Your Posts  Check Ins  Photos And Videos 1', filename='your_facebook_activity/posts/your_posts__check_ins__photos_and_videos_1.json', static_fields={}, list_blocks={(): {'timestamp': ('timestamp',), 'title': ('title',)}, ('data',): {'update_timestamp': ('update_timestamp',), 'post': ('post',), 'backdated_timestamp': ('backdated_timestamp',)}, ('attachments', 'data'): {'url': ('external_context', 'url'), 'name': ('external_context', 'name'), 'source': ('external_context', 'source'), 'title': ('life_event', 'title'), 'year': ('life_event', 'start_date', 'year'), 'month': ('life_event', 'start_date', 'month'), 'day': ('life_event', 'start_date', 'day')}}),
    ],
    'Your Preferred Categories (Original)': [
        Entry(table='Your Preferred Categories', filename='preferences/preferences/your_preferred_categories.json', static_fields={'media': ('media',), 'fbid': ('fbid',), 'ent_name': ('ent_name',)}, list_blocks={('label_values',): {'ent_field_name': ('ent_field_name',), 'label': ('label',)}, ('label_values', 'vec'): {'ent_field_name': ('ent_field_name',)}, ('label_values', 'vec', 'dict'): {'ent_field_name': ('ent_field_name',), 'label': ('label',), 'value': ('value',)}}),
    ],
    'Your Preferred Categories (Merged)': [
        Entry(table='Your Preferred Categories', filename='preferences/preferences/your_preferred_categories.json', static_fields={'media': ('media',), 'fbid': ('fbid',), 'ent_name': ('ent_name',)}, list_blocks={('label_values',): {'ent_field_name': ('ent_field_name',), 'label': ('label',), 'vec.ent_field_name': ('vec', 'ent_field_name'), 'vec.dict.ent_field_name': ('vec', 'dict', 'ent_field_name'), 'vec.dict.label': ('vec', 'dict', 'label'), 'value': ('vec', 'dict', 'value')}}),
    ],
    'Your Recent Reported Conversions (Unchanged)': [
        Entry(table='Your Recent Reported Conversions', filename='ads_information/your_recent_reported_conversions.json', static_fields={'media': ('media',)}, list_blocks={(): {'media': ('media',), 'fbid': ('fbid',), 'ent_name': ('ent_name',)}, ('label_values',): {'label': ('label',), 'timestamp_value': ('timestamp_value',), 'ent_field_name': ('ent_field_name',)}}),
    ],
    'Your Recently Followed History (Original)': [
        Entry(table='Your Recently Followed History', filename='personal_information/profile_information/your_facebook_activity/other_activity/your_recently_followed_history.json', static_fields={'media': ('media',), 'fbid': ('fbid',)}, list_blocks={('label_values',): {'label': ('label',)}, ('label_values', 'vec', 'dict'): {'label': ('label',), 'value': ('value',)}}),
        Entry(table='Your Recently Followed History', filename='your_activity_across_facebook/other_activity/your_recently_followed_history.json', static_fields={'media': ('media',)}, list_blocks={('label_values',): {'label': ('label',)}, ('label_values', 'vec', 'dict'): {'label': ('label',), 'value': ('value',)}}),
        Entry(table='Your Recently Followed History', filename='your_facebook_activity/other_activity/your_recently_followed_history.json', static_fields={'media': ('media',), 'fbid': ('fbid',), 'ent_name': ('ent_name',)}, list_blocks={('label_values',): {'label': ('label',), 'ent_field_name': ('ent_field_name',)}, ('label_values', 'vec', 'dict'): {'label': ('label',), 'value': ('value',)}}),
    ],
    'Your Recently Followed History (Merged)': [
        Entry(table='Your Recently Followed History', filename='personal_information/profile_information/your_facebook_activity/other_activity/your_recently_followed_history.json', static_fields={'media': ('media',), 'fbid': ('fbid',)}, list_blocks={('label_values',): {'label': ('label',), 'vec.dict.label': ('vec', 'dict', 'label'), 'value': ('vec', 'dict', 'value')}}),
        Entry(table='Your Recently Followed History', filename='your_activity_across_facebook/other_activity/your_recently_followed_history.json', static_fields={'media': ('media',)}, list_blocks={('label_values',): {'label': ('label',), 'vec.dict.label': ('vec', 'dict', 'label'), 'value': ('vec', 'dict', 'value')}}),
        Entry(table='Your Recently Followed History', filename='your_facebook_activity/other_activity/your_recently_followed_history.json', static_fields={'media': ('media',), 'fbid': ('fbid',), 'ent_name': ('ent_name',)}, list_blocks={('label_values',): {'label': ('label',), 'ent_field_name': ('ent_field_name',), 'vec.dict.label': ('vec', 'dict', 'label'), 'value': ('vec', 'dict', 'value')}}),
    ],
    'Your Saved Items (Original)': [
        Entry(table='Your Saved Items', filename='personal_information/profile_information/your_facebook_activity/saved_items_and_collections/your_saved_items.json', static_fields={}, list_blocks={('saves_v2',): {'timestamp': ('timestamp',), 'title': ('title',)}, ('saves_v2', 'attachments', 'data'): {'name': ('external_context', 'name'), 'source': ('external_context', 'source'), 'url': ('external_context', 'url')}}),
        Entry(table='Your Saved Items', filename='your_facebook_activity/saved_items_and_collections/your_saved_items.json', static_fields={}, list_blocks={('saves_v2',): {'timestamp': ('timestamp',), 'title': ('title',)}}),
    ],
    'Your Saved Items (Merged)': [
        Entry(table='Your Saved Items', filename='personal_information/profile_information/your_facebook_activity/saved_items_and_collections/your_saved_items.json', static_fields={}, list_blocks={('saves_v2',): {'timestamp': ('timestamp',), 'title': ('title',), 'name': ('attachments', 'data', 'external_context', 'name'), 'source': ('attachments', 'data', 'external_context', 'source'), 'url': ('attachments', 'data', 'external_context', 'url')}}),
        Entry(table='Your Saved Items', filename='your_facebook_activity/saved_items_and_collections/your_saved_items.json', static_fields={}, list_blocks={('saves_v2',): {'timestamp': ('timestamp',), 'title': ('title',)}}),
    ],
    'Your Search History (Original)': [
        Entry(table='Your Search History', filename='logged_information/search/your_search_history.json', static_fields={}, list_blocks={('searches_v2',): {'timestamp': ('timestamp',), 'title': ('title',)}, ('searches_v2', 'data'): {'text': ('text',)}, ('searches_v2', 'attachments', 'data'): {'text': ('text',)}}),
    ],
    'Your Search History (Merged)': [
        Entry(table='Your Search History', filename='logged_information/search/your_search_history.json', static_fields={}, list_blocks={('searches_v2',): {'timestamp': ('timestamp',), 'title': ('title',), 'text': ('data', 'text'), 'attachments.data.text': ('attachments', 'data', 'text')}}),
    ],
    'Your Story Highlights (Unchanged)': [
        Entry(table='Your Story Highlights', filename='personal_information/profile_information/preferences/preferences/your_story_highlights.json', static_fields={'media': ('media',), 'fbid': ('fbid',)}, list_blocks={('label_values',): {'label': ('label',), 'value': ('value',)}}),
        Entry(table='Your Story Highlights', filename='preferences/preferences/your_story_highlights.json', static_fields={'media': ('media',), 'fbid': ('fbid',)}, list_blocks={('label_values',): {'label': ('label',), 'value': ('value',)}}),
    ],
    'Your Video Consumption Summary (Unchanged)': [
        Entry(table='Your Video Consumption Summary', filename='personal_information/profile_information/your_facebook_activity/other_activity/your_video_consumption_summary.json', static_fields={'media': ('media',), 'fbid': ('fbid',)}, list_blocks={('label_values',): {'label': ('label',)}}),
        Entry(table='Your Video Consumption Summary', filename='your_facebook_activity/other_activity/your_video_consumption_summary.json', static_fields={'media': ('media',), 'fbid': ('fbid',), 'ent_name': ('ent_name',)}, list_blocks={('label_values',): {'label': ('label',), 'ent_field_name': ('ent_field_name',), 'value': ('value',)}}),
    ],
    'Your Videos (Original)': [
        Entry(table='Your Videos', filename='personal_information/profile_information/your_facebook_activity/posts/your_videos.json', static_fields={}, list_blocks={('videos_v2',): {'uri': ('uri',), 'creation_timestamp': ('creation_timestamp',), 'title': ('title',), 'description': ('description',), 'dubbing_info': ('dubbing_info',), 'media_variants': ('media_variants',)}, ('videos_v2', 'media_metadata', 'video_metadata', 'exif_data'): {'upload_ip': ('upload_ip',), 'upload_timestamp': ('upload_timestamp',)}}),
        Entry(table='Your Videos', filename='your_facebook_activity/posts/your_videos.json', static_fields={}, list_blocks={('videos_v2',): {'uri': ('uri',), 'creation_timestamp': ('creation_timestamp',), 'title': ('title',), 'description': ('description',), 'dubbing_info': ('dubbing_info',), 'media_variants': ('media_variants',)}, ('videos_v2', 'media_metadata', 'video_metadata', 'exif_data'): {'upload_ip': ('upload_ip',), 'upload_timestamp': ('upload_timestamp',)}}),
    ],
    'Your Videos (Merged)': [
        Entry(table='Your Videos', filename='personal_information/profile_information/your_facebook_activity/posts/your_videos.json', static_fields={}, list_blocks={('videos_v2',): {'uri': ('uri',), 'creation_timestamp': ('creation_timestamp',), 'title': ('title',), 'description': ('description',), 'dubbing_info': ('dubbing_info',), 'media_variants': ('media_variants',), 'upload_ip': ('media_metadata', 'video_metadata', 'exif_data', 'upload_ip'), 'upload_timestamp': ('media_metadata', 'video_metadata', 'exif_data', 'upload_timestamp')}}),
        Entry(table='Your Videos', filename='your_facebook_activity/posts/your_videos.json', static_fields={}, list_blocks={('videos_v2',): {'uri': ('uri',), 'creation_timestamp': ('creation_timestamp',), 'title': ('title',), 'description': ('description',), 'dubbing_info': ('dubbing_info',), 'media_variants': ('media_variants',), 'upload_ip': ('media_metadata', 'video_metadata', 'exif_data', 'upload_ip'), 'upload_timestamp': ('media_metadata', 'video_metadata', 'exif_data', 'upload_timestamp')}}),
    ],
    'Your Watch Settings (Unchanged)': [
        Entry(table='Your Watch Settings', filename='personal_information/profile_information/preferences/preferences/your_watch_settings.json', static_fields={'media': ('media',), 'fbid': ('fbid',)}, list_blocks={('label_values',): {'label': ('label',), 'value': ('value',)}}),
        Entry(table='Your Watch Settings', filename='preferences/preferences/your_watch_settings.json', static_fields={'media': ('media',), 'fbid': ('fbid',), 'ent_name': ('ent_name',)}, list_blocks={('label_values',): {'label': ('label',), 'value': ('value',), 'ent_field_name': ('ent_field_name',), 'vec': ('vec',), 'timestamp_value': ('timestamp_value',)}}),
    ],
}

