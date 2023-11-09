##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday_info in the birthdays.csv
import datetime as dt

today = dt.datetime.now().date()
# print(today.month)
print(today)

import pandas

birthdays_dataframe = pandas.read_csv("birthdays.csv")
print(birthdays_dataframe)
birthdays_dictionary = {}
# birthdays_dict can be {[name, email] : birthday}
for birthday_row in birthdays_dataframe.iterrows():
    # print(birthday_row[1])
    birthday_info = birthday_row[1]
    name = birthday_info["name"]
    email = birthday_info["email"]
    month = birthday_info["month"]
    day = birthday_info["day"]
    year = birthday_info["year"]
    birthday_date = dt.datetime(year=year, month=month, day=day).date()
    print(birthday_date)
    birthdays_dictionary.update({name: birthday_date})

print(birthdays_dictionary)


def same_date(date1, date2):
    if date1.month == date2.month and date1.day == date2.day:
        print(f"{date1} and {date2} are the same day")
        return True
    return False


# print(birthdays_dictionary["John"])
# same_date(today, birthdays_dictionary["John"])
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
if same_date(today, )
# 4. Send the letter generated in step 3 to that person's email address.
