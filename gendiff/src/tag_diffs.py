def tag_diffs(dict_before, dict_after):

    common_data = {}
    tags = {}
    dict_before_keys = set(dict_before.keys())
    dict_after_keys = set(dict_after.keys())

    equal_keys = list(dict_before_keys & dict_after_keys)
    removed_keys = list(dict_before_keys - dict_after_keys)
    added_keys = list(dict_after_keys - dict_before_keys)

    equal_keys.sort()
    removed_keys.sort()
    added_keys.sort()

    for key in removed_keys:
        value_before = dict_before[key]
        common_data[key] = value_before
        tags[key] = "removed"

    for key in added_keys:
        value_after = dict_after[key]
        common_data[key] = value_after
        tags[key] = "added"

    for key in equal_keys:
        value_before = dict_before[key]
        value_after = dict_after[key]

        if value_before == value_after:
            common_data[key] = value_after
            tags[key] = "not_modified"
        else:
            val_before_is_dict = isinstance(value_before, dict)
            val_after_is_dict = isinstance(value_after, dict)
            if val_before_is_dict and val_after_is_dict:
                common_data[key], tags[key] = tag_diffs(value_before, value_after)
            else:
                common_data[f"{key}_removed"] = value_before
                common_data[f"{key}_added"] = value_after
                tags[f"{key}_removed"] = "modified_removed"
                tags[f"{key}_added"] = "modified_added"

    return common_data, tags
