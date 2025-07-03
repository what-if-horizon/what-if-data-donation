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

   
#####################################################
# Execute the simplify_json_structure() function   
# -- Open the zipfile
# -- Iterate over each file in the zipfile
# -- Load the JSON
# -- Apply the simplify_json_structure()
# -- Save in output_structure
# -- Return the JSON
#####################################################

def structure_from_zip(zip_path):
    output_structure = {}

    with zipfile.ZipFile(zip_path, 'r') as z:
        for file_info in z.infolist():
            if file_info.filename.endswith('.json') and not file_info.is_dir():
                with z.open(file_info.filename) as f:
                    try:
                        content = json.load(f)
                        placeholder_content = simplify_json_structure(content)
                        output_structure[file_info.filename] = placeholder_content
                    except json.JSONDecodeError:
                        output_structure[file_info.filename] = "Invalid JSON"

    return json.dumps(output_structure, indent=2, ensure_ascii=False)