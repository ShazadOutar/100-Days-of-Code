my_dict = {
        "key 1": "Value 1",
        "key 2": "Value 2",
}

my_dict_2 = [
        {
            "key 1": "Value 1"
        },
        {
            "key 2": "Value 2"
        }
]

#if the dictionary is in a list, you can access the elements of it
print(my_dict)
print(my_dict_2[0])
# use .get(key) to get the values at the index you want and the index
print(my_dict_2[0].get("key 1"))
