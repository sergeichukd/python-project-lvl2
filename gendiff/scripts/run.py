import argparse
import json


def make_common_key_diffs(file1_data, file2_data, *, common_keys):
    diff_lines = []

    for key in common_keys:
        if file1_data[key] == file2_data[key]:
            file_line = f"  {key}: {file2_data[key]}"
            diff_lines.append(file_line)
        else:
            file1_line = f"- {key}: {file1_data[key]}"
            file2_line = f"+ {key}: {file2_data[key]}"
            diff_lines.extend([file1_line, file2_line])
    return tuple(diff_lines)


def make_removed_key_diffs(file_data, *, removed_keys):
    diff_lines = []

    for key in removed_keys:
        file_line = f"- {key}: {file_data[key]}"
        diff_lines.append(file_line)
    return tuple(diff_lines)


def make_added_key_diffs(file_data, *, added_keys):
    diff_lines = []

    for key in added_keys:
        file_line = f"+ {key}: {file_data[key]}"
        diff_lines.append(file_line)
    return tuple(diff_lines)


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


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str, nargs=1, help='the first comparable file')  # noqa: E501
    parser.add_argument('second_file', type=str, nargs=1, help='the second comparable file')  # noqa: E501
    parser.add_argument('-f', '--format', type=str, nargs=1, help='set format of output')  # noqa: E501
    args = parser.parse_args()
    print(args.first_file)
    print(args.second_file)


out = generate_diff("before.json", "after.json")
print(out)
