import requests
import os

sheety_endpoint = os.environ["sheety_endpoint"]


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = None

    def read_sheet(self):
        response = requests.get(url=sheety_endpoint)
        response.raise_for_status()
        self.destination_data = response.json()["prices"]
        return self.destination_data

    def print_sheet(self):
        print(self.destination_data)


    def update_iata_code(self):
        for city_dict in self.destination_data:
            print(city_dict)
            # price is the key for the dict the put request goes to
            new_data = {
                "price": {
                    "iataCode": ""
                }
            }
            print(f"\nCity Dict is {city_dict}\n new data is {new_data}")
            iataCode = city_dict["iataCode"]
            if iataCode == "":
            # if True:
                row_id = city_dict["id"]
                response = requests.put(
                    url=f"{sheety_endpoint}/{row_id}",
                    json=new_data
                )
                response.raise_for_status()
                print(response.status_code)