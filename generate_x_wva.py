#%%
# Load schema
import pandas as pd

schema_df = pd.read_csv("Merged_structures_X.csv")
schema_df.columns = schema_df.columns.str.strip()
schema_df = schema_df.dropna(subset=["json_name", "row_path"])
schema_df = schema_df[schema_df['row_path'] != 'No data']

#%%


def build_field_mappings_orig(schema_group: pd.DataFrame):
    static_fields = []
    seen_static_fields = set()
    list_blocks = {}

    for _, row in schema_group.iterrows():
        path = []
        list_path = []
        last_key = None
        row_path = row["row_path"]
        path.append(row_path)

        for i in range(1, 6):
            col_val = row.get(f"col_path_{i}")
            list_status = row.get(f"col_path_{i}_LIST", "NO LIST")
            if pd.notna(col_val):
                path.append(col_val)
                if list_status == "LIST":
                    list_path = path.copy()

        last_key = path[-1] if path else None


        if list_path:
            list_path_tuple = tuple(list_path[:-1])
            list_blocks.setdefault(list_path_tuple, set()).add(list_path[-1])
        elif last_key and last_key not in seen_static_fields:
            static_fields.append(path)
            seen_static_fields.add(last_key)

    return static_fields, list_blocks


def build_field_mappings(schema_group: pd.DataFrame):
    static_fields = []
    list_blocks = {}
    seen_static = set()

    for _, row in schema_group.iterrows():
        path = extract_path(row)

        for i, key in enumerate(path):
            if str(row.get(f"col_path_{i+1}_LIST", "")).strip().upper() == "LIST":
                list_path = tuple(path[:i+1])
                subfield_path = path[i+1:]
                if subfield_path:
                    list_blocks.setdefault(list_path, set()).add(tuple(subfield_path))
                break
        else:
            field = path[-1]
            if field not in seen_static:
                static_fields.append(path)
                seen_static.add(field)

    return static_fields, list_blocks

#%%


def snake_case(name: str) -> str:
    return name.lower().replace("-", "_").replace(".json", "").replace(".js", "").replace(" ", "_")

def extract_path(row):
    path = []
    for col in ["row_path"] + [f"col_path_{i}" for i in range(1, 6)]:
        val = row.get(col)
        if pd.notna(val) and str(val).strip().upper() != "MISSING":
            path.append(str(val).strip())
    return path


def generate_df_function(json_name: str, group: pd.DataFrame) -> str:
    root_key = json_name
    func_name = f"{snake_case(json_name)}_df"

    lines = [
        f"def {func_name}(file_input: list[str]) -> pd.DataFrame:",
        f"    data = read_js(file_input, ['/{json_name}'])",
        "    records = []",
        "    for item in data:",
        "        base_row = {}",
    ]

    static_fields = []
    list_blocks = {}
    seen_static = set()

    for _, row in group.iterrows():
        path = extract_path(row)

        for i, key in enumerate(path):
            if str(row.get(f"col_path_{i+1}_LIST", "")).strip().upper() == "LIST":
                list_path = tuple(path[:i+1])
                subfield_path = path[i+1:]
                if subfield_path:
                    list_blocks.setdefault(list_path, set()).add(tuple(subfield_path))
                break
        else:
            field = path[-1]
            if field not in seen_static:
                static_fields.append(path)
                seen_static.add(field)

    return static_fields, list_blocks

    for path in static_fields:
        field = path[-1]
        path_str = "', '".join(path)
        lines.append(f"        base_row['{field}'] = get_in(item, '{path_str}')")

    if not list_blocks:
        lines.append("        records.append(base_row)")
    else:
        for list_path, fields in list_blocks.items():
            path_str = "', '".join(list_path)
            lines += [
                f"        for entry in get_list(item, '{path_str}'):",
                "            row = base_row.copy()",
                f"            row['__source_list__'] = '{list_path[-1]}'"
            ]
            for field_path in sorted(fields):
                field_name = field_path[-1]
                path_str = "', '".join(field_path)
                lines.append(f"            row['{field_name}'] = get_in(entry, '{path_str}')")
            lines.append("            records.append(row)")

    lines.append("    return pd.DataFrame(records)\n")
    return "\n".join(lines)



json_name, group = list(schema_df.groupby("json_name"))[21]
sf1 = generate_df_function(json_name, group)

sf2, lb2 = build_field_mappings(group)
print(sf1)
print(sf2)
print(sf1 == sf2)


#%%


for i,(json_name, group) in enumerate(schema_df.groupby("json_name")):
    sf1, lb1 = build_field_mappings(group)

    sf2, lb2 = build_field_mappings_orig(group)
    if sf1 != sf2:
        print("SF different:" ,i, json_name)
        print(sf1)
        print(sf2)
    if lb1 != lb2:
        print("LB different:" ,i, json_name)
        print(lb1)
        print(lb2)


# %%


schema_df = pd.read_csv("Merged_structures_TT.csv")
schema_df.columns = schema_df.columns.str.strip()
schema_df["json_name"] = "TT"
print(schema_df.shape)
schema_df = schema_df.dropna(subset=["json_name", "row_path"])
schema_df = schema_df[schema_df['row_path'] != 'No data']
print(schema_df.shape)
