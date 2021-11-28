import sys

import numpy as np


class DataSet:
    """
    DataSet class handling csv parsing
    """

    # pylint: disable=too-few-public-methods
    def __init__(self):
        self.data = None

    def load_csv(self, csv_path):
        """
        Opens the csv_path and loads the data contained
            exit if csv_path is invalid
        :param csv_path:    the path containing the dataset as csv
        """
        try:
            with open(csv_path, encoding="utf-8") as file:
                self.data = np.loadtxt(file, delimiter=",", skiprows=1)
        except FileNotFoundError:
            print("Wrong file or file path", file=sys.stderr)
            sys.exit(0)
        except ValueError:
            print("Invalid data format", file=sys.stderr)
            sys.exit(0)
