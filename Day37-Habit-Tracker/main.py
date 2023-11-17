import requests
from datetime import datetime

TOKEN = "cFtJQEjOkfNiETOcvMmM"
USERNAME = "shazad"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "cFtJQEjOkfNiETOcvMmM",
    "username": "shazad",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# make a post request to create the account
# only run once at the beginning to create the account
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_id = "graph1"

graph_config = {
    "id": graph_id,
    "name": "Coding Graph",
    "unit": "lines",
    "type": "int",
    "color": "ichou",
}

headers = {
    "X-USER-TOKEN": TOKEN
}
# use headers pass the api key in the request header
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# post a pixel to the graph
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_id}"

# today = datetime(year=, month=, day=)
today = datetime.now().strftime("%Y%m%d")
# print(today)

pixel_config = {
    "date": today,
    "quantity": input("How many lines for today? "),
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_config, headers=headers)
print(response.text)

# update a pixel using a put request
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_id}/{today}"
new_pixel_data = {
    "quantity": "2"
}
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

# delete a pixel
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_id}/{today}"
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
