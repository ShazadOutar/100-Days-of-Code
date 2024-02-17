from bs4 import BeautifulSoup
import requests
from listing_model import Listing

link = "https://docs.google.com/forms/d/e/1FAIpQLSfUw8vjdoyNsxhbt3JwSDSltWxNlxew6J4jVhF3djWIlwHTmQ/viewform?usp=sf_link"


# scrape the website data
def get_house_listings() -> list[Listing]:
    """ Read the Zillow page to get the Address, Price per month, and the property link
    :return: House Listings List
    """
    listings_list = []
    # first get the page data
    response = requests.get(url="https://appbrewery.github.io/Zillow-Clone/")
    print(response.status_code)
    response.raise_for_status()
    house_listings_page = response.text

    soup = BeautifulSoup(house_listings_page, "html.parser")
    listings_result_set = soup.find_all(name="li", class_="ListItem-c11n-8-84-3-StyledListCardWrapper")
    # This is the way to get each part from each listing
    # print(listings[0].find(name="a", class_="StyledPropertyCardDataArea-anchor").get("href"))
    # print(listings[0].find(name="span", class_="PropertyCardWrapper__StyledPriceLine").text)
    # print(" ".join(listings[0].find(name="address").text.split()))

    for house in listings_result_set:
        listing_link = house.find(name="a", class_="StyledPropertyCardDataArea-anchor").get("href")
        listing_price = house.find(name="span", class_="PropertyCardWrapper__StyledPriceLine").text
        listing_address = " ".join(house.find(name="address").text.split())

        # store each listing
        listings_list.append(Listing(link=listing_link, price_per_month=listing_price, address=listing_address))

    return listings_list


listings = get_house_listings()
for listing in listings:
    print(f"Link: {listing.link}\n Address: {listing.address}\n Price: {listing.price_per_month}\n")
