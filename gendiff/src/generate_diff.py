import json
from .make_added_key_diffs import make_added_key_diffs
from gendiff.src.make_removed_key_diffs import make_removed_key_diffs
from gendiff.src.make_common_key_diffs import make_common_key_diffs


def generate_diff(file1, file2):
    diff_lines = []
    file1_data = json.load(open(file1))
    file2_data = json.load(open(file2))

    file1_keys = set(file1_data.keys())
    file2_keys = set(file2_data.keys())

    common_keys = file1_keys & file2_keys
    removed_keys = file1_keys - file2_keys
    added_keys = file2_keys - file1_keys

    common_key_diffs = make_common_key_diffs(file1_data, file2_data, common_keys=common_keys)
    removed_key_diffs = make_removed_key_diffs(file1_data, removed_keys=removed_keys)
    added_key_diffs = make_added_key_diffs(file2_data, added_keys=added_keys)

    diff_lines.extend(common_key_diffs)
    diff_lines.extend(removed_key_diffs)
    diff_lines.extend(added_key_diffs)

    return "{\n" + "\n".join(diff_lines) + "\n}"