import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 40.7690837799405  # Your latitude
MY_LONG = -73.96769396344857  # Your longitude
my_email = "j2tJyiA3hMqd@gmail.com"
with open("password.txt", mode="r") as password_file:
    password = password_file.read()


# Your position is within +5 or -5 degrees of the ISS position.
def is_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    # if iss_latitude == MY_LAT and iss_longitude == MY_LONG:
    if abs(iss_latitude - MY_LAT) < 5 and abs(iss_longitude - MY_LONG) < 5:
        return True
    return False


def is_dark():
    # if current time is not between sunrise and sunset return True
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour
    if sunrise < time_now < sunset:
        return False
    return True


def send_email():
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg="Subject: ISS is overhead!\n\nLook up"
        )


# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
while True:
    if is_overhead() and is_dark():
        print("Yes")
        send_email()
    else:
        print("Not yet")
    time.sleep(60)