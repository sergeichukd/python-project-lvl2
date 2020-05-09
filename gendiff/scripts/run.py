import argparse


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str, nargs=1, help='the first comparable file')  # noqa: E501
    parser.add_argument('second_file', type=str, nargs=1, help='the second comparable file')  # noqa: E501
    parser.add_argument('-f', '--format', type=str, nargs=1, help='set format of output')  # noqa: E501
    args = parser.parse_args()
    print(args.first_file)
    print(args.second_file)


main()
