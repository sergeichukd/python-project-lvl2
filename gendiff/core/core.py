from gendiff import src
from gendiff import cli


def run_generate_diff():
    args = src.parse_args()
    difference = src.generate_diff(args.file1, args.file2, file_format=args.format)  # noqa: E501
    cli.print_diff(difference)
