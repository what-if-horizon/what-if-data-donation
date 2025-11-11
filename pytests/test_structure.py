from conftest import get_tables, inputfiles
import pytest


@pytest.mark.parametrize("platform,input", inputfiles().items())
def test_structure(platform, input):
    tables = get_tables(platform.lower(), input)
    structure_dicts = tables["placeholder"].data_frame.to_dict(orient="records")
    assert (
        structure_dicts[0].get("Placeholder for research purpose") != "{}"
    ), f"Structure file for {platform} missing or empty: {structure_dicts}"
