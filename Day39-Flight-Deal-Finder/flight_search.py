import os
import requests
# print(tequila_api_key)
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.search = None

    def get_iata_code(self, city_name):
        end_point = "https://api.tequila.kiwi.com"
        parameters = {
            "term": city_name,
            "locale": "",
            "location_types": "airport",
            "active_only": "true",
            "limit": 10
        }
        headers = {
            "apikey": os.environ["TEQUILA_API_KEY"],
        }
        response = requests.get(url=f"{end_point}/locations/query", headers=headers, params=parameters)
        response.raise_for_status()
        data = response.json()
        print(data)
