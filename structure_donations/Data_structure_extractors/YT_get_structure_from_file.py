import json
from typing import IO, Iterable, Tuple

def get_json_structure(json_data, prefix: list, mask_primitives=True) -> Iterable[Tuple[list, str]]:
    if isinstance(json_data, list):
        for i, subval in enumerate(json_data):
            yield from get_json_structure(subval, prefix + [i], mask_primitives=mask_primitives)
    elif isinstance(json_data, dict):
        for subkey, subval in json_data.items():
            yield from get_json_structure(subval, prefix + [subkey], mask_primitives=mask_primitives)
    else:
        leaf = type(json_data).__name__ if mask_primitives else json_data
        yield prefix, leaf

def change_values_to_type(json_data):
    if isinstance(json_data, list):
        return [change_values_to_type(subval) for subval in json_data]
    elif isinstance(json_data, dict):
        return {key: change_values_to_type(subval) for key, subval in json_data.items()}
    else:
        return type(json_data).__name__

def get_structure_from_file(file: IO) -> list[Tuple[dict, list, str]]:
    json_data = json.load(file)
    output = []

    if isinstance(json_data, dict):
        for key, subtree in json_data.items():
            treestruct = change_values_to_type(subtree)
            for prefix, datatype in get_json_structure(treestruct, [], mask_primitives=False):
                output.append(({key: treestruct}, [key] + prefix, datatype))
    elif isinstance(json_data, list):
        treestruct = change_values_to_type(json_data)
        for prefix, datatype in get_json_structure(treestruct, [], mask_primitives=False):
            output.append(({"root": treestruct}, ["root"] + prefix, datatype))
    else:
        raise ValueError("JSON top-level must be dict or list")

    return output

# For testing / running standalone
if __name__ == "__main__":
    import sys
    data = get_structure_from_file(sys.stdin)
    json.dump(data, sys.stdout, indent=2)