import functools
import importlib

from conftest import Scenario
from pandas import DataFrame


@functools.lru_cache()
def get_tables(platform, input):
    flow_module = importlib.import_module(f"port.donation_flows.{platform}")
    flow = flow_module.create_donation_flow([input])
    return {table.id: table for table in flow.tables}


def test_extract_table(scenario: Scenario):
    tables = get_tables(scenario.platform, scenario.input)
    assert scenario.id in tables, f"No table {scenario.id} (tables: {list(tables.keys())})"
    df: DataFrame = tables[scenario.id].data_frame
    assert set(df.columns) == set(scenario.columns)
    assert len(df) == len(scenario.data)
    for i, row in enumerate(scenario.data):
        for j, col in enumerate(scenario.columns):
            val = df.iloc[i][col]
            assert val == row[j], f"Row {i} column {j}:{col} mismatch: expected {row[j]}, found {val}"
