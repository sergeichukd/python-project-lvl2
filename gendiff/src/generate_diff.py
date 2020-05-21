from gendiff.src.parse_file import parse_file
from gendiff.src.make_tags_and_common_data import make_tags_and_common_data
from gendiff.src.make_formatted_string import make_formatted_string


def generate_diff(file1, file2, *, out_format='nested'):
    before_data = parse_file(file1)
    after_data = parse_file(file2)
    common_data, tags = make_tags_and_common_data(before_data, after_data)
    return make_formatted_string(common_data, tags, out_format=out_format)
