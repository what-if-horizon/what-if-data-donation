# Auto-generated TikTok extractors

from port.helpers.donation_flow import donation_flow, donation_table
from port.helpers.entries_data import X_ENTRIES
from port.helpers.parsers import create_entry_df


def create_donation_flow(file_input: list[str]):
    """Create donation flow from TikTok JSON."""
    tables = []
    for entry in X_ENTRIES:
        try:
            df = create_entry_df(file_input, entry)
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

    file_input = sys.argv[1]
    entry = X_ENTRIES[int(sys.argv[2])]
    print(entry.table)
    print(create_entry_df([file_input], entry))
