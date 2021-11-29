from constants import COURSES, TRAIN_DATA_PATH
from dslr.models import DataSet, Filter


def get_marks_by_house(data, house):
    filters = Filter(label="Hogwarts House", value=house, cols=COURSES)
    return data.get_features(filters)


dataset = DataSet(TRAIN_DATA_PATH)
ravenclaw_marks = get_marks_by_house(dataset, "Ravenclaw")
slytherin_marks = get_marks_by_house(dataset, "Slytherin")
gryffindor_marks = get_marks_by_house(dataset, "Gryffindor")
hufflepuff_marks = get_marks_by_house(dataset, "Hufflepuff")
