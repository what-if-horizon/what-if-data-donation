# structure_to_csv.py
import json
import csv
import logging
import sys
from typing import Iterable, TextIO, Tuple

def structure_to_csv(rows: Iterable[Tuple[dict, list, str]], outfile: TextIO = sys.stdout, ncolumns=7):
    w = csv.writer(outfile)
    w.writerow(["treestructure"] + [f"col_{x}" for x in range(1, ncolumns + 1)] + ["datatype"])
    for struct, path, datatype in rows:
        if len(path) > ncolumns:
            logging.warning(f"Path ({len(path)}) is longer than ncolumns ({ncolumns}), merging tail")
            path = path[: (ncolumns - 1)] + [".".join(str(p) for p in path[(ncolumns - 1):])]
        path = path + [None] * (ncolumns - len(path))
        w.writerow([json.dumps(struct)] + path + [datatype])

if __name__ == "__main__":
    structure = json.load(sys.stdin)
    structure_to_csv(structure, outfile=sys.stdout)