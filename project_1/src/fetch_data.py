import pandas as pd
from get_data import get_data


def create_dataframe(num):
    people_list = []

    for _ in range(num):
        _, data = get_data()
        people_list.append(data)

    data = pd.DataFrame(people_list, index=None)

    return data
