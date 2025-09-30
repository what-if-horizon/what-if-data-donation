"""
Donation file structure data for takeout flows

This file contains a list of Entries for each platform.
Each Entry represents a table to be generated from the appropriate file.

To generate this file, please run structure/flow_generation/generate_entries.py
which will use the Merged_structures_*.csv to determine the required entries.
"""

from port.helpers.parsers import Entry


FB_ENTRIES: dict[str, list[Entry]] = {
    "Your Search History (current)": [
        Entry(
            table="Your Search History",
            filename="logged_information/search/your_search_history.json",
            static_fields={},
            list_blocks={
                ("searches_v2",): {"timestamp": ("timestamp",), "title": ("title",)},
                ("searches_v2", "data"): {"text": ("text",)},
                ("searches_v2", "attachments", "data"): {"text": ("text",)},
            },
        ),
    ],
    "Your Search History (New)": [
        Entry(
            table="Your Search History",
            filename="logged_information/search/your_search_history.json",
            static_fields={},
            list_blocks={
                ("searches_v2",): {
                    "timestamp": ("timestamp",),
                    "title": ("title",),
                    "text": ("data", "text"),
                    "attachment-text": ("attachments", "data", "text"),
                },
            },
        ),
    ],
}
