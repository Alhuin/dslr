import pytest

from dslr.models import DataSet
from dslr.stats import count_, max_, mean_, min_, percentile_, std_

#   DataSet


def test_dataset_wrong_path(capfd):
    with pytest.raises(SystemExit):
        DataSet("d")
    captured = capfd.readouterr()
    assert captured.err == "Wrong file or file path: [Errno 2] No such file or directory: 'd'\n"


#   Stats


def test_count_():
    assert count_([1, 2, 3]) == 3


def test_mean_():
    assert mean_([1, 2, 3]) == 2


def test_std_():
    assert std_([1, 2, 8, 13]) == 5.597618541248888


def test_min_():
    assert min_([1, 2, 8, 13, -5]) == -5


def test_max_():
    assert max_([1, 2, 8, 13, -5]) == 13


def test_percentile_():
    assert percentile_([0, 1, 5, 5, 5, 6, 6, 7, 7, 8, 11, 12, 21, 23, 23, 24], 0.85) == 22.5
