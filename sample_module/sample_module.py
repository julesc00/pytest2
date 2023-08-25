import requests


# def get_data() -> dict:
#     request = requests.get("https://jsonplaceholder.typicode.com/todos/1")
#     data = request.json()
#     return data


def get_data() -> dict:
    return {"hello": 1234}


requests.get = get_data()
print(requests.get)
