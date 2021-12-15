import argparse

from constants import HOUSES


def parse_describe(args):
    parser = argparse.ArgumentParser(prog="describe.py", description="description of a csv file. (pandas style)")
    parser.add_argument("csv_path", type=str, help="the path where the csv file is stored")
    return parser.parse_args(args)


def parse_histogram(args):  # pylint: disable=missing-function-docstring
    parser = argparse.ArgumentParser(
        prog="histogram.py",
        description="plot house grades by class as histograms",
        epilog="by default, plot only the class with the most similar marks distribution between houses",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="plot all classes",
        default=False,
    )
    parser.add_argument("-c", "--course", type=str, help="plot one class", default="Care of Magical Creatures")
    return parser.parse_args(args)


def parse_scatter_plot(args):  # pylint: disable=missing-function-docstring
    parser = argparse.ArgumentParser(
        prog="scatter_plot.py",
        description="plot comparison of class marks distribution as scatter plots",
        epilog="by default, plot only the comparison between classes with the most similar marks distributions",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="plot all the comparisons",
        default=False,
    )
    parser.add_argument(
        "-c",
        "--courses",
        nargs=2,
        type=str,
        help="plot one scatter plot representing how much the grades of one course impacts the grades of another",
        default=["Defense Against the Dark Arts", "Astronomy"],
    )
    parser.add_argument(
        "-afo",
        "--all_for_one",
        nargs=1,
        type=str,
        help="plot all the comparisons for one course",
    )
    return parser.parse_args(args)


def parse_pair_plot(args):
    parser = argparse.ArgumentParser(prog="pair_plot.py", description="plot the dataset as a pair plot")
    return parser.parse_args(args)


def get_colors(data):
    return [HOUSES[house] for house in data["Hogwarts House"]]
