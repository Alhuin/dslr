import sys
import numpy as np


class DataSet:
    def __init__(self):
        self.data = None

    def load_csv(self, csv_path):
        """
            Opens the csv_path and loads the data contained
                exit if csv_path is invalid
            :param csv_path:    the path containing the dataset as csv
        """
        try:
            self.data = np.loadtxt(
                open(csv_path),
                delimiter=",",
                skiprows=1
            )
        except FileNotFoundError:
            print("Wrong file or file path", file=sys.stderr)
            sys.exit(0)
        except ValueError:
            print("Invalid data format", file=sys.stderr)
            sys.exit(0)
