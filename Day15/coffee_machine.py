MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# print(resources.keys())
# print(resources.values())
# print(resources["milk"])
#print(MENU.values())
#print(MENU["latte"])
#print(MENU["latte"].values())
# methods to get the individual values from the MENU dict
#print(MENU["latte"]["ingredients"]["water"])
#print(MENU.get("latte").get("ingredients").get("water"))

# TODO: Prompt user input for a drink choice
def get_user_choice():
    """
    Call to prompt the user for their choice of drink or to exit
    """
    choice = input("What would you like? (espresso/latte/cappuccino) ")
    return choice


choice = get_user_choice()
print(choice)

# TODO: Turn off the coffee machine by entering off

# TODO: Print Report 
def print_report():
    """
    Print the contents of the resources dictionary
    """
    print(resources)
    print(f"Water: {resources.get('water')}")
    print(f"Milk: {resources.get('milk')}")
    print(f"Coffee: {resources.get('coffee')}")

print_report()

# TODO: Check if Sufficent Resources
def sufficent_resources(drink_name):
    """
    Pass the drink choice from get_user_choice and check if 
    resources has enough to make the drink.
    Return True if enough of each resource, False otherwise
    """
    resource_cost = drink_name.get("ingredients")
    resources_available = resources
    #print(f"Drink name passed as {drink_name.get('ingredients')}")
    #print(f"Resources accessed as {resources}")
    print(f"Resource cost: {resource_cost}")
    print(f"Resources available: {resources}")
    # check if the key values in resource cost are smaller than in resources
    if resource_cost.get("water") > resources_available.get("water"):
        print("Not enough water")
        return False
    if resource_cost.get("milk") >= resources_available.get("milk"):
        print("Not enough milk")
        return False
    if resource_cost.get("coffee") >= resources_available.get("coffee"):
        print("Not enough coffee")
        return False
    print("Enough resources")
    return True


print(sufficent_resources(MENU.get("latte")))
    
# TODO: Prompt the use to enter coins, process the coins inserted and return the amount of money inserted
coin_values = {
        "quarter" : 25,
        "dime"    : 10, 
        "nickel"  : 5,
        "penny"  : 1,
}

print(f"dime is {coin_values.get('dime')}")
print(type(coin_values.get("dime")))
def get_coins():
    """
    Get the coin inputs, process them into dollars, and return the dollar amount
    """
    sum = 0
    # Get how many of each coin
    # TODO: Uncomment these out at the end
    #quarters = int(input("How many quarters: "))
    #dimes = int(input("How many quarters: "))
    #nickels = int(input("How many quarters: "))
    #pennies = int(input("How many quarters: "))
    
    quarters = 12
    dimes = 1
    nickles = 1
    pennies = 1

    # Multiply the values of each coin by the amount of each
    #for key in coin_values.values():
    #    print(key)
    sum += (quarters * coin_values.get("quarter"))
    sum += (dimes * coin_values.get("dime"))
    sum += (nickles * coin_values.get("nickel"))
    sum += (pennies * coin_values.get("penny"))



    return sum / 100

print(f"Sum is: {get_coins()}")
# TODO: Check if the user entered enough money and return the change if they did
# Also add the money to the report
def is_enough_money(drink_name):
    """
    From the drink name, get the cost of the drink and see if the user entered enough money to pay for it
    """
    # Get the money the user entered and the cost of the drink
    money = get_coins()
    cost = MENU.get("latte").get("cost")
    print(f"cost is: {cost}")
    # If the cost is higher than the amount of money the user has, return False and tell the user they don't have enough
    if cost > money:
        print("You don't have enough money")
        return False

    # If the user has enough money, add the cost of the drink to the resources dictionary
    resources["money"] = cost
    change = round(money - cost, 2)
    print(f"Your change is {change}")
    return True



print(is_enough_money(MENU.get("latte")))
print(f"resources is now: {resources}")
# TODO: If everything is good, then make the coffee and deduct the ingredients from the resources dictionary


