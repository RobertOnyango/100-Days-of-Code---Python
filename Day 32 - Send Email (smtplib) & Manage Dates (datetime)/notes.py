import smtplib

# Assign your email address to a variable
my_email = "xxxxxxxxxxxxxxxxxxxx"
password = "xxxxxxxxxxxxxxxxxxxx" #Ensure you enable 'APP Password' from your mail account to get this password generated
recepient_email = "xxxxxxxxxxxxxxxxxxxx"

'''
# Create a new object that is a connection to your email provider. Need to specify the location of provider's server e.g. smtp.live.com->hotmail, smtp.mail.yahoo.com->Yahoo
connection = smtplib.SMTP("smtp.gmail.com") 
# Start Transport Layer Security to ensure communciation between client and server is encrypted
connection.starttls()
# Login by providing credentials
connection.login(user=my_email, password=password)
# Send email, from your address to sender address
connection.sendmail(from_addr=my_email, to_addrs=recepient_email, msg="Subject:Hello \n\n This is the body of the email")
# Close the connection
connection.close()
'''

'''
# Above code without having to close the connection. Let python do it automatically using with()
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email, 
        to_addrs=recepient_email, 
        msg="Subject:Hello \n\n This is the body of the email")
'''


import datetime as dt

# Tap into the datetime class, its method now() to get the current time of the datetime object
now = dt.datetime.now()
print(type(now))
# Tap into the attributes of the method
print(now.year) # 2026
print(now.microsecond)
print(now.weekday()) # 1 (which is Tuesday)


# Create a custom datetime object
date_of_birth = dt.datetime(year=1995, month=1, day=28)
print(date_of_birth) #1995-01-28 00:00:00

date_of_birth2 = dt.datetime(year=1990, month=12, day=28, hour=6)
print(date_of_birth2) #1990-12-28 06:00:00


    

