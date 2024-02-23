import requests

name = "Mike"


def get_gender(name):
    query = {"name": name}
    response = requests.get("https://api.agify.io/", params=query)
    response.raise_for_status()
    print(response)
    data = response.json()

    print(data)
    return data


print(get_gender(name)["age"])
