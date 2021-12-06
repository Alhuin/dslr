import argparse


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
    parser.add_argument("-c", "--course", type=str, help="the course to plot", default="Care of Magical Creatures")
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


def get_marks_by_house_and_course(dataframe, course, house=None):
    if house is not None:
        return dataframe[dataframe["Hogwarts House"] == house][course]
    return dataframe[course]
