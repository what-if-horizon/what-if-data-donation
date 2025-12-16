import json
import logging
import pandas as pd
from port.helpers.donation_flow import donation_flow, donation_table
from port.helpers.parsers import create_table
from port.helpers.Structure_extractor_libraries.TT_get_json_structure import structure_from_json_file


def is_data_valid(file_input: str) -> bool:
    try:
        with open(file_input) as f:
            content = json.load(f)
            return isinstance(content, dict)
    except Exception as e:
        logging.error(f"Error on reading file {file_input}: {e}")
        return False


def create_donation_flow(file_input: list[str]):
    """Create donation flow from TikTok JSON."""
    tables = []

    # Do a lazy import to avoid importerror while entries are being generated
    from port.helpers.entries_data import TIKTOK_ENTRIES

    # --- normal donation tables ---
    for key, entries in TIKTOK_ENTRIES.items():
        try:
            df = create_table(file_input, entries)
            if not df.empty:
                tables.append(donation_table(name=key, df=df, title={"en": key, "nl": key, "es": key}))
        except Exception as e:
            print(f"Error in {key}:", e)

    # --- structure table ---
    zip_path = file_input[0]
    placeholder_json = structure_from_json_file(zip_path)
    df_placeholder = pd.DataFrame(
        [
            {
                "Anonymized data structure": placeholder_json,
            }
        ]
    )

    tables.append(
        donation_table(
            name="placeholder",
            df=df_placeholder,
            title={"en": "Data structure", "es": "Estructura de datos", "nl": "Gegevensstructuur"},
        )
    )

    # --- donation flow ---
    if tables:
        return donation_flow(id="tiktok", tables=tables)
    else:
        return None
