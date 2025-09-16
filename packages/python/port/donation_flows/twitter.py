import logging
import json
import pandas as pd

from port.helpers.Structure_extractor_libraries.X_get_json_structure import infer_placeholder, simplify_json_structure, extract_json_from_js, structure_from_zip
from port.helpers.donation_flow import donation_flow, donation_table
from port.helpers.parsers import create_entry_df


def create_donation_flow(file_input: list[str]):
    # Do a lazy import to avoid importerror while entries are being generated
    from port.helpers.entries_data import X_ENTRIES

    tables = []
    # --- normal donation tables ---
    for entry in X_ENTRIES:
        try:
            df = create_entry_df(file_input, entry)

            if not df.empty:
                tables.append(
                    donation_table(name=entry.table, df=df, title={"en": entry.table})
                )
        except Exception as e:
            logging.exception(f"Error in {entry.table}")

    # --- structure table ---
    zip_path = file_input[0]
    placeholder_json = structure_from_zip(zip_path)
    df_placeholder = pd.DataFrame([{"Data Structure": "Anonymized", "Placeholder for research purpose": placeholder_json}])

    tables.append(
        donation_table(name="placeholder", df=df_placeholder, title={"en": "Placeholders"})
    )

    # --- donation flow ---
    if tables:
        return donation_flow(id="twitter", tables=tables)
    else:
        return None