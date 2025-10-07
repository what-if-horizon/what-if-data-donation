# Parser Structures to Merged Structures

This folder contains jupyter notebooks to collect the structure donations (JSONs with the values masked) and create the merged structure data frames.


To obtain the full JSON path, a python script has been created for each platform separately as the JSON structure of each platform is different with its own challenges and quirks. Also, due to the deeply nested structures most existing libraries to extract JSON paths do not work. The processing output is a CSV file named [<'platform'>_Merged_Structures.csv](https://github.com/what-if-horizon/what-if-data-donation/tree/master/structure_donations/Processed_structure_donations) with the following columns:
- json_name: Name of the JSON file in which the JSON path can be found
- id: Unique ID for each data field. 
    - See below for more detail on the construction of the IDs
    - Note that due to slight differences in the JSON paths, identical data fields can have different IDs and hence need to be modified by hand
- column_name: The name of the lowest level key in the JSON path
- path: The full JSON path
- list_path: In case the value of a key is a list rather than a value, this column contains the JSON path until the list
- subfield_path: In case of a static path, this column contains the full JSON path. In case a list is included in the JSON path, the part of the JSON path enlisted is stored here. 
- var_type: Describes whether the variable is included in a list ('list') or is a regular variable ('static')
- file_path: Certain data takeouts are zipfiles consisting of a nested folder structure. The path to the JSON files are specified in this column. 
- duplicate_flag: In case there is an ID that is duplicated due to JSON paths containing keys holding identical information but different json paths. For example parts of the data can be enlisted whereas in other cases the data is not. When a duplicate ID is found, this ID is marked as 'Yes'

##### ID creation
###### Instagram
The ID for Instagram initially consist of the folder name in which the JSON is stored, the name of the json and the column name. In case this does not result into a unique ID, in the following iterations (max 4), json keys are added starting at the deepest level. If again this does not result in a unique ID, the folder one level higher is added to the ID as well. In other words the most minimal ID consist of lowest folder name + json name + column name. The maximum ID consist of the second lowest folder + lowest folder name + json name + key[1,2,3] + column name.

###### Facebook
The ID for Facebook initially consist of the folder name in which the JSON is stored, the name of the json and the column name. In case this does not result into a unique ID, in the following iterations (max 6), json keys are added starting at the deepest level. If again this does not result in a unique ID, the folder up until 3 levels higher is added to the ID as well. In other words the most minimal ID consist of lowest folder name + json name + column name. The maximum ID consist of the second lowest folder[1,2,3] + lowest folder name + json name + key[1,2,3] + column name.

##### TikTok
The ID for TikTok initially consist of the highest level key in combination with the lowest level key. If this does not result in an unique ID, more keys are added until the maximum number of keys present in the JSON is reached or a unique ID has been established. 


##### Twitter
The ID for Twitter initially consist of the name of the Java script file combined with the name of the lowest level key. In case this does not result in an unique ID, more keys are added starting at the deepest level until the maximum number of keys has been reached or an unique ID has been created.

##### Youtube 
###### JSON
The ID for the Youtube JSONs initially consist of the name of the Java script file combined with the name of the lowest level key. In case this does not result in an unique ID, more keys are added starting at the deepest level until the maximum number of keys has been reached or an unique ID has been created.
###### CSV
The ID for the Youtube CSV consist of the name of the CSV and the column name. 


#### The code
The jupyter notebooks to generate the <'platform'>_Merged_Structures.csv can be found [here](https://github.com/what-if-horizon/what-if-data-donation/tree/master/structure_donations/Parser_structures_to_schema_df) in the GIT repository. After loading the data structures, the code flattens the JSON while taking into account and labeling the enlisted JSON paths. This is done for each data structure independently after which the CSVs containing the flattened JSON files are merged and the IDs are generated. 