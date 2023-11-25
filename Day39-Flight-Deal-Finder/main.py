from data_manager import DataManager
from pprint import pprint
from flight_search import FlightSearch

# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to
# achieve the program requirements.

# Read the sheet and print what the sheet currently has
sheet = DataManager()
# sheet.update_iata_codes()
sheet_data = sheet.read_sheet()
sheet.update_iata_codes()
pprint(sheet_data)

# search = FlightSearch()
# search.get_trip_price("PAR")
