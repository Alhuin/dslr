import sys

from dslr.utils import parse_describe


def main():
    parse_describe(sys.argv[1:])


if __name__ == "__main__":
    main()
