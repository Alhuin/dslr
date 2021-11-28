import pytest

from constants import WRONG_FORMAT_DATA_PATH
from dslr.models import DataSet, Feature, NumericFeature

#   DataSet


def test_dataset_wrong_path(capfd):
    with pytest.raises(SystemExit):
        DataSet("d")
    captured = capfd.readouterr()
    assert captured.err == "Wrong file or file path: [Errno 2] No such file or directory: 'd'\n"


def test_dataset_wrong_format(capfd):
    with pytest.raises(SystemExit):
        DataSet(WRONG_FORMAT_DATA_PATH)
    captured = capfd.readouterr()
    assert captured.err == "Invalid data format\n"


#   Feature


def test_feature_init_no_data(capfd):
    with pytest.raises(SystemExit):
        Feature("label", "category", [])
    captured = capfd.readouterr()
    assert captured.err == "Cannot initialize feature: No data\n"


def test_feature_str(capfd):
    feature = Feature("label", "category", [1, 2, 3])
    print(feature)
    captured = capfd.readouterr()
    assert captured.out == "category feature: label\n"


#   NumericFeature


def test_count():
    feature = NumericFeature("label", [1, 2, 3])
    assert feature.count() == 3


def test_mean():
    feature = NumericFeature("label", [1, 2, 3])
    assert feature.mean() == 2


def test_std():
    feature = NumericFeature("label", [1, 2, 8, 13])
    assert feature.std() == 54.270925303824825


def test_min():
    feature = NumericFeature("label", [1, 2, 8, 13, -5])
    assert feature.min() == -5


def test_max():
    feature = NumericFeature("label", [1, 2, 8, 13, -5])
    assert feature.max() == 13


def test_percentile():
    feature = NumericFeature("label", [0, 1, 5, 5, 5, 6, 6, 7, 7, 8, 11, 12, 21, 23, 23, 24])
    assert feature.percentile(0.85) == 22.5


def test_describe(capfd):
    feature = NumericFeature("label", [1, 2, 3, 4, 5])
    feature.describe()
    captured = capfd.readouterr()
    assert (
        captured.out
        == "count      5.000000\n"
        "mean       3.000000\n"
        "std        5.000000\n"
        "min        1.000000\n"
        "25%        2.000000\n"
        "50%        3.000000\n"
        "75%        4.000000\n"
        "max        5.000000\n"
    )
