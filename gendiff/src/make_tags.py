from gendiff.src.add_indents import add_indents


def make_tags(dict_before, dict_after):

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
        tags[key] = "removed"

    for key in added_keys:
        tags[key] = "added"

    for key in equal_keys:
        value_before = dict_before[key]
        value_after = dict_after[key]

        if value_before == value_after:
            tags[key] = "not_modified"
        else:
            val_before_is_dict = isinstance(value_before, dict)
            val_after_is_dict = isinstance(value_after, dict)
            if val_before_is_dict and val_after_is_dict:
                tags[key] = make_tags(value_before, value_after)
            else:
                tags[key + "_removed"] = "modified_removed"
                tags[key + "_added"] = "modified_added"

    return tags
