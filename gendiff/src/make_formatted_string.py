from gendiff.src.out_format import make_flat_out_string, make_nested_out_string


def make_formatted_string(common_data, tags, *, out_format):
    if out_format == 'nested':
        return make_nested_out_string(common_data, tags)
    if out_format == 'flat':
        return make_flat_out_string(common_data, tags)
