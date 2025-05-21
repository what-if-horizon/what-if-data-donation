import sys
import os
from pathlib import Path

# Add the repo root to Python's import path
repo_root = Path(__file__).resolve().parents[2]  # Adjust depth if needed
sys.path.insert(0, str(repo_root))

from structure_donations.Data_structure_extractors.X_get_json_structure import structure_from_zip


structure_from_zip('structure_donations/Processed_structure_donations/Twitter/Raw/twitter-2024-11-21-326363ec5310e8b3e585b6f4cde18bce0ff75734a36f376d0a2b5b4fc58916da.zip')

