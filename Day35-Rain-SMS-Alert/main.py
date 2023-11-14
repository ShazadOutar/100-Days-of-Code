import requests
# from twilio.rest import Client
import smtplib

OWM_ENDPOINT = "http://api.openweathermap.org/data/2.5/forecast"

weather_parameters = {
    "lat": -11.092,
    "lon": 170.288,
    "units": "imperial",
    "appid": api_key,
}

response = requests.get(OWM_ENDPOINT, params=weather_parameters)
response.raise_for_status()
print(f"Status code is {response.status_code}")
data = response.json()
print(f"data is:\n{data}\nEnd of data")
# time = data["list"][0]["dt_txt"]
# print(f"time is {time}")
# print(data["list"][0]["main"])
#
# time_2 = data["list"][39]["dt_txt"]
# print(f"time_2 is {time_2}")
# print(data["list"][39]["main"])

# get the hourly forcast of the next 48 hours
two_day_forcast = data["list"][:17]
# print(two_day_forcast)

twelve_hour_forcast = data["list"][:5]
print(twelve_hour_forcast)

will_rain = False

for hour_data in twelve_hour_forcast:
    # print(twelve_hour_forcast[index]["dt_txt"])
    # print(index["dt_txt"])
    print(hour_data["weather"][0]["id"])
    weather_id = hour_data["weather"][0]["id"]
    if weather_id < 800:
        # print("Bring an umbrella.")
        will_rain = True
        break


def send_email(subject, message):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=receiving_email,
            msg=f"Subject: {subject}\n\n{message}"
        )

# send_email()

if will_rain:
    print("Bring an umbrella.")
    send_email(subject="Rain Warning", message="Bring an umbrella today.")
    # client = Client(account_sid, auth_token)
    #
    # message = client.messages \
    #     .create(
    #         body="It's going to rain today, remember to bring an umbrella. ☔",
    #         from_='+18333620565',
    #         to='+13475203321'
    #     )
    #
    # print(message.status)
