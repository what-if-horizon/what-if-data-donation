import sys
import os
from pathlib import Path

# Add the repo root to Python's import path
repo_root = Path(__file__).resolve().parents[2]  # Adjust depth if needed
sys.path.insert(0, str(repo_root))


from structure_donations.Data_structure_extractors.YT_get_json_structure import structure_from_zip


structure_from_zip("structure_donations/Processed_structure_donations/Youtube/Raw/youtube_takeout-20250314T090052Z-001.zip")

#import structure_donations.Data_structure_extractors.YT_get_json_structure as yt

#print(dir(yt))
