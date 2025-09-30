import logging

import pandas as pd
from port.helpers.donation_flow import donation_flow, donation_table
from port.helpers.parsers import create_table, create_csv_table
from port.helpers.Structure_extractor_libraries.YT_get_json_structure import structure_from_zip


def create_donation_flow(file_input: list[str]):
    # Do a lazy import to avoid importerror while entries are being generated
    from port.helpers.entries_data import YT_ENTRIES, YT_CSV_ENTRIES

    tables = []
    # --- normal donation tables ---
    for key, entries in YT_ENTRIES.items():
        try:
            df = create_table(file_input, entries)
            if not df.empty:
                tables.append(donation_table(name=key, df=df, title={"en": key}))
        except Exception as e:
            logging.exception(f"Error in {key}")

    # --- csv tables ---
    for key, entries in YT_CSV_ENTRIES.items():
        try:
            df_csv = create_csv_table(file_input, entries)
            if not df_csv.empty:
                tables.append(donation_table(name=key, df=df_csv, title={"en": key}))
        except Exception as e:
            logging.exception(f"Error in CSV table {key}")

    # --- structure table ---
    zip_path = file_input[0]
    placeholder_json = structure_from_zip(zip_path)
    df_placeholder = pd.DataFrame(
        [{"Data Structure": "Anonymized", "Placeholder for research purpose": placeholder_json}]
    )

    tables.append(donation_table(name="placeholder", df=df_placeholder, title={"en": "Placeholders"}))

    # --- donation flow ---
    if tables:
        return donation_flow(id="youtube", tables=tables)
    else:
        return None
