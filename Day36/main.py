import requests
import os
from twilio.rest import Client

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"


STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = "S1CPB2P725FMPRN1"

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "5f6aff126d2e410d9d507b63dba1a541"
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}
news_parameters = {
    "q": STOCK_NAME,
    "apiKey": NEWS_API_KEY,
    "sortBy": "popularity"
}


# TODO 1. - Get yesterday's closing stock price.

stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
stock_response.raise_for_status()
stock_data = stock_response.json()
stock_time_series = stock_data["Time Series (Daily)"]
stock_data = [value for(key, value) in stock_time_series.items()]
yesterday_closing_stock_price = float(stock_data[0]["4. close"])

# TODO 2. - Get the day before yesterday's closing stock price

before_yesterday_closing_stock_price = float(stock_data[1]["4. close"])

# TODO 3. - Find the positive difference between 1 and 2.


price_difference = yesterday_closing_stock_price - before_yesterday_closing_stock_price
abs_price_difference = abs(price_difference)
# TODO 4. - Work out the percentage difference
percentage_difference = round((abs_price_difference / before_yesterday_closing_stock_price) * 100)
if price_difference < 0:
    up_down = "🔻"
elif price_difference > 0:
    up_down = "🔺"
# TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if percentage_difference > 0:
    # TODO 6. - Instead of printing ("Get News"),
    #  use the News API to get articles related to the COMPANY_NAME.
    # TODO 7. - Use Python slice operator to create a list that contains the first 3 articles.
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
    news_response.raise_for_status()
    news_data = news_response.json()
    articles = news_data["articles"][:3]

# TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
    articles_list = {(article["title"], article["description"]) for article in articles}

# TODO 9. - Send each article as a separate message via Twilio.
    for article in articles_list:
        client = Client(account_sid, auth_token)

        message = client.messages \
            .create(
                body=f"{COMPANY_NAME}: {up_down}{percentage_difference}%\n"
                     f"Headline: {article[0]}\n"
                     f"Brief: {article[1]}\n",
                from_='+15034064177',
                to='+254707371677'
            )

        print(message.sid)
