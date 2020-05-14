import json
import yaml


YAML_FORMATS = ["yaml", "YAML", "yml", "YML"]
JSON_FORMATS = ["json", "JSON"]


def check_format(file_format):
    valid_formats = YAML_FORMATS + JSON_FORMATS
    try:
        assert file_format in valid_formats
    except AssertionError:
        print("ERROR: Wrong format option!")
        print("Valid formats: --format=yml; --format=json")
        raise SystemExit("wrong format")


def make_dict_if_is_none(data):
    return {} if data is None else data


def parse_file(file_name, *, file_format):
    check_format(file_format)
    with open(file_name) as file_descriptor:
        if file_format in JSON_FORMATS:
            file_data = json.load(file_descriptor)
        else:
            file_data = yaml.safe_load(file_descriptor)
            file_data = make_dict_if_is_none(file_data)
    return file_data
