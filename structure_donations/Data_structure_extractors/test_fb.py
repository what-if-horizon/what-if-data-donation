import sys
import os

import os
import sys

# Automatically add the project root (3 levels up from this file) to sys.path
current_file = os.path.abspath(__file__)
project_root = os.path.abspath(os.path.join(current_file, "../../.."))
sys.path.insert(0, project_root)

from structure_donations.Data_structure_extractors.FB_get_json_structure import structure_from_zip


structure_from_zip('structure_donations/Processed_structure_donations/Facebook/Raw/facebook-61568298782340-2024-11-18-tP4KIfRH-20250214T091955Z-001.zip')

