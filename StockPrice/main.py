import requests
from datetime import date
from datetime import timedelta
from config import *
import os

# Get stock prices of the one we're interested in, get closing price over two days and get diff
# Get percentage of the rise


# News message

# Twiligo message
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

def check_stock_status():
    api_key = os.getenv('stock_password')
    today = date.today()
    yesterday = today - timedelta(days=1)
    yesterday = yesterday.strftime('20%y-%m-%d')
    today = today.strftime('20%y-%m-%d')
    response = requests.get(
        url=f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={STOCK}&apikey={api_key}')
    response.raise_for_status()
    data = response.json()
    today_closing_price = float(data['Time Series (Daily)'][today]["4. close"])
    yesterday_closing_price = float(data['Time Series (Daily)'][yesterday]["4. close"])
    pct_change = 100 * ((yesterday_closing_price - today_closing_price) / yesterday_closing_price)
    if pct_change >= 5:
        status_stocks = "Increase"
        print("Get news")
    elif pct_change <= -5:
        status_stocks = "Decrease"
        print("Get news")
    else:
        status_stocks = "Minor changes"
    return status_stocks, pct_change


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
def get_news():
    api_key = os.getenv('news_password')
    response = requests.get(
        url=f'https://newsapi.org/v2/everything?q=tesla&from=2023-02-16&sortBy=popularity&language=en&page=1&pageSize'
            f'=3&apiKey={api_key}')
    response.raise_for_status()
    data = response.json()
    articles = data['articles']
    return data


print(check_stock_status())
print(get_news())

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
