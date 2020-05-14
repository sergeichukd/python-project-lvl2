from gendiff import generate_diff
import pytest


class TestGenegateDiffJson:
    def test_compare_nonempty_files(self):
        before_file = "tests/fixtures/before.json"
        after_file = "tests/fixtures/after.json"
        expected_before_after_diff_file = "tests/fixtures/expected_before_after_diff.txt"  # noqa: E501
        with open(expected_before_after_diff_file, "r") as fixture_file:
            expected_before_after_diff = fixture_file.read()

        assert generate_diff(before_file, after_file, file_format="json") == expected_before_after_diff  # noqa: E501

    def test_compare_empty_files(self):
        empty_file = "tests/fixtures/empty.json"
        assert generate_diff(empty_file, empty_file, file_format="json") == "{\n\n}"

    def test_wrong_format(self):
        empty_file = "tests/fixtures/empty.json"
        with pytest.raises(SystemExit) as pytest_wrapped_e:
            generate_diff(empty_file, empty_file, file_format="wrong_format")
        assert pytest_wrapped_e.type == SystemExit
        assert pytest_wrapped_e.value.code == "wrong format"