def is_leap(year):
  leap_year = True
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        #print("Leap year.")
        leap_year = True
      else:
        #print("Not leap year.")
        leap_year = False
    else:
      #print("Leap year.")
      leap_year = True
  else:
    #print("Not leap year.")
    leap_year = False
  return leap_year

def days_in_month(year, month):
    month -= 1
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
    #first check if its a leap year
    if is_leap(year):
        #if it's leap year and the month is feb
        #print(f"It's a leap in month: {month}")
        if month == 1:
            #print("feb in leap")
            return month_days[month] + 1
    #if not a leap year in feb, then return the month from the list
    #print("Not leap or not feb")
    return month_days[month]        

  
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
