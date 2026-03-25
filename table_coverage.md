# Table coverage: old `*_ENTRIES` vs new `platforms/`

For each platform this document lists every table in the old `donation_flows/`
`*_ENTRIES` specification and every table in the new `data-donation-task`
`platforms/` implementation, then marks the overlap and gaps.

Legend:
- **Old only** — in `*_ENTRIES`, not in new code; needs a decision (port or drop)
- **New only** — in new code, not in `*_ENTRIES`; free gain if the data is wanted
- **Both** — present in both (name may differ; fields listed for comparison)

---

## Instagram

### New `platforms/instagram.py` — 12 tables

| Table id | Columns |
|----------|---------|
| `instagram_followers` | Account, URL, Date |
| `instagram_following` | Account, URL, Date |
| `instagram_ads_viewed` | Account name, Name, URL, Date |
| `instagram_posts_viewed` | Author, URL, Date |
| `instagram_videos_watched` | Author, URL, Date |
| `instagram_post_comments` | Comment, Media owner, Date |
| `instagram_liked_comments` | Account name, Value, Date |
| `instagram_liked_posts` | Account name, Value, Date |
| `instagram_profile_searches` | Timestamp, Name |
| `instagram_story_likes` | Account name, Date |
| `instagram_threads_viewed` | Author, URL, Date |
| `instagram_saved_posts` | Title, URL, Timestamp |

### `IG_ENTRIES` — ~70 unique table keys

Tables also present in the new code are marked **Both**.

| `IG_ENTRIES` key | Status |
|-----------------|--------|
| Ads About Meta | Old only |
| Ads Clicked | Old only |
| Ads Viewed | **Both** (new: `instagram_ads_viewed`) |
| Advertisers Using Your Activity Or Information | Old only |
| Archived Posts | Old only |
| Avatar Story Reactions | Old only |
| Blocked Profiles | Old only |
| Close Friends | Old only |
| Comments Allowed From | Old only |
| Consents | Old only |
| Content Interactions | Old only |
| Countdowns | Old only |
| Custom Lists | Old only |
| Emoji Sliders | Old only |
| Emoji Story Reactions | Old only |
| Filtered Keywords For Comments And Messages | Old only |
| Filtered Keywords For Posts | Old only |
| Follow Requests You've Received | Old only |
| Followers 1 | **Both** (new: `instagram_followers`) |
| Following | **Both** (new: `instagram_following`) |
| Following Hashtags | Old only |
| Hide Story From | Old only |
| Hype | Old only |
| Igtv Videos | Old only |
| Instagram Friend Map | Old only |
| Instagram Signup Details | Old only |
| Liked Comments | **Both** (new: `instagram_liked_comments`) |
| Liked Posts | **Both** (new: `instagram_liked_posts`) |
| Link History | Old only |
| Live Videos | Old only |
| Other Categories Used To Reach You | Old only |
| Other Content | Old only |
| Personal Information | Old only |
| Polls | Old only |
| Post Comments 1 | **Both** (new: `instagram_post_comments`; new also handles `_2`, `_3`…) |
| Posts 1 | Old only |
| Posts Viewed | **Both** (new: `instagram_posts_viewed`) |
| Professional Information | Old only |
| Profile Privacy Changes | Old only |
| Profile Searches | **Both** (new: `instagram_profile_searches`) |
| Question Media Response | Old only |
| Questions | Old only |
| Quizzes | Old only |
| Recommended Topics | Old only |
| Reels | Old only |
| Reels Comments | Old only |
| Removed Suggestions | Old only |
| Replies 1 | Old only |
| Reported Conversations | Old only |
| Reposts | Old only |
| Restricted Profiles | Old only |
| Saved Collections | Old only |
| Saved Posts | **Both** (new: `instagram_saved_posts`) |
| Signup Details | Old only |
| Stories | Old only |
| Story Likes | **Both** (new: `instagram_story_likes`) |
| Story Reaction Sticker Reactions | Old only |
| Subscription For No Ads | Old only |
| Suggested Profiles Viewed | Old only |
| Time Spent On Instagram | Old only |
| Videos Watched | **Both** (new: `instagram_videos_watched`) |
| Word Or Phrase Searches | Old only |
| Your Activity Off Meta Technologies | Old only |
| Your Information Download Requests | Old only |
| Your Link History Settings | Old only |
| Your Muted Story Teaser Creators | Old only |
| Your Topics | Old only |

### New-only Instagram tables (not in `IG_ENTRIES`)

| Table | Note |
|-------|------|
| `instagram_threads_viewed` | Threads (Meta's Twitter alternative); new platform feature |

### Summary

| | Count |
|-|-------|
| `IG_ENTRIES` total | ~70 |
| Covered by new code | 10 |
| New-only (not in entries) | 1 (`threads_viewed`) |
| Old-only (not in new code) | ~60 |

---

## Facebook

### New `platforms/facebook.py` — 28 tables

| Table id |
|----------|
| `facebook_who_youve_followed` |
| `facebook_news_your_locations` |
| `facebook_notifications` |
| `facebook_reels_usage` |
| `facebook_last_28` |
| `facebook_search_history` |
| `facebook_recently_visited` |
| `facebook_recently_viewed` |
| `facebook_profile_update_history` |
| `facebook_likes_and_reactions_base` |
| `facebook_likes_and_reactions` |
| `facebook_your_group_membership_activity` |
| `facebook_pages_and_profiles_you_follow` |
| `facebook_pages_youve_liked` |
| `facebook_your_posts_and_check_ins` |
| `facebook_story_reactions` |
| `facebook_feed_controls` |
| `facebook_content_sharing_links_you_created` |
| `facebook_your_friends` |
| `facebook_ads_interests` |
| `facebook_your_event_responses` |
| `facebook_group_posts_and_comments` |
| `facebook_your_answers_to_membership_questions` |
| `facebook_your_comments_in_groups` |
| `facebook_your_saved_items` |
| `facebook_comments` |
| `facebook_your_comment_active_days` |
| `facebook_your_pages` |

### `FB_ENTRIES` — ~80 unique table keys (selected)

The full list is large; below are the keys, marked against new coverage.

| `FB_ENTRIES` key | Status |
|-----------------|--------|
| Ad Preferences | Old only |
| Admin Activity | Old only |
| Ads About Meta | Old only |
| Ads Feedback Activity | Old only |
| Ads Interests | **Both** (new: `facebook_ads_interests`) |
| Ads Personalization Consent | Old only |
| Ads Viewed | Old only |
| Advertisers Using Your Activity Or Information | Old only |
| Advertisers You Ve Interacted With | Old only |
| Ai Conversations | Old only |
| Archived Stories | Old only |
| Close Friends | Old only |
| Collections | Old only |
| Comments | **Both** (new: `facebook_comments`) |
| Comments Allowed From | Old only |
| Consents | Old only |
| Content Sharing Links You Have Created | **Both** (new: `facebook_content_sharing_links_you_created`) |
| Controls | **Both** (new: `facebook_feed_controls`) |
| Edits You Made To Posts | Old only |
| Emails We Sent You | Old only |
| Facebook Reels Usage Information | **Both** (new: `facebook_reels_usage`) |
| Feed | Old only |
| Followers 1 | Old only |
| Following | Old only |
| Group Posts And Comments | **Both** (new: `facebook_group_posts_and_comments`) |
| Groups And Pages That You May Find Engaging | Old only |
| Groups You Ve Visited | Old only |
| Join Requests | Old only |
| Likes And Reactions (1–6) | **Both** (new: `facebook_likes_and_reactions`, `facebook_likes_and_reactions_base`) |
| Link History | Old only |
| Other Categories Used To Reach You | Old only |
| Pages And Profiles You Follow | **Both** (new: `facebook_pages_and_profiles_you_follow`) |
| Pages You Are A Customer Of | Old only |
| Pages You Ve Liked | **Both** (new: `facebook_pages_youve_liked`) |
| People And Friends | **Both** (new: `facebook_your_friends`) |
| People We Think You Should Follow | Old only |
| Polls You Voted On | Old only |
| Posts On Other Pages And Profiles | Old only |
| Posts Viewed | Old only |
| Privacy Settings | Old only |
| Professional Information | Old only |
| Profile Information | **Both** (new: `facebook_profile_update_history`) |
| Recently Viewed | **Both** (new: `facebook_recently_viewed`) |
| Recently Visited | **Both** (new: `facebook_recently_visited`) |
| Recommended Topics | Old only |
| Reduce | Old only |
| Reels Preferences | Old only |
| Registration Information | Old only |
| Shared Memories | Old only |
| Snooze | Old only |
| Story Reactions | **Both** (new: `facebook_story_reactions`) |
| Story Views In Past 7 Days | Old only |
| Subscription For No Ads | Old only |
| Support Messages | Old only |
| Time Spent On Facebook | Old only |
| Video | Old only |
| Videos Watched | Old only |
| Who You Ve Followed | **Both** (new: `facebook_who_youve_followed`) |
| Your Actions On Violating Content In Your Groups | Old only |
| Your Activity Off Meta Technologies | Old only |
| Your Comment Active Days | **Both** (new: `facebook_your_comment_active_days`) |
| Your Comment Edits | Old only |
| Your Comments In Groups | **Both** (new: `facebook_your_comments_in_groups`) |
| Your Consent Settings | Old only |
| Your Facebook Watch Activity In The Last 28 Days | **Both** (new: `facebook_last_28`) |
| Your Friends | **Both** (new: `facebook_your_friends`) |
| Your Group Membership Activity | **Both** (new: `facebook_your_group_membership_activity`) |
| Your Groups | Old only |
| Your Information Download Requests | Old only |
| Your Pages | **Both** (new: `facebook_your_pages`) |
| Your Pages Mentions | Old only |
| Your Pending Posts In Groups | Old only |
| Your Poll Votes | Old only |
| Your Post Audiences | Old only |
| Your Posts, Check Ins, Photos And Videos 1 | **Both** (new: `facebook_your_posts_and_check_ins`) |
| Your Preferred Categories | Old only |
| Your Recent Reported Conversions | Old only |
| Your Recently Followed History | Old only |
| Your Reels | Old only |
| Your Saved Items | **Both** (new: `facebook_your_saved_items`) |
| Your Search History | **Both** (new: `facebook_search_history`) |
| Your Story Highlights | Old only |
| Your Video Consumption Summary | Old only |
| Your Videos | Old only |
| Your Watch Settings | Old only |

### New-only Facebook tables (not in `FB_ENTRIES`)

| Table | Note |
|-------|------|
| `facebook_news_your_locations` | Location data from news browsing |
| `facebook_notifications` | Notification history |
| `facebook_your_answers_to_membership_questions` | Group join questionnaires |
| `facebook_your_event_responses` | Event RSVPs |

### Summary

| | Count |
|-|-------|
| `FB_ENTRIES` total | ~80 |
| Covered by new code | ~22 |
| New-only (not in entries) | 4 |
| Old-only (not in new code) | ~58 |

---

## TikTok

### New `platforms/tiktok.py` — 11 tables

| Table id | Columns |
|----------|---------|
| `tiktok_activity_summary` | Metric, Count |
| `tiktok_settings` | Setting, Keywords |
| `tiktok_watch_history` | Date, Link |
| `tiktok_favorite_videos` | Date, Link |
| `tiktok_follower` | Date, UserName |
| `tiktok_following` | Date, UserName |
| `tiktok_hashtag` | HashtagName, HashtagLink |
| `tiktok_like_list` | Date, Link |
| `tiktok_searches` | Date, SearchTerm |
| `tiktok_share_history` | Date, SharedContent, Link, Method |
| `tiktok_comments` | Date, Comment, Photo, Url |

### `TIKTOK_ENTRIES` — 9 table keys

| `TIKTOK_ENTRIES` key | Status |
|---------------------|--------|
| Activity | **Both** (maps to `watch_history`, `follower`, `following`, `hashtag`, `like_list`, `searches`, `share_history`, `favorite_videos`) |
| Ads And Data | Old only |
| App Settings | **Both** (new: `tiktok_settings`) |
| Comment | **Both** (new: `tiktok_comments`) |
| Post | Old only |
| Profile | **Both** (new: `tiktok_activity_summary`) |
| Tiktok Live | Old only |
| Video | Old only |
| Your Activity | **Both** (duplicate of Activity in newer export format) |

> Note: `TIKTOK_ENTRIES` uses broad keys (e.g. "Activity") that each extract
> many sub-tables in one pass. The new code splits these into individual named
> tables. The mapping above is approximate — check which specific sub-fields
> matter to your study.

### Summary

| | Count |
|-|-------|
| `TIKTOK_ENTRIES` total | 9 (broad keys) |
| Old-only entries | Ads And Data, Post, TikTok Live, Video |
| New-only tables | `tiktok_favorite_videos`, `tiktok_follower`, `tiktok_hashtag` (previously nested under "Activity") |

---

## Twitter / X

### New `platforms/x.py` — 10 tables

| Table id | Columns |
|----------|---------|
| `x_ad_engagement` | Text, Impression time |
| `x_follower` | Link to user |
| `x_following` | Link to user |
| `x_block` | Blocked users |
| `x_like` | Tweet Id, Tweet |
| `x_tweet` | Date, Tweet, Retweeted |
| `x_personalization` | Interest, is disabled |
| `x_mute` | Muted users |
| `x_tweet_headers` | Tweet id, User id, Created at |
| `x_user_link_clicks` | Tweet id, Link, Datum en tijd |

### `X_ENTRIES` — ~39 table keys

| `X_ENTRIES` key | Status |
|----------------|--------|
| Account | Old only |
| Account-Suspension | Old only |
| Ad-Engagements | **Both** (new: `x_ad_engagement`) |
| Ad-Impressions | Old only |
| Ad-Mobile-Conversions-Attributed | Old only |
| Ad-Mobile-Conversions-Unattributed | Old only |
| Ad-Online-Conversions-Attributed | Old only |
| Ad-Online-Conversions-Unattributed | Old only |
| Article | Old only |
| Article-Metadata | Old only |
| Block | **Both** (new: `x_block`) |
| Community-Note | Old only |
| Community-Note-Batsignal | Old only |
| Community-Note-Rating | Old only |
| Community-Note-Tombstone | Old only |
| Community-Tweet | Old only |
| Follower | **Both** (new: `x_follower`) |
| Following | **Both** (new: `x_following`) |
| Grok-Chat-Item | Old only |
| Like | **Both** (new: `x_like`) |
| Lists-Created | Old only |
| Lists-Member | Old only |
| Lists-Subscribed | Old only |
| Manifest | Old only |
| Moment | Old only |
| Mute | **Both** (new: `x_mute`) |
| Note-Tweet | Old only |
| Personalization | **Both** (new: `x_personalization`) |
| Professional-Data | Old only |
| Protected-History | Old only |
| Reply-Prompt | Old only |
| Saved-Search | Old only |
| Smartblock | Old only |
| Spaces-Metadata | Old only |
| Tweet-Headers | **Both** (new: `x_tweet_headers`) |
| Tweetdeck | Old only |
| Tweets | **Both** (new: `x_tweet`) |
| User-Link-Clicks | **Both** (new: `x_user_link_clicks`) |
| Verified | Old only |

### Summary

| | Count |
|-|-------|
| `X_ENTRIES` total | ~39 |
| Covered by new code | 10 |
| New-only | 0 |
| Old-only | ~29 |

---

## YouTube

### New `platforms/youtube.py` — 4 tables

| Table id | Columns | Languages |
|----------|---------|-----------|
| `youtube_watch_history` | Title, URL, Timestamp | EN + NL |
| `youtube_search_history` | Title, URL, Timestamp, Ad | EN + NL |
| `youtube_subscriptions` | Channel Id, Channel URL, Channel Name | EN + NL |
| `youtube_comments` | Comment ID, Channel ID, Timestamp, Price, Video ID, Comment text | EN + NL |

### `YT_ENTRIES` — structure note

`YT_ENTRIES` takes a different approach from the other platforms: instead of a small
set of semantic table keys, it contains one entry **per language variant** of each
file. The same four underlying tables (search history, watch history, subscriptions,
comments) appear under dozens of localised filenames covering English, Dutch,
Spanish, Catalan, Romanian, Lithuanian, and others.

Representative keys (English/Dutch subset):

| `YT_ENTRIES` key | Maps to |
|-----------------|---------|
| `Search-History` | `youtube_search_history` (EN) |
| `Zoekgeschiedenis` | `youtube_search_history` (NL) |
| `Historial-De-Búsqueda` | `youtube_search_history` (ES) |
| `Watch-History` | `youtube_watch_history` (EN) |
| `Kijkgeschiedenis` | `youtube_watch_history` (NL) |
| `Historial-De-Reproducciones` | `youtube_watch_history` (ES) |
| `subscriptions` | `youtube_subscriptions` (EN) |
| `abonnementen` | `youtube_subscriptions` (NL) |
| `comments` | `youtube_comments` (EN) |
| `reacties` | `youtube_comments` (NL) |
| Various playlist/watch-later/favorites keys | Old only (no equivalent in new code) |

The new YouTube platform handles multilingual exports via `DDPCategory` language
detection — one code path per language, not one entry per locale. This replaces
~30+ `YT_ENTRIES` rows with 2 `DDPCategory` entries (EN and NL).

### Old-only YouTube data

| `YT_ENTRIES` key category | Note |
|--------------------------|------|
| Playlists (`Listas_de_reproducción`, `playlists`, `grojaraščiai`, …) | Playlist metadata in many locales |
| Watch Later (`Watch_later-videos`, `Video_s_in_Watch_later`, …) | Watch later queue |
| Favorites (`Favorites-videos`, `Video_s_in_Favorites`, …) | Favorited videos |
| Channel settings/metadata (`channel`, `kanaal`, `channel_URL_configs`, …) | Channel owner data; likely not relevant for participant studies |

### Summary

| | Count |
|-|-------|
| `YT_ENTRIES` unique underlying tables | ~4 + playlists/watch-later/favorites |
| Covered by new code | 4 (watch history, search history, subscriptions, comments) |
| Old-only | Playlists, Watch Later, Favorites |

---

## Cross-platform summary

| Platform | `*_ENTRIES` keys | New tables | Overlap | Old-only | New-only |
|----------|-----------------|------------|---------|----------|----------|
| Instagram | ~70 | 12 | 10 | ~60 | 1 (threads) |
| Facebook | ~80 | 28 | ~22 | ~58 | 4 |
| TikTok | 9 (broad) | 11 | ~7 | ~2–3 | ~3–4 |
| Twitter/X | ~39 | 10 | 10 | ~29 | 0 |
| YouTube | ~30 locale variants of 4–7 tables | 4 | 4 | Playlists, Watch Later, Favorites | 0 |

**Key observations:**

1. **Instagram and Facebook have the largest old-only footprint.** ~60 IG tables and
   ~58 FB tables are in `*_ENTRIES` but absent from the new code. Most are metadata,
   privacy settings, and minor interaction types — consult the Excel sheet to decide
   which are scientifically required.

2. **TikTok entries are broad, new code is granular.** Each `TIKTOK_ENTRIES` key
   often covers multiple sub-tables. The mapping is not one-to-one; you need to check
   which sub-fields each old entry actually extracted.

3. **Twitter/X has full overlap on what the new code covers**, but the new code
   covers only 10 of ~39 entries. The old-only entries are mostly ad conversion data,
   community notes, lists, and account metadata.

4. **YouTube's old entries are a multilingual fan-out of 4 tables**, not additional
   data. The new code covers the same 4 tables more cleanly, but drops Playlists,
   Watch Later, and Favorites.

5. **New-only tables** (threads viewed on Instagram; location, notifications, event
   responses, membership answers on Facebook) represent data the old study did not
   collect. These are free gains if the research questions call for them.
