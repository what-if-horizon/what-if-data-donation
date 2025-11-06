

import json
import pandas as pd
import numpy as np
from pathlib import Path 
import ast
import gc
import datetime
import warnings
warnings.filterwarnings("ignore")



#main_path = "/home/rvissche/Nextcloud/What-If/what-if-data-donation/what-if-data-donation/structure_donations/Processed_structure_donations/"

time = datetime.datetime.now()
print(f'{time} START PROCESSING JSONS TWITTER')

main_path = Path.cwd()
main_path = Path(f'{main_path}/structure_donations/Processed_structure_donations/Twitter') 

input_directory = Path(f'{main_path}/Input_test') 
output_directory = Path(f'{main_path}/Output')  
final_directory = Path (f'{main_path}/Final')

for file in output_directory .iterdir():
   if file.is_file():
      file.unlink()

max_columns = 8


for i in range(max_columns):
        col_path = [f"col_path_{i}" for i in range(1, max_columns)]
        col_path_values = [f"col_path_{i}_values" for i in range(1, max_columns)]
        col_path_list = [f"col_path_{i}_lIST" for i in range(1, max_columns)]


##################
# loading_data() #
##################


def loading_data(data):


    try:
        with open(data, 'r') as file:
            data = json.load(file)
            if isinstance(data, str):
                data = json.loads(data)
    except:
        print('JSON loading failed')

   
    
    if len(data) == 0:
        print('JSON is empty')


    df = pd.DataFrame()
    df['col_path_0_values'] = data
    df['json_name'] = df.index
    df['file_path'] = df.index
    df['json_name'] = df['json_name'].str.replace(r'^data/', '', regex=True)
    df['col_path_0_LIST'] = ''



    col = df.pop('json_name') 
    df.insert(0, 'json_name', col)

    df.reset_index(inplace = True)
    df = df.drop('index', axis = 1)



    for i in range(1,max_columns):   
        df[f'col_path_{i}'] = ''
        df[f'col_path_{i}_values'] = ''
        df[f'col_path_{i}_LIST'] = ''

    index_list = []
    for idx, row in df.iterrows():
        if row['col_path_0_values'] == 'No data':
            index_list.append(idx)

    df_no_data = df.loc[index_list]
    df = df.drop(index_list)




    return(df, df_no_data)




################## 
# flatten_json() #
##################



def flatten_json(df):

    def add_rows(row, v, k, list_holder ):
        new_row = row.copy()
        new_row[f'col_path_{i+1}_values'] = v
        new_row[f'col_path_{i+1}'] = k
        new_row[f'col_path_{i+1}_LIST'] = list_holder
        return(new_row)


    new_rows = []
    current_rows = df.copy()  # snapshot to iterate over

    for ix, row in current_rows.iterrows():
        value= row['col_path_0_values']

        if isinstance(value, list):
                    # Check if list of dicts
            if value and isinstance(value[0], dict):

                seen = set()
                unique = []
                for d in value:
                    # Use json.dumps to get a hashable, sorted representation
                    s = json.dumps(d, sort_keys=True)
                    if s not in seen:
                        seen.add(s)
                        unique.append(d)
                value = unique


                for item in value:
                    new_row = row.copy()
                    new_row['col_path_0_values'] = item
                    new_row['col_path_0_LIST'] = 'LIST'
                    new_rows.append(new_row)
            else:
             df.at[ix, 'col_path_0_LIST'] = 'NO LIST'





    df = pd.concat([df, pd.DataFrame(new_rows)], ignore_index=True)

    new_rows.clear()



    new_rows = []

    for i in range(max_columns):
        current_rows = df.copy()  # snapshot to iterate over

        for ix, row in current_rows.iterrows():
            value = row.get(f'col_path_{i}_values', None)


            if isinstance(value, dict):
                for k, v in value.items():
                    if isinstance(v, list):
                        # Check if list of dicts
                        if v and isinstance(v[0], dict):

                            seen = set()
                            unique = []
                            for d in v:
                                # Use json.dumps to get a hashable, sorted representation
                                s = json.dumps(d, sort_keys=True)
                                if s not in seen:
                                    seen.add(s)
                                    unique.append(d)
                            v = unique


                            for item in v:

                                new_row = add_rows(row, item, k, list_holder='LIST' )
                                new_rows.append(new_row)


                        else:
                            # Regular list (e.g., strings, ints)
                            v = v[0]

                            new_row = add_rows(row, v, k, list_holder='LIST' )
                            new_rows.append(new_row)

                    #elif isinstance(v, dict) and not v:
                       # v = 'object'
                       # new_row = add_rows(row, v, k, list_holder='NO LIST')
                        #new_rows.append(new_row)



                    else:


                        new_row = add_rows(row, v, k, list_holder='NO LIST' )
                        new_rows.append(new_row)



        df = pd.concat([df, pd.DataFrame(new_rows)], ignore_index=True)
        new_rows.clear()






    df = df.replace(r'^\s*$', np.nan, regex=True)
    df = df.reset_index(drop=True)  # ensure clean indexing
    unique_idx = df.astype(str).drop_duplicates().index  # get unique row indices
    df = df.loc[unique_idx].reset_index(drop=True) 
    


    df_red = df.drop(columns=[col for col in df.columns if col.endswith("_LIST")])

    df_red['last_valid_index'] = df_red.apply(pd.Series.last_valid_index, axis=1)

    
    df = df.join(df_red['last_valid_index'])


    return(df)



######################
# process_col_path() # 
######################

# The 'process_col_path()' function checks whether the value in a row of for one of the column paths is actually a datatype and stores this value in a column data_type and replaces the original value with NA. The data types are the lowest level values in the JSON files



# Define the data types
data_types = ['string', 'array', 'number', 'boolean', 'object']



# Define the function 'process_col_path()'
def process_col_path(df, col_path_values, data_types):
    df['data_type'] = ''

    """
    row: Rows in the dataframe
    columns: List of column names of column path columns 
    data_types: List of the values that are data types
    """

    for ix, row in df.iterrows():
        for col in col_path_values:


            #If the value stored in the column is found in the list 'data_types', 
            if row[col] in data_types:
                # this value is placed in the column 'data_type'
                value = row[col]

                df.at[ix, 'data_type'] = value
            else:
                continue



    return df


##############################
# remove_intermediate_rows() #
##############################



def remove_intermediate_rows(df):
    drop_index = []
    for ix, row in df.iterrows():
            last_value = row[f"{row['last_valid_index']}"]


            if isinstance(last_value, str):
                if last_value not in (data_types):
                        #col =  row['last_valid_index']
                        #col_level = re.findall(r'\d+', col)
                        #col_level = col_level[0]


                        #df.at[ix, f"col_path_{col_level}_LIST"] = np.nan
                         drop_index.append(ix)


            else:
                drop_index.append(ix)



    df = df.drop(drop_index)
    df = df.drop(columns=[col for col in df.columns if col.endswith("values")])


    return df



##################
# extract_path() #
##################




def extract_path(df, max_columns):

    df['path']= ''

    for ix, row in df.iterrows():
        path = []

        for col in [f"col_path_{i}" for i in range(1, max_columns)]:
            val = row[col]

            if pd.notna(val):

                path.append(str(val))



        df.at[ix, 'path'] = path




    return df




############### 
# list_path() #
###############




def list_path(df):



    df['list_path'] = ''
    df['subfield_path'] = ''
    df['column_name'] = ''
    df['var_type'] = ''

    new_rows = []
    delete_rows = []

    for ix, row in df.iterrows():

        path = row['path'] 
        found_list = False
        var_type = 'static'
        subfield_path = path
        column_name = path[-1]


        for i in reversed(range(1, len(path))):

            if row[f"col_path_{i}_LIST"] == 'LIST':

                new_row = row.copy()
                delete_rows.append(ix)
                new_row['var_type'] = 'list'
                new_row['list_path'] = path[:i]
                new_row['subfield_path'] = path[i:]
                new_row['column_name'] = path[-1]
                new_rows.append(new_row)
                found_list = True
                break

            elif row[f"col_path_{i}_LIST"] == "NO LIST":
                var_type = 'static'

                subfield_path = path

                column_name = path[-1]


            else:
                var_type = 'skip'
                subfield_path = path
                column_name = path[-1]

        if not found_list:
            df.at[ix, 'subfield_path'] = subfield_path
            df.at[ix, 'column_name'] = column_name
            df.at[ix, 'var_type'] = var_type

    df = df.drop(index=delete_rows).reset_index(drop=True)
    df = pd.concat([df, pd.DataFrame(new_rows)], ignore_index=True)
    new_rows.clear()







    return df



##################### 
# clean_and_store() #
#####################

# This function orders the columns in the DataFrame, resets the index, fills the NA and saves the DataFrame as CSV




def clean_and_store(df, df_no_data, file_name):

    """
    df: The dataframe that will be cleaned and stored
    file_name: The filename of data structure that is being processed
    """


    df = pd.concat([df, df_no_data], ignore_index=True)

    for ix, row in df.iterrows():
        if pd.isna(row['column_name']):
            df.at[ix, 'var_type'] = 'skip'


    df = df[['json_name','column_name', 'path', 'list_path', 'subfield_path', 'var_type', 'data_type', 'file_path']]
    df = df.astype(str)
    df = df.drop_duplicates()
    

    # Save the DataFrame 
    df.to_csv(f"{output_directory}/Output_" + file_name + '.csv', index=False)

    return df


######################### 
# structure_donations() #
#########################


# The structure_donations() function executes all functions above and results in a saved DataFrame for each data structure.



def structure_donations(data, col_path, max_columns):
     # Store the path to the data structure
    data = Path(data)  

    # Save teh file name of the data structure
    file_name = Path(data).stem 

    df, df_no_data = loading_data(data)
    print('FINISH: loading_data()')
    df = flatten_json(df)
    print('FINISH: flatten_json()')
    df = process_col_path(df, col_path_values, data_types)
    print('FINISH: process_col_path()')
    df = remove_intermediate_rows(df)
    print('FINISH: remove_intermediate_rows()')
    df = extract_path(df, max_columns)
    print('FINISH: extract_path()')
    df = list_path(df)
    print('FINISH: list_path()')
    df = clean_and_store(df, df_no_data, file_name)
    print('FINISH: clean_and_store()')

    del df,df_no_data, data








####################################################################################################
# Execute 'structure_donations()': Transform data structures from JSON format to tabular format    #
####################################################################################################



#Execute the 'structure_donations()' function for each file (data structure) in the input directory
for file in input_directory.iterdir():  
    if file.is_file():  
        print("--------------------------------------------------------------------------------------")
        time = datetime.datetime.now()
        print(f"{time} START PROCESSING:", file.name)

        try:
            result = structure_donations(file, col_path, max_columns)
        except Exception as e:
            print(f"Error in processing {file}: {e}")
            continue

        
        print(f"{time} FINISH PROCESSING:", file.name)
        print("--------------------------------------------------------------------------------------")
        del result
        gc.collect()




############################################################ 
# Merge all data structures into one merged_structure.csv  #
############################################################


# Get a list of all CSV files in the folder
csv_files = list(Path(output_directory).glob("*.csv"))

# Load all CSVs into a list of DataFrames
dfs = [pd.read_csv(file) for file in csv_files]

# Concatenate all DataFrames
merged_df = pd.concat(dfs, axis=0, ignore_index=True)

# Drop rows that are completely identical across all columns
merged_df = merged_df.drop_duplicates()

time = datetime.datetime.now()
print(f'{time}: Merged Structure Created')

################## 
# Id creation    #
##################



merged_df['name'] = merged_df['json_name'].str.replace(".js", "")

id_df = merged_df[['name', 'path']]
id_df = id_df.drop_duplicates()
id_df['id'] = ''


for n in range(1,max_columns):
    duplicates = id_df[id_df.duplicated(subset='id', keep=False)]

    for i, row in duplicates.iterrows():
        path = row['path']
        name = row['name']  

        if pd.notna(path):

            path =  ast.literal_eval(path)

            path_rest = path[-n:]


            if not isinstance(path_rest, list):
                path_rest = [path_rest]

            if path_rest:

                id_list = [name] + path_rest
            else:
                id_list = [name]


            new_id = ':'.join(id_list)

        else:

            new_id = name

        id_df.at[i, 'id'] = new_id  


merged_df = pd.merge(merged_df, id_df, on = ['name', 'path'], how = 'left')

col = merged_df.pop('id') 
merged_df.insert(0, 'id', col) 

time = datetime.datetime.now()
print(f'{time}: IDs Created')


###################### 
# ID duplicate flags #
######################



merged_df = merged_df.astype(str)
merged_df = merged_df.drop_duplicates()
dup = merged_df[merged_df.duplicated('id', keep= False)]
dup['duplicate_flag'] = 'Yes'
dup = dup[['id', 'duplicate_flag']]
merged_df = pd.merge(merged_df, dup, on = 'id', how = 'left')
merged_df['duplicate_flag'] = merged_df['duplicate_flag'].fillna(value = 'No')


time = datetime.datetime.now()
print(f'{time}: Duplicate Flags Created')

###################### 
# Format JSON paths  #
######################


def to_json_list(x):
    # Skip missing values
    if pd.isna(x):
        return x
    # If it's already a list, just dump
    if isinstance(x, list):
        return json.dumps(x)
    # If it's a string that looks like a list
    if isinstance(x, str) and x.strip().startswith("[") and x.strip().endswith("]"):
        try:
            return json.dumps(ast.literal_eval(x))
        except Exception:
            return x  # leave as is if parsing fails
    # Otherwise just return the string
    return x

for col in ['path', 'list_path', 'subfield_path']:
    merged_df[col] = merged_df[col].apply(to_json_list)

time = datetime.datetime.now()
print(f'{time}: JSON paths formatted')

################### 
# Clean and Save  #
###################



keep_columns = ['json_name','id', 'column_name', 
                 'path', 'list_path', 'subfield_path', 
                 'var_type', 'data_type', 'file_path', 'duplicate_flag']


merged_df = merged_df[keep_columns ]

merged_df = merged_df.drop_duplicates()

# Save the final merged DataFrame
merged_df.to_csv(f"{final_directory}/X_Merged_structures.csv", index=False)

time = datetime.datetime.now()
print(f'{time}: X_Merged_structures.csv saved')

time = datetime.datetime.now()
print(f'{time}: FINISHED PROCESSING TWITTER')

