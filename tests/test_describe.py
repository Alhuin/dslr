import pandas

from constants import test_dataset_path
from dslr.describe import describe


def test_describe_on_test_dataset(capfd):
    csvfile = pandas.read_csv(test_dataset_path, encoding="utf-8")
    describe(test_dataset_path)
    out, err = capfd.readouterr()
    assert out == csvfile.describe().__str__()
