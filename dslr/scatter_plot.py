from matplotlib import pyplot as plt

from constants import COURSES, TRAIN_DATA_PATH
from dslr.models import DataSet
from dslr.utils import get_marks_by_house_and_course


def plot_courses_comparison(dataset, marks_x, course_y, axis):
    marks_y = get_marks_by_house_and_course(dataset, course=course_y)[0]
    axis.scatter(marks_x.raw_data, marks_y.raw_data, s=1)
    axis.set_title(course_y, fontsize=10)


def main():
    """
    Show a plot of the grades repartition for each house for each course
    """
    dataset = DataSet(TRAIN_DATA_PATH)

    for course_x in COURSES:
        fig, axes = plt.subplots(3, 4)
        fig.suptitle(course_x)
        marks_x = get_marks_by_house_and_course(dataset, course=course_x)[0]
        i = 0
        for course_y in COURSES:
            if course_x != course_y:
                plot_courses_comparison(dataset, marks_x, course_y, axes.flat[i])
                i += 1
        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    main()
