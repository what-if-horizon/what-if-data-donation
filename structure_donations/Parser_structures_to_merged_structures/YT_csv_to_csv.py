

#  The purpose of his jupyter notebook is to parse the collected data structures in earlier iterations of utilising the data donation tool into a schema_df which can be used to inform future iterations of the data donation tool.ote that there are two notebooks to parse the Youtube data structures in the repository as the Youtube data takeout contains both CSV and JSON files. 



# importing libraries 
import pandas as pd 
import glob 
import os 
from pathlib import Path
import datetime
import warnings
warnings.filterwarnings("ignore")


time = datetime.datetime.now()
print(f'{time} START PROCESSING CSVs YOUTUBE')

# Specify the main path 
#main_path = "/home/rvissche/Nextcloud/What-If/what-if-data-donation/what-if-data-donation/structure_donations/Processed_structure_donations/Youtube/"
main_path = Path.cwd()
main_path = Path(f'{main_path}/structure_donations/Processed_structure_donations/Youtube/') 
input_directory = Path(f'{main_path}/Column_names_input')   
final_directory = Path (f'{main_path}/Column_names_final')



# Create a pattern to find all csv files in the folder
pattern = os.path.join(input_directory, "*.csv")

# Combine all csv files in a list
joined_list = glob.glob(pattern)


# Join the files
df = pd.concat(map(pd.read_csv, joined_list), ignore_index=True) 

#Drop duplicated rows
df = df.drop_duplicates() 


# Format rows
df['name'] = df['File_name'].str.replace(".csv", "")
df['id'] =   df.apply(lambda x: f"{x['name']}:{x['Column_names']}", axis = 1)
df['id'] = df['id'].str.replace(" ", "_")

df = df.drop('name', axis = 1)


# Save the DF
df.to_csv(f"{final_directory}/YT_Merged_Column_Names.csv", index=False)

time = datetime.datetime.now()
print(f'{time}: YT_Merged_Column_Names.csv saved')

time = datetime.datetime.now()
print(f'{time}: FINISHED PROCESSING YOUTUBE (CSV)')