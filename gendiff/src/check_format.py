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
