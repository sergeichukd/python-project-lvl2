import json


# def _add_prefixes(data_string, tags):
#     out_string = data_string
#     for key, tag in tags.items():
#         if _is_dict(tag):
#             out_string = _add_prefixes(out_string, tag)
#         else:
#             if "removed" in tag:
#                 out_string = _make_key_prefix(out_string, key, prefix="- ")
#             elif "added" in tag:
#                 out_string = _make_key_prefix(out_string, key, prefix="+ ")
#     return out_string


def make_flat_out_string(common_data, tags):
    out_string = json.dumps(common_data, indent=4)

    return out_string
