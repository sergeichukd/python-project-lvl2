import pytest
from gendiff.src.tag_diffs import tag_diffs
from gendiff.src.parse_file import parse_file


class TestTagDiffs:
    before_flat_file = "tests/fixtures/before_flat.json"
    after_flat_file = "tests/fixtures/after_flat.json"
    before_nested_file = "tests/fixtures/before_nested.json"
    after_nested_file = "tests/fixtures/after_nested.json"

    empty_file = "tests/fixtures/empty.json"
    expected_before_after_diff_file_flat = "tests/fixtures/expected_before_after_tagged_dict_flat.json"  # noqa: E501
    expected_before_after_diff_file_nested = "tests/fixtures/expected_before_after_tagged_dict_nested.json"  # noqa: E501

    def test_tag_diffs_flat(self):
        expected_dict = parse_file(self.expected_before_after_diff_file_flat, file_format="json")
        file_before_data = parse_file(self.before_flat_file, file_format="json")
        file_after_data = parse_file(self.after_flat_file, file_format="json")
        assert tag_diffs(file_before_data, file_after_data) == expected_dict

    def test_tag_diffs_nested(self):
        expected_dict = parse_file(self.expected_before_after_diff_file_nested, file_format="json")
        file_before_data = parse_file(self.before_nested_file, file_format="json")
        file_after_data = parse_file(self.after_nested_file, file_format="json")
        print(tag_diffs(file_before_data, file_after_data))
        assert tag_diffs(file_before_data, file_after_data) == expected_dict


if __name__ == "__main__":
    test = TestTagDiffs()
    test.before_flat_file = "fixtures/before_flat.json"
    test.after_flat_file = "fixtures/after_flat.json"
    test.before_nested_file = "fixtures/before_nested.json"
    test.after_nested_file = "fixtures/after_nested.json"
    test.empty_file = "fixtures/empty.json"
    test.expected_before_after_diff_file_nested = "fixtures/expected_before_after_tagged_dict_nested.json"  # noqa: E501

    test.test_tag_diffs_nested()
