import requests
from bs4 import BeautifulSoup
import smtplib
import os

my_email = "j2tJyiA3hMqd@gmail.com"
password = os.environ["email_password"]
personal_email = os.environ["personal_email"]

headers = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/119.0.0.0 Safari/537.36"
}

# get the html for the site search
response = requests.get(url="https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1",
                        headers=headers)
response.raise_for_status()
search_results = response.text

# Parse the html data
site_html = BeautifulSoup(search_results, "html.parser")
# print(site_html)
# find where the price is in the html
price_span = site_html.find(name="span", class_="a-price aok-align-center reinventPricePriceToPayMargin priceToPay")
print(price_span)
price_value = (float(price_span.find(name="span", class_="a-price-whole").text) +
               float(price_span.find(name="span", class_="a-price-fraction").text) / 100)
print(price_value)


# send the email alert
def send_email(price):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=personal_email,
            msg=f"Subject: Amazon Price Drop\n\nPrice dropped below 100 down to ${price}!"
        )


if price_value < 100:
# if True:
    send_email(price_value)
