# The data donation task

The data donation task is front end that guides participants through the data donation steps, used in conjunction with Next.
Next is a software as a service platform developed by [Eyra](https://eyra.co/) to facilitate scientific research.

## Documentation

Because we are extracting fields from five platforms in five different languages, we decided to introduce a declarative 'Entry' to represent a table to be extracted. 
Each entry represents a tree of fields to be extracted from a target json structure and converted into a tabular form.
See [parsers.py](https://github.com/what-if-horizon/what-if-data-donation/blob/master/packages/python/port/helpers/parsers.py) for the Entry class definition 
and especially the `extract_rows` method that is responsible for extracting the tabular values from the json tree. 
All platforms are essentially thin wrappers around a call to that function for each entry. 

Entries are generated automatically and placed in [entries_data.py](https://github.com/what-if-horizon/what-if-data-donation/blob/master/packages/python/port/helpers/entries_data.py).
For an overview of the generation process, see the [workflow documentation](https://github.com/what-if-horizon/what-if-data-donation/blob/master/workflow_data_donation_tool.md).

Note: This repository is based on the [original data donation repository published by d3i](https://github.com/d3i-infra/data-donation-task). 
Please see that repository, and especially their [documentation](https://d3i-infra.github.io/data-donation-task/) for general information about the data donation task and software. 

## Installation and local testing

In order to start a local instance of the data donation task go through the following steps:

0. Pre-requisites

   - Fork or clone this repo
   - Install [Node.js](https://nodejs.org/en)
   - Install [Python](https://www.python.org/)
   - Install [Poetry](https://python-poetry.org/)

1. Install dependencies & tools:

   ```sh
   npm install
   ```

2. Start the local web server:

   ```sh
   npm run start
   ```

3. You can now go to the browser: [`http://localhost:3000`](http://localhost:3000).

If the installation went correctly you should be greeted with a mock data donation study. 
For detailed installation instructions see the [documentation](https://d3i-infra.github.io/data-donation-task/).

 citation details in the [`CITATION.cff`](CITATION.cff) file.
