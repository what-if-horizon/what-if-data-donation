import json
import os

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

def simplify_json_structure(data):
    if isinstance(data, dict):
        return {k: simplify_json_structure(v) for k, v in data.items()}
    elif isinstance(data, list):
        if len(data) > 0:
            return [simplify_json_structure(data[0])]
        else:
            return ["array"]
    else:
        return infer_placeholder(data)

def structure_from_json_file(json_path):
    
    output_dir = "structure_donations/Processed_structure_donations/TikTok/Input_test"

    json_path = json_path.strip()
    
    with open(json_path, 'r') as f:
        try:
            content = json.load(f)
            placeholder_content = simplify_json_structure(content)
        except json.JSONDecodeError:
            print(f"Error: Could not decode JSON from {json_path}")
            return None

    json_base_name = os.path.splitext(os.path.basename(json_path))[0]
    output_filename = f"{json_base_name}_structure.json"

    
    output_path = os.path.join(output_dir, output_filename)

    with open(output_path, 'w') as f:
        json.dump(placeholder_content, f, indent=2)

    print(f"Structure saved to {output_path}")
    return placeholder_content
