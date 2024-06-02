"""
This module uses the request the request module to access
data in a random user api and mimick a login session
"""

import json
import requests


def get_data():
    """
    get data from random user api
    """
    try:
        url = "https://randomuser.me/api/"
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        status_code = response.status_code
        response_json = response.json()
        return status_code, response_json["results"][0]
    except requests.exceptions.RequestException as e:
        print(f"There was a network error: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"There was an error decoding the JSON response: {e}")
        return None
