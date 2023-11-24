from data_manager import DataManager
from pprint import pprint
from flight_search import FlightSearch

# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to
# achieve the program requirements.

# Read the sheet and print what the sheet currently has
# sheet = DataManager()
# sheet.read_sheet()
# pprint(sheet.destination_data)
# sheet_data = sheet.destination_data
# sheet.update_iata_code()
# pprint(sheet.destination_data)

flight_search = FlightSearch()
flight_search.get_iata_code("Paris")