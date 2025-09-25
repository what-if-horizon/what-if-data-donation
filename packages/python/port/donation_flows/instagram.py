import json
import logging

import pandas as pd
from port.helpers.donation_flow import donation_flow, donation_table
from port.helpers.parsers import create_entry_df, create_table
from port.helpers.Structure_extractor_libraries.IG_get_json_structure import (
    infer_placeholder,
    simplify_json_structure,
    structure_from_zip,
)


def create_donation_flow(file_input: list[str]):
    # Do a lazy import to avoid importerror while entries are being generated
    from port.helpers.entries_data import IG_ENTRIES

    tables = []
    # --- normal donation tables ---
    for key, entries in IG_ENTRIES.items():
        try:
            df = create_table(file_input, entries, search_subfolders=True)
            if not df.empty:
                tables.append(donation_table(name=key, df=df, title={"en": key}))
        except Exception as e:
            logging.exception(f"Error in {key}")

    # --- structure table ---
    zip_path = file_input[0]
    placeholder_json = structure_from_zip(zip_path)
    df_placeholder = pd.DataFrame(
        [{"Data Structure": "Anonymized", "Placeholder for research purpose": placeholder_json}]
    )

    tables.append(donation_table(name="placeholder", df=df_placeholder, title={"en": "Placeholders"}))

    # --- donation flow ---
    if tables:
        return donation_flow(id="instagram", tables=tables)
    else:
        return None
