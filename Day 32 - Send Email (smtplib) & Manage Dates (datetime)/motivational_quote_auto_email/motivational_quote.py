# An application that emails you motivational quotes depending on the day of the week
import datetime as dt
import random
import smtplib

# Assign your email address to a variable
MY_EMAIL = "xxxxxxxxxxxxxxxxxxxx"
PASSWORD = "xxxxxxxxxxxxxxxxxxxx" 
RECEPIENT_EMAIL = "xxxxxxxxxxxxxxxxxxxx"

# Get the date today
now = dt.datetime.now()
weekday = now.weekday()
# Confirm today is Thursday
if weekday == 3:
    #Opeen the file
    with open("quotes.txt") as quote_file:
        # Read each line and store as list
        all_quotes = quote_file.readlines()
        # Pick a random line
        quote = random.choice(all_quotes)
    
    # Create a connection
    connection = smtplib.SMTP("smtp.gmail.com")
    # Start TLS
    connection.starttls()
    # Login to mail server
    connection.login(user=MY_EMAIL, password=PASSWORD)
    # Send the email
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=RECEPIENT_EMAIL,
        msg=f"Subject:Thursday Motivation \n\n {quote}"
    )
    #Close the connection
    connection.close()

