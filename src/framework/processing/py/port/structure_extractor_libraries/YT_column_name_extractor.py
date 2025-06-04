# importing the required modules 
import glob 
import pandas as pd 
import os
from pathlib import Path  
import zipfile

def column_names_from_zip(main_path):

    #main_path = "/home/rvissche/Documents/Data_takeout_Nienke_PRIVATE/takeout-20250604T082845Z-1-001.zip"
    main_path = main_path

    data_frame = pd.DataFrame()
    keys = []
    values = []

    with zipfile.ZipFile(main_path, 'r') as z:
        zip_name = os.path.basename(z.filename)
        zip_name = os.path.splitext(zip_name)[0]
        print(f"Opening zip-file: {zip_name}")
        # List all files in the zip
        all_files = z.namelist()
        
        # Filter CSV files
        csv_files = [f for f in all_files if f.endswith('.csv')]
        print("CSV files found:", csv_files)

        for filename in csv_files:
            key = os.path.basename(filename)
            keys.append(key)
            print(f"Reading: {key}")
            
            with z.open(filename) as f:
                # Try utf-8, fallback if needed
                try:
                    df = pd.read_csv(f)
                except UnicodeDecodeError:
                    f.seek(0)
                    df = pd.read_csv(f, encoding='latin1')
            
            values.append(df)


    csv_dict = {}
    # Using a for loop to populate the dictionary
    for i in range(len(keys)):
        csv_dict[keys[i]] = values[i]

    # Print the resulting dictionary
    print(csv_dict)

    column_names = []
    for csv in csv_dict.values():
        #print(csv.columns)
        column_names.append(csv.columns.tolist())

    column_dict = {}
    # Using a for loop to populate the dictionary
    for i in range(len(keys)):
        column_dict[keys[i]] =  column_names[i]

    print(column_dict)  

    #column_names_df =  pd.DataFrame.from_dict(column_dict)

    column_names_df = pd.DataFrame(list(column_dict.items()), columns=['Key', 'Values'])
    column_names_df = column_names_df.explode('Values')
    # Save the final merged DataFrame
    output_dir = "/home/rvissche/Nextcloud/What-If/what-if-data-donation/what-if-data-donation/structure_donations/Processed_structure_donations/"
    column_names_df.to_csv(f"{output_dir}Youtube/Column_names_output/Column_Names_YT_{zip_name}.csv", index=False)

    return  column_names_df

