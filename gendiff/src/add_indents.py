from collections import Iterable


def is_dict(arg):
    return isinstance(arg, dict)


def add_indents(arg, *, indent=4):

    if not is_dict(arg):
        return arg

    indented_keys_dict = {}
    indent_str = " " * indent

    for key in arg:
        value = arg[key]
        indented_key = indent_str + key
        if is_dict(value):
            indented_keys_dict[indented_key] = add_indents(value)
        else:
            indented_keys_dict[indented_key] = value
    return indented_keys_dict
