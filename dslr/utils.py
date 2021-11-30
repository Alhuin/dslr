import argparse

from dslr.models import Filter


def parse_describe(args):
    """
    Parse arguments from sys.argv
    :param
        list: args:     all the arguments passed from command line
    :return:
        Namespace: parsed_args:    the parsed arguments
    """
    parser = argparse.ArgumentParser(prog="describe.py", description="description of a csv file. (pandas style)")
    parser.add_argument("csv_path", type=str, help="the path where the csv file is stored")
    return parser.parse_args(args)


def get_marks_by_house_and_course(data, course, house=None):
    if house is not None:
        filters = Filter(label="Hogwarts House", value=house, cols=[course])
    else:
        filters = Filter(cols=[course])
    return data.get_features(filters)
