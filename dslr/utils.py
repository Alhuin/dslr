import argparse


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


def is_num(string):
    try:
        float(string)
    except ValueError:
        return False
    else:
        return True
