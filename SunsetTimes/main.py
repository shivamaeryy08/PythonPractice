import requests
from datetime import datetime
import time
import math

LONGITUDE = -73.567253
LATITUDE = 45.501690


def is_iss_overhead():
    response_iss = requests.get(url='http://api.open-notify.org/iss-now.json')
    response_iss.raise_for_status()
    data_iss = response_iss.json()
    iss_lat = float(data_iss['iss_position']['latitude'])
    iss_longitude = float(data_iss['iss_position']['longitude'])
    if math.isclose(iss_longitude, LONGITUDE) and math.isclose(iss_lat, LATITUDE):
        return True
    return False


def is_night():
    response = requests.get(url=f'https://api.sunrise-sunset.org/json?lat={LATITUDE}&lng={LONGITUDE}&formatted=0')
    response.raise_for_status()
    data = response.json()
    sunrise = data['results']['sunrise']
    sunset = data['results']['sunset']
    sunrise_hour = int(sunrise.split('T')[1].split(':')[0])
    sunset_hour = int(sunset.split('T')[1].split(':')[0])
    time_now = datetime.now()
    cur_hour = time_now.hour
    if sunset_hour <= cur_hour <= sunrise_hour:
        return True
    return False


while True:
    if is_night() and is_iss_overhead():
        print("Look up the iss is above you")
    time.sleep(60)
