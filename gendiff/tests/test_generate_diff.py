from gendiff import generate_diff


class TestGenegateDiff:
    def test_compare_nonempty_files(self):
        before_file = "gendiff/tests/fixtures/before.json"
        after_file = "gendiff/tests/fixtures/after.json"
        expected_before_after_diff_file = "gendiff/tests/fixtures/expected_before_after_diff.txt"  # noqa: E501
        with open(expected_before_after_diff_file, "r") as fixture_file:
            expected_before_after_diff = fixture_file.read()

        assert generate_diff(before_file, after_file) == expected_before_after_diff  # noqa: E501

    def test_compare_empty_files(self):
        empty_file = "gendiff/tests/fixtures/empty.json"
        assert generate_diff(empty_file, empty_file) == "{\n\n}"
