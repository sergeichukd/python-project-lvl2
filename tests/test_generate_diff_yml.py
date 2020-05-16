from gendiff import generate_diff
import pytest


class TestGenegateDiffYml:
    before_file = "tests/fixtures/before.yml"
    after_file = "tests/fixtures/after.yml"
    empty_file = "tests/fixtures/empty.yml"
    expected_before_after_diff_file = "tests/fixtures/expected_before_after_diff.txt"  # noqa: E501

    def test_compare_nonempty_files(self):
        with open(self.expected_before_after_diff_file, "r") as fixture_file:
            expected_before_after_diff = fixture_file.read()
        assert generate_diff(self.before_file, self.after_file, file_format="yml") == expected_before_after_diff  # noqa: E501

    def test_compare_empty_files(self):
        assert generate_diff(self.empty_file, self.empty_file, file_format="yml") == "{\n\n}"

    def test_wrong_format(self):
        with pytest.raises(SystemExit) as pytest_wrapped_e:
            generate_diff(self.empty_file, self.empty_file, file_format="wrong_format")
        assert pytest_wrapped_e.type == SystemExit
        assert pytest_wrapped_e.value.code == "wrong format"


if __name__ == "__main__":
    local_test = TestGenegateDiffYml()
    local_test.before_file = "fixtures/before.yml"
    local_test.after_file = "fixtures/after.yml"
    local_test.empty_file = "fixtures/empty.yml"
    local_test.expected_before_after_diff_file = "fixtures/expected_before_after_diff.txt"  # noqa: E501

    local_test.test_compare_nonempty_files()
