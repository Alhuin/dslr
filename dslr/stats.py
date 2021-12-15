import numpy as np  # for sigmoid


def count_(data):
    """Count number of non-NA/null observations"""
    return sum(1 for _ in data)


def mean_(data):
    """Mean of the values"""
    return sum(data) / len(data)


def std_(data):
    """Standard deviation of the observations"""
    return (sum((x - mean_(data)) ** 2 for x in data) / (len(data) - 1)) ** 0.5


def min_(data):
    """Minimum of the values in the object"""
    minimum = data[0]
    for value in data:
        minimum = value if value < minimum else minimum
    return minimum


def max_(data):
    """Maximum of the values in the object"""
    maximum = data[0]
    for value in data:
        maximum = value if value > maximum else maximum
    return maximum


def percentile_(data, percentile):
    """Calculates the given percentile of the object with linear interpolation"""
    sorted_data = sorted(data)
    i = percentile * (len(data) - 1)
    floor = int(i // 1)
    frac = i % 1
    return sorted_data[floor] + (sorted_data[floor + 1] - sorted_data[floor]) * frac


def sigmoid_(value):
    return 1 / (1 + np.exp(-value))
