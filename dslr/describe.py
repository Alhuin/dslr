import sys

from dslr.models.dataset import DataSet
from dslr.utils import parse_describe


def main(args=None):
    if args is None:
        args = parse_describe(sys.argv[1:])
        csv_path = args.csv_path  # pragma: no cover  (unreachable by tests)
    else:
        csv_path = args["csv_path"]

    dataset = DataSet(csv_path)
    dataset.describe()


if __name__ == "__main__":  # pragma: no cover
    main()
