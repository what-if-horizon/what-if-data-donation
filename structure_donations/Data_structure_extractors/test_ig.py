import sys
import os

current_file = os.path.abspath(__file__)
project_root = os.path.abspath(os.path.join(current_file, "../../.."))
sys.path.insert(0, project_root)

from structure_donations.Data_structure_extractors.IG_get_json_structure import structure_from_zip


structure_from_zip('structure_donations/Processed_structure_donations/Instagram/Raw/instagram-geodag91-2024-11-20-poQTe0ag-20250214T091036Z-001.zip')
