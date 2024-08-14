"""
This module provides functionality to create a pandas DataFrame 
using data fetched from the get_data function.

The create_dataframe function takes an integer input to specify
the number of data entries and returns a pandas DataFrame containing
that many records.
"""

import pandas as pd
from .get_data import get_data


def create_dataframe(num: int) -> pd.DataFrame:
    """
    Function to create a pandas DataFrame.

    Parameters:
    num (int): The number of data entries to include in the DataFrame.

    Returns:
    pd.DataFrame: A DataFrame containing the specified number of records.

    Example:
    df = create_dataframe(10)
    print(df)
    """
    people_list = []

    for _ in range(num):
        _, data = get_data()
        people_list.append(data)

    data = pd.DataFrame(people_list)

    print("my name")
    return data
