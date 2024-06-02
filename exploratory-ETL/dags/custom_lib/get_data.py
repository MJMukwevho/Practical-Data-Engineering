"""
This module uses the request the request module to access
data in a random user api and mimick a login session
"""

import requests
import json


def get_data():
    """
    get data from random user api
    """
    try:
        url = "https://randomuser.me/api/"
        response = requests.get(url)
        status_code = response.status_code
        response = json.loads(response.text)
        return status_code, response["results"][0]
    except Exception as e:
        print(f"there was an error{e}")
        return None
