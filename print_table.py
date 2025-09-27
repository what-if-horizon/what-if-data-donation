"""Print a single table to inspect"""

import argparse
import logging
import sys
from pathlib import Path

from pytests.create_scenario import Renderers, create_scenario, list_tables  # type: ignore

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("platform", choices=["tiktok", "facebook", "instagram", "twitter", "youtube"])
    parser.add_argument("inputfile", help="The path or name of the donation file (i.e. .zip or .json)", type=Path)
    parser.add_argument("table", nargs="?", help="Specify table to extract. If not specified, print list of tables)")
    parser.add_argument(
        "--format", "-f", choices=["json", "html", "md"], default="md", help="Use this format (default: md)"
    )

    args = parser.parse_args()

    logging.basicConfig(format="[%(levelname)-7s:%(name)-15s] %(message)s", level=logging.INFO)

    inputfile = args.inputfile.resolve()
    if not args.table:
        for id, shape in list_tables(args.platform, inputfile):
            print(f"{id} - {shape[0]} rows x {shape[1]} cols")
    else:
        scenario = create_scenario(args.platform, inputfile, tables=[args.table])
        if not scenario["expected_output"]:
            logging.warning("No tables generated!")
        getattr(Renderers, args.format)(scenario, sys.stdout)
