import pytest

from constants import DUMMY_DATA_PATH
from dslr.data_viz.describe import main


def test_main_on_test_dataset(capfd):
    main({"csv_path": DUMMY_DATA_PATH})
    captured = capfd.readouterr()
    assert (
        captured.out
        == "              Index      Feature1      Feature2\n"
        "Count      3.000000      3.000000      3.000000\n"
        "Mean       1.000000    169.884067    208.333333\n"
        "Std        1.000000    328.060293    618.449944\n"
        "Min        0.000000    -73.347800   -442.000000\n"
        "25%        0.500000    -16.673900    -82.000000\n"
        "50%        1.000000     40.000000    278.000000\n"
        "75%        1.500000    291.500000    533.500000\n"
        "Max        2.000000    543.000000    789.000000\n"
    )


def test_main_no_args(capfd):
    with pytest.raises(SystemExit):
        main()
    captured = capfd.readouterr()
    assert (
        captured.err
        == "usage: describe.py [-h] csv_path\ndescribe.py: error: the following arguments are required: csv_path\n"
    )
