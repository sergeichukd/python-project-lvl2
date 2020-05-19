import json
import yaml
from gendiff.src.check_format import check_extension
from gendiff.src.get_extension import get_extension


def _make_dict_if_is_none(data):
    return {} if data is None else data


def parse_file(file_name):
    file_extension = get_extension(file_name)
    check_extension(file_extension)
    with open(file_name) as file_descriptor:
        if file_extension == ".json":
            file_data = json.load(file_descriptor)
        else:
            file_data = yaml.safe_load(file_descriptor)
            file_data = _make_dict_if_is_none(file_data)
    return file_data
