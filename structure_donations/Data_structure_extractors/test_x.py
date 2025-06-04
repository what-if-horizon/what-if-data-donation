import sys
import os
from pathlib import Path

# Add the repo root to Python's import path
repo_root = Path(__file__).resolve().parents[2]  # Adjust depth if needed
sys.path.insert(0, str(repo_root))

from structure_donations.Data_structure_extractors.X_get_json_structure import structure_from_zip


structure_from_zip('structure_donations/Processed_structure_donations/Twitter/Raw/twitter-2025-03-15-76701c7591722b08ff3886a6ec1a130366b8ce153f72f649e364ff2f3ecf77bb.zip')


