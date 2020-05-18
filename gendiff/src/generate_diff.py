from gendiff.src.parse_file import parse_file
from gendiff.src.make_tags_and_common_data import make_tags_and_common_data
from gendiff.src.generate_out_string import generate_out_string


def generate_diff(file1, file2, *, file_format):
    before_data = parse_file(file1, file_format=file_format)
    after_data = parse_file(file2, file_format=file_format)
    common_data, tags = make_tags_and_common_data(before_data, after_data)
    return generate_out_string(common_data, tags)
