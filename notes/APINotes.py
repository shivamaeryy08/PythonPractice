# API Application Programming Interface

# Set of commands, functions, protocols and objects that programmers use to make software or interact

# with external system

# API endpt is a url

import requests

response = requests.get(url='http://api.open-notify.org/iss-now.json')
response.raise_for_status()
data = response.json()
# 1xx Hold on process still happening result not final

# 2xx then request good

# 3xx u have no permission

# 4xx u did error

# 5xx internal server problem

# API PARAMS

parameters = {
    'lat': 14.0,
    'lng': 15.0

}

# REQUEST WITH PARAMS

sunset_response = requests.get(url=f'https://api.sunrise-sunset.org/json', params=parameters)
sunset_response.raise_for_status()
sun_data = sunset_response.json()
print(sun_data)
