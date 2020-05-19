from gendiff import generate_diff
from tests.constants import TEST_DIR_PATH
import os
import pytest


@pytest.fixture
def empty_file():
    input_data_file = os.path.join(TEST_DIR_PATH, "fixtures/input_data/empty.yml")
    return input_data_file


@pytest.fixture
def before_flat_file():
    input_data_file = os.path.join(TEST_DIR_PATH, "fixtures/input_data/before_flat.yml")
    return input_data_file


@pytest.fixture
def after_flat_file():
    input_data_file = os.path.join(TEST_DIR_PATH, "fixtures/input_data/after_flat.yml")
    return input_data_file


@pytest.fixture
def before_nested_file():
    input_data_file = os.path.join(TEST_DIR_PATH, "fixtures/input_data/before_nested.yml")
    return input_data_file


@pytest.fixture
def after_nested_file():
    input_data_file = os.path.join(TEST_DIR_PATH, "fixtures/input_data/after_nested.yml")
    return input_data_file


@pytest.fixture
def expected_before_after_diff_file_flat():
    expected_file = os.path.join(TEST_DIR_PATH, "fixtures/expected/expected_flat_diff.txt")
    with open(expected_file, "r") as expected_descriptor:
        return expected_descriptor.read()


@pytest.fixture
def expected_before_after_diff_file_nested():
    expected_file = os.path.join(TEST_DIR_PATH, "fixtures/expected/expected_nested_diff.txt")
    with open(expected_file, "r") as expected_descriptor:
        return expected_descriptor.read()


def test_compare_nonempty_files_flat(before_flat_file,
                                     after_flat_file,
                                     expected_before_after_diff_file_flat
                                     ):
    assert generate_diff(before_flat_file, after_flat_file) == expected_before_after_diff_file_flat  # noqa: E501


def test_compare_nonempty_files_nested(before_nested_file,
                                       after_nested_file,
                                       expected_before_after_diff_file_nested
                                       ):
    assert generate_diff(before_nested_file, after_nested_file) == expected_before_after_diff_file_nested  # noqa: E501


def test_compare_empty_files(empty_file):
    assert generate_diff(empty_file, empty_file) == "{}"
