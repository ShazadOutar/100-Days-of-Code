from data_manager import DataManager


class FlightData:
    #This class is responsible for structuring the flight data.
    def find_discounted(self) -> dict:
        # read the sheet to find the discounts
        # return the dict of all the flights with a cheaper price
        sheet = DataManager().read_sheet()
        # print(sheet)
        for row in sheet:
            # print(row)
            current_price = row["currentPrice"]
            lowest_price = row["lowestPrice"]
            if current_price < lowest_price:
                print(f"Discount found for {row['city']}")



        return {}