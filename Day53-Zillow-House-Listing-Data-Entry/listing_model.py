import requests
from bs4 import BeautifulSoup


class Listing:
    def __init__(self, address, price_per_month, link):
        # the listing has 3 things it needs
        # address, price per month, and link to the property
        self.address = address
        self.price_per_month = price_per_month
        self.link = link

# scrape the website data
def get_house_listings() -> list[Listing]:
    """ Read the Zillow page to get the Address, Price per month, and the property link
    :return: House Listings List
    """
    # Create a list to hold the listings
    listings_list = []
    # first get the page data
    response = requests.get(url="https://appbrewery.github.io/Zillow-Clone/")
    print(response.status_code)
    response.raise_for_status()
    # get the html for the page
    house_listings_page = response.text

    # parse the page's HTML
    soup = BeautifulSoup(house_listings_page, "html.parser")
    # get the listing cards
    listings_result_set = soup.find_all(name="li", class_="ListItem-c11n-8-84-3-StyledListCardWrapper")
    # This is the way to get each part from each listing
    # print(listings[0].find(name="a", class_="StyledPropertyCardDataArea-anchor").get("href"))
    # print(listings[0].find(name="span", class_="PropertyCardWrapper__StyledPriceLine").text)
    # print(" ".join(listings[0].find(name="address").text.split()))

    # get the 3 parts from each listing that we need to store
    for house in listings_result_set:
        listing_link = house.find(name="a", class_="StyledPropertyCardDataArea-anchor").get("href")
        listing_price = house.find(name="span", class_="PropertyCardWrapper__StyledPriceLine").text
        listing_address = " ".join(house.find(name="address").text.split())

        # store each listing in the listings_list
        listings_list.append(Listing(link=listing_link, price_per_month=listing_price, address=listing_address))

    return listings_list
