my_dict = {
        "Key 1": "Value 1",
}

programming_dictionary = {
        "Bug": "An error in a program that prevents the program from running as expected.", 
        "Function": "A piece of code that you can easily call over and over again.",
}
#getting values out of the dictionary
#print(programming_dictionary["Bug"])

#adding pairs to the dictionary
programming_dictionary["New Key"] = "Some new value text"

print(programming_dictionary)

#starting with a empty dict to fill
empty_dict = {}
empty_dict["Key 1"] = "Value 1 details"
print(empty_dict)

#empty a dictionary by doing dict = {}
empty_dict = {}
print(empty_dict)

#to edit values of a dict
programming_dictionary["Bug"] = "Literal bug in your computer"
print(programming_dictionary)

#looping iterates on the key values
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

#nesting dicts in a dict
travel_log = {
        "France": {"cities_visited": ["Paris", "Lille", "Dijon"]},
        "Germany": ["Berlin", "Hamburg"]
}
print(travel_log)

#nesting dictionary in a list
travel_log = [
        {
            "country": "France",
            "cities_visited": ["Paris", "Lille", "Dijon"],
            "total_visits": 12
        },
        {
            "country": "Germany",
            "cities_visited": ["Berlin", "Hamburg"],
            "total_visits": 17
        },
]
print(travel_log)
