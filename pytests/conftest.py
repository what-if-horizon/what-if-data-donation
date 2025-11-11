import functools
import importlib
import json
import logging
from pathlib import Path
from typing import NamedTuple

from pytest import fixture

FOLDER_SCENARIOS = Path.cwd() / "pytests" / "scenarios"
TESTFILES = Path.cwd() / "pytests" / "testfiles"


class Scenario(NamedTuple):
    input: Path
    platform: str
    id: str
    columns: list[str]
    data: list[list[str | int | float]]


def inputfiles():
    return dict(
        Tiktok="pytests/public_testfiles/TT_user_data_tiktok.json",
        Twitter="pytests/public_testfiles/X_public_test_files.zip",
        Facebook="pytests/public_testfiles/FB_public_test_file.zip",
        Instagram="pytests/public_testfiles/IG_public_test_file.zip",
        Youtube="pytests/public_testfiles/YT_public_test_file.zip",
    )


def get_scenario_files():
    for f in FOLDER_SCENARIOS.glob("*.json"):
        with f.open() as jf:
            yield f.name, json.load(jf)


def get_scenarios():
    """Generate the test scenarios

    pytests/testfiles should contain test specifications structured as follows:

    {
        "input_file": <name of the input file>
        "platform": <"twitter", "tiktok" etc>
        "google_file_id": <google drive share link for the file>
        "expected_output": [
            {
                "id": <table id>,
                "data_frame": { # output of df.to_dict(orient='split', index=False)
                    "columns": [<column names>],
                    "rows": [[<values>]]
                }
            }, # etc, one entry per table
        ]
    }

    The file will be downloaded using the google share link to the INPUTFILES folder if needed.
    Then, each tables in the "expected_output" key will generate one scenario
    specifying a table with columns and rows (values)
    """
    for fname, d in get_scenario_files():
        for output in d["expected_output"]:
            id = output["id"]
            df = output["data_frame"]
            yield f"{fname}::{id}", Scenario(
                input=Path(d["input_file"]),
                platform=d["platform"],
                id=id,
                columns=df["columns"],
                data=df["data"],
            )


def pytest_generate_tests(metafunc):
    scenarios = dict(get_scenarios())
    if "scenario" in metafunc.fixturenames:
        metafunc.parametrize(
            "scenario", list(scenarios.values()), ids=list(scenarios.keys())
        )


@functools.lru_cache()
def get_tables(platform, input):
    flow_module = importlib.import_module(f"port.donation_flows.{platform}")
    flow = flow_module.create_donation_flow([str(input)])
    return {table.id: table for table in flow.tables}
