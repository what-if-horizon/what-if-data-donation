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
    return flow_module.create_donation_flow([inputfile])


def list_tables(platform: str, inputfile: Path):
    flow = get_flow(platform, inputfile)
    for table in flow.tables:
        yield table.id, table.data_frame.shape


def create_scenario(platform: str, inputfile: Path, tables: list[str] | None):
    flow = get_flow(platform, inputfile)
    tables = list(extract_tables(flow, tables))
    return dict(input_file=str(inputfile), platform=platform, expected_output=tables)


def render_html(tables, file):
    print(
        """<html><head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
  <style>h1 {padding:.3em}</style>
  </head><body><div class='container-fluid'>""",
        file=file,
    )
    for name, df in tables.items():
        print(f"<h1>Table '{name}'</h1>", file=file)
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


def render_md(tables, file):
    for name, df in tables.items():
        print(f"\n# Table '{name}'", file=file)
        print(df.to_markdown(), file=file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("platform", choices=["tiktok", "facebook", "tiktok", "twitter", "youtube"])
    parser.add_argument("inputfile", help="The path or name of the donation file (i.e. .zip or .json)", type=Path)
    parser.add_argument("tables", nargs="*", help="Specify table ids to extract (default extracts all tables)")
    parser.add_argument(
        "--list-tables", "-l", action="store_true", help="List only existing table ids and size instead"
    )
    parser.add_argument("--output", "-o", type=Path, help="Save json into this file instead of printing to stdout")
    parser.add_argument(
        "--print-tables",
        "-p",
        nargs="?",
        type=Path,
        const=sys.stderr,
        help="Print generated tables to this file (or to stderr)",
    )
    args = parser.parse_args()

    logging.basicConfig(format="[%(levelname)-7s:%(name)-15s] %(message)s", level=logging.INFO)

    # Make inputfile relative to project root
    inputfile: Path = args.inputfile.resolve().relative_to(Path.cwd())
    outputfile = sys.stdout if args.output is None else open(args.output, "w")
    if not inputfile.exists():
        raise FileNotFoundError(f"Cannot find input file {inputfile}")

    if args.list_tables:
        for id, shape in list_tables(args.platform, inputfile):
            print(f"{id} - {shape[0]} rows x {shape[1]} cols")
    else:
        scenario = create_scenario(args.platform, inputfile, tables=args.tables)
        logging.info(f"Writing output to {outputfile.name}")
        json.dump(scenario, outputfile, indent=4)
    print(args.print_tables)
    if args.print_tables:
        tables = {
            x["id"]: pd.DataFrame(data=x["data_frame"]["data"], columns=x["data_frame"]["columns"])
            for x in scenario["expected_output"]
        }
        o = sys.stderr if args.print_tables == sys.stderr else open(args.print_tables, "w")
        logging.info(f"Printing {len(args.tables)} table{'s' if len(tables) > 1 else ''} to {o.name}")
        if str(args.print_tables).endswith(".html"):
            render_html(tables, o)
        else:
            render_md(tables, o)
