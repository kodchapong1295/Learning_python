from decouple import config
import requests
from datetime import datetime

GENDER = 'male'
WEIGHT_KG = 82
HEIGHT_CM = 170
AGE = 20

NUTRITIONIX_APP_ID = config("NUTRITIONIX_APP_ID")
NUTRITIONIX_API_KEY = config("NUTRITIONIX_API_KEY")
SHEETY_BEARER_KEY = config("SHEETY_BEARER_KEY")

nutritionix_endpoint = "https://trackapi.nutritionix.com/"

exercise_endpoint=f"{nutritionix_endpoint}/v2/natural/exercise"
exercise_params = {
    "query": input("Tell me which exercise you did?: "),
    "gender":"female",
    "weight_kg":WEIGHT_KG,
    "height_cm":HEIGHT_CM,
    "age":AGE
}

headers = {
    'x-app-id': NUTRITIONIX_APP_ID,
    'x-app-key': NUTRITIONIX_API_KEY,
    'Content-Type': 'application/json'
}

response = requests.post(url=exercise_endpoint, json=exercise_params, headers=headers)
result = response.json()
print(result)

now = datetime.now()
current_date = now.date().strftime('%d/%m/%Y')
current_time = now.time().strftime('%X')


sheety_add_record_endpoint = "https://api.sheety.co/302424d51f43453377ceccb76743d6d4/workoutTracking/workouts"

for exercise in result["exercises"]:
    exercise_name = exercise["name"].title()
    duration = exercise["duration_min"]
    calories = exercise["nf_calories"]
    sheety_params = {
        "workout": {
            "date": current_date,
            "time": current_time,
            "exercise": exercise_name.title(),
            "duration": str(duration),
            "calories": calories
        }
    }
    sheety_header = {
        'Content-Type': "application/json",
        'Authorization': SHEETY_BEARER_KEY
    }
    sheety_response = requests.post(sheety_add_record_endpoint, json=sheety_params, headers=sheety_header)
    print(sheety_response.text)

