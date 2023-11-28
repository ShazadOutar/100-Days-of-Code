# from twilio.rest import Client
import smtplib
import requests
# TWILIO_SID = YOUR TWILIO ACCOUNT SID
# TWILIO_AUTH_TOKEN = YOUR TWILIO AUTH TOKEN
# TWILIO_VIRTUAL_NUMBER = YOUR TWILIO VIRTUAL NUMBER
# TWILIO_VERIFIED_NUMBER = YOUR TWILIO VERIFIED NUMBER

import os

sending_email = "j2tJyiA3hMqd@gmail.com"
email_password = os.environ["email_password"]
receiving_email = "shazadoutar8@gmail.com"


class NotificationManager:
    def __init__(self):
        self.emails = []

    def get_emails(self) -> list:
        sheety_endpoint = os.environ["sheety_user_endpoint"]
        response = requests.get(url=sheety_endpoint)
        response.raise_for_status()
        data = response.json()
        self.emails = data
        return data

    def send_email(self, message):
        # get the emails and store them in self.emails list
        self.get_emails()
        # then use self.emails to email everyone in the list
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=sending_email, password=email_password)
            for email in self.emails:
                connection.sendmail(
                    from_addr=sending_email,
                    to_addrs=email,
                    msg=message.encode("utf-8")
                )

# def __init__(self):
#     self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

# def send_sms(self, message):
#     message = self.client.messages.create(
#         body=message,
#         from_=TWILIO_VIRTUAL_NUMBER,
#         to=TWILIO_VERIFIED_NUMBER,
#     )
#     Prints if successfully sent.
# print(message.sid)
