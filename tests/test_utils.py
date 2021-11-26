from argparse import Namespace

import pytest

from constants import USAGE
from dslr.utils import parse_describe


def test_parse_describe_no_args(capfd):
    with pytest.raises(SystemExit):
        parse_describe([])
    out, err = capfd.readouterr()
    assert err == (
        "usage: describe.py [-h] csv_path\n"
        "describe.py: error: the following arguments are required: csv_path\n"
    )


def test_parse_describe():
    arguments = parse_describe(["test"])
    assert arguments == Namespace(csv_path="test")


def test_parse_print_help_and_exit(capfd):
    with pytest.raises(SystemExit):
        parse_describe(["-h"])
    out, err = capfd.readouterr()
    assert out == USAGE


def test_parse_describe_unrecognized_aguments(capfd):
    with pytest.raises(SystemExit):
        parse_describe(["path.csv", "-q"])
    out, err = capfd.readouterr()
    assert err == (
        "usage: describe.py [-h] csv_path\n"
        "describe.py: error: unrecognized arguments: -q\n"
    )
