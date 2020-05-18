import json


def _is_dict(arg):
    return isinstance(arg, dict)


def _remove_quotes(arg_str):
    return arg_str.replace('"', '')


def _remove_commas(arg_str):
    return arg_str.replace(',', '')


def _is_removed_or_added(tag):
    return not ("modified" in tag)


def _remove_postfix(string, *, postfix):
    return string.replace(postfix, "")


def _make_key_prefix(data_str, key, *, prefix):
    prefix_length = len(prefix)
    indents_to_delete = " " * prefix_length
    old_key = f"{indents_to_delete}{key}"
    new_key = f"{prefix}{key}"
    return data_str.replace(old_key, new_key)


def _remove_key_postfix(key, *, postfix):
    new_key_length = len(key) - len(postfix)
    old_key = key
    new_key = old_key[:new_key_length]
    return new_key


def _add_prefixes(data_string, tags):
    out_string = data_string
    for key, tag in tags.items():
        if _is_dict(tag):
            out_string = _add_prefixes(out_string, tag)
        else:
            if "removed" in tag:
                out_string = _make_key_prefix(out_string, key, prefix="- ")
            elif "added" in tag:
                out_string = _make_key_prefix(out_string, key, prefix="+ ")
    return out_string


def _remove_postfixes(data_string, tags):
    out_string = data_string
    for key, tag in tags.items():
        if _is_dict(tag):
            out_string = _remove_postfixes(out_string, tag)

        new_key = key
        if tag == "modified_removed":
            new_key = _remove_key_postfix(key, postfix="_removed")
        if tag == "modified_added":
            new_key = _remove_key_postfix(key, postfix="_added")
        out_string = out_string.replace(key, new_key)

    return out_string


def generate_out_string(common_data, tags):
    out_string = json.dumps(common_data, indent=4)
    out_string = _remove_quotes(out_string)
    out_string = _remove_commas(out_string)
    out_string = _add_prefixes(out_string, tags)
    out_string = _remove_postfixes(out_string, tags)
    return out_string
