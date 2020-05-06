import argparse


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str, nargs=1, help='the first comparable file')
    parser.add_argument('second_file', type=str, nargs=1, help='the second comparable file')
    args = parser.parse_args()
    print(args.first_file)
    print(args.second_file)
