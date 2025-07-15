import argparse
import importlib
import json
from pathlib import Path
from venv import create

from port.api.d3i_props import PropsUIPromptConsentFormViz


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


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("platform", choices=["tiktok", "facebook", "tiktok", "twitter", "youtube"])
    parser.add_argument("inputfile", help="The path or name of the donation file (i.e. .zip or .json)", type=Path)
    parser.add_argument("tables", nargs="*", help="Specify table ids to extract (default extracts all tables)")
    parser.add_argument("--list-tables", action="store_true", help="List only existing table ids and size instead")
    args = parser.parse_args()

    # Make inputfile relative to project root
    inputfile: Path = args.inputfile.resolve().relative_to(Path.cwd())
    if not inputfile.exists():
        raise FileNotFoundError(f"Cannot find input file {inputfile}")

    if args.list_tables:
        for id, shape in list_tables(args.platform, inputfile):
            print(f"{id} - {shape[0]} rows x {shape[1]} cols")
    else:
        scenario = create_scenario(args.platform, inputfile, tables=args.tables)
        print(json.dumps(scenario, indent=4))
