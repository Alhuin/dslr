import sys

from matplotlib import pyplot as plt

from constants import COURSES, HOUSES, TRAIN_DATA_PATH
from dslr.models import DataSet
from dslr.utils import get_marks_by_house_and_course, parse_histogram


def plot_histogram_by_course(dataset, course, axis=plt):
    """
    add a plot of the repartition of grades by house for a given course
    """
    for house in HOUSES:
        marks = get_marks_by_house_and_course(dataset.data, course, house["name"])
        axis.hist(marks, bins="rice", color=house["color"], label=house["name"], alpha=0.5)


def plot_all_histograms(dataset):
    """
    Plots all the courses as histograms in one plot
    """
    fig, axes = plt.subplots(3, 5)

    for i, course in enumerate(COURSES):
        plot_histogram_by_course(dataset, course, axes.flat[i])
        axes.flat[i].set_title(f"{course}", fontsize=10)

    axes.flat[-1].axis("off")
    axes.flat[-2].axis("off")
    handles, labels = axes.flat[-3].get_legend_handles_labels()
    fig.legend(handles, labels, loc="lower right", ncol=2)
    fig.tight_layout()
    plt.show()


def plot_one_histogram(dataset, course):
    plt.title(course)
    plot_histogram_by_course(dataset, course)
    plt.xlabel("Marks")
    plt.ylabel("Number of Students")
    plt.legend(loc="upper right", ncol=2)
    plt.show()


def main():
    """
    Show a plot of the grades repartition for each house for each course
    """
    args = parse_histogram(sys.argv[1:])
    dataset = DataSet(TRAIN_DATA_PATH)

    if args.all:
        plot_all_histograms(dataset)
    else:
        plot_one_histogram(dataset, args.course)


if __name__ == "__main__":
    main()
