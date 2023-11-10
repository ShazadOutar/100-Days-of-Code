# import requests
# # ISS API Example
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# # get the json response data
# print(response.json())
# data = response.json()
# # print the status code
# print(response.status_code)
# # raise an error if the status code is one of failure
# response.raise_for_status()
# print(data["iss_position"])
# longitude = data["iss_position"]["longitude"]
# print(longitude)
# latitude = data["iss_position"]["latitude"]
# print(latitude)
# position = (latitude, longitude)
# print(position)

import requests
LOCATION = (40.7690837799405, -73.96769396344857)
MY_LAT = LOCATION[0]
MY_LONG = LOCATION[1]

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
print(response.status_code)
print(data)
