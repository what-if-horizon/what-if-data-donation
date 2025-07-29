# Unit tests for WHAT-IF Data Donatino

This folder contains the unit tests for WHAT-IF data donation. These are based on pytest using scenario-based parametrization. 

# Installation and running

To install and run the tests:

```{sh}
pip install -e .[dev]   # if needed, this will install pytest based on the dev requirements in pyproject.toml
pytest
```

or

```{sh}
pip install -e '.[dev]'  
pytest
```

### Details:

The setup is a bit non-standard as we're not really testing code paths, but rather expected input-output pairs. 
So, the idea is to encode 'scenarios' as json files in [pytests/scenarios](pytests/scenarios).

For example, [pytests/scenarios/user_data_tiktok.json]([pytests/scenarios/user_data_tiktok.json]) creates a scenario for tiktok 
with a (public) input file [pytests/public_testfiles/user_data_tiktok.json](pytests/public_testfiles/user_data_tiktok.json) and lists expected output for a number of tables. 

These scenarios are read by [pytests/conftest.py](pytests/conftest.py) to create Scenario objects and use them to parametrize any unit test which asks for a 'scenario' fixture. 
The actual tests are run by [pytests/test_extract.py](pytests/test_extract.py) which is called once for each Scenario, testing whether a single table is extracted as expected

### Public and private test data

Ideally, the unit tests would work on completely non-private data that can be added to this repository.
However, since takeout data by its nature is sensitive, it is also possible to use non-public test data.
Practically, any input file specified in a scenario that cannot be found will result in a warning and these tests are skipped. 

Please be **very careful** to check any test files for personal data (IP addresses, usernames, email addresses, phone numbers etc) before committing to the repository!

### Generating test scenarios

To help with generating scenario files, you can use the [pytests/create_scenario.py](pytests/create_scenario.py) helper script. 

This script takes the platform and inputfile as arguments, and will print a scenario json to the command line
(so you can save by appending `> /path/to/destination.json`).

You can also list the table IDs to generate (to only generate one or some tables). 
Finally, you can use `--list-tables` to print a list of all table ids (and sizes) on the command line. 

```{sh}
$ python pytests/create_scenario.py --help
usage: create_scenario.py [-h] [--list-tables]
                          {tiktok,facebook,tiktok,twitter,youtube} inputfile [tables ...]

Create scenario json files for takeout unit tests You can use this helper script to create
a json file with some or all tables from an input file. This json file can then be edited
and/or placed in pytests/scenarios to be included as a unit test. If the input file is not
included in the repository, it will be skiped with a warning if it doesn't exist. If also
adding the test file to the repo, please be **very careful** to check it for personal data
(IP addresses, usernames, email addresses, phone numbers etc) before committing!

positional arguments:
  {tiktok,facebook,tiktok,twitter,youtube}
  inputfile             The path or name of the donation file (i.e. .zip or .json)
  tables                Specify table ids to extract (default extracts all tables)

options:
  -h, --help            show this help message and exit
  --list-tables         List only existing table ids and size instead
```

Example usage:
List all table ids in the user_data_tiktok.json input file:
```{sh}
$ python pytests/create_scenario.py tiktok pytests/public_testfiles/user_data_tiktok.json --list-tables
```
Extract all or some tables into a scenario:
```{sh}
$ python pytests/create_scenario.py tiktok pytests/public_testfiles/user_data_tiktok.json > /tmp/scenario.json
$ python pytests/create_scenario.py tiktok pytests/public_testfiles/user_data_tiktok.json activity_summary follower_list > /tmp/scenario2.json
```
