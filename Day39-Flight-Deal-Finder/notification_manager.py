import smtplib



class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def send_email(self):
        body = "body"
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=sending_email, password=email_password)
            connection.sendmail(
                from_addr=sending_email,
                to_addrs=receiving_email,
                msg=f"Subject:Trip Discount\n\n{body}"
            )
