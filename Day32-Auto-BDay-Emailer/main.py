# Extra Hard Starting Project #
# 1. Update the birthdays.csv

# 2. Check if today matches a birthday_info in the birthdays.csv
import datetime as dt
import os
import random
import pandas
import smtplib

my_email = "j2tJyiA3hMqd@gmail.com"
with open("password.txt", mode="r") as password_file:
    password = password_file.read()

today = dt.datetime.now().date()
# print(today.month)
# print(today)

birthdays_dataframe = pandas.read_csv("birthdays.csv")
# print(birthdays_dataframe)
birthdays_dictionary = {}
# birthdays_dict can be {(name, email) : birthday}
for birthday_row in birthdays_dataframe.iterrows():
    # print(birthday_row[1])
    birthday_info = birthday_row[1]
    name = birthday_info["name"]
    email = birthday_info["email"]
    month = birthday_info["month"]
    day = birthday_info["day"]
    year = birthday_info["year"]
    birthday_date = dt.datetime(year=year, month=month, day=day).date()
    # print(birthday_date)
    birthdays_dictionary.update({(name, email): birthday_date})

print(birthdays_dictionary)


def same_date(date1, date2):
    if date1.month == date2.month and date1.day == date2.day:
        print(f"{date1} and {date2} are the same day")
        return True
    return False


for person_info, date in birthdays_dictionary.items():
    print(f"date is {date}")
    name = person_info[0]
    email = person_info[1]
    print(f"Name: {name}\ndate: {date}\nemail: {email}")
    if same_date(date, today):
        print("Found a match")
        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME]
        # with the person's actual name from birthdays.csv
        # print(os.listdir("letter_templates"))
        letter_template = random.choice(os.listdir("letter_templates"))
        with open(f"letter_templates/{letter_template}") as letter:
            # print(letter.read())
            filedata = letter.read().replace("[NAME]", name)
        # print(filedata)
        # 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=email,
                msg=f"Subject:Happy Birthday {name}!!!\n\n{filedata}"
            )
