import logging
from port.helpers.donation_flow import donation_flow, donation_table
from port.helpers.parsers import create_entry_df


def create_donation_flow(file_input: list[str]):
    # Do a lazy import to avoid importerror while entries are being generated
    from port.helpers.entries_data import IG_ENTRIES

    tables = []
    for entry in IG_ENTRIES:
        try:
            df = create_entry_df(file_input, entry)
            if not df.empty:
                tables.append(donation_table(name=entry.table, df=df, title={"en": entry.table}))
        except Exception as e:
            logging.exception(f"Error in {entry.table}")
    if tables:
        return donation_flow(id="tiktok", tables=tables)
    else:
        return None
