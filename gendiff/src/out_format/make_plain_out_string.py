def _is_modified(tag):
    return "modified" in tag


def _is_dict(value):
    return type(value) == dict


def _make_line_removed(file_property):
    return f"\nProperty '{file_property}' was removed"


def _make_line_added(file_property, value):
    if _is_dict(value):
        value = "complex value"
    return f"\nProperty '{file_property}' was added with value: '{value}'"


def _make_line_modified(file_property, removed_value, added_value):
    if _is_dict(removed_value):
        removed_value = "complex value"
    if _is_dict(added_value):
        added_value = "complex value"
    return f"\nProperty '{file_property}' was changed. From '{removed_value}' to '{added_value}'"  # noqa: E501


def _remove_key_postfix(key, *, postfix):
    new_key_length = len(key) - len(postfix)
    old_key = key
    new_key = old_key[:new_key_length]
    return new_key


def make_plain_out_string(common_data, tags):
    init_out_string = ""
    init_path = ""

    def inner(inner_common_data, inner_tags, property_path, out_string):

        for key, tag in inner_tags.items():
            value = inner_common_data[key]

            if _is_dict(tag):
                new_path = property_path + key + "."
                out_string = inner(value, tag, new_path, out_string)
            elif tag == "removed":
                file_property = property_path + key
                out_string = out_string + _make_line_removed(file_property)
            elif tag == "added":
                file_property = property_path + key
                out_string = out_string + _make_line_added(file_property, value)  # noqa: E501
            elif tag == "modified_removed":
                key_without_postfix = _remove_key_postfix(key, postfix='_removed')  # noqa: E501
                key_removed = key
                key_added = key_without_postfix + '_added'

                file_property = property_path + key_without_postfix
                removed_value = inner_common_data[key_removed]
                added_value = inner_common_data[key_added]
                out_string = out_string + _make_line_modified(file_property, removed_value, added_value)  # noqa: E501
        return out_string
    return inner(common_data, tags, init_path, init_out_string)
