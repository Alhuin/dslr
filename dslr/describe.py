import sys

from dslr.utils import parse_describe


def describe(csv_path):
    """

    :param csv_path: the path of the dataset to describe
    :return: nothing, prints on stdout
    """
    print(csv_path)


def main():
    args = parse_describe(sys.argv[1:])
    describe(args.csv_path)


if __name__ == "__main__":
    main()
