import pytest
import os
from gendiff.src.generate_diff import generate_diff
from tests.constants import TEST_DIR_PATH


@pytest.fixture
def wrong_extension_file():
    return os.path.join(TEST_DIR_PATH, "fixtures/input_data/empty.wrong_extension")


def test_wrong_extension(wrong_extension_file):
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        generate_diff(wrong_extension_file, wrong_extension_file)
    assert pytest_wrapped_e.value.code == "wrong extension"
