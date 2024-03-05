import smtplib
import os

EMAIL = os.environ["EMAIL"]
PASSWORD = os.environ["PASSWORD"]
PERSONAL_EMAIL = os.environ["PERSONAL_EMAIL"]


def send_email(name, email, phone_number, message):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=PERSONAL_EMAIL,
            msg=f"Subject:Blog Contact Email\n\n"
                f"{message}\n"
                f"From: \n{name}, {email}, {phone_number}"
        )


# send_email()
