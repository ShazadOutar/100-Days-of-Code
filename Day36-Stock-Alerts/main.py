import smtplib

import requests
import json
import os
from datetime import datetime

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
# alphavantage_api_key = ""
# news_api_key = ""
SENDING_EMAIL = "j2tJyiA3hMqd@gmail.com"
# SENDING_EMAIL_PASSWORD = ""
# PERSONAL_EMAIL = ""
alphavantage_api_key = os.environ["alphavantage_api_key"]
news_api_key = os.environ["news_api_key"]
SENDING_EMAIL_PASSWORD = os.environ["SENDING_EMAIL_PASSWORD"]
PERSONAL_EMAIL = os.environ["PERSONAL_EMAIL"]


# def get_passwords():
#     with open("passwords.txt", "r") as file:
#         global alphavantage_api_key, news_api_key, SENDING_EMAIL_PASSWORD, PERSONAL_EMAIL
#         data = file.readlines()
        # alphavantage_api_key = data[0]
        # news_api_key = data[1]
        # SENDING_EMAIL_PASSWORD = data[2]
        # PERSONAL_EMAIL = data[3]
        # alphavantage_api_key = os.environ["alphavantage_api_key"]
        # news_api_key = os.environ["news_api_key"]
        # SENDING_EMAIL_PASSWORD = os.environ["SENDING_EMAIL_PASSWORD"]
        # PERSONAL_EMAIL = os.environ["PERSONAL_EMAIL"]
        # print(f"API keys are alphavantage = {alphavantage_api_key}\n"
        #       f"news api key = {news_api_key}\n")


def get_stock_data(stock_name: str):
    parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": stock_name,
        "outputsize": "compact",
        "apikey": alphavantage_api_key
    }
    # make the api call to alphavantage
    response = requests.get(url="https://www.alphavantage.co/query", params=parameters)
    response.raise_for_status()
    data = response.json()
    # print(f"data is {data}\n")
    return data


def get_stock_data_r(stock_name):
    # temp function while I can't make any more api calls
    with open("data.json") as json_file:
        data = json.load(json_file)
    # print(data)
    return data


def percent_change(value_1: float, value_2: float) -> float:
    top = abs(value_1 - value_2)
    bottom = (value_1 + value_2) / 2
    result = top * 100 / bottom
    print(result)
    return result


def get_previous_days() -> tuple[str, str]:
    # get the string of yesterday but check if it's a weekend
    today = datetime.date(datetime.now())
    today = today.replace(day=14)
    print(f"Today is {today} of type {type(today)}")
    # if today.isoweekday() == 2:
    # if today is tuesday then can get yesterday fine but need to change the previous day to Friday instead
    # yesterday = today.replace(day=today.day-1)
    if today.isoweekday() == 1:
        # if today is monday, then yesterday needs to be friday
        yesterday = today.replace(day=today.day - 3)
        previous_day = today.replace(day=today.day - 4)
    elif today.isoweekday() == 2:
        # if today is Tuesday, then previous day needs to be Friday and yesterday to Monday
        previous_day = today.replace(day=today.day - 4)
        yesterday = today.replace(day=today.day - 1)
    else:
        yesterday = today.replace(day=today.day - 1)
        previous_day = today.replace(day=today.day - 2)
    print(f"Yesterday is {yesterday}")
    print(f"Previous day is {previous_day}")
    yesterday_str = yesterday.__str__()
    previous_day_str = previous_day.__str__()
    return yesterday_str, previous_day_str


# TODO: STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
def get_news(company_name) -> list:
    today = datetime.date(datetime.now()).__str__()
    parameters = {
        "q": company_name,
        "from": today,
        "sortBy": "popularity",
        "apiKey": "f2ee3e7a67b64eddb584afd333449f04"
        # "apiKey": news_api_key.rstrip("%0A")
    }
    print(f"Today {today} {type(today)}")
    print(f"Api key is {news_api_key} {type(news_api_key)}")
    response = requests.get(url="https://newsapi.org/v2/everything", params=parameters)
    response.raise_for_status()
    data = response.json()
    # articles = data["articles"]
    # TODO: Make this  try and catch for if there's less than 3 articles that return
    articles = [article for article in data["articles"][:3]]
    print(data)
    print(articles)
    return articles


# TODO: STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.
def send_message(subject, body):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=SENDING_EMAIL, password=SENDING_EMAIL_PASSWORD)
        connection.sendmail(
            from_addr=SENDING_EMAIL,
            to_addrs=PERSONAL_EMAIL,
            msg=f"Subject:{subject}\n\n{body}"
        )


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file
 by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the 
 coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file
 by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the 
 coronavirus market crash.
"""


def main():
    # get_passwords()
    # data = get_stock_data(STOCK)
    # print(data)
    # TODO: STEP 1: Use https://www.alphavantage.co
    # # When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
    # print(data["Time Series (Daily)"])
    # current_date = datetime.date(datetime.now())
    # yesterday = current_date.replace(day=current_date.day - 1)
    # two_days_ago = current_date.replace(day=current_date.day - 2)
    # yesterday_str = str(yesterday)
    # two_days_ago_str = str(two_days_ago)
    # print(f"yesterday is {yesterday} and yesterday_str is {yesterday_str}")
    # print(f"current_date-1 is {two_days_ago} and current_date-1_str is {two_days_ago_str}")
    # print(data["Time Series (Daily)"])
    # # compare the closing prices of yesterday and the previous day
    # yesterday_close_value = float(data["Time Series (Daily)"]["2023-11-13"]["4. close"])
    # two_days_ago_close_value = float(data["Time Series (Daily)"]["2023-11-10"]["4. close"])
    # print(f"{yesterday_close_value}, {two_days_ago_close_value}")
    # print(f"{yesterday_str}, {data['Time Series (Daily)'][yesterday_str]}")
    # print(f'{two_days_ago_str}, {data["Time Series (Daily)"]["2023-11-10"]}')

    # print(get_previous_days())
    # get_passwords()
    data = get_stock_data(STOCK)
    print(data)
    print(data["Time Series (Daily)"])

    previous_days = get_previous_days()

    yesterday_close_value = float(data["Time Series (Daily)"][previous_days[0]]["4. close"])
    # print(data["Time Series (Daily)"][previous_days[0]]["4. close"])
    print(yesterday_close_value)

    previous_day_close_value = float(data["Time Series (Daily)"][previous_days[1]]["4. close"])
    print(previous_day_close_value)
    # percent_change(yesterday_close_value, previous_day_close_value)
    # percent_change(previous_day_close_value, yesterday_close_value)
    percent_change_value = percent_change(yesterday_close_value, previous_day_close_value)
    percent_change_value = 5
    if percent_change_value >= 5:
        # if the percent difference is over 5% do the next part
        print("get news")
        top_three_articles = get_news(COMPANY_NAME)
        # article_title = top_three_articles[0]["title"]
        # article_description = top_three_articles[0]["description"]
        # body = f"{article_title}\n{article_description}"
        # send_message(subject=f"{STOCK}: {percent_change_value}", body=body)
        for count in range(3):
            article_title = top_three_articles[count]["title"]
            article_description = top_three_articles[count]["description"]
            body = "".join((article_title, article_description)).encode("utf-8").strip()
            send_message(subject=f"{STOCK}: {percent_change_value}", body=body)
    else:
        print(f"Change was only: {percent_change_value}")
    # get_news(COMPANY_NAME)
    # send_message(subject="Hello", body="From Day 36")

# def main():
#     print("Hello")
    # data = get_stock_data(STOCK)
    # print(data)

if __name__ == "__main__":
    main()
