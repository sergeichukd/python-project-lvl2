from gendiff import src
from gendiff import cli


def run_generate_diff():
    args = src.parse_args()
    difference = src.generate_diff(args.file1, args.file2)
    cli.print_diff(difference)
