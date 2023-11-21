import requests
from datetime import datetime
import os


# Get exercise stats for a user input
nutrition_endpoint = "https://trackapi.nutritionix.com/v2"
exercise_endpoint = f"{nutrition_endpoint}/natural/exercise"
APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]
nutrition_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

user_input = input("What exercises did you do today? (Enter the name of the exercise and how long you spent doing it)\n")
# user_input = "10 minutes of walking and 30 minutes of swimming"
exercise_parameters = {
    "query": user_input,
    "gender": "male",
    "weight_kg": 72.5,
    "height_cm": 167.64,
    "age": 30
}

response = requests.post(url=exercise_endpoint, json=exercise_parameters, headers=nutrition_headers)
response.raise_for_status()
data = response.json()
print(data)

# exercise = data["exercises"][0]["user_input"]
# duration = data["exercises"][0]["duration_min"]
# calories = data["exercises"][0]["nf_calories"]

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")


sheety_endpoint = os.environ["SHEETY_ENDPOINT"]
sheety_headers = {
    "Authorization": os.environ["SHEETY_TOKEN"]
}

for exercise in data["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["user_input"],
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    response = requests.post(url=sheety_endpoint, json=sheet_inputs, headers=sheety_headers)
    response.raise_for_status()
    print(response.json())

