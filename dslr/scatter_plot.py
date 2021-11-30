import sys

from matplotlib import pyplot as plt

from constants import COURSES, TRAIN_DATA_PATH
from dslr.models import DataSet
from dslr.utils import get_marks_by_house_and_course, parse_scatter_plot


def plot_all_scatters(dataset, courses):
    """
    Plot all the possible comparison between courses (one view by course)
    """
    for course_x in courses:
        fig, axes = plt.subplots(3, 4)
        fig.suptitle(course_x)
        marks_x = get_marks_by_house_and_course(dataset, course=course_x)[0]
        i = 0
        for course_y in COURSES:
            if course_x != course_y:
                axis = axes.flat[i]
                marks_y = get_marks_by_house_and_course(dataset, course=course_y)[0]
                axis.scatter(marks_x.raw_data, marks_y.raw_data, s=1)
                axis.set_title(marks_y.label, fontsize=10)
                i += 1
        plt.tight_layout()
        plt.show()


def plot_one_scatter(dataset, courses):
    course_x, course_y = courses
    marks_x = get_marks_by_house_and_course(dataset, course=course_x)[0]
    marks_y = get_marks_by_house_and_course(dataset, course=course_y)[0]
    plt.title(f"{course_x} vs {course_y}")
    plt.scatter(marks_x.raw_data, marks_y.raw_data, s=1)
    plt.xlabel(course_x)
    plt.ylabel(course_y)
    plt.show()


def main():
    """
    Show a plot of the grades repartition for each house for each course
    """
    args = parse_scatter_plot(sys.argv[1:])
    dataset = DataSet(TRAIN_DATA_PATH)

    if args.all:
        plot_all_scatters(dataset, COURSES)
    elif args.all_for_one:
        plot_all_scatters(dataset, args.all_for_one)
    else:
        plot_one_scatter(dataset, args.courses)


if __name__ == "__main__":
    main()
