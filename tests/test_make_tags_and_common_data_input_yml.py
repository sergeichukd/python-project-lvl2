import pytest
import json
import yaml
import os
from gendiff.src.make_tags_and_common_data import make_tags_and_common_data
from tests.constants import TEST_DIR_PATH


@pytest.fixture
def before_flat_data():
    file_path = "fixtures/input_data/before_flat.yml"
    input_data_file = os.path.join(TEST_DIR_PATH, file_path)
    input_data = yaml.safe_load(open(input_data_file))
    return input_data


@pytest.fixture
def after_flat_data():
    file_path = "fixtures/input_data/after_flat.yml"
    input_data_file = os.path.join(TEST_DIR_PATH, file_path)  # noqa: E501
    input_data = yaml.safe_load(open(input_data_file))
    return input_data


@pytest.fixture
def before_nested_data():
    file_path = "fixtures/input_data/before_nested.yml"
    input_data_file = os.path.join(TEST_DIR_PATH, file_path)  # noqa: E501
    input_data = yaml.safe_load(open(input_data_file))
    return input_data


@pytest.fixture
def after_nested_data():
    file_path = "fixtures/input_data/after_nested.yml"
    input_data_file = os.path.join(TEST_DIR_PATH, file_path)  # noqa: E501
    input_data = yaml.safe_load(open(input_data_file))
    return input_data


@pytest.fixture
def empty_data():
    file_path = "fixtures/empty.yml"
    input_data_file = os.path.join(TEST_DIR_PATH, file_path)  # noqa: E501
    input_data = yaml.safe_load(open(input_data_file))
    return input_data


@pytest.fixture
def expected_tags_flat_data():
    file_path = "fixtures/expected/expected_tags_flat.json"
    expected_data_file = os.path.join(TEST_DIR_PATH, file_path)  # noqa: E501
    expected_data = json.load(open(expected_data_file))
    return expected_data


@pytest.fixture
def expected_tags_nested_data():
    file_path = "fixtures/expected/expected_tags_nested.json"
    expected_data_file = os.path.join(TEST_DIR_PATH, file_path)  # noqa: E501
    expected_data = json.load(open(expected_data_file))
    return expected_data


@pytest.fixture
def expected_common_data_flat():
    file_path = "fixtures/expected/expected_common_data_flat.json"
    expected_data_file = os.path.join(TEST_DIR_PATH, file_path)  # noqa: E501
    expected_data = json.load(open(expected_data_file))
    return expected_data


@pytest.fixture
def expected_common_data_nested():
    file_path = "fixtures/expected/expected_common_data_nested.json"
    expected_data_file = os.path.join(TEST_DIR_PATH, file_path)  # noqa: E501
    expected_data = json.load(open(expected_data_file))
    return expected_data


def test_tags_flat(before_flat_data,
                   after_flat_data,
                   expected_tags_flat_data
                   ):
    _, tags = make_tags_and_common_data(before_flat_data, after_flat_data)
    assert tags == expected_tags_flat_data


def test_tags_nested(before_nested_data,
                     after_nested_data,
                     expected_tags_nested_data
                     ):
    _, tags = make_tags_and_common_data(before_nested_data, after_nested_data)
    assert tags == expected_tags_nested_data


def test_common_data_flat(before_flat_data,
                          after_flat_data,
                          expected_common_data_flat
                          ):
    common_data, _ = make_tags_and_common_data(before_flat_data, after_flat_data)
    assert common_data == expected_common_data_flat


def test_common_data_nested(before_nested_data, after_nested_data, expected_common_data_nested):
    common_data, _ = make_tags_and_common_data(before_nested_data, after_nested_data)
    assert common_data == expected_common_data_nested
