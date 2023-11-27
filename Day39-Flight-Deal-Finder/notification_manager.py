import os
import smtplib

sending_email = "j2tJyiA3hMqd@gmail.com"
email_password = os.environ["email_password"]
receiving_email = "shazadoutar8@gmail.com"


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    @staticmethod
    def send_email(discounts: list):
        # body = discounts
        # body = ""
        starting_message = "New deal to [city] with a price of [currentPrice]"
        # for deal in discounts:
        #     body.join(deal[""])
        for deal in discounts:
            body = f'New deal to {deal["city"]} for ${deal["currentPrice"]}'
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=sending_email, password=email_password)
                connection.sendmail(
                    from_addr=sending_email,
                    to_addrs=receiving_email,
                    msg=f"Subject:Trip Discount\n\n{body}"
                )

