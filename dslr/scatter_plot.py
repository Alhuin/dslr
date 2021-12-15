import sys

from matplotlib import pyplot as plt

from constants import COURSES, TRAIN_DATA_PATH
from dslr.models.dataset import DataSet
from dslr.utils import get_colors, parse_scatter_plot


def plot_all_scatters(data, courses):
    """
    Plot all the possible comparison between courses (one view by course)
    """
    for course_x in courses:
        fig, axes = plt.subplots(3, 4)
        fig.suptitle(course_x)
        i = 0
        for course_y in COURSES:
            if course_x != course_y:
                axis = axes.flat[i]
                axis.scatter(data[course_x], data[course_y], s=1, c=get_colors(data))
                axis.set_title(course_y, fontsize=10)
                i += 1
        plt.tight_layout()
        plt.show()


def plot_one_scatter(data, courses):
    course_x, course_y = courses
    data.plot.scatter(x=course_x, y=course_y, s=1, c=get_colors(data))
    plt.title(f"{course_x} vs {course_y}")
    plt.show()


def main():
    """
    Show a plot of the grades repartition for each house for each course
    """
    args = parse_scatter_plot(sys.argv[1:])
    dataset = DataSet(TRAIN_DATA_PATH)

    if args.all:
        plot_all_scatters(dataset.data, COURSES)
    elif args.all_for_one:
        plot_all_scatters(dataset.data, args.all_for_one)
    else:
        plot_one_scatter(dataset.data, args.courses)


if __name__ == "__main__":
    main()
