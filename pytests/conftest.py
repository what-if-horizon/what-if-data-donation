import json
import logging
from pathlib import Path
from typing import NamedTuple

import gdown

BASE_FOLDER = Path.cwd() / "pytests" / "testfiles"
INPUTFILES = BASE_FOLDER / "tmp_inputfiles"


class Scenario(NamedTuple):
    input: Path
    platform: str
    id: str
    columns: list[str]
    data: list[list[str | int | float]]


def get_inputfiles():
    for f in BASE_FOLDER.glob("*.json"):
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
    if not INPUTFILES.exists():
        INPUTFILES.mkdir(parents=True, exist_ok=True)
    for fname, d in get_inputfiles():
        fn = INPUTFILES / d["input_file"]
        if not fn.exists():
            gdown.download(d["google_file_id"], str(fn), fuzzy=True)
        for output in d["expected_output"]:
            id = output["id"]
            df = output["data_frame"]
            yield f"{fname}::{id}", Scenario(
                input=fn, platform=d["platform"], id=id, columns=df["columns"], data=df["data"]
            )


def pytest_generate_tests(metafunc):
    scenarios = dict(get_scenarios())
    if "scenario" in metafunc.fixturenames:
        metafunc.parametrize("scenario", list(scenarios.values()), ids=list(scenarios.keys()))
