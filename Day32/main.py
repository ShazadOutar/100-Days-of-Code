import smtplib
import socket
# socket.getaddrinfo('localhost', 8080)


my_email = "j2tJyiA3hMqd@gmail.com"
# password = "+8Wr9FhRmsN"
password = "aptobeejheobmmwd"
receiving_email = "testing_something42@yahoo.com"

# this is different for each email provider, Gmail and Yahoo are different
# connection = smtplib.SMTP("smtp.gmail.com", port=587)
# # Secure the connection to the email provider
# connection.starttls()
# connection.login(user=my_email,password=password)
# connection.sendmail(
#     from_addr=my_email,
#     to_addrs=receiving_email,
#     msg="Subject:Hello in the Subject Line\n\nThis is the body of the email")
# connection.close()

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=receiving_email,
        msg="Subject:Hello in the Subject Line\n\nThis is the body of the email")
