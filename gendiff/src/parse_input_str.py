import argparse


def parse_input_str():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('file1', type=str, help='the first comparable file')  # noqa: E501
    parser.add_argument('file2', type=str, help='the second comparable file')  # noqa: E501
    parser.add_argument('-f', '--format', type=str, default="nested", help='set format of output')  # noqa: E501
    args = parser.parse_args()
    return args
