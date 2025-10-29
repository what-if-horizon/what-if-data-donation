import zipfile
from tempfile import TemporaryDirectory

import pytest
from port.script import is_valid

TEST_FILES = dict(
    Tiktok="pytests/public_testfiles/TT_user_data_tiktok.json",
    Twitter="pytests/public_testfiles/X_public_test_files.zip",
    Facebook="pytests/public_testfiles/FB_public_test_file.zip",
    Instagram="pytests/public_testfiles/IG_public_test_file.zip",
    Youtube="pytests/public_testfiles/YT_public_test_file.zip",
)


def platform_compatability():
    # FB/IG/YT are mutually compatible (since we only look for zipped json)
    compatible = {"Facebook", "Instagram", "Youtube"}
    for i, platform in enumerate(TEST_FILES.keys()):
        for platform2 in list(TEST_FILES.keys())[:i]:
            yield platform, platform2, (platform in compatible and platform2 in compatible)


@pytest.mark.parametrize("platform", TEST_FILES.keys())
def test_validate_garbage(platform):
    "simple text files or zips containing only a text file should never be valid"
    with TemporaryDirectory() as d:
        with open(f"{d}/test.txt", "w") as f:
            f.write("Test!")
        assert not is_valid(f.name, platform=platform), f"{platform} accepted a simple text file"

        with zipfile.ZipFile(f"{d}/test.zip", "w", zipfile.ZIP_DEFLATED) as zf:
            zf.write(f.name, arcname="test.txt")
        assert not is_valid(zf.filename, platform=platform), f"{platform} accepted a simple zipped text file"


@pytest.mark.parametrize("platform", TEST_FILES.keys())
def test_validate_files(platform):
    "All files should be valid on their own platform"
    assert is_valid(TEST_FILES[platform], platform), f"{platform} says {TEST_FILES[platform]} is invalid"


@pytest.mark.parametrize("platform1, platform2, is_compatible", platform_compatability())
def test_incompatible(platform1, platform2, is_compatible):
    "All files should be valid on their own platform"
    if is_compatible:
        assert is_valid(
            TEST_FILES[platform1], platform2
        ), f"{platform1}:{TEST_FILES[platform1]} was not accepted by {platform2}"
    else:
        assert not is_valid(
            TEST_FILES[platform1], platform2
        ), f"{platform1}:{TEST_FILES[platform1]} was accepted by {platform2}"
