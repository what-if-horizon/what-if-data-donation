import sys
import os

# Automatically add the project root (3 levels up from this file) to sys.path
current_file = os.path.abspath(__file__)
project_root = os.path.abspath(os.path.join(current_file, "../../.."))
sys.path.insert(0, project_root)

from structure_donations.Data_structure_extractors.TT_get_json_structure import structure_from_json_file


#structure_from_json_file("structure_donations/Processed_structure_donations/TikTok/Raw/tiktok_takeout_dutch.json")