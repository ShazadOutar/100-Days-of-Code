# from listing_model import Listing
from listing_model import get_house_listings
from form_filler import fill_forms


def main():
    # create an array of the listings, each of type Listing
    listings = get_house_listings()
    for listing in listings:
        print(f"Link: {listing.link}\n Address: {listing.address}\n Price: {listing.price_per_month}\n")
    fill_forms(listings)

if __name__ == "__main__":
    main()
