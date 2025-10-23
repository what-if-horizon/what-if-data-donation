
import pandas as pd
from pathlib import Path 
import os
import glob
from datetime import datetime

#main_path = "/home/rvissche/Nextcloud/What-If/what-if-data-donation/what-if-data-donation/structure_donations/"

main_path = Path.cwd()
main_path = Path(f'{main_path}/structure_donations/') 

# Folder containing CSVs
folder_annotated = f"{main_path}/Annotated_Merged_Structures"

# Folder with new merged structures
folder_new = f"{main_path}/Processed_structure_donations"


############################################# 
# Load the annotated data for all platforms #
#############################################

# Dictionary to hold DataFrames
dfs_annotated = {}

for file in os.listdir(folder_annotated):
    if file.endswith(".csv"):
        name = os.path.splitext(file)[0]
        path = os.path.join(folder_annotated, file)
        dfs_annotated[name] = pd.read_csv(path)




dfs_annotated.keys()


######################################### 
# Loading the (new) merged structures   #
#########################################




dfs_new = {}

for path in glob.glob(f"{folder_new}/**/Final/*_Merged_structures.csv", recursive=True):
    name = os.path.splitext(os.path.basename(path))[0]
    dfs_new[name] = pd.read_csv(path)


YT_column = os.path.join(folder_new, "Youtube/Column_names_final/YT_Merged_Column_Names.csv")
if os.path.exists(YT_column):
    name = os.path.splitext(os.path.basename(YT_column))[0]
    dfs_new[name] = pd.read_csv(YT_column)


######################### 
# Identify the new rows #
#########################


new_rows_dict = {}

dict_dfs = {
    'YT_merged_structure_annotated': 'YT_Merged_structures',
    'IG_merged_structure_annotated': 'IG_Merged_structures',
    'TT_merged_structure_annotated': 'TT_Merged_structures',
    'FB_merged_structure_annotated': 'FB_Merged_structures',
    'YT_merged_column_names_annotated': 'YT_Merged_Column_Names'

}

for k,v in dict_dfs.items():

    dfs_annotated[f'{k}'] = dfs_annotated[k].loc[:, ~dfs_annotated[k].columns.str.startswith('Unnamed')]

    print(k)

    merge_cols = list(dfs_annotated[k].columns)

    if 'keepID' in merge_cols:
        merge_cols.remove('keepID')
    if 'keep_id' in merge_cols:
        merge_cols.remove('keep_id')
    if 'date_added' in merge_cols:
        merge_cols.remove('date_added')


    new_rows_dict[f'{v}_new'] = dfs_new[v].merge(dfs_annotated[k], how="left", on = merge_cols, indicator=True).query('_merge == "left_only"').drop(columns=["_merge"])

    date_col = 'date_added'

    if date_col not in new_rows_dict[f'{v}_new'].columns:
        new_rows_dict[f'{v}_new'][date_col] = datetime.now().strftime("%Y-%m-%d")


############################################################# 
# Append the new rows to the annotated merged structure     #
#############################################################


for k,v in dict_dfs.items():

    date_col = 'date_added'
    if date_col not in dfs_annotated[f'{k}'].columns:
         dfs_annotated[f'{k}'][date_col] = 'pre-trial'


    dfs_annotated[f'{k}'] = pd.concat([dfs_annotated[f'{k}'], new_rows_dict[f'{v}_new']], ignore_index=True)


###################################### 
# Save annotated merged structures   #
######################################


# Assume dfs_dict is your dictionary of DataFrames
for key, df in dfs_annotated.items():
    # Create a filename from the key
    filename = f"{key}.csv"
    path = os.path.join(folder_annotated, filename)

    # Save DataFrame to CSV
    df.to_csv(path, index=False)
    print(f"Saved {filename} ({len(df)} rows)")

