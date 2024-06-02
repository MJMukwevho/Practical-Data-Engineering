import pandas as pd
from .get_data import get_data

"""
This module is for creating pandas dataframe from API data
"""


def create_dataframe(num):
    """
    Function to create pandas dataframe

    Input:
        num --> number of data entries

    return:
        Pandas dataframe with number of records equal to num

    """
    people_list = []

    for _ in range(num):
        _, data = get_data()
        people_list.append(data)

    data = pd.DataFrame(people_list, index=None)

    return data
