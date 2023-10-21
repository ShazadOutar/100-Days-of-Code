# # add each line of data to a list called data
# with open("weather_data.csv") as weather_file:
#     data = weather_file.readlines()
# print(data)

# we could do this above but python has built-in support for csv data
# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     # print(data)
#     # how to get the data from the reader
#     # for row in data:
#     #     print(row)
#     # get the temperatures from data
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             # print(row[1])
#             temperatures.append(int(row[1]))
#     print(temperatures)

# even easier using the pandas library
import pandas
data = pandas.read_csv("weather_data.csv")
print(data)
print(type(data["temp"]))

# pandas allows easy conversions to other data types
data_dict = data.to_dict()
print(data_dict)

# conversions with dataframes and series
temp_list = data["temp"].to_list()
print(temp_list)

print(type(data["temp"]))

# find the average temp from the temp_list
average = sum(temp_list) / len(temp_list)
print(average)

# pandas has functions to handle some calculations
print(f"Average is: {data['temp'].mean()}")
print(f"Highest temp is: {data['temp'].max()}")

# different ways to get data in columns
print(data["condition"])
print(data.condition)

# get data for a row
print(data[data.day == "Monday"])
# filter the row printed by finding based on a condition
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)
# print(type(monday.temp))
print(monday.temp[0])