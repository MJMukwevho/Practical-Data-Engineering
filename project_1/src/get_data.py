def get_data():
    """
    get data from random user api
    """
    try:
        url = "https://randomuser.me/api/"
        response = requests.get(url)
        response = json.loads(response.text)
        return response["results"][0]
    except Exception as e:
        print(f"there was an error{e}")
        return None
