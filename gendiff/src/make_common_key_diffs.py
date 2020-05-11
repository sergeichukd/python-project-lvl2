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
