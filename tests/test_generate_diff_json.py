from gendiff import generate_diff
import pytest


class TestGenerateDiffJson:

    before_flat_file = "tests/fixtures/before_flat.json"
    after_flat_file = "tests/fixtures/after_flat.json"
    before_nested_file = "tests/fixtures/before_nested.json"
    after_nested_file = "tests/fixtures/after_nested.json"

    empty_file = "tests/fixtures/empty.json"
    expected_before_after_diff_file_flat = "tests/fixtures/expected_before_after_flat_diff.txt"  # noqa: E501
    expected_before_after_diff_file_nested = "tests/fixtures/expected_before_after_nested_diff.txt"  # noqa: E501

    def test_compare_nonempty_files_flat(self):
        with open(self.expected_before_after_diff_file_flat, "r") as fixture_file:
            expected_before_after_diff = fixture_file.read()
        assert generate_diff(self.before_flat_file, self.after_flat_file, file_format="json") == expected_before_after_diff  # noqa: E501

    def test_compare_nonempty_files_nested(self):
        with open(self.expected_before_after_diff_file_nested, "r") as fixture_file:
            expected_before_after_diff = fixture_file.read()
            print(generate_diff(self.before_nested_file, self.after_nested_file, file_format="json"))
        assert generate_diff(self.before_nested_file, self.after_nested_file, file_format="json") == expected_before_after_diff  # noqa: E501

    def test_compare_empty_files(self):
        assert generate_diff(self.empty_file, self.empty_file, file_format="json") == "{}"

    def test_wrong_format(self):
        with pytest.raises(SystemExit) as pytest_wrapped_e:
            generate_diff(self.empty_file, self.empty_file, file_format="wrong_format")
        assert pytest_wrapped_e.type == SystemExit
        assert pytest_wrapped_e.value.code == "wrong format"
