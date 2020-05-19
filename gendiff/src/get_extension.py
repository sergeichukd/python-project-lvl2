import os.path


def get_extension(file_name):
    _, extension = os.path.splitext(file_name)
    return extension
