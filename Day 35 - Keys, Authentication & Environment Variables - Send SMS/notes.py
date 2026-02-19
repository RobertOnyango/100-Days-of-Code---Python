# https://www.ventusky.com/thunderstorms-map/cape#p=-9.4;36.8;4
# https://www.latlong.net/
# https://www.pythonanywhere.com/

import requests
from twilio.rest import Client


# Key authenticates your account to the OpenWeatherAPI provider
openweather_api_key = "----"
twilio_account_sid = "----"

# Python program that fetches the 5 day weather forecast of my location from the API url api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API key}
# 
# MY_LAT = -1.292066
MY_LAT = 6.524379
# MY_LONG = 36.821945
MY_LONG = 3.379206

API_URL = "https://api.openweathermap.org/data/2.5/forecast"

# API params
parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": openweather_api_key,
    "cnt": 4
}

# Fetch the data using get()
response = requests.get(url=API_URL, params=parameters)
# Manage the exceptions
response.raise_for_status()
# Extract the data
weather_data = response.json()

# Get the first weather id
# print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False

for hour_data in weather_data["list"]:
    # print(hour_data["weather"][0]["id"])
    condition_code = hour_data["weather"][0]["id"]

    if int(condition_code) > 700:
        # print("Bring an umbrella")
        will_rain = True

if will_rain:
    print("Bring an umbrella")
    # Create the twilio client
    client = Client(twilio_account_sid, twilio_auth_token)

    # Construct the message 
    message = client.api.account.messages.create(
        to="----",
        from_="-----",
        body="It's going to rain today. Remember to carry an umbrella")
    
    print(message.sid)

#---------- ENVIRONMENT VARIABLES ----------#
''' 
On Terminal, to see the environment variables:
    - Windows -> dir Env:
    - Linux -> env

Are used for: 1. Convenience 
              2. Security: Allows us to store keys and auth tokens in a separate file to the main code base

Save an environment variable and use it in your Python code
    On Terminal:
        - Save environment variable -> export AUTH_TOKEN=<token_key> [AUTH_TOKEN is a variable name]
    
    In Python code:
        - import os module
        - Call token -> auth_token = os.environ.get("AUTH_TOKEN")
'''