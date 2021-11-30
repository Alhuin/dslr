import csv
import sys

import numpy as np


class DataSet:
    """
    DataSet class handling csv parsing
    """

    def __init__(self, csv_path):
        self.header = None
        self.data = None
        self.features = []
        self.load_csv(csv_path)

    def load_csv(self, csv_path):
        """
        Opens the csv_path and loads the data contained
            exit if csv_path is invalid
        :param csv_path:    the path containing the dataset as csv
        """
        try:
            with open(csv_path, encoding="utf-8") as file:
                data = list(csv.reader(file, delimiter=","))
        except FileNotFoundError as error:
            print(f"Wrong file or file path: {error}", file=sys.stderr)
            sys.exit(0)

        self.header = np.array(data[0])
        self.data = np.array(data[1:], dtype=object)
        nb_cols = len(self.header)

        for row in self.data:
            if len(row) != nb_cols:
                sys.stderr.write("Invalid data format")
                sys.exit()

    def get_features(self, filters=None):
        if filters:
            data, header = self.filter_data(filters)
            filter_condition = f"{filters.label} == {filters.value}"
        else:
            data = self.data
            header = self.header
            filter_condition = None
        return [self.load_feature(header[i], column, filter_condition) for i, column in enumerate(zip(*data))]

    @staticmethod
    def load_feature(label, values, filters_name):
        first_value = next(value for value in values if value)
        try:
            float(first_value)
            return NumericFeature(label, [float(v) if v is not None else None for v in values], filters_name)
        except ValueError:
            return LiteralFeature(label, values, filters_name)

    def filter_data(self, filters):
        """
        Filter rows by condition label == value (eg house == ravenclaw)
        Then filter the selected cols
        """
        if filters.label:
            label_index = np.where(self.header == filters.label)[0][0]
            rows_mask = self.data[:, label_index] == filters.value
        else:
            rows_mask = [True for _ in range(self.data.shape[0])]
        cols_mask = np.in1d(self.header, filters.cols if filters.cols else self.header)
        return self.data[rows_mask][:, cols_mask], self.header[cols_mask]

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
        for feature in self.get_features():
            if feature.category == "numeric":
                output[0] += f"{feature.label if len(feature.label) <= 12 else f'{feature.label[:7]}...':>14}"
                output[1] += f"{feature.count():>14.6f}"
                output[2] += f"{feature.mean():>14.6f}"
                output[3] += f"{feature.std():>14.6f}"
                output[4] += f"{feature.min():>14.6f}"
                output[5] += f"{feature.percentile(0.25):>14.6f}"
                output[6] += f"{feature.percentile(0.5):>14.6f}"
                output[7] += f"{feature.percentile(0.75):>14.6f}"
                output[8] += f"{feature.max():>14.6f}"
        print("\n".join(output))


class Feature:  # pylint: disable=too-few-public-methods
    """Abstract Class for all Features"""

    def __init__(self, label, category, data, filter_condition):
        self.label = label
        self.filter_condition = filter_condition
        self.category = category
        self.raw_data = data
        self.data = [x for x in data if x is not None]
        self.len = len(self.data)
        if self.len == 0:
            sys.stderr.write("Cannot initialize feature: No data")
            sys.exit()

    def __str__(self):
        return f"{self.category} feature: {self.label}"


class NumericFeature(Feature):
    """
    Numeric Feature Class, handling basic statistics
    """

    def __init__(self, label, data, filter_condition=None):
        super().__init__(label, "numeric", data, filter_condition)

    def count(self):
        """Count number of non-NA/null observations"""
        return sum(1 for _ in self.data)

    def mean(self):
        """Mean of the values"""
        return sum(self.data) / self.len

    def std(self):
        """Standard deviation of the observations"""
        return (sum((x - self.mean()) ** 2 for x in self.data) / (self.len - 1)) ** 0.5

    def min(self):
        """Minimum of the values in the object"""
        minimum = self.data[0]
        for value in self.data:
            minimum = value if value < minimum else minimum
        return minimum

    def max(self):
        """Maximum of the values in the object"""
        maximum = self.data[0]
        for value in self.data:
            maximum = value if value > maximum else maximum
        return maximum

    def percentile(self, percentile):
        """Calculates the given percentile of the object with linear interpolation"""
        sorted_data = sorted(self.data)
        i = percentile * (self.len - 1)
        floor = int(i // 1)
        frac = i % 1
        return sorted_data[floor] + (sorted_data[floor + 1] - sorted_data[floor]) * frac

    def describe(self):
        """Prints the feature statistics (panda's style)"""
        print(
            f"{'count':<5}{self.count():>14.6f}\n"
            f"{'mean':<5}{self.mean():>14.6f}\n"
            f"{'std':<5}{self.std():>14.6f}\n"
            f"{'min':<5}{self.min():>14.6f}\n"
            f"{'25%':<5}{self.percentile(0.25):>14.6f}\n"
            f"{'50%':<5}{self.percentile(0.5):>14.6f}\n"
            f"{'75%':<5}{self.percentile(0.75):>14.6f}\n"
            f"{'max':<5}{self.max():>14.6f}"
        )


class LiteralFeature(Feature):  # pylint: disable=too-few-public-methods
    def __init__(self, label, data, filter_condition=None):
        super().__init__(label, "literal", data, filter_condition)


class Filter:  # pylint: disable=too-few-public-methods
    def __init__(self, label=None, value=None, cols=None):
        self.cols = cols
        self.label = label
        self.value = value

    def __str__(self):
        return f"cols {self.cols.__str__()} for {self.label} == {self.value}"
