"""
Donation file structure data for takeout flows

This file contains a list of Entries for each platform.
Each Entry represents a table to be generated from the appropriate file.

To generate this file, please run structure/flow_generation/generate_entries.py
which will use the Merged_structures_*.csv to determine the required entries.
"""

from port.helpers.parsers import Entry, Node

FB_ENTRIES: dict[str, list[Entry]] = {
    '$Username': [
        Entry(table='$Username', filename='your_facebook_activity/groups/your_group_messages/$USERNAME.json', static_fields={'thread_name': ('thread_name',), 'messages': ('messages',)}, tree=Node(columns={}, children={})),
    ],
    'Message 1': [
        Entry(table='Message 1', filename='your_facebook_activity/messages/inbox/$USERNAME/message_1.json', static_fields={'title': ('title',), 'is_still_participant': ('is_still_participant',), 'thread_path': ('thread_path',), 'magic_words': ('magic_words',)}, tree=Node(columns={}, children={})),
    ],
}

YT_CSV_ENTRIES: dict[str, list[Entry]] = {
}
