import json
import yaml
from gendiff.src.check_format import check_format, JSON_FORMATS


def _make_dict_if_is_none(data):
    return {} if data is None else data


def parse_file(file_name, *, file_format):
    check_format(file_format)
    with open(file_name) as file_descriptor:
        if file_format in JSON_FORMATS:
            file_data = json.load(file_descriptor)
        else:
            file_data = yaml.safe_load(file_descriptor)
            file_data = _make_dict_if_is_none(file_data)
    return file_data
