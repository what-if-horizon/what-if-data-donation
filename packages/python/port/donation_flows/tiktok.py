# Auto-generated TikTok extractors

from port.helpers.donation_flow import donation_flow, donation_table
from port.helpers.entries_data import TIKTOK_ENTRIES
from port.helpers.parsers import create_entry_df


def create_donation_flow(file_input: list[str]):
    """Create donation flow from TikTok JSON."""
    tables = []
    for entry in TIKTOK_ENTRIES:
        try:
            df = create_entry_df(file_input, entry, json_root="Activity")
            if not df.empty:
                tables.append(donation_table(name=entry.table, df=df, title={"en": entry.table}))
        except Exception as e:
            print(f"Error in {entry.table}:", e)
    if tables:
        return donation_flow(id="tiktok", tables=tables)
    else:
        return None


if __name__ == "__main__":
    import sys

    entry = TIKTOK_ENTRIES[4]
    file_input = sys.argv[1]
    print(create_entry_df([file_input], entry, json_root="Activity"))
