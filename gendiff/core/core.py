from gendiff import src
from gendiff import cli


def run_generate_diff():
    args = src.parse_input_str()
    difference = src.generate_diff(args.file1, args.file2)  # noqa: E501
    cli.print_diff(difference)
