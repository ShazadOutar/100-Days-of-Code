import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census.csv")
# print(data["Primary Fur Color"])
# print(data["Hectare Squirrel Number"])
primary_fur_color_data = data["Primary Fur Color"]
squirrel_number_data = data["Hectare Squirrel Number"]
# print(type(data))
squirrel_data = pandas.DataFrame({})
# print(squirrel_data)
# print(type(squirrel_data))
# squirrel_data.insert(0, "Fur Color", primary_fur_color_data)
# squirrel_data.insert(1, "Squirrel Number", squirrel_number_data)
# print(squirrel_data)
# count the number of each color type and build the dataframe from that
print(type(primary_fur_color_data))
print(primary_fur_color_data.count())
# print(data["Primary Fur Color"].value_counts()["Gray"])
grey_squirrels = data["Primary Fur Color"].value_counts()["Gray"]
red_squirrels = data["Primary Fur Color"].value_counts()["Cinnamon"]
black_squirrels = data["Primary Fur Color"].value_counts()["Black"]
# squirrel_data.loc[-1] = grey_squirrels
# print(squirrel_data)