# importing the required modules 
import pandas as pd 
import os
from pathlib import Path  
import zipfile
import gc

###################################################
# Extract CSVs from ZIP file
###################################################

def structure_from_zip(data):
    zip_name = Path(data).stem 

    df_column_names = pd.DataFrame()
    df_column_names['File_name'] = ''
    df_column_names['Column_names'] = ''
    

    with zipfile.ZipFile(data, 'r') as z:
        # List all files in the zip
        all_files = z.namelist()
 
        
        # Filter CSV files
        csv_files = [f for f in all_files if f.endswith('.csv')]

        for filename in csv_files:
            file_name = os.path.basename(filename)
            
            with z.open(filename) as f:
                # Try utf-8, fallback if needed
                try:
                    df = pd.read_csv(f)
                except UnicodeDecodeError:
                    f.seek(0)
                    df = pd.read_csv(f, encoding='latin1')
            
            column_names = df.columns

            # Add a row missing one column
            new_row = {'File_name': file_name, "Column_names": column_names}  

            df_column_names = pd.concat([df_column_names, pd.DataFrame([new_row])], ignore_index=True)

        df_column_names = df_column_names.explode("Column_names")


    print('FINSIH:', zip_name)
    return df_column_names




     

