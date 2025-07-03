

"""
The purpose of this python script is to obtain the data structures of the donated data takeouts.
All 'real' data is removed and replaced with the data type.
In this way, we obtain the data structure without collecting any personal data 
"""
#############################################################################
# Import libraries                                                 
#############################################################################

import zipfile
import json
import os
import re

##############################################################################
# Infer the data type  
# -- Change the value into a string stating the data type   
# -- If the value is None, None is returned
# -- If the data type is not one of the data types specified in this function,
#       'unknown is returned                                      
###############################################################################

def infer_placeholder(value):
    if isinstance(value, str):
        return "string"
    elif isinstance(value, bool):
        return "boolean"
    elif isinstance(value, int) or isinstance(value, float):
        return "number"
    elif isinstance(value, list):
        return ["array"]
    elif isinstance(value, dict):
        return {k: infer_placeholder(v) for k, v in value.items()}
    elif value is None:
        return None
    else:
        return "unknown"

#############################################################################################
# Function to iterate over all dictionaries and list to apply the infer_placeholder function 
#############################################################################################

def simplify_json_structure(data):
    # If the data is a dictionary...
    if isinstance(data, dict):
        # ...create a new dictionary where:
        # - each key is kept the same
        # - each value is simplified by calling this function recursively
        return {k: simplify_json_structure(v) for k, v in data.items()}

    # If the data is a list...
    
    elif isinstance(data, list):
        if len(data) > 0:
            # Map each item in the list through this function
            simplified_items = [simplify_json_structure(item) for item in data]

            # If all items are the same, keep only one to reduce noise
            if all(item == simplified_items[0] for item in simplified_items):
                return [simplified_items[0]]
            else:
                return simplified_items
        else:
            return ["array"]

    else:
        return infer_placeholder(data)

################################################
# Extract the json from the JavaScript wrapper #
################################################
def extract_json_from_js(js_content):
    """
    Extract JSON from JavaScript by removing variable assignment like: window.YT_DATA = {...};
    """
    try:
        # Remove anything before the first `{` and anything after the last `}`
        json_str = re.search(r'{.*}', js_content, re.DOTALL).group()
        return json.loads(json_str)
    except Exception as e:
        return None
    






##############################################################################
# Execute the extract_json_from_js() and simplify_json_structure() functions
# -- Open the zipfile
# -- Iterate over each file in the zipfile
# -- Split the path to the file into parts
# -- Process only files where 'data' is in the second position
# -- Open the file
# -- Convert the file into bytes
# -- Delete the JavaScrip wrapper with extract_json_from_js()
# -- Apply the simplify_json_structure() function
# -- Return the data structure
##############################################################################
def structure_from_zip(zip_path):
    output_structure = {}
   
    with zipfile.ZipFile(zip_path, 'r') as z:
        for file_info in z.infolist():
            # Split the path into parts
            path_parts = file_info.filename.split('/')

            # Process only files where 'data' is in the second position
            if file_info.is_dir() or len(path_parts) < 2 or path_parts[0] != 'data':
                continue

            with z.open(file_info.filename) as f:
                try:
                    raw_bytes = f.read()
                except Exception:
                    output_structure[file_info.filename] = "Failed to read file"
                    continue

                try:
                    content_str = raw_bytes.decode("utf-8")
                except UnicodeDecodeError:
                    try:
                        content_str = raw_bytes.decode("latin1")
                    except Exception:
                        output_structure[file_info.filename] = "Encoding error"
                        continue

                content = None

                if file_info.filename.endswith('.js'):
                    content = extract_json_from_js(content_str)
                    if content is None:
                        output_structure[file_info.filename] = "No data"
                        continue
                else:
                    continue  # Skip unknown file types

                placeholder_content = simplify_json_structure(content)
                output_structure[file_info.filename] = placeholder_content

    return output_structure
