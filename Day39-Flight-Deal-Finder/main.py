from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from flight_data import FlightData

# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to
# achieve the program requirements.

# # Read the sheet and print what the sheet currently has
# sheet = DataManager()
# # sheet.update_iata_codes()
# sheet_data = sheet.read_sheet()
# sheet.update_iata_codes()
# pprint(sheet_data)

# search = FlightSearch()
# search.get_trip_price("PAR")

def main():
    # Read the sheet and print what the sheet currently has
    # sheet = DataManager()
    # sheet_data = sheet.read_sheet()
    # sheet.update_iata_codes()
    # pprint(sheet_data)
    # email = NotificationManager()
    # email.send_email()
    # search for discounts first, update new ones

    # read the sheet data
    # sheet_data = DataManager().read_sheet()
    discounts = FlightData().find_discounted()
    print(discounts)
    # pass the discounts list to the notification manager

    # email discount info
    NotificationManager.send_email(discounts)




if __name__ == "__main__":
    main()
