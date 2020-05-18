import pytest
from gendiff.src.make_tags_and_common_data import make_tags_and_common_data
import json


class TestTagDiffs:
    before_flat_file = "tests/fixtures/input_data/before_flat.json"
    after_flat_file = "tests/fixtures/input_data/after_flat.json"
    before_nested_file = "tests/fixtures/input_data/before_nested.json"
    after_nested_file = "tests/fixtures/input_data/after_nested.json"

    empty_file = "tests/fixtures/empty.json"
    expected_tags_file_flat = "tests/fixtures/expected/expected_tags_flat.json"  # noqa: E501
    expected_tags_file_nested = "tests/fixtures/expected/expected_tags_nested.json"  # noqa: E501
    expected_common_data_file_flat = "tests/fixtures/expected/expected_common_data_flat.json"  # noqa: E501
    expected_common_data_file_nested = "tests/fixtures/expected/expected_common_data_nested.json"  # noqa: E501

    def test_tags_flat(self):
        expected_tags = json.load(open(self.expected_tags_file_flat))
        file_before_data = json.load(open(self.before_flat_file))
        file_after_data = json.load(open(self.after_flat_file))
        _, tags = make_tags_and_common_data(file_before_data, file_after_data)
        assert tags == expected_tags

    def test_tags_nested(self):
        expected_tags = json.load(open(self.expected_tags_file_nested))
        file_before_data = json.load(open(self.before_nested_file))
        file_after_data = json.load(open(self.after_nested_file))
        _, tags = make_tags_and_common_data(file_before_data, file_after_data)
        assert tags == expected_tags
        
    def test_common_data_flat(self):
        expected_common_data = json.load(open(self.expected_common_data_file_flat))
        file_before_data = json.load(open(self.before_flat_file))
        file_after_data = json.load(open(self.after_flat_file))
        common_data, _ = make_tags_and_common_data(file_before_data, file_after_data)
        assert common_data == expected_common_data
        
    def test_common_data_nested(self):
        expected_common_data = json.load(open(self.expected_common_data_file_nested))
        file_before_data = json.load(open(self.before_nested_file))
        file_after_data = json.load(open(self.after_nested_file))
        common_data, _ = make_tags_and_common_data(file_before_data, file_after_data)
        assert common_data == expected_common_data
