<div align="justify">
 
# How to use and implement this human in the loop data donation tool
This data donation tool is an extension of the Feldspar repository, designed for integration into the Eyra environment to facilitate the collection of data donations. The goal of this extension is to collect data donations according to the highest standards of data privacy, while minimizing the risk of omitted variables and unnecessary data loss. We depart from the code [Next and Port did X] to add a workflow that minimizes manual work for researchers and reduces even more the likelihood of data loss.   

This documentation serves as a step-by-step guide to: 1) Explain the rationale and strategy behind each component of the tool, and 2) Describe how to use and update the tool during production.

In essence, this workflow enables researchers to start from real, anonymized data downloaded from social media platforms and automatically generate the Python code needed to parse and structure that data. This approach greatly reduces manual work and minimizes errors that typically arise from inconsistencies in the data structures and field names provided by different platforms.

The documentation is organized as follows: First, we describe each component of the tool — from anonymizing raw data to generating the final tables — including the expected inputs and outputs, a brief conceptual explanation, and the code to be executed. Then, we explain how to update the tool with additional anonymized data, allowing researchers to expand or adjust the parsing logic with minimal manual coding.

## Workflow Data Donation Tool

 The workflow of this tool consists of four parts: 1. Data structure collection, 2.Processing of data structures, 3. Variable selection by researchers, and 4. Implementation of data donation tool. In short, the idea behind this tool is to obtain the data structures of social media takeouts to specifically inform the data donation tool running on the participant's local machine which data should be collected from their social media takeout. In this way, we avoid collecting highly personal, sensitive or unnecessary data. In this workflow description we will go trough the rationale behind each step, how to perform the step and how to asses the step in case of problems during the data collection. 

![Workflow](workflow_visuals/workflow.png)
![Git](workflow_visuals/git_repository.png)

### 1. Masked Data Structure Collection
- **Input**: Zip folder including JSON files (YT, FB, IG, X) or JSON (TT) containing the full data takeout
- **Output**: JSON containing the masked data structures 
#### The Rationale
Social media takeout data contains highly sensitive and private data. Think about IP addresses, contact details and photos. Moreover, according to the article 5(1)(c) of the GDPR, which states: “Personal data shall be adequate, relevant and limited to what is necessary in relation to the purposes for which they are processed (‘data minimisation’).”, on other words, only data that will be of use for achieving the goal of the project should be collected. To do so, we need the exact variable names and as most data takeouts are provided in JSON format, the exact json paths to these variables,  to only collect data we intent to collect. Unfortunately, the social media takeout formats and structures are not consistent over time, location and platform. Hence, we need to collect a representative sample of these social media structures to properly select the variables we intend to collect and avoid unintentionally omitted variables. 

#### The Strategy 
The strategy to collect the social media data takeout structures is rather simple. When participants upload their social media data takeout in the donation tool, all keys in te case of JSON and all column names in the case of CSVs are saved with the values masked through replacing the real data with a string specifying the data type (eg. 'string', 'boolean'). These data structures are then used to inform the data donation tool for the next iteration of collecting data using the tool. When there are no data structures available yet, we run a test round with a small but representative sample of participants to obtain these structures. During the data collection process, the data structures should be used to update the tool with the latests variables and paths. In the future, we hope that each data donation study will make the data structures publicly available to support new studies. 

#### The Code
The python code which does the masking of real values in the social media can be found [here](https://github.com/what-if-horizon/what-if-data-donation/tree/master/structure_donations/Structure_extractor_libraries) in the GIT repository. There is a specific script for each of the social media platforms. The code recursively loops through all JSON files in the zip file (in case of multi-document takeouts) and consequently trough all values in the JSON, replacing them with a string indicating the data type.


### 2. Mapping Data Structures 
- **Input**: JSONs containing the masked data structures per platform per participant
- **Output**: One CSV per platform containing the file paths to the different JSON files and the consequent JSON paths to the lowest key
#### The Rationale
To comply with rules on informed consent we need to inform the participants clearly on what data they will be donating. As JSON files are not easily interpretable by humans, the data should be transformed to a more easily readable tabular format. To do so we need to obtain the full JSON path to each lowest level key to be able to transform the data to tabular format. Also, as only necessary and non highly sensitive or private data should be selected, the researcher needs to make decisions on exactly which data to obtain and which data to exclude. Due to differences in data takeout structures, the JSON paths might differ slightly but point to the same data. Therefore, we generate IDs for each data field that are easy to interpret for researchers. Using the IDs the researcher decides what data to collect.

#### The Strategy
To obtain the full JSON path, a python script has been created for each platform separately as the JSON structure of each platform is different with its own challenges and quirks. Also, due to the deeply nested structures most existing libraries to extract JSON paths do not work. The processing output is a CSV file named [<'platform'>_Merged_Structures.csv](https://github.com/what-if-horizon/what-if-data-donation/tree/master/structure_donations/Processed_structure_donations) with the following columns:
- **json_name**: Name of the JSON file in which the JSON path can be found
- **column_name**: The name of the lowest level key in the JSON path
- **path**: The full JSON path
- **list_path**: In case the value of a key is a list rather than a value, this column contains the JSON path until the list
- **subfield_path**: In case of a static path, this column contains the full JSON path. In case a list is included in the JSON path, the part of the JSON path enlisted is stored here. 
- **var_type**: Describes whether the variable is included in a list ('list') or is a regular variable ('static')
- **file_path**: Certain data takeouts are zipfiles consisting of a nested folder structure. The path to the JSON files are specified in this column. 
- **duplicate_flag**: In case there is an ID that is duplicated due to JSON paths containing keys holding identical information but different json paths. For example parts of the data can be enlisted whereas in other cases the data is not. When a duplicate ID is found, this ID is marked as 'Yes'
- ***id**: Unique ID for each data field. 
    - See below for more detail on the construction of the IDs
    - Note that due to slight differences in the JSON paths, identical data fields can have different IDs and hence need to be modified by hand


> **ID creation**
> ###### Instagram
> The ID for Instagram initially consist of the folder name in which the JSON is stored, the name of the JSON and the column name. In case this does not result into a unique ID, in the following iterations (max 4), JSON keys are added starting at the deepest level. If again this does not result in an unique ID, the folder one level higher is added to the ID as well. In other words the most minimal ID consist of lowest folder name + JSON name + column name. The maximum ID consist of the second lowest folder + lowest folder name + json name + key[1,2,3] + column name.
>
>###### Facebook
>The ID for Facebook initially consist of the folder name in which the JSON is stored, the name of the json and the column name. In case this does not result into a unique ID, in the following iterations (max 6), json keys are added starting at the deepest level. If again this does not result in a unique ID, the folder up until 3 levels higher is added to the ID as well. In other words the most minimal ID consist of lowest folder name + json name + column name. The maximum ID consist of the second lowest folder[1,2,3] + lowest folder name + json name + key[1,2,3] + column name.
>
>###### TikTok
>The ID for TikTok initially consist of the highest level key in combination with the lowest level key. If this does not result in an unique ID, more keys are added until the maximum number of keys present in the JSON is reached or a unique ID has been established. 
>
>###### Twitter
>The ID for Twitter initially consist of the name of the Java script file combined with the name of the lowest level key. In case this does not result in an unique ID, more keys are added starting at the deepest level until the maximum number of keys has been reached or an unique ID has been created.
>
>###### Youtube 
>- **JSON**:
>The ID for the Youtube JSONs initially consist of the name of the Java script file combined with the name of the lowest level key. In case this does not result in an unique ID, more keys are added starting at the deepest level until the maximum number of keys has been reached or an unique ID has been created.
>- **CSV**:
The ID for the Youtube CSV consist of the name of the CSV and the column name. 


#### The Code
To generate the <'platform'>_Merged_Structures.csv, run the [structure_parsers.py](.). After loading the data structures, the code flattens the JSON while taking into account and labeling the enlisted JSON paths. This is done for each data structure independently after which the CSVs containing the flattened JSON files are merged and the IDs are generated. 

```
python3 structure_donations/structure_parsers.py
```

### 3. Variable Selection by Researchers (manual annotation)
- **Input**: CSV per platform containing the merged data structures
- **Output**:  CSV per platform containing the merged data structures including a column KeepID containing the IDs of the variables that should be collected

#### The Rationale 
As explained above only relevant non highly personal data should be collected. The decision of which variables to collect should be made by the researcher.

#### The Strategy
The researcher merges new rows including a timestamp of the <'platform'>_Merged_Structures.csv to the [<'platform'>_Merged_Structures_Annotated.csv](https://github.com/what-if-horizon/what-if-data-donation/tree/master/structure_donations/Annotated_schema_df) using the he [updating_annotations.py](https://github.com/what-if-horizon/what-if-data-donation/blob/master/structure_donations/Updating_merged_structures/Updating_merged_structures_annotated.ipynb).  The researcher goes trough the new rows and pastes the ID in the 'KeepID' column in case she wishes to collect that variable. In case she finds different IDs pointing at the same data, she decides on the final ID and replaces the original ID. It is highly important that the row is kept with the new ID as the differing JSON path is important to maintain as to collect the variable correctly. 

#### The Code
The [updating_annotations.py](.) performs an anti-join between the <'platform'>_Merged_Structures_Annotated.csv and the newly generated <'platform'>_Merged_Structures.csv to indicate the new rows and provide a timestamp. Then, the new rows are appended to the [<'platform'>_Merged_Structures_Annotated.csv](https://github.com/what-if-horizon/what-if-data-donation/tree/master/structure_donations/Annotated_schema_df)

```
python3 structure_donations/updating_annotations.py
```


### 4. Implementation of Data Donation Tool
- **Input**: Annotated merged structure CSVs
- **Output**: Data donations flattened into multiple interpretable tables 

#### The Rationale
To make the data interpretable for participants — and to give them a fair opportunity to opt out of specific information — the raw JSON files provided by platforms must be flattened into tabular form.

While Port (Boeschoten et al., 2023) in conjunttion with Next defines the overall architecture of the Data Donation Tool, researchers are responsible for writing a Python script that specifies which data to extract and how to parse it for each platform and language analyzed.

This process is challenging and time-consuming because of the extensive variation in data structures across and within social media companies. Folder names, JSON file names, internal paths, and key names all vary inconsistently — introducing substantial complexity and risk of error.

To address this, we developed a method to automatically generate the necessary parsing logic. The approach relies on a CSV file describing the structure of each platform’s data and uses it to generate Python objects that contain detailed parsing instructions for each JSON file (or for tabular data, in the case of TikTok).

This modular approach significantly reduces manual coding effort, minimizes structural errors across platforms, and ensures reproducibility in how data is parsed and flattened.

#### The Strategy
1) **Entry Generation** – We use the script generate_entries.py to generate what we call entries. The input to this script is the annotated merged structure CSV file for a given platform (e.g., Facebook_Merged_Structures_Annotated.csv). Variables marked with an ID in the KeepID column are selected as those to be retained.
The CSV includes information about the data’s nested structure — specifying both the containing file and the exact path to each target variable within it.

2) **Entry Creation** – The script processes this information to create Entry objects. Each Entry defines the properties of every variable to extract, its path within the original JSON file, and the name of the resulting table. These entries are automatically saved in the file entries_data.py.

3) **Data Extraction and Table Generation** – The generated entries are then imported into the platform-specific donation flow scripts (e.g., facebook.py, tiktok.py).
These scripts orchestrate the entire process — locating the data files, applying the parsing logic described by each Entry, and constructing the final interpretable tables for donation.

#### The Code
The annotated merged structure CSVs are used as input to run the [generate_entries.py](https://github.com/what-if-horizon/what-if-data-donation/blob/master/structure_donations/generate_entries.py) (structure_donations/generate_entries.py) which outputs the entries_data.py. Only variables specified in the 'KeepID' column are included.  This entries_data.py script serves as input for the [donation flow scripts](https://github.com/what-if-horizon/what-if-data-donation/tree/master/packages/python/port/donation_flows) which flatten the JSONs into tables and provide these tables to the participants in the user interface. To generate these entries, just run the following code:

```
python3 structure_donations/generate_entries.py
```


## Updating the Data Donation Tool 
Due to the novelty of the strategy applied in this data donation tool, we need to run through two different phases to collect sufficient data structures to execute the tool with minimal data loss. The phases are as follows: 
1. **Collecting Masked Data Structures**: Due to differences in data takeout across platforms, each countries and over time, we first collect masked data structures (JSON structures of the data takeouts with the values containing true data masked out) The main goal of this phase is to collect a representative sample of data structures. During this phase the tool should be administered to a small but representative sample of respondents in each of the participating countries. This phase is optional to a certain extend. In case there has been a recent data donation study and the masked structures have been obtained, these can be re-used to inform the data donation tool. However, in case no such recent data is available, we highly recommend  collecting recent data structures as using old data structures might result in not capturing all data. We would like to urge researchers who have collected masked data structures to make them publicly available. . 
2. **Production phase**: During this phase the tool will be administered to the full panel of participants who will donate their data takeouts. 

During the data collection, the data donation tool needs to be updated after each newly received batch of data donation This updating entails three main steps: 1. Obtain the newly donated masked data structures from the Yoda environment, 2. updating the the  <'platform'>_Merged_Structures.csv; 3. updating the  <platform>_Merged_Structures_Annotated.csv; and 4. Rerun the generate_entries.py 


### How To Update the Data Donation Tool
During the test phase and the production phase, the tool needs to be updated in regular intervals to obtain optimal benefit from the donated data structures.

#### 1. Obtain the newly donated masked data structures from the Yoda environment
NOT READY

#### 2. Updating the  <'platform'>_Merged_Structures.csv
1. Execute the [structure_parsers.py](.) (structure_donations/structure_parsers.py) from the repository root
```
python3 structure_donations/structure_parsers.py
```

2. Check if the [merged structure csv](https://github.com/what-if-horizon/what-if-data-donation/tree/master/structure_donations/Processed_structure_donations) (structure_donations/Processed_structure_donations/<'platform'>/Final) has been updated correctly. 


#### 3. Updating the  <'platform'>_Merged_Structures_Annotated.csv
1. Execute the [updating_annotations.py](.)
```
python3 structure_donations/updating_annotations.py
```
2. Check the [annotated merged structures](https://github.com/what-if-horizon/what-if-data-donation/tree/master/structure_donations/Annotated_Merged_Structures) (structure_donations/Annotated_Merged_Structures) to see if new rows are added
3. Copy the IDs from the variables that should be collected into the 'KeepID' column

![Updating](workflow_visuals/updating.png)

#### 4. Rerun the generate_entries.py
Rerun the [generate_entries.py](https://github.com/what-if-horizon/what-if-data-donation/blob/master/structure_donations/generate_entries.py) (structure_donations/generate_entries.py) to update the entries_data.py 
![Workflow](workflow_visuals/workflow.png)

```
python3 structure_donations/generate_entries.py
```

</div>




