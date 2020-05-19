VALID_EXTENSIONS = [".json", ".yml"]


def check_extension(file_extension):
    try:
        assert file_extension in VALID_EXTENSIONS
    except AssertionError:
        print("ERROR: Wrong file extension!")
        print("Valid extensions: .json; .yml")
        raise SystemExit("wrong extension")
