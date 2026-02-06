# An Application Programming Interface (API) is a set of commands, functions, protocols, and objects that programmers can use to create software or interact with an external system. 
# API Endpoint: Where the data can be found.
# API Request: From you to the API endpoint. 
# API Response: From API endpoint to you, with the data.

import requests
from datetime import datetime

# Make a request to an endpoint
'''
response = requests.get(url="http://api.open-notify.org/iss-now.json")
'''

# print(response)

#----------- RESPONSE CODES -------------#
'''
1XX - Hold On
2XX - Here you Go
3XX - Go away
4XX - Client screwed up
5XX - Server fault

https://www.webfx.com/web-development/glossary/http-status-codes/
'''

# print(response.status_code) #200

# Confirm the data was pulled correctly from the API endpoint
'''
if response.status_code == 404:
    raise Exception("Page does not exist")
elif response.status_code == 401:
    raise Exception("Not authorized")
'''

#---------- ERRORS and EXCEPTIONS IN THE REQUESTS MODULE -------------#

'''
response.raise_for_status()

#------------ GET HOLD OF THE DATA --------------#
data = response.json()
print(data) # Python dictionary
print(data["iss_position"]) #{'latitude': '-21.5549', 'longitude': '-154.3353'}

latitude = data["iss_position"]["latitude"]
longitude = data["iss_position"]["longitude"]

iss_position = (latitude, longitude)
print(iss_position)
'''


#---------- API PARAMETERS ----------#
# Input that allows you to get specific output.
MY_LAT = -1.292066
MY_LONG = 36.821945

# NOTE: The keys in the dictionary are specified from the API documentation
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json() 
# Get time (12 Hour format)
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
print(sunrise) # 2026-02-05T03:40:36+00:00
print(sunrise.split("T")) #['2026-02-05', '03:40:36+00:00']
print(sunrise.split("T")[1].split(":")) #['03', '40', '36+00', '00']

# To get just the hour values
sunrise_hour = sunrise.split("T")[1].split(":")[0]
sunset_hour = sunset.split("T")[1].split(":")[0]

# Get current time from daytime module
time_now = datetime.now()
# print(time_now)
hour_now = time_now.hour
print(hour_now)
