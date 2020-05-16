def add_diff_tags(dict_before, dict_after):

    tagged_dict = {'removed_keys': {},
                   'added_keys': {},
                   'equal_keys': {
                       'both_dict': {},
                       'equal_vals': {},
                       'diff_vals': {
                           'deleted_val': {},
                           'added_val': {},
                       },
                   }
                   }
    dict_before_keys = set(dict_before.keys())
    dict_after_keys = set(dict_after.keys())

    equal_keys = dict_before_keys & dict_after_keys
    removed_keys = dict_before_keys - dict_after_keys
    added_keys = dict_after_keys - dict_before_keys

    for key in removed_keys:
        tagged_dict['removed_keys'][key] = dict_before[key]

    for key in added_keys:
        tagged_dict['added_keys'][key] = dict_after[key]

    for key in equal_keys:
        if dict_before[key] == dict_after[key]:
            tagged_dict['equal_keys']['equal_vals'][key] = dict_after[key]
        else:
            val_before_is_dict = isinstance(dict_before[key], dict)
            val_after_is_dict = isinstance(dict_after[key], dict)
            if val_before_is_dict and val_after_is_dict:
                tagged_dict['equal_keys']['both_dict'][key] = add_diff_tags(dict_before[key], dict_after[key])
            else:
                tagged_dict['equal_keys']['diff_vals']['deleted_val'][key] = dict_before[key]
                tagged_dict['equal_keys']['diff_vals']['added_val'][key] = dict_after[key]

    return tagged_dict


def make_common_key_diffs(file1_data, file2_data, *, equal_keys):
    diff_lines = []

    for key in equal_keys:
        if file1_data[key] == file2_data[key]:
            file_line = f"  {key}: {file2_data[key]}"
            diff_lines.append(file_line)
        else:
            file1_line = f"- {key}: {file1_data[key]}"
            file2_line = f"+ {key}: {file2_data[key]}"
            diff_lines.extend([file1_line, file2_line])
    return tuple(diff_lines)
