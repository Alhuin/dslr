import pytest

from constants import WRONG_FORMAT_DATA_PATH
from dslr.models import DataSet


def test_dataset_wrong_path(capfd):
    dataset = DataSet()
    with pytest.raises(SystemExit):
        dataset.load_csv("d")
    captured = capfd.readouterr()
    assert captured.err == "Wrong file or file path\n"


def test_dataset_wrong_format(capfd):
    dataset = DataSet()
    with pytest.raises(SystemExit):
        dataset.load_csv(WRONG_FORMAT_DATA_PATH)
    captured = capfd.readouterr()
    assert captured.err == "Invalid data format\n"
