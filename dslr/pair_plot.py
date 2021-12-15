import sys

import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix

from constants import TRAIN_DATA_PATH
from dslr.models.dataset import DataSet
from dslr.utils import get_colors, parse_pair_plot


def get_data():
    data = DataSet(TRAIN_DATA_PATH).data
    data = data.dropna()
    colors = get_colors(data)
    data = data[data.columns[6:]]
    return data, colors


def main():  # pylint: disable=missing-function-docstring
    parse_pair_plot(sys.argv[1:])
    dataset, colors = get_data()
    matrix = scatter_matrix(dataset, c=colors, alpha=0.2, figsize=(6, 6), diagonal="hist")
    for data in matrix.reshape(-1):
        # rotate x labels
        data.xaxis.label.set_rotation(45)
        # padding y label
        data.get_yaxis().set_label_coords(-1, 0.5)
        # # del ticks
        data.set_xticks(())
        data.set_yticks(())
        plt.show()


if __name__ == "__main__":
    main()
