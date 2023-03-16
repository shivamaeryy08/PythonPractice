import requests
import os
from datetime import date, datetime
from config import *

height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))
gender = input("Enter your gender (male/female): ")
age = int(input("Enter your age: "))
exercises = input("Tell me what exercises you did: ")
app_id = os.getenv('app_id')
api_key = os.getenv('api_key')

exercise_params = {
    "query": exercises,
    "gender": gender,
    "weight_kg": weight,
    "height_cm": height,
    "age": age
}
sheet_endpt = f'https://api.sheety.co/{os.getenv("sheety_key")}/exercisesasd/sheet1'
exercise_endpt = 'https://trackapi.nutritionix.com/v2/natural/exercise'
headers = {
    'x-app-id': app_id,
    'x-app-key': api_key,

}
response = requests.post(url=f'{exercise_endpt}', json=exercise_params, headers=headers)
response.raise_for_status()
data = response.json()
exercises = data['exercises']
cur_time = datetime.now().time()
sheety_body = {
    "sheet1": {
        "date": date.today().strftime('%d/%m/%y'),
        "time": f"{cur_time.hour}:{cur_time.minute}:{cur_time.second}",
        "exercise": "Running",
        "duration": 22,
        "calories": 130
    }
}
for exercise in exercises:
    sheety_body['sheet1']['exercise'] = exercise['name']
    sheety_body['sheet1']['duration'] = exercise['duration_min']
    sheety_body['sheet1']['calories'] = exercise['nf_calories']
    response = requests.post(url=f'{sheet_endpt}', json=sheety_body)
    response.raise_for_status()
