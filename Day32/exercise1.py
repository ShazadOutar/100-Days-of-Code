# import smtplib
# import socket
# # socket.getaddrinfo('localhost', 8080)
#
#
import random

my_email = "j2tJyiA3hMqd@gmail.com"
receiving_email = "testing_something42@yahoo.com"
#
# # this is different for each email provider, Gmail and Yahoo are different
# # connection = smtplib.SMTP("smtp.gmail.com", port=587)
# # # Secure the connection to the email provider
# # connection.starttls()
# # connection.login(user=my_email,password=password)
# # connection.sendmail(
# #     from_addr=my_email,
# #     to_addrs=receiving_email,
# #     msg="Subject:Hello in the Subject Line\n\nThis is the body of the email")
# # connection.close()
#
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs=receiving_email,
#         msg="Subject:Hello in the Subject Line\n\nThis is the body of the email")

# import datetime as dt
#
# # get the current date and time
# now = dt.datetime.now()
# year = now.year
# month = now.month
# print(now)
# print(year)
#
# b_day = dt.datetime(year=2000, month=4, day=1)
# print(b_day)

# Email a motivational quote from the quotes file on Mondays
import smtplib
import datetime as dt

today = dt.datetime.now().weekday()
Monday = 0
# today = 0
with open("password.txt", mode="r") as password_file:
    password = password_file.read()
print(password)
print(today)
if today == Monday:
    print("Monday")
    with open("quotes.txt", mode="r") as quotes_file:
        # read the quotes file and get a list of the quotes
        quotes = quotes_file.readlines()
    # print(random.choice(quotes))
    quote = random.choice(quotes)
    print(quote)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        # Start the connection
        connection.starttls()
        # log in with the email and app password
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=receiving_email,
            msg=f"Subject:Monday Motivational Quote\n\n{quote}")
