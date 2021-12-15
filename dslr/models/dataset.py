import sys

import pandas as pd
from pandas.core.dtypes.common import is_numeric_dtype

from dslr.stats import count_, max_, mean_, min_, percentile_, std_


class DataSet:
    """
    DataSet class handling csv parsing
    """

    def __init__(self, csv_path: str):
        self.data = None
        self.load_csv(csv_path)

    def load_csv(self, csv_path: str) -> None:
        """
        Opens the csv_path and loads the data contained
            exit if csv_path is invalid
        :param csv_path:    the path containing the dataset as csv
        """
        try:
            self.data = pd.read_csv(csv_path)
        except FileNotFoundError as error:
            print(f"Wrong file or file path: {error}", file=sys.stderr)
            sys.exit(0)

    def describe(self):
        """
        Describes the numeric features of the dataset (panda's style)
        """
        output = [
            f"{'':<5}",
            f"{'Count':<5}",
            f"{'Mean':<5}",
            f"{'Std':<5}",
            f"{'Min':<5}",
            f"{'25%':<5}",
            f"{'50%':<5}",
            f"{'75%':<5}",
            f"{'Max':<5}",
        ]

        for feature in self.data:
            if is_numeric_dtype(self.data[feature]):
                data = self.data[feature].dropna()
                output[0] += f"{feature if len(feature) <= 12 else f'{feature[:7]}...':>14}"
                output[1] += f"{count_(data):>14.6f}"
                output[2] += f"{mean_(data):>14.6f}"
                output[3] += f"{std_(data):>14.6f}"
                output[4] += f"{min_(data):>14.6f}"
                output[5] += f"{percentile_(data, 0.25):>14.6f}"
                output[6] += f"{percentile_(data, 0.5):>14.6f}"
                output[7] += f"{percentile_(data, 0.75):>14.6f}"
                output[8] += f"{max_(data):>14.6f}"
        print("\n".join(output))
