"""
Donation file structure data for takeout flows

This file contains a list of Entries for each platform.
Each Entry represents a table to be generated from the appropriate file.

To generate this file, please run structure/flow_generation/generate_entries.py
which will use the Merged_structures_*.csv to determine the required entries.
"""

from port.helpers.parsers import Entry

FB_ENTRIES: dict[str, list[Entry]] = {

'Your Post Audiences': [
        Entry(table='Your Post Audiences', filename='connections/friends/your_post_audiences.json', static_fields={}, list_blocks={(): {'media': ('media',), 'fbid': ('fbid',), 'ent_name': ('ent_name',)}, ('label_values',): {'label': ('label',), 'value': ('value',), 'ent_field_name': ('ent_field_name',), 'dict': ('dict',), 'title': ('title',)}}),

    ],
}
