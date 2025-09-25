"""
Donation file structure data for takeout flows

This file contains a list of Entries for each platform.
Each Entry represents a table to be generated from the appropriate file.

To generate this file, please run structure/flow_generation/generate_entries.py
which will use the Merged_structures_*.csv to determine the required entries.
"""

from port.helpers.parsers import Entry

X_ENTRIES: dict[str, list[Entry]] = {
    'Account-Label.Js': [
        Entry(table='Account-Label.Js', filename='data/account-label.js', static_fields={'accountLabel': ('accountLabel',)}, list_blocks={}),
    ],
    'Account-Suspension.Js': [
        Entry(table='Account-Suspension.Js', filename='data/account-suspension.js', static_fields={'No data': ('No data',)}, list_blocks={}),
    ],
    'Account.Js': [
        Entry(table='Account.Js', filename='data/account.js', static_fields={'accountId': ('account', 'accountId'), 'createdAt': ('account', 'createdAt')}, list_blocks={}),
    ],
    'Ad-Engagements.Js': [
        Entry(table='Ad-Engagements.Js', filename='data/ad-engagements.js', static_fields={'displayLocation': ('ad', 'adsUserData', 'adEngagements', 'engagements', 'impressionAttributes', 'displayLocation'), 'tweetId': ('ad', 'adsUserData', 'adEngagements', 'engagements', 'impressionAttributes', 'promotedTweetInfo', 'tweetId'), 'tweetText': ('ad', 'adsUserData', 'adEngagements', 'engagements', 'impressionAttributes', 'promotedTweetInfo', 'tweetText'), 'advertiserName': ('ad', 'adsUserData', 'adEngagements', 'engagements', 'impressionAttributes', 'advertiserInfo', 'advertiserName'), 'screenName': ('ad', 'adsUserData', 'adEngagements', 'engagements', 'impressionAttributes', 'publisherInfo', 'screenName'), 'targetingType': ('ad', 'adsUserData', 'adEngagements', 'engagements', 'impressionAttributes', 'matchedTargetingCriteria', 'targetingType'), 'targetingValue': ('ad', 'adsUserData', 'adEngagements', 'engagements', 'impressionAttributes', 'matchedTargetingCriteria', 'targetingValue'), 'impressionTime': ('ad', 'adsUserData', 'adEngagements', 'engagements', 'impressionAttributes', 'impressionTime'), 'engagementTime': ('ad', 'adsUserData', 'adEngagements', 'engagements', 'engagementAttributes', 'engagementTime'), 'engagementType': ('ad', 'adsUserData', 'adEngagements', 'engagements', 'engagementAttributes', 'engagementType'), 'trendId': ('ad', 'adsUserData', 'adEngagements', 'engagements', 'impressionAttributes', 'promotedTrendInfo', 'trendId'), 'name': ('ad', 'adsUserData', 'adEngagements', 'engagements', 'impressionAttributes', 'promotedTrendInfo', 'name'), 'description': ('ad', 'adsUserData', 'adEngagements', 'engagements', 'impressionAttributes', 'promotedTrendInfo', 'description'), 'publisherName': ('ad', 'adsUserData', 'adEngagements', 'engagements', 'impressionAttributes', 'publisherInfo', 'publisherName')}, list_blocks={('ad', 'adsUserData', 'adEngagements', 'engagements', 'impressionAttributes', 'promotedTweetInfo'): {'mediaUrls': ('mediaUrls',), 'urls': ('urls',)}}),
    ],
    'Ad-Impressions.Js': [
        Entry(table='Ad-Impressions.Js', filename='data/ad-impressions.js', static_fields={'No data': ('No data',)}, list_blocks={}),
    ],
    'Ad-Mobile-Conversions-Attributed.Js': [
        Entry(table='Ad-Mobile-Conversions-Attributed.Js', filename='data/ad-mobile-conversions-attributed.js', static_fields={'No data': ('No data',)}, list_blocks={}),
    ],
    'Ad-Mobile-Conversions-Unattributed.Js': [
        Entry(table='Ad-Mobile-Conversions-Unattributed.Js', filename='data/ad-mobile-conversions-unattributed.js', static_fields={'No data': ('No data',)}, list_blocks={}),
    ],
    'Ad-Online-Conversions-Attributed.Js': [
        Entry(table='Ad-Online-Conversions-Attributed.Js', filename='data/ad-online-conversions-attributed.js', static_fields={'No data': ('No data',)}, list_blocks={}),
    ],
    'Ad-Online-Conversions-Unattributed.Js': [
        Entry(table='Ad-Online-Conversions-Unattributed.Js', filename='data/ad-online-conversions-unattributed.js', static_fields={'No data': ('No data',)}, list_blocks={}),
    ],
    'Article-Metadata.Js': [
        Entry(table='Article-Metadata.Js', filename='data/article-metadata.js', static_fields={'No data': ('No data',)}, list_blocks={}),
    ],
    'Article.Js': [
        Entry(table='Article.Js', filename='data/article.js', static_fields={'No data': ('No data',)}, list_blocks={}),
    ],
    'Block.Js': [
        Entry(table='Block.Js', filename='data/block.js', static_fields={'No data': ('No data',)}, list_blocks={}),
    ],
    'Community-Note-Batsignal.Js': [
        Entry(table='Community-Note-Batsignal.Js', filename='data/community-note-batsignal.js', static_fields={'No data': ('No data',)}, list_blocks={}),
    ],
    'Community-Note-Rating.Js': [
        Entry(table='Community-Note-Rating.Js', filename='data/community-note-rating.js', static_fields={'noteId': ('communityNoteRating', 'noteId'), 'helpfulnessLevel': ('communityNoteRating', 'helpfulnessLevel'), 'createdAt': ('communityNoteRating', 'createdAt'), 'userId': ('communityNoteRating', 'userId')}, list_blocks={('communityNoteRating',): {'helpfulTags': ('helpfulTags',)}}),
    ],
    'Community-Note-Tombstone.Js': [
        Entry(table='Community-Note-Tombstone.Js', filename='data/community-note-tombstone.js', static_fields={'No data': ('No data',)}, list_blocks={}),
    ],
    'Community-Note.Js': [
        Entry(table='Community-Note.Js', filename='data/community-note.js', static_fields={'No data': ('No data',)}, list_blocks={}),
    ],
    'Community-Tweet.Js': [
        Entry(table='Community-Tweet.Js', filename='data/community-tweet.js', static_fields={'No data': ('No data',)}, list_blocks={}),
    ],
    'Follower.Js': [
        Entry(table='Follower.Js', filename='data/follower.js', static_fields={'accountId': ('follower', 'accountId'), 'userLink': ('follower', 'userLink')}, list_blocks={}),
    ],
    'Following.Js': [
        Entry(table='Following.Js', filename='data/following.js', static_fields={'accountId': ('following', 'accountId'), 'userLink': ('following', 'userLink')}, list_blocks={}),
    ],
    'Grok-Chat-Item.Js': [
        Entry(table='Grok-Chat-Item.Js', filename='data/grok-chat-item.js', static_fields={'No data': ('No data',)}, list_blocks={}),
    ],
    'Like.Js': [
        Entry(table='Like.Js', filename='data/like.js', static_fields={'tweetId': ('like', 'tweetId'), 'fullText': ('like', 'fullText'), 'expandedUrl': ('like', 'expandedUrl')}, list_blocks={}),
    ],
    'Lists-Created.Js': [
        Entry(table='Lists-Created.Js', filename='data/lists-created.js', static_fields={'No data': ('No data',), 'url': ('userListInfo', 'url')}, list_blocks={}),
    ],
    'Lists-Member.Js': [
        Entry(table='Lists-Member.Js', filename='data/lists-member.js', static_fields={'No data': ('No data',), 'url': ('userListInfo', 'url')}, list_blocks={}),
    ],
    'Lists-Subscribed.Js': [
        Entry(table='Lists-Subscribed.Js', filename='data/lists-subscribed.js', static_fields={'No data': ('No data',), 'url': ('userListInfo', 'url')}, list_blocks={}),
    ],
    'Manifest.Js': [
        Entry(table='Manifest.Js', filename='data/manifest.js', static_fields={'generationDate': ('archiveInfo', 'generationDate')}, list_blocks={}),
    ],
    'Moment.Js': [
        Entry(table='Moment.Js', filename='data/moment.js', static_fields={'No data': ('No data',)}, list_blocks={}),
    ],
    'Mute.Js': [
        Entry(table='Mute.Js', filename='data/mute.js', static_fields={'No data': ('No data',)}, list_blocks={}),
    ],
    'Note-Tweet.Js': [
        Entry(table='Note-Tweet.Js', filename='data/note-tweet.js', static_fields={'No data': ('No data',)}, list_blocks={}),
    ],
    'Personalization.Js': [
        Entry(table='Personalization.Js', filename='data/personalization.js', static_fields={'language': ('p13nData', 'demographics', 'languages', 'language'), 'isDisabled': ('p13nData', 'interests', 'interests', 'isDisabled'), 'gender': ('p13nData', 'demographics', 'genderInfo', 'gender'), 'name': ('p13nData', 'interests', 'interests', 'name'), 'numAudiences': ('p13nData', 'interests', 'audienceAndAdvertisers', 'numAudiences'), 'birthDate': ('p13nData', 'inferredAgeInfo', 'birthDate')}, list_blocks={('p13nData', 'interests', 'audienceAndAdvertisers'): {'lookalikeAdvertisers': ('lookalikeAdvertisers',), 'advertisers': ('advertisers',)}, ('p13nData', 'interests'): {'shows': ('shows',)}, ('p13nData', 'inferredAgeInfo'): {'age': ('age',)}}),
    ],
    'Professional-Data.Js': [
        Entry(table='Professional-Data.Js', filename='data/professional-data.js', static_fields={'No data': ('No data',)}, list_blocks={}),
    ],
    'Protected-History.Js': [
        Entry(table='Protected-History.Js', filename='data/protected-history.js', static_fields={'No data': ('No data',)}, list_blocks={}),
    ],
    'Reply-Prompt.Js': [
        Entry(table='Reply-Prompt.Js', filename='data/reply-prompt.js', static_fields={'No data': ('No data',)}, list_blocks={}),
    ],
    'Saved-Search.Js': [
        Entry(table='Saved-Search.Js', filename='data/saved-search.js', static_fields={'savedSearchId': ('savedSearch', 'savedSearchId'), 'query': ('savedSearch', 'query')}, list_blocks={}),
    ],
    'Smartblock.Js': [
        Entry(table='Smartblock.Js', filename='data/smartblock.js', static_fields={'No data': ('No data',)}, list_blocks={}),
    ],
    'Spaces-Metadata.Js': [
        Entry(table='Spaces-Metadata.Js', filename='data/spaces-metadata.js', static_fields={'No data': ('No data',)}, list_blocks={}),
    ],
    'Tweet-Headers.Js': [
        Entry(table='Tweet-Headers.Js', filename='data/tweet-headers.js', static_fields={'user_id': ('tweet', 'user_id')}, list_blocks={}),
    ],
    'Tweetdeck.Js': [
        Entry(table='Tweetdeck.Js', filename='data/tweetdeck.js', static_fields={'No data': ('No data',)}, list_blocks={}),
    ],
    'Tweets.Js': [
        Entry(table='Tweets.Js', filename='data/tweets.js', static_fields={'editableUntil': ('tweet', 'edit_info', 'initial', 'editableUntil'), 'editsRemaining': ('tweet', 'edit_info', 'initial', 'editsRemaining'), 'isEditEligible': ('tweet', 'edit_info', 'initial', 'isEditEligible'), 'retweeted': ('tweet', 'retweeted'), 'source': ('tweet', 'source'), 'url': ('tweet', 'entities', 'urls', 'url'), 'expanded_url': ('tweet', 'entities', 'urls', 'expanded_url'), 'display_url': ('tweet', 'entities', 'urls', 'display_url'), 'favorite_count': ('tweet', 'favorite_count'), 'id_str': ('tweet', 'entities', 'user_mentions', 'id_str'), 'truncated': ('tweet', 'truncated'), 'retweet_count': ('tweet', 'retweet_count'), 'id': ('tweet', 'entities', 'user_mentions', 'id'), 'possibly_sensitive': ('tweet', 'possibly_sensitive'), 'created_at': ('tweet', 'created_at'), 'favorited': ('tweet', 'favorited'), 'full_text': ('tweet', 'full_text'), 'lang': ('tweet', 'lang'), 'name': ('tweet', 'entities', 'user_mentions', 'name'), 'screen_name': ('tweet', 'entities', 'user_mentions', 'screen_name'), 'in_reply_to_status_id_str': ('tweet', 'in_reply_to_status_id_str'), 'in_reply_to_user_id': ('tweet', 'in_reply_to_user_id'), 'in_reply_to_status_id': ('tweet', 'in_reply_to_status_id'), 'in_reply_to_screen_name': ('tweet', 'in_reply_to_screen_name'), 'in_reply_to_user_id_str': ('tweet', 'in_reply_to_user_id_str'), 'text': ('tweet', 'entities', 'hashtags', 'text'), 'media_url_https': ('tweet', 'entities', 'media', 'media_url_https'), 'source_status_id_str': ('tweet', 'entities', 'media', 'source_status_id_str')}, list_blocks={('tweet', 'edit_info', 'initial'): {'editTweetIds': ('editTweetIds',)}, ('tweet', 'entities', 'urls'): {'indices': ('indices',)}, ('tweet',): {'display_text_range': ('display_text_range',)}, ('tweet', 'entities', 'user_mentions'): {'indices': ('indices',)}, ('tweet', 'entities', 'hashtags'): {'indices': ('indices',)}}),
    ],
    'User-Link-Clicks.Js': [
        Entry(table='User-Link-Clicks.Js', filename='data/user-link-clicks.js', static_fields={'No data': ('No data',)}, list_blocks={}),
    ],
    'Verified-Organization.Js': [
        Entry(table='Verified-Organization.Js', filename='data/verified-organization.js', static_fields={'verifiedOrganization': ('verifiedOrganization',)}, list_blocks={}),
    ],
    'Verified.Js': [
        Entry(table='Verified.Js', filename='data/verified.js', static_fields={'verified': ('verified', 'verified')}, list_blocks={}),
    ],
}

IG_ENTRIES: dict[str, list[Entry]] = {
    'Ads About Meta': [
        Entry(table='Ads About Meta', filename='ads_information/instagram_ads_and_businesses/ads_about_meta.json', static_fields={'media': ('media',), 'fbid': ('fbid',), 'ent_name': ('ent_name',)}, list_blocks={('label_values',): {'ent_field_name': ('ent_field_name',), 'label': ('label',), 'value': ('value',), 'timestamp_value': ('timestamp_value',)}}),
    ],
    'Ads Clicked': [
        Entry(table='Ads Clicked', filename='ads_information/ads_and_topics/ads_clicked.json', static_fields={}, list_blocks={('impressions_history_ads_clicked',): {'title': ('title',)}, ('impressions_history_ads_clicked', 'string_list_data'): {'timestamp': ('timestamp',)}}),
    ],
    'Ads Viewed': [
        Entry(table='Ads Viewed', filename='ads_information/ads_and_topics/ads_viewed.json', static_fields={}, list_blocks={('impressions_history_ads_seen',): {'value': ('string_map_data', 'Author', 'value'), 'timestamp': ('string_map_data', 'Time', 'timestamp')}}),
    ],
    'Advertisers Using Your Activity Or Information': [
        Entry(table='Advertisers Using Your Activity Or Information', filename='ads_information/instagram_ads_and_businesses/advertisers_using_your_activity_or_information.json', static_fields={}, list_blocks={('ig_custom_audiences_all_types',): {'advertiser_name': ('advertiser_name',), 'has_data_file_custom_audience': ('has_data_file_custom_audience',), 'has_remarketing_custom_audience': ('has_remarketing_custom_audience',), 'has_in_person_store_visit': ('has_in_person_store_visit',)}}),
    ],
    'Blocked Profiles': [
        Entry(table='Blocked Profiles', filename='connections/followers_and_following/blocked_profiles.json', static_fields={}, list_blocks={('relationships_blocked_users',): {'title': ('title',)}, ('relationships_blocked_users', 'string_list_data'): {'href': ('href',), 'timestamp': ('timestamp',)}}),
    ],
    'Close Friends': [
        Entry(table='Close Friends', filename='connections/followers_and_following/close_friends.json', static_fields={}, list_blocks={('relationships_close_friends',): {'title': ('title',), 'media_list_data': ('media_list_data',)}, ('relationships_close_friends', 'string_list_data'): {'href': ('href',), 'value': ('value',), 'timestamp': ('timestamp',)}}),
    ],
    'Comments Allowed From': [
        Entry(table='Comments Allowed From', filename='preferences/media_settings/comments_allowed_from.json', static_fields={}, list_blocks={('settings_allow_comments_from',): {'title': ('title',), 'href': ('string_map_data', 'Comments Allowed From', 'href'), 'value': ('string_map_data', 'Comments Allowed From', 'value'), 'timestamp': ('string_map_data', 'Comments Allowed From', 'timestamp')}}),
        Entry(table='Comments Allowed From', filename='preferences/settings/comments_allowed_from.json', static_fields={}, list_blocks={('settings_allow_comments_from',): {'title': ('title',), 'href': ('string_map_data', 'Comments Allowed From', 'href'), 'value': ('string_map_data', 'Comments Allowed From', 'value'), 'timestamp': ('string_map_data', 'Comments Allowed From', 'timestamp')}}),
    ],
    'Consents': [
        Entry(table='Consents', filename='preferences/media_settings/consents.json', static_fields={'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',), 'ent_name': ('ent_name',)}, list_blocks={('label_values',): {'ent_field_name': ('ent_field_name',), 'label': ('label',), 'timestamp_value': ('timestamp_value',)}}),
        Entry(table='Consents', filename='preferences/settings/consents.json', static_fields={'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',), 'ent_name': ('ent_name',)}, list_blocks={('label_values',): {'ent_field_name': ('ent_field_name',), 'label': ('label',), 'timestamp_value': ('timestamp_value',)}}),
    ],
    'Emoji Sliders': [
        Entry(table='Emoji Sliders', filename='your_instagram_activity/story_sticker_interactions/emoji_sliders.json', static_fields={}, list_blocks={('story_activities_emoji_sliders',): {'title': ('title',)}, ('story_activities_emoji_sliders', 'string_list_data'): {'value': ('value',), 'timestamp': ('timestamp',)}}),
    ],
    "Follow Requests You'Ve Received": [
        Entry(table="Follow Requests You'Ve Received", filename="connections/followers_and_following/follow_requests_you've_received.json", static_fields={}, list_blocks={('relationships_follow_requests_received',): {'title': ('title',), 'media_list_data': ('media_list_data',)}, ('relationships_follow_requests_received', 'string_list_data'): {'href': ('href',), 'value': ('value',), 'timestamp': ('timestamp',)}}),
    ],
    'Followers 1': [
        Entry(table='Followers 1', filename='connections/followers_and_following/followers_1.json', static_fields={'title': ('title',), 'media_list_data': ('media_list_data',)}, list_blocks={('string_list_data',): {'href': ('href',), 'value': ('value',), 'timestamp': ('timestamp',)}, (): {'title': ('title',), 'media_list_data': ('media_list_data',)}}),
    ],
    'Following': [
        Entry(table='Following', filename='connections/followers_and_following/following.json', static_fields={}, list_blocks={('relationships_following',): {'title': ('title',), 'media_list_data': ('media_list_data',)}, ('relationships_following', 'string_list_data'): {'href': ('href',), 'value': ('value',), 'timestamp': ('timestamp',)}}),
    ],
    'Following Hashtags': [
        Entry(table='Following Hashtags', filename='connections/followers_and_following/following_hashtags.json', static_fields={}, list_blocks={('relationships_following_hashtags',): {'title': ('title',), 'media_list_data': ('media_list_data',)}, ('relationships_following_hashtags', 'string_list_data'): {'href': ('href',), 'value': ('value',), 'timestamp': ('timestamp',)}}),
    ],
    'Liked Comments': [
        Entry(table='Liked Comments', filename='your_instagram_activity/likes/liked_comments.json', static_fields={}, list_blocks={('likes_comment_likes',): {'title': ('title',)}, ('likes_comment_likes', 'string_list_data'): {'href': ('href',), 'value': ('value',), 'timestamp': ('timestamp',)}}),
    ],
    'Liked Posts': [
        Entry(table='Liked Posts', filename='your_instagram_activity/likes/liked_posts.json', static_fields={}, list_blocks={('likes_media_likes',): {'title': ('title',)}, ('likes_media_likes', 'string_list_data'): {'href': ('href',), 'value': ('value',), 'timestamp': ('timestamp',)}}),
    ],
    'Other Categories Used To Reach You': [
        Entry(table='Other Categories Used To Reach You', filename='ads_information/instagram_ads_and_businesses/other_categories_used_to_reach_you.json', static_fields={'media': ('media',), 'fbid': ('fbid',), 'ent_name': ('ent_name',)}, list_blocks={('label_values',): {'ent_field_name': ('ent_field_name',), 'label': ('label',)}, ('label_values', 'vec'): {'value': ('value',)}}),
    ],
    'Personal Information': [
        Entry(table='Personal Information', filename='personal_information/personal_information/personal_information.json', static_fields={}, list_blocks={('profile_user',): {'href': ('string_map_data', 'Private Account', 'href'), 'value': ('string_map_data', 'Private Account', 'value'), 'timestamp': ('string_map_data', 'Private Account', 'timestamp')}}),
    ],
    'Polls': [
        Entry(table='Polls', filename='your_instagram_activity/story_interactions/polls.json', static_fields={}, list_blocks={('story_activities_polls',): {'title': ('title',)}, ('story_activities_polls', 'string_list_data'): {'value': ('value',), 'timestamp': ('timestamp',)}}),
        Entry(table='Polls', filename='your_instagram_activity/story_sticker_interactions/polls.json', static_fields={}, list_blocks={('story_activities_polls',): {'title': ('title',)}, ('story_activities_polls', 'string_list_data'): {'value': ('value',), 'timestamp': ('timestamp',)}}),
    ],
    'Post Comments 1': [
        Entry(table='Post Comments 1', filename='your_instagram_activity/comments/post_comments_1.json', static_fields={'value': ('string_map_data', 'Media Owner', 'value'), 'timestamp': ('string_map_data', 'Time', 'timestamp')}, list_blocks={('media_list_data',): {'uri': ('uri',)}, (): {'value': ('string_map_data', 'Media Owner', 'value'), 'timestamp': ('string_map_data', 'Time', 'timestamp')}}),
    ],
    'Posts 1': [
        Entry(table='Posts 1', filename='your_instagram_activity/content/posts_1.json', static_fields={'title': ('title',), 'creation_timestamp': ('creation_timestamp',)}, list_blocks={('media',): {'uri': ('uri',), 'creation_timestamp': ('creation_timestamp',), 'title': ('title',), 'source_app': ('cross_post_source', 'source_app'), 'has_camera_metadata': ('media_metadata', 'camera_metadata', 'has_camera_metadata')}}),
        Entry(table='Posts 1', filename='your_instagram_activity/media/posts_1.json', static_fields={}, list_blocks={(): {'title': ('title',), 'creation_timestamp': ('creation_timestamp',)}, ('media',): {'uri': ('uri',), 'creation_timestamp': ('creation_timestamp',), 'title': ('title',), 'source_app': ('cross_post_source', 'source_app')}}),
    ],
    'Posts Viewed': [
        Entry(table='Posts Viewed', filename='ads_information/ads_and_topics/posts_viewed.json', static_fields={}, list_blocks={('impressions_history_posts_seen',): {'value': ('string_map_data', 'Author', 'value'), 'timestamp': ('string_map_data', 'Time', 'timestamp')}}),
    ],
    "Posts You'Re Not Interested In": [
        Entry(table="Posts You'Re Not Interested In", filename="ads_information/ads_and_topics/posts_you're_not_interested_in.json", static_fields={}, list_blocks={('impressions_history_posts_not_interested', 'string_list_data'): {'href': ('href',), 'value': ('value',)}}),
    ],
    'Profile Privacy Changes': [
        Entry(table='Profile Privacy Changes', filename='security_and_login_information/login_and_profile_creation/profile_privacy_changes.json', static_fields={}, list_blocks={('account_history_account_privacy_history',): {'title': ('title',), 'href': ('string_map_data', 'Time', 'href'), 'value': ('string_map_data', 'Time', 'value'), 'timestamp': ('string_map_data', 'Time', 'timestamp')}}),
    ],
    'Profile Searches': [
        Entry(table='Profile Searches', filename='logged_information/recent_searches/profile_searches.json', static_fields={}, list_blocks={('searches_user',): {'title': ('title',), 'href': ('string_map_data', 'Time', 'href'), 'value': ('string_map_data', 'Time', 'value'), 'timestamp': ('string_map_data', 'Time', 'timestamp')}}),
    ],
    "Profiles You'Re Not Interested In": [
        Entry(table="Profiles You'Re Not Interested In", filename="ads_information/ads_and_topics/profiles_you're_not_interested_in.json", static_fields={}, list_blocks={('impressions_history_recs_hidden_authors',): {'title': ('title',), 'href': ('string_map_data', 'Time', 'href'), 'value': ('string_map_data', 'Time', 'value'), 'timestamp': ('string_map_data', 'Time', 'timestamp')}}),
    ],
    'Questions': [
        Entry(table='Questions', filename='your_instagram_activity/story_interactions/questions.json', static_fields={}, list_blocks={('story_activities_questions',): {'title': ('title',), 'media_list_data': ('media_list_data',)}, ('story_activities_questions', 'string_list_data'): {'href': ('href',), 'value': ('value',), 'timestamp': ('timestamp',)}}),
    ],
    'Quizzes': [
        Entry(table='Quizzes', filename='your_instagram_activity/story_sticker_interactions/quizzes.json', static_fields={}, list_blocks={('story_activities_quizzes',): {'title': ('title',)}, ('story_activities_quizzes', 'string_list_data'): {'value': ('value',), 'timestamp': ('timestamp',)}}),
    ],
    'Recommended Topics': [
        Entry(table='Recommended Topics', filename='preferences/your_topics/recommended_topics.json', static_fields={}, list_blocks={('topics_your_topics',): {'title': ('title',), 'href': ('string_map_data', 'Name', 'href'), 'value': ('string_map_data', 'Name', 'value'), 'timestamp': ('string_map_data', 'Name', 'timestamp')}}),
    ],
    'Reels': [
        Entry(table='Reels', filename='your_instagram_activity/media/reels.json', static_fields={}, list_blocks={('ig_reels_media', 'media'): {'uri': ('uri',), 'creation_timestamp': ('creation_timestamp',), 'title': ('title',), 'dubbing_info': ('dubbing_info',), 'media_variants': ('media_variants',), 'source_app': ('cross_post_source', 'source_app'), 'music_genre': ('media_metadata', 'video_metadata', 'music_genre')}, ('ig_reels_media', 'media', 'media_metadata', 'video_metadata', 'exif_data'): {'source_type': ('source_type',)}}),
    ],
    'Reels Comments': [
        Entry(table='Reels Comments', filename='your_instagram_activity/comments/reels_comments.json', static_fields={}, list_blocks={('comments_reels_comments',): {'value': ('string_map_data', 'Media Owner', 'value'), 'timestamp': ('string_map_data', 'Time', 'timestamp')}}),
    ],
    'Removed Suggestions': [
        Entry(table='Removed Suggestions', filename='connections/followers_and_following/removed_suggestions.json', static_fields={}, list_blocks={('relationships_dismissed_suggested_users',): {'title': ('title',), 'media_list_data': ('media_list_data',)}, ('relationships_dismissed_suggested_users', 'string_list_data'): {'href': ('href',), 'value': ('value',), 'timestamp': ('timestamp',)}}),
    ],
    'Saved Collections': [
        Entry(table='Saved Collections', filename='your_instagram_activity/saved/saved_collections.json', static_fields={}, list_blocks={('saved_saved_collections',): {'title': ('title',), 'value': ('string_map_data', 'Name', 'value'), 'timestamp': ('string_map_data', 'Added Time', 'timestamp'), 'href': ('string_map_data', 'Name', 'href')}}),
    ],
    'Saved Posts': [
        Entry(table='Saved Posts', filename='your_instagram_activity/saved/saved_posts.json', static_fields={}, list_blocks={('saved_saved_media',): {'title': ('title',), 'href': ('string_map_data', 'Saved on', 'href'), 'timestamp': ('string_map_data', 'Saved on', 'timestamp')}}),
    ],
    'Signup Details': [
        Entry(table='Signup Details', filename='security_and_login_information/login_and_profile_creation/signup_details.json', static_fields={}, list_blocks={('account_history_registration_info',): {'timestamp': ('string_map_data', 'Time', 'timestamp')}}),
    ],
    'Stories': [
        Entry(table='Stories', filename='your_instagram_activity/content/stories.json', static_fields={}, list_blocks={('ig_stories',): {'uri': ('uri',), 'creation_timestamp': ('creation_timestamp',), 'title': ('title',), 'dubbing_info': ('dubbing_info',), 'media_variants': ('media_variants',), 'backup_uri': ('backup_uri',), 'source_app': ('cross_post_source', 'source_app'), 'music_genre': ('media_metadata', 'video_metadata', 'music_genre')}, ('ig_stories', 'media_metadata', 'video_metadata', 'exif_data'): {'date_time_digitized': ('date_time_digitized',), 'date_time_original': ('date_time_original',), 'source_type': ('source_type',)}, ('ig_stories', 'media_metadata', 'photo_metadata', 'exif_data'): {'source_type': ('source_type',), 'date_time_digitized': ('date_time_digitized',), 'date_time_original': ('date_time_original',)}}),
        Entry(table='Stories', filename='your_instagram_activity/media/stories.json', static_fields={}, list_blocks={('ig_stories',): {'uri': ('uri',), 'creation_timestamp': ('creation_timestamp',), 'title': ('title',), 'dubbing_info': ('dubbing_info',), 'media_variants': ('media_variants',), 'source_app': ('cross_post_source', 'source_app')}, ('ig_stories', 'media_metadata', 'video_metadata', 'exif_data'): {'date_time_digitized': ('date_time_digitized',), 'date_time_original': ('date_time_original',), 'source_type': ('source_type',)}}),
    ],
    'Story Likes': [
        Entry(table='Story Likes', filename='your_instagram_activity/story_interactions/story_likes.json', static_fields={}, list_blocks={('story_activities_story_likes',): {'title': ('title',)}, ('story_activities_story_likes', 'string_list_data'): {'timestamp': ('timestamp',)}}),
        Entry(table='Story Likes', filename='your_instagram_activity/story_sticker_interactions/story_likes.json', static_fields={}, list_blocks={('story_activities_story_likes',): {'title': ('title',)}, ('story_activities_story_likes', 'string_list_data'): {'timestamp': ('timestamp',)}}),
    ],
    'Subscription For No Ads': [
        Entry(table='Subscription For No Ads', filename='ads_information/instagram_ads_and_businesses/subscription_for_no_ads.json', static_fields={'media': ('media',), 'fbid': ('fbid',)}, list_blocks={('label_values',): {'label': ('label',), 'value': ('value',)}}),
    ],
    'Suggested Profiles Viewed': [
        Entry(table='Suggested Profiles Viewed', filename='ads_information/ads_and_topics/suggested_profiles_viewed.json', static_fields={}, list_blocks={('impressions_history_chaining_seen',): {'value': ('string_map_data', 'Username', 'value'), 'timestamp': ('string_map_data', 'Time', 'timestamp')}}),
    ],
    'Time Spent On Instagram': [
        Entry(table='Time Spent On Instagram', filename='your_instagram_activity/other_activity/time_spent_on_instagram.json', static_fields={}, list_blocks={(): {'timestamp': ('timestamp',), 'media': ('media',), 'fbid': ('fbid',)}, ('label_values',): {'label': ('label',)}, ('label_values', 'vec', 'dict'): {'label': ('label',), 'timestamp_value': ('timestamp_value',)}}),
    ],
    'Videos Watched': [
        Entry(table='Videos Watched', filename='ads_information/ads_and_topics/videos_watched.json', static_fields={}, list_blocks={('impressions_history_videos_watched',): {'value': ('string_map_data', 'Author', 'value'), 'timestamp': ('string_map_data', 'Time', 'timestamp')}}),
    ],
    'Word Or Phrase Searches': [
        Entry(table='Word Or Phrase Searches', filename='logged_information/recent_searches/word_or_phrase_searches.json', static_fields={}, list_blocks={('searches_keyword',): {'title': ('title',), 'href': ('string_map_data', 'Time', 'href'), 'value': ('string_map_data', 'Time', 'value'), 'timestamp': ('string_map_data', 'Time', 'timestamp')}}),
    ],
    'Your Activity Off Meta Technologies': [
        Entry(table='Your Activity Off Meta Technologies', filename='apps_and_websites_off_of_instagram/apps_and_websites/your_activity_off_meta_technologies.json', static_fields={}, list_blocks={('apps_and_websites_off_meta_activity',): {'name': ('name',)}, ('apps_and_websites_off_meta_activity', 'events'): {'id': ('id',), 'type': ('type',), 'timestamp': ('timestamp',)}}),
    ],
    'Your Information Download Requests': [
        Entry(table='Your Information Download Requests', filename='your_instagram_activity/other_activity/your_information_download_requests.json', static_fields={'timestamp': ('timestamp',)}, list_blocks={(): {'timestamp': ('timestamp',)}, ('label_values',): {'timestamp_value': ('timestamp_value',)}}),
    ],
    'Your Muted Story Teaser Creators': [
        Entry(table='Your Muted Story Teaser Creators', filename='your_instagram_activity/subscriptions/your_muted_story_teaser_creators.json', static_fields={}, list_blocks={('subscriptions_muted_story_teaser_creators',): {'title': ('title',), 'href': ('string_map_data', 'Muted Creators', 'href'), 'value': ('string_map_data', 'Muted Creators', 'value'), 'timestamp': ('string_map_data', 'Muted Creators', 'timestamp')}}),
    ],
    'Your Topics': [
        Entry(table='Your Topics', filename='preferences/your_topics/your_topics.json', static_fields={}, list_blocks={('topics_your_topics',): {'title': ('title',), 'href': ('string_map_data', 'Name', 'href'), 'value': ('string_map_data', 'Name', 'value'), 'timestamp': ('string_map_data', 'Name', 'timestamp')}}),
    ],
}

