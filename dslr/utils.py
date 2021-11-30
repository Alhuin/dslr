import argparse

from dslr.models import Filter


def parse_describe(args):
    parser = argparse.ArgumentParser(prog="describe.py", description="description of a csv file. (pandas style)")
    parser.add_argument("csv_path", type=str, help="the path where the csv file is stored")
    return parser.parse_args(args)


def parse_histogram(args):
    parser = argparse.ArgumentParser(prog="histogram.py", description="plot house grades by class as histograms")
    parser.add_argument(
        "--all",
        action="store_true",
        help="plot all classes (by default, plot only the class with the most similar distribution between houses)",
        default=False,
    )
    return parser.parse_args(args)


def parse_scatter_plot(args):  # pylint: disable=missing-function-docstring
    parser = argparse.ArgumentParser(
        prog="scatter_plot.py", description="plot comparison of class marks distribution as scatter plots"
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help=(
            "plot all the comparisons (by default, plot only the comparison between classes with the most similar "
            "distributions)"
        ),
        default=False,
    )
    return parser.parse_args(args)


def get_marks_by_house_and_course(data, course, house=None):
    if house is not None:
        filters = Filter(label="Hogwarts House", value=house, cols=[course])
    else:
        filters = Filter(cols=[course])
    return data.get_features(filters)
