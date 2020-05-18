from gendiff import generate_diff
import pytest
import json
import yaml


class TestGenerateDiffYml:

    # Input files
    before_flat_file = "tests/fixtures/input_data/before_flat.yml"
    after_flat_file = "tests/fixtures/input_data/after_flat.yml"
    before_nested_file = "tests/fixtures/input_data/before_nested.yml"
    after_nested_file = "tests/fixtures/input_data/after_nested.yml"
    empty_file = "tests/fixtures/input_data/empty.yml"

    # Expected files
    expected_before_after_diff_file_flat = "tests/fixtures/expected/expected_flat_diff.txt"  # noqa: E501
    expected_before_after_diff_file_nested = "tests/fixtures/expected/expected_nested_diff.txt"  # noqa: E501

    def test_compare_nonempty_files_flat(self):
        with open(self.expected_before_after_diff_file_flat, "r") as fixture_file:
            expected_before_after_diff = fixture_file.read()
        assert generate_diff(self.before_flat_file, self.after_flat_file, file_format="yml") == expected_before_after_diff  # noqa: E501

    def test_compare_nonempty_files_nested(self):
        with open(self.expected_before_after_diff_file_nested, "r") as fixture_file:
            expected_before_after_diff = fixture_file.read()
        assert generate_diff(self.before_nested_file, self.after_nested_file, file_format="yml") == expected_before_after_diff  # noqa: E501

    def test_compare_empty_files(self):
        assert generate_diff(self.empty_file, self.empty_file, file_format="yml") == "{}"

    def test_wrong_format(self):
        with pytest.raises(SystemExit) as pytest_wrapped_e:
            generate_diff(self.empty_file, self.empty_file, file_format="wrong_format")
        assert pytest_wrapped_e.type == SystemExit
        assert pytest_wrapped_e.value.code == "wrong format"

