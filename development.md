## Updating the Data Donation Tool 
Due to the novelty of the strategy applied in this data donation tool, we need to run through three different phases to collect sufficient data structures to execute the tool with minimal data loss. The phases are as follows:
1. **Pre-production phase**: In this phase we manually collect data takeouts and convert them into merged data structures. The merged structures are used to inform the tool on what and how to retrieve the data from the data takeouts. This is needed to be able to execute the tool for the test phase. The main goal of this phase is to design and test the tool. 
2. **Test phase**: As the manually collected data takeouts are not sufficient to capture all data structures for each platform, each country and over time, we do a test phase. The main goal of this phase is to collect a more representative sample of data structures and to test the functionality of the tool. During this phase the tool will be administered to a small but representative sample of respondents in each of the participating countries. 
3. **Production phase**: During this phase the tool will be administered to the full panel of participants who will donate their data takeouts. 

During the data collection, the data donation tool needs to be updated after each newly received batch of data donation This updating entails three main steps: 1. updating the the  <'platform'>_Merged_Structures.csv; 2. updating the  <platform>_Merged_Structures_Annotated.csv; 3. Rerun the generate_entries.py and 4. performing an end-to-end integration test.

### Pre-production phase
As the data donation tool needs masked data structures to be executed, before going into the test-production phase, some data takeouts have been manually collected, masked and used to create the merged data structures. As the pre-production phase cannot be done fully automated, the workflow for the pre-production phase is somewhat different than for the test-production and production phase.

#### 1. Masking Data Structures
1. Create a folder on your local machine named 'Raw' using this file path structure_donations/Processed_structure_donations/<'platform'>/Raw
    - The gitignores contains instructions to never push the 'Raw' folder to git to avoid accidental pushing of private and sensitive data to git
2. Execute the [structure_extractor_notebooks](.) (structure_donations/Structure_extractor_notebooks)
3. Check the [masked data structures](https://github.com/what-if-horizon/what-if-data-donation/tree/master/structure_donations/Processed_structure_donations) (structure_donations/Processed_structure_donations/<'platform'>/Input)

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

´´´
python3 structure_donations/generate_entries.py
´´´

### Test phase and Production phase
During the test phase and the production phase, the tool needs to be updated in regular intervals to obtain optimal benefit from the donated data structures.

#### 1. Obtain the newly donated data structures from the Yoda environment
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
