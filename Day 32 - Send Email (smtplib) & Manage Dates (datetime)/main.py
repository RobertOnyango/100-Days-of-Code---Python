##################### Extra Hard Starting Project ######################
# A Python Program that sends a birthday email to someone (see birthday.csv) when the date is their birthday
# Host on Cloud so that the code runs autumatically: PythonAnywhere
import pandas
import datetime as dt
import random
import smtplib

# Assign your email address to a variable
MY_EMAIL = "xxxxxxxxxxxxxxxxxxxx"
PASSWORD = "xxxxxxxxxxxxxxxxxxxx" 

#  Function that sends emails. Accepts the receipent address and email content
def send_mail(receipient, content):
    global MY_EMAIL, PASSWORD
    #Create a connection
    connection = smtplib.SMTP("smtp.gmail.com")
    # Start TLS
    connection.starttls()
    # Login to mail server
    connection.login(user=MY_EMAIL, password=PASSWORD)
    #Send teh email
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=receipient,
        msg=f"Subject:Happy Birthday\n\n {content}"
    )
    #Close the connection after sending email
    connection.close()

#----------------------------------------------------------------------------#
# 1. Update the birthdays.csv and retrieve the data
'''
data = pandas.read_csv("birthdays.csv")
print(data.year)
robs = data[data.name == "Robs"]
print(robs)
print(robs.month)

# Iterate over the data to extract the year, date
for (index, row) in data.iterrows():
    # Extract the year and date to a dictionary where the key is a tuple of (year, day) and value the entire row of data
    birthdays_dict[(row.year, row.day)] = row
'''

# Read the csv file
data = pandas.read_csv("birthdays.csv")

# Dictionary that will hold the birthdays
birthdays_dict = {}

# Iterate over the data to extract the date, month as the key
# {new_key:new_value for item in list}
birthdays_dict={(row.month, row.day) : row for (index, row) in data.iterrows()}
# print(birthdays_dict)



#---------------------------------------------------------------------------#
# TODO 2: Check if today matches a birthday in the birthdays.csv
# Get the date today
now = dt.datetime.now()
# Create a tuple of today
today = (now.month, now.day)
# print(today)

# Iterate through the birthdays dictionary and confirm if the tuples match
for key in birthdays_dict:
    # if birthday is today
    if key == today:
        print(f"It's your birthday, {birthdays_dict[key]["name"]}!")
        # Get the name and email from the list
        receipient_name = birthdays_dict[key]["name"]
        receipient_email = birthdays_dict[key]["email"]

        # TODO 3: Pick a random letter from the templates
        # Pick a random number 1,3
        number = random.randint(1,3)
        # Pick a radom letter to open based on the random number
        with open(f"letter_templates/letter_{number}.txt") as letter:
            # Read the letter
            template_email = letter.read()

            # TODO 4: Replace the [name] placeholder with the name of the receipient from the dictionary value 
            birthday_email = template_email.replace("[NAME]", receipient_name).replace("Angela", "Robert")
 
            # TODO 5: Send the email
            send_mail(receipient=receipient_email, content=birthday_email)
    else:
        pass





