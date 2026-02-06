import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "___YOUR_EMAIL_HERE____"
MY_PASSWORD = "___YOUR_PASSWORD_HERE___"
MY_LAT = -1.292066 # Your latitude
MY_LONG = 36.821945 # Your longitude


# Function that gets the current latitude and longitude position of the iss_satellite, and finds its proximity uses to my current latitude and longitude positions. Returns true if both are (-5 <= x <= +5)
def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the iss position.
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True


# Function that takes the current time (only the hour) and figures out if it is night time in my current loaction
def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    # Here we only pick the hour value of the projected sunrise and sunset times of my location
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    # Pick the hour value for now()
    time_now = datetime.now().hour

    # Find out if its dark using the time now and sunrise, sunset times
    if time_now >= sunset or time_now <= sunrise:
        return True

# Loop that will always run since it is always true
while True:
    # Run the code succeeding the time.sleep() every 60 seconds
    time.sleep(60)
    # Confirm if iss_is_overhead and it is_night.
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("__YOUR_SMTP_ADDRESS_HERE___")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look Up👆\n\nThe ISS is above you in the sky."
        )


