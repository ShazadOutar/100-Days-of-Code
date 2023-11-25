import os
import requests
from datetime import datetime, timedelta

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        # self.search = None
        self.headers = {
            "apikey": os.environ["TEQUILA_API_KEY"],
        }

    def get_iata_code(self, city_name):
        """
        Input the name of a city and return the iata code of that city
        :param city_name:
        :return iata_code:
        """
        end_point = "https://api.tequila.kiwi.com"
        parameters = {
            "term": city_name,
            "locale": "en-US",
            "location_types": "airport",
            "active_only": "true",
            "limit": 10
        }
        # headers = {
        #     "apikey": os.environ["TEQUILA_API_KEY"],
        # }
        response = requests.get(url=f"{end_point}/locations/query", headers=self.headers, params=parameters)
        response.raise_for_status()
        data = response.json()
        iata_code = data["locations"][0]["city"]["code"]
        print(iata_code)
        return iata_code

    def get_trip_price(self, destination_iata_code):
        """
        Enter a cities iata code and return the price of  trip from NYC to there
        :param destination_iata_code:
        :return price as a float:
        """
        search_endpoint = "https://api.tequila.kiwi.com/v2/search"
        print(datetime.today().strftime("%d/%m/%Y"))
        today = datetime.today().date()
        # print(f"Today is {today.strftime('%d/%m/%Y')}")
        # Use timedelta to increase the date instead of manually replacing it
        # use
        tomorrow = (today + timedelta(1)).strftime("%d/%m/%Y")
        print(f"Tomorrow is {tomorrow}")
        six_months_away = (today + timedelta(6 * 30)).strftime("%d/%m/%Y")
        print(six_months_away)
        query = {
            "fly_from": "NYC",
            "fly_to": destination_iata_code,
            "date_from": tomorrow,
            "date_to": six_months_away,
            "return_from": six_months_away,
            "return_to": six_months_away,
            "partner_market": "us",
            "limit": 500,
            "curr": "usd",
        }
        response = requests.get(url=search_endpoint, headers=self.headers, params=query)
        response.raise_for_status()
        print(f"Status code of {response.status_code} for city {destination_iata_code}")
        data = response.json()
        price = data["data"][0]["price"]
        # print(price)
        return float(price)