"""Create scenario json files for takeout unit tests

You can use this helper script to create a json file with some or all tables from an input file.
This json file can then be edited and/or placed in pytests/scenarios to be included as a unit test.

If the input file is not included in the repository, it will be skiped with a warning if it doesn't exist.
If also adding the test file to the repo, please be **very careful** to check it for personal data
(IP addresses, usernames, email addresses, phone numbers etc) before committing!
"""

import argparse
import importlib
import json
import logging
import sys
from io import StringIO
from pathlib import Path
from venv import create

import pandas as pd
from port.api.d3i_props import PropsUIPromptConsentFormViz  # type: ignore


def extract_tables(flow: PropsUIPromptConsentFormViz, tables: list[str] | None):
    for table in flow.tables:
        df = table.data_frame.to_dict(orient="split", index=False)
        if tables and table.id not in tables:
            continue
        yield dict(id=table.id, data_frame=df)


def get_flow(platform: str, inputfile: Path) -> PropsUIPromptConsentFormViz:
    flow_module = importlib.import_module(f"port.donation_flows.{platform}")
    return flow_module.create_donation_flow([str(inputfile)])


def list_tables(platform: str, inputfile: Path):
    flow = get_flow(platform, inputfile)
    for table in flow.tables:
        yield table.id, table.data_frame.shape


def create_scenario(platform: str, inputfile: Path, tables: list[str] | None):
    flow = get_flow(platform, inputfile)
    tables = list(extract_tables(flow, tables))
    return dict(input_file=str(inputfile), platform=platform, expected_output=tables)


class Renderers:
    def json(scenario, file):
        json.dump(scenario, file, indent=4)

    def html(scenario, file):
        print(
            """<html><head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <style>h1 {padding:.3em}</style>
    </head><body><div class='container-fluid'>""",
            file=file,
        )
        for table in scenario["expected_output"]:
            print(f"<h1>Table '{table['id']}'</h1>", file=file)
            df = pd.DataFrame(data=table["data_frame"]["data"], columns=table["data_frame"]["columns"])
            print(
                df.to_html(
                    border=False,
                    index=False,
                    justify="right",
                    classes="thead-dark table-striped table-bordered table-sm table-hover",
                ),
                file=file,
            )
        print("</div></body></html>", file=file)

    def md(scenario, file):
        for table in scenario["expected_output"]:
            print(f"\n# Table '{table['id']}'\n", file=file)
            df = pd.DataFrame(data=table["data_frame"]["data"], columns=table["data_frame"]["columns"])
            print(df.to_markdown(), file=file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("platform", choices=["tiktok", "facebook", "instagram", "twitter", "youtube"])
    parser.add_argument("inputfile", help="The path or name of the donation file (i.e. .zip or .json)", type=Path)
    parser.add_argument(
        "outputfile",
        help="The path or name of the output file (i.e. .json, .html, .md), or '-' to print to stdout",
    )

    parser.add_argument("tables", nargs="*", help="Specify table ids to extract (default: extracts all tables)")
    parser.add_argument(
        "--list-tables", "-l", action="store_true", help="List only existing table ids and size instead"
    )
    parser.add_argument(
        "--format", "-f", choices=["json", "html", "md"], help="Use this format (default: from outfile extension)"
    )

    args = parser.parse_args()

    logging.basicConfig(format="[%(levelname)-7s:%(name)-15s] %(message)s", level=logging.INFO)

    # Make inputfile relative to project root
    try:
        inputfile: Path = args.inputfile.resolve().relative_to(Path.cwd())
    except ValueError as e:
        logging.warning(f"Could not make relative path, so scenario contains an absolute path: {e}")
        inputfile = args.inputfile.resolve()
    if not inputfile.exists():
        raise FileNotFoundError(f"Cannot find input file {inputfile}")

    if args.list_tables:
        for id, shape in list_tables(args.platform, inputfile):
            print(f"{id} - {shape[0]} rows x {shape[1]} cols")
    else:
        if args.format:
            format = args.format
        elif args.outputfile == "-":
            format = "json"
        else:
            format = Path(args.outputfile).suffix.lstrip(".")
        outputfile = sys.stdout if args.outputfile == "-" else open(args.outputfile, "w")
        scenario = create_scenario(args.platform, inputfile, tables=args.tables)
        if not scenario["expected_output"]:
            logging.warning("No tables generated!")
        getattr(Renderers, format)(scenario, outputfile)
