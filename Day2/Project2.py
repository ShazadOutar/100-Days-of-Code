
print("Welcome to the tip calculator")

#Get the required info from the user
total_bill = float(input("What was the total bill? $"))
people_count = int(input("How many people to split the bill? "))
percent = int(input("What percentage tip would you like to give? 10, 12 or 15? "))

#Find the total bill with the tip
tip_amount = total_bill * (percent / 100.0)
total_bill += tip_amount

#split the total bill by the amount of people
per_person = round(total_bill / people_count, 2)
#this line formats the output better so it always has both decimal places filled
per_person_formatted = "{:.2f}".format(per_person)
print(f"Each person should pay: ${per_person_formatted}")



