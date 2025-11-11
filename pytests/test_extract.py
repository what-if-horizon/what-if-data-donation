import functools
import importlib
import logging
import warnings

import numpy as np
from conftest import Scenario, get_tables
from pandas import DataFrame


def test_extract_table(scenario: Scenario):
    if not scenario.input.exists():
        warnings.warn(f"Cannot find file {scenario.input}, skipping test")
        return
    tables = get_tables(scenario.platform, scenario.input)
    assert (
        scenario.id in tables
    ), f"No table {scenario.id} (tables: {list(tables.keys())})"
    df: DataFrame = tables[scenario.id].data_frame
    assert set(df.columns) == set(scenario.columns)
    assert len(df) == len(scenario.data)
    for i, row in enumerate(scenario.data):
        for j, col in enumerate(scenario.columns):
            found = df.iloc[i][col]
            expected = row[j]
            # we would like to just assert found == expected, but NaN != NaN, so we want to special case that
            # and need to check for float first to avoid an error from isnan
            if all(isinstance(x, float) and np.isnan(x) for x in (found, expected)):
                continue
            assert (
                found == expected
            ), f"Row {i} column {j}:{col} mismatch: expected {expected!r}, found {found!r}"
