import pandas

from constants import test_dataset_path
from dslr.describe import describe


def test_main_output_w_test_dataset(capfd):
    csvfile = pandas.read_csv(test_dataset_path, encoding='utf-8')
    assert describe(test_dataset_path) == csvfile.describe().__str__()
