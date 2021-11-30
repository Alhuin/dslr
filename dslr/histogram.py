import numpy as np
from matplotlib import pyplot as plt

from constants import COURSES, HOUSES, TRAIN_DATA_PATH
from dslr.models import DataSet
from dslr.utils import get_marks_by_house_and_course


def plot_house(axis, dataset, house, course, bins):
    marks = get_marks_by_house_and_course(dataset, course, house["name"])[0]
    axis.hist(marks.data, bins=bins, color=house["color"], label=house["name"], alpha=0.5)


def plot_histogram_by_course(dataset, course, axis):
    """
    add a plot of the repartition of grades by house for a given course
    """
    global_marks = get_marks_by_house_and_course(dataset, course)[0]
    bins = np.linspace(global_marks.min(), global_marks.max())

    for house in HOUSES:
        plot_house(axis, dataset, house, course, bins)
    axis.set_title(f"{course}", fontsize=10)


def main():
    """
    Show a plot of the grades repartition for each house for each course
    """
    fig, axes = plt.subplots(3, 5)
    dataset = DataSet(TRAIN_DATA_PATH)

    for i, course in enumerate(COURSES):
        plot_histogram_by_course(dataset, course, axes.flat[i])

    axes.flat[-1].axis("off")
    axes.flat[-2].axis("off")
    handles, labels = axes.flat[-3].get_legend_handles_labels()
    fig.legend(handles, labels, loc="lower right", ncol=2)
    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
