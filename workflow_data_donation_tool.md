# Workflow Data Donation Tool

This data donation tool in an extension of the Feldspar repository which can be implemented in the Eyra environment to collect data donations. The aim of this extension in to collect data donations with the highest standards for data privacy while reducing the risk of omitted variables or unnecessary data loss as much as possible. The workflow of this tool consists of four parts: 1. Data structure collection, 2.Processing of data structures, 3. Variable selection by researchers, and 4. Implementation of data donation tool. In short, the idea behind this tool is to obtain the data structures of social media takeouts to specifically inform the data donation tool running on the participant's local machine which data should be collected from their social media takeout. In this way, we avoid collecting highly personal or sensitive data. In this workflow description we will go trough the rationale behind each step, how to perform the step and how to asses the step in case of problems during the data collection. 

## 1. Data structure collection
### The rationale
Social media takeout data contains highly sensitive and private data. Think about IP addresses, contact details and photos. Moreover, according to the article 5(1)(c) form the GDPR, which states: “Personal data shall be adequate, relevant and limited to what is necessary in relation to the purposes for which they are processed (‘data minimisation’).”, only data that will be of use for achieving the goal of the project should be collected. To do so, we need the exact variable names and as most data takeouts are provided in JSON format, the exact json paths to these variables,  to only collect data we intent to collect. Unfortunately, the social media takeout formats and structures are not consistent over time and location. Hence, we need to collect a representative sample of these social media structures to properly select the variables we intend to collect and avoid unintentionally omitted variables. 

### The strategy 
The strategy to collect the social media data takeout structures is rather simple. When participants upload their social media data takeout in the donation tool, all keys in te case of JSON and all column names in the case of CSVs are saved with the values masked through replacing the real data with a string specifying the data type (eg. 'string', 'boolean'). These data structures can then be used to inform the data donation tool for the next iteration of collecting data using the tool. When there are no data structures available yet, we propose to run a test round with a small but representative sample of participants to obtain these structures. During the data collection process, the data structures should be used to update the tool with the latests variables and paths. In the future, we hope that each data donation study will make the data structures publically available to support new studies. 

### The code
The python code which does the masking of real values in the social media can be found [here](https://github.com/what-if-horizon/what-if-data-donation/tree/master/structure_donations/Structure_extractor_libraries) in the GIT repository. There is a specific script for each of the social media platforms. The code recursively loops through all JSON files in the zip file (in case of multi-document takeouts) and consequently trough all values in the JSON, replacing them with a string indicating the data type.

## 2. Processing of data structures
### The rationale
According to the [include GDPR on informed consent], we need to inform the participants clearly on what data they will be donating. As JSON files are not easily interpretable by humans, the data should be transformed to a more easily readable tabular format. To do so we need to obtain the full JSON path to each lowest level key to be able to transform the data to tabular format. Also, as only necessary and non highly sensitive or private data should be selected, the researcher needs to make decisions on exactly which data to obtain and which data to exclude. Due to differences in data takeout structures, the JSON paths might differ slightly but point to the same data. Therefore, we generate IDs for each data field that are easy to interpret for researchers. Using the IDs the researcher decides what data to collect.

### The strategy
To obtain the full JSON path, a python script has been created for each platform separately as the JSON structure of each platform is different with its own challenges and quirks. Also, due to the deeply nested structures most existing libraries to extract JSON paths do not work. The processing output is a CSV file named [<platform>_Merged_Structures.csv](https://github.com/what-if-horizon/what-if-data-donation/tree/master/structure_donations/Processed_structure_donations) with the following columns:
- json_name: Name of the JSON file in which the JSON path can be found
- id: Unique ID for each data field. 
    - The IDs are generated using the first folder name of teh file path or the first key of the JSON path, adding an extra key, starting at the lowest level, until an ID has been generated that is ID in the <platform>_Merged_Structures.csv
    - Note that due to slight differences in the JSON paths, identical data fields can have different IDs and hence need to be modified by hand
- column_name: The name of the lowest level key in the JSON path
- path: The full JSON path
- list_path: In case the value of a key is a list rather than a value, this column contains the JSON path until the list
- subfield_path: In case of a static path, this column contains the full JSON path. In case a list is included in the JSON path, the part of the JSON path enlisted is stored here. 
- var_type: Describes whether the variable is included in a list ('list') or is a regular variable ('static')
- file_path: Certain data takeouts are zipfiles consisting of a nested folder structure. The path to the JSON files are specified in this column. 
- duplicate_flag: In case there is an ID that is duplicated due to JSON paths containing identical keys but different structures as in one case parts of the data can be enlisted whereas in other cases the data is not. When a duplicate ID is found, this ID is marked as 'Yes'

### The code
The jupyter notebooks to generate the <platform>_Merged_Structures.csv can be found [here](https://github.com/what-if-horizon/what-if-data-donation/tree/master/structure_donations/Parser_structures_to_schema_df) in the GIT repository. After loading the data structures, the code flattens the JSON while taking into account and labeling the enlisted JSON paths. This is done for each data structure independently after which the CSVs containing the flattened JSON files are merged and the IDs are generated. 


## 3. Variable selection by researchers
### The rationale 
As explained above only relevant non highly personal data should be collected. The decision of which variables to collect should be made by the researcher

### The strategy
The researcher creates an extra column in the <platform>_Merged_Structures.csv and only pastes the ID in that column in case she wishes to collect that variable. In case she finds different IDs pointing at the same data, she decides on the final ID and replaces the original ID. It is highly important that the row is kept with the new ID as the differing JSON path is important to maintain as to collect the variable correctly. The annotated <platform>_Merged_Structures.csv can be found [here](https://github.com/what-if-horizon/what-if-data-donation/tree/master/structure_donations/Annotated_schema_df) 

### The code 
The python script [TO BE DETERMINED] deselects the rows without an ID as this indicates that the variable should not be collected. The <platform>_Merged_Structures_Reduced.csv is saved here [NOT READY]


## 4. Implementation of data donation tool
### The rationale

### The strategy

### The code

