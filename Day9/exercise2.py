travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(country_name, number_of_visits, cities):
    #append the new dict to the list of the travel log
    travel_log.append({
        #go key by key
        "country"   : country_name,
        "visits"    : number_of_visits,
        "cities"    : cities
        })
    #could've also made an empty dict and then filled it before adding it
    new_country = {}
    new_country["country"] = country_name
    #travel_log.append(new_country)



#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

