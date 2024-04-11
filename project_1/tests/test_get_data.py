import sys

sys.path.insert(0, "src")
import pytest
from src.get_data import get_data


def test_data():
    """
    Tests API is returning values by checking 200
    """
    status_code, _ = get_data()

    assert status_code == 200
