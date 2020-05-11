def make_added_key_diffs(file_data, *, added_keys):
    diff_lines = []

    for key in added_keys:
        file_line = f"+ {key}: {file_data[key]}"
        diff_lines.append(file_line)
    return tuple(diff_lines)
