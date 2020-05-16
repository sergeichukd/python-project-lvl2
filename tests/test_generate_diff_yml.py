from gendiff import generate_diff
import pytest
import json
import yaml


class TestGenerateDiffYml:
    before_flat_file = "tests/fixtures/before_flat.yml"
    after_flat_file = "tests/fixtures/after_flat.yml"
    before_nested_file = "tests/fixtures/before_nested.yml"
    after_nested_file = "tests/fixtures/after_nested.yml"

    empty_file = "tests/fixtures/empty.yml"
    expected_before_after_diff_file_flat = "tests/fixtures/expected_before_after_flat_diff.txt"  # noqa: E501
    expected_before_after_diff_file_nested = "tests/fixtures/expected_before_after_nested_diff.txt"  # noqa: E501

    def test_compare_nonempty_files_flat(self):
        with open(self.expected_before_after_diff_file_flat, "r") as fixture_file:
            expected_before_after_diff = fixture_file.read()
        assert generate_diff(self.before_flat_file, self.after_flat_file, file_format="yml") == expected_before_after_diff  # noqa: E501

    def test_compare_nonempty_files_nested(self):
        with open(self.expected_before_after_diff_file_nested, "r") as fixture_file:
            expected_before_after_diff = fixture_file.read()
        assert generate_diff(self.before_nested_file, self.after_nested_file, file_format="yml") == expected_before_after_diff  # noqa: E501

    def test_compare_empty_files(self):
        assert generate_diff(self.empty_file, self.empty_file, file_format="yml") == "{\n\n}"

    def test_wrong_format(self):
        with pytest.raises(SystemExit) as pytest_wrapped_e:
            generate_diff(self.empty_file, self.empty_file, file_format="wrong_format")
        assert pytest_wrapped_e.type == SystemExit
        assert pytest_wrapped_e.value.code == "wrong format"


if __name__ == "__main__":
    local_test = TestGenerateDiffYml()
    local_test.before_flat_file = "fixtures/before_flat.yml"
    local_test.after_flat_file = "fixtures/after_flat.yml"
    local_test.before_nested_file = "fixtures/before_nested.yml"
    local_test.after_nested_file = "fixtures/after_nested.yml"
    local_test.empty_file = "fixtures/empty.yml"
    local_test.expected_before_after_diff_file_flat = "fixtures/expected_before_after_flat_diff.txt"  # noqa: E501

    local_test.test_compare_nonempty_files_nested()
