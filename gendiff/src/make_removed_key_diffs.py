def make_removed_key_diffs(file_data, *, removed_keys):
    diff_lines = []

    for key in removed_keys:
        file_line = f"- {key}: {file_data[key]}"
        diff_lines.append(file_line)
    return tuple(diff_lines)
