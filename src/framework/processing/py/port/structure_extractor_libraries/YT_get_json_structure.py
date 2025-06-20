import zipfile
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