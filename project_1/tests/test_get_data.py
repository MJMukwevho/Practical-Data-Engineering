import sys

sys.path.insert(0, "src")
import pytest
import pandas as pd
from src.get_data import get_data
from src.fetch_data import create_dataframe


def test_data():
    """
    Tests API is returning values by checking 200
    """
    status_code, _ = get_data()

    assert status_code == 200


def test_fetch_data():

    data = create_dataframe(num=5)

    assert len(data) == 5
