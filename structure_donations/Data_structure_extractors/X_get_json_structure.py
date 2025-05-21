import zipfile
import json
import os
import re

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

def structure_from_zip(zip_path):
    output_structure = {}
    output_folder = "structure_donations/Processed_structure_donations/Twitter/Input_test"

    with zipfile.ZipFile(zip_path, 'r') as z:
        for file_info in z.infolist():
            # Split the path into parts
            path_parts = file_info.filename.split('/')

            # Process only files where 'data' is in the second position
            if file_info.is_dir() or len(path_parts) < 2 or path_parts[1] != 'data':
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

                if file_info.filename.endswith('.json'):
                    try:
                        content = json.loads(content_str)
                    except json.JSONDecodeError:
                        output_structure[file_info.filename] = "Invalid JSON"
                        continue
                elif file_info.filename.endswith('.js'):
                    content = extract_json_from_js(content_str)
                    if content is None:
                        output_structure[file_info.filename] = "No data"
                        continue
                else:
                    continue  # Skip unknown file types

                placeholder_content = simplify_json_structure(content)
                output_structure[file_info.filename] = placeholder_content

    zip_base_name = os.path.splitext(os.path.basename(zip_path))[0]
    output_path = os.path.join(output_folder, f"{zip_base_name}_structure.json")



    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(output_structure, f, indent=2)

    print(f"Structure saved to {output_path}")
    return output_structure
