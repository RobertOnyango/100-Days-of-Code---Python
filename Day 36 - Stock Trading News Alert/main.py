# A Python Program that fetches the changes in Stock price in the last two days, compares the values and find a positive percentage change. If % is >= 5%, fetch new related to the Stock price and send an SMS to the user.

import requests
# import datetime as dt
from datetime import date, timedelta
from twilio.rest import Client
import smtplib
    

# Function that calculates the percentage change
def calculatePercentage (yesterday_value, day_before_value):
    # Get the difference, ensure its a positive value using the abs()
    difference = abs(yesterday_value - day_before_value)
    
    # calculate the percentage change
    return (difference / yesterday_value) * 100 


STOCK = "TSLA"
COMPANY_NAME = "tesla"
MY_PHONE_NUMBER = "---"

# API URLs and Keys
ALPHA_ADVANTAGE_API_KEY = "---"
STOCK_PRICE_API = "https://www.alphavantage.co/query"

NEWS_API = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "---"

TWILIO_SID = "---"
TWILIO_AUTH_TOKEN = "---"
TWILIO_VIRTUAL_PHONE_NUMBER = "---"

MY_EMAIL = "---"
PASSWORD = "---"
RECEPIENT_EMAIL = "---"


#----------- PART 1 ---------------#

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# TODO 1: Get the two stock prices

# Parameters for the daily time series as per the API docs
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": ALPHA_ADVANTAGE_API_KEY
}

# Fetch the data
response = requests.get(url=STOCK_PRICE_API, params=stock_parameters)
# Manage exceptions
response.raise_for_status()
# Retrieve the data
stock_data = response.json()

# NOTE: Stock data is two dictionaries:  First dict is the metadata about stock. Second dict has nested dictionaries within it, whereby the key to each dictionary is the date the stock data was captured e.g. # print(stock_data["Time Series (Daily)"]["2026-02-23"]) #{'1. open': '407.2850', '2. high': '407.7000', '3. low': '394.0400', '4. close': '399.8300', '5. volume': '69680026'}

# Data we need
print(stock_data["Time Series (Daily)"]["2026-03-03"]["4. close"])

# NOTE: THIS IS VERY HARDCODED AND WILL RUN INTO AN ERROR IS THE CODE IS RUN ON A MONDAY OR TUESDAY. SEE INSTRUCTOR SOLUTION WHERE LIST COMPREHENSION HAS BEEN USED TO EXTRACT THE DATA FROM THE API.

# TODO 2: Get the dates: today and previous day
today = date.today()
yesterday = today - timedelta(1)

# Get the data for the day before yesterday
day_before_yesterday = yesterday - timedelta(1)
print(stock_data["Time Series (Daily)"][str(day_before_yesterday)]["4. close"])

yesterday_stock_price = stock_data["Time Series (Daily)"][str(yesterday)]["4. close"]
day_before_stock_price = stock_data["Time Series (Daily)"][str(day_before_yesterday)]["4. close"]

# Scnerio where one of the days is a weekend and the stock market is closed meaning we have an empty key 


# TODO 3: Calculate the difference change in percentage
stock_price_change = calculatePercentage(float(yesterday_stock_price), float(day_before_stock_price))

# Variable list that will hold the 3 article obejcts
# new_articles = []

if stock_price_change > 5:
    print("Get News")
    # TODO 4: Get the first three news articles for the company
    news_params = {
       "q": COMPANY_NAME,
       "from": yesterday,
       "sortBy": "publishedAt",
       "apiKey": NEWS_API_KEY
    }

    # Fetch the news articles
    response = requests.get(url=NEWS_API, params=news_params)
    # Manage exceptions
    response.raise_for_status()
    # Retrieve the data
    stock_news = response.json()
    # print(stock_news["articles"][0])

    # Create the twilio client
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    # Create a connection to email server
    connection = smtplib.SMTP("smtp.gmail.com")
    # Start TLS service
    connection.starttls()
    # Login to mail server
    connection.login(user=MY_EMAIL, password=PASSWORD)

    # Pick the first 3 news articles
    for i in range(3):
        # Add the article object to the list
        # new_articles.append(stock_news["articles"][i])

        # TODO 5: Send the message via twilio
        message = client.messages.create(
            messaging_service_sid = 'MGc3a3f59035264e27194b4d7e7eda8203',
            body = f"{STOCK}: {int(stock_price_change)}%\nHeadline: {stock_news['articles'][i]['title']}\nBrief: {stock_news['articles'][i]['description']}\n",
            to = MY_PHONE_NUMBER,
            from_ = TWILIO_VIRTUAL_PHONE_NUMBER,
        )
        print(message.sid)

        '''
        # TODO 6: Send emails
        connection.sendmail(
            from_addr = MY_EMAIL,
            to_addrs = RECEPIENT_EMAIL,
            msg = f"{STOCK}: {int(stock_price_change)}%\nHeadline: {stock_news['articles'][i]['title']}\nBrief: {stock_news['articles'][i]['description']}\n"
        )
        '''
        

    #Close the connection to the mail server
    connection.close()

    print(f"{STOCK}: {int(stock_price_change)}%\nHeadline: {stock_news["articles"][0]["title"]}\nBrief: {stock_news["articles"][0]["description"]}")

else:
    print(f"Stock price change less than 5%: {stock_price_change}")



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

