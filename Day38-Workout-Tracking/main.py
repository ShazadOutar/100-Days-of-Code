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

# user_input = input("What exercise did you do today?\n")
user_input = "10 minutes of walking"
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

exercise = data["exercises"][0]["user_input"]
duration = data["exercises"][0]["duration_min"]
calories = data["exercises"][0]["nf_calories"]

username = "shazadOutar"
projectName = "workoutTracking"
sheetName = "workouts"
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

sheety_endpoint = f"https://api.sheety.co/54a5c9fc2c1ce03f86296e0da8c2aee0/{projectName}/{sheetName}"
sheety_headers = {
    "Authorization": "Bearer dsAwOIwklqxP"
}

sheet_inputs = {
    "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise,
            "duration": duration,
            "calories": calories,
        }
}

response = requests.post(url=sheety_endpoint, json=sheet_inputs, headers=sheety_headers)
response.raise_for_status()
print(response.json())

