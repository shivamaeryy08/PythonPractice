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
    pct_change_ = 100 * ((yesterday_closing_price - today_closing_price) / yesterday_closing_price)
    if pct_change_ >= 5:
        status_stocks_ = "Increase"
        report_news_ = True
    elif pct_change_ <= -5:
        status_stocks_ = "Decrease"
        report_news_ = True
    else:
        status_stocks_ = "Minor changes"
        report_news_ = False
    return status_stocks_, pct_change_, report_news_


def get_news():
    api_key = os.getenv('news_password')
    response = requests.get(
        url=f'https://newsapi.org/v2/everything?q=tesla&from=2023-02-16&sortBy=popularity&language=en&page=1&pageSize'
            f'=3&apiKey={api_key}')
    response.raise_for_status()
    data = response.json()
    articles_ = data['articles']
    return articles_


def send_message(pct_change_, articles_, report_news_, status_stocks_):
    news_to_display = ""
    for article in articles_:
        news_to_display += f"Title: {article['title']}\nDescription: {article['description']}\n" \
                           f"Published: {article['publishedAt'].split('T')[0]}\n\n\n"
    if report_news_:
        if status_stocks_ == 'Increase':
            print(f'{STOCK} ⬆️ {pct_change_}%\n\n'
                  f'{news_to_display}')
        elif status_stocks_ == 'Decrease':
            print(f'{STOCK} ⬇️ {pct_change_}%\n\n'
                  f'{news_to_display}')
    else:
        print(f'{STOCK} 🤷‍♂️ No Major Change {pct_change_}%')


status_stocks, pct_change, report_news = check_stock_status()
articles = get_news()
send_message(pct_change, articles, report_news, status_stocks)
