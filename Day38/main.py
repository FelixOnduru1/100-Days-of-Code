import requests
from datetime import datetime
import os

NT_APP_ID = os.environ["NT_APP_ID"]
NT_API_KEY = os.environ["NT_API_KEY"]
NUTRITION_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
GENDER = "male"
WEIGHT = "75"
HEIGHT = "200"
AGE = "23"
SHEETY_KEY = os.environ["SHEETY_KEY"]

date_today = datetime.now().strftime("%d/%m/%Y")
time_today = datetime.now().strftime("%H:%M:%S")

sheety_endpoint = os.environ["SHEETY_ENDPOINT"]
sheety_headers = {
    "Authorization": f"Basic {SHEETY_KEY}"
}
user_response = input("Tell me which exercises you did?")
headers = {
    "x-app-id": NT_APP_ID,
    "x-app-key": NT_API_KEY,
    "x-remote-user-id": "0",
}

exercise_params = {
    "query": user_response,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

response = requests.post(url=NUTRITION_ENDPOINT, json=exercise_params, headers=headers)
result = response.json()

exercises = result["exercises"]
for exercise in exercises:
    exercise_name = exercise["name"]
    exercise_duration = exercise["duration_min"]
    exercise_calories = exercise["nf_calories"]

    input_data = {
        "workout": {
            "date": date_today,
            "time": time_today,
            "exercise": exercise_name.title(),
            "duration": exercise_duration,
            "calories": exercise_calories
        }
    }

    response = requests.post(url=sheety_endpoint, json=input_data, headers=sheety_headers)
    print(response.text)
