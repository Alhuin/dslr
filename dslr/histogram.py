import numpy as np
from matplotlib import pyplot as plt

from constants import COURSES, TRAIN_DATA_PATH
from dslr.models import DataSet, Filter


def get_marks_by_house_and_course(data, course, house=None):
    if house is not None:
        filters = Filter(label="Hogwarts House", value=house, cols=[course])
    else:
        filters = Filter(cols=[course])
    return data.get_features(filters)


def get_worst_grade(data):
    minimum = data[0].min()
    for course in data:
        minimum = course.min() if course.min() < minimum else minimum
    return minimum


def get_best_grade(data):
    maximum = data[0].max()
    for course in data:
        maximum = course.max() if course.max() > maximum else maximum
    return maximum


def plot_histogram_by_course(dataset, course, axis):
    """
    add a plot of the repartition of grades by house for a given course
    """
    global_marks = get_marks_by_house_and_course(dataset, course)
    best_grade = get_best_grade(global_marks)
    worst_grade = get_worst_grade(global_marks)
    ravenclaw_marks = get_marks_by_house_and_course(dataset, course, "Ravenclaw")[0]
    slytherin_marks = get_marks_by_house_and_course(dataset, course, "Slytherin")[0]
    gryffindor_marks = get_marks_by_house_and_course(dataset, course, "Gryffindor")[0]
    hufflepuff_marks = get_marks_by_house_and_course(dataset, course, "Hufflepuff")[0]
    bins = np.linspace(worst_grade, best_grade)

    axis.hist(ravenclaw_marks.data, bins=bins, color="b", label="Ravenclaw", alpha=0.5)
    axis.hist(gryffindor_marks.data, bins=bins, color="r", label="Gryffindor", alpha=0.5)
    axis.hist(slytherin_marks.data, bins=bins, color="g", label="Slytherin", alpha=0.5)
    axis.hist(hufflepuff_marks.data, bins=bins, color="y", label="Hufflepuff", alpha=0.5)
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
