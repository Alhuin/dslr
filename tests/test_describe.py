import pandas
import pytest

from constants import TEST_DATA_PATH
from dslr.describe import describe


@pytest.mark.xfail
def test_describe_on_test_dataset(capfd):
    csvfile = pandas.read_csv(TEST_DATA_PATH, encoding="utf-8")
    describe(TEST_DATA_PATH)
    captured = capfd.readouterr()
    assert captured.out == csvfile.describe().__str__()
