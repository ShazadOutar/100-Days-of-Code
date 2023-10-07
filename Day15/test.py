# TODO: Clean this up later

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
profit = 0

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
    choice = input("What would you like? (espresso/latte/cappuccino) ").lower()
    return choice


#choice = get_user_choice()
#print(choice)

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
    print(f"Money is: ${profit}")

#print_report()

# TODO: Check if Sufficent Resources
def sufficent_resources(drink_name):
    """
    Pass the drink choice from get_user_choice and check if 
    resources has enough to make the drink.
    Return True if enough of each resource, False otherwise
    """
    resource_cost = drink_name.get("ingredients")
    resources_available = resources
    print(f"Drink value is: {drink_name}")
    #print(f"Drink name passed as {drink_name.get('ingredients')}")
    #print(f"Resources accessed as {resources}")
    print(f"Resource cost: {resource_cost}")
    print(f"Resources available: {resources}")
    # check if the key values in resource cost are smaller than in resources
    if resource_cost.get("water") > resources_available.get("water"):
        print("Not enough water")
        return False

    if resource_cost.get("milk") > resources_available.get("milk"):
        print("Not enough milk")
        return False
    if resource_cost.get("coffee") > resources_available.get("coffee"):
        print("Not enough coffee")
        return False
    print("Enough resources")
    return True


#print(sufficent_resources(MENU.get("latte")))
    
# TODO: Prompt the use to enter coins, process the coins inserted and return the amount of money inserted
coin_values = {
        "quarter" : 25,
        "dime"    : 10, 
        "nickel"  : 5,
        "penny"  : 1,
}

#print(f"dime is {coin_values.get('dime')}")
#print(type(coin_values.get("dime")))
def get_coins():
    """
    Get the coin inputs, process them into dollars, and return the dollar amount
    """
    sum = 0
    # Get how many of each coin
    # TODO: Uncomment these out at the end
    quarters = int(input("How many quarters: "))
    dimes = int(input("How many dimes: "))
    nickels = int(input("How many nickels: "))
    pennies = int(input("How many pennies: "))
    
    # quarters = 12
    # dimes = 1
    # nickles = 1
    # pennies = 1

    # Multiply the values of each coin by the amount of each
    #for key in coin_values.values():
    #    print(key)
    sum += (quarters * coin_values.get("quarter"))
    sum += (dimes * coin_values.get("dime"))
    sum += (nickels * coin_values.get("nickel"))
    sum += (pennies * coin_values.get("penny"))

    return sum / 100

#print(f"Sum is: {get_coins()}")
# TODO: Check if the user entered enough money and return the change if they did
# Also add the money to the report
def is_enough_money(drink_name):
    """
    From the drink name, get the cost of the drink and see if the user entered enough money to pay for it
    Return True if they did, return False otherwise.
    """
    # Get the money the user entered and the cost of the drink
    money = get_coins()
    print(f"Drink name is {drink_name}")
    print(f"Drink cost is {drink_name.get('cost')}")
    cost = drink_name.get('cost')
    #cost = MENU.get("latte").get("cost")
    print(f"Drink cost is {drink_name.get('cost')}")
    # If the cost is higher than the amount of money the user has, return False and tell the user they don't have enough
    if cost > money:
        print("You don't have enough money")
        return False

    # If the user has enough money, add the cost of the drink to the resources dictionary
    #resources["money"] += cost
    profit += cost
    change = round(money - cost, 2)
    print(f"Your change is {change}")
    return True

def enough_money(input_money, drink_cost):
    """ Return true if input is greater than the drink cost"""
    print(f"input_money is :{input_money}")
    print(f"drink_cost is :{drink_cost}")
    if input_money >= drink_cost:
        global profit
        profit += drink_cost
        change = round(input_money - drink_cost, 2)
        print(f"Here is your change: ${change}")
        return True
    else: 
        print("Sorry that's not enough money")
        return False



#print(is_enough_money(MENU.get("latte")))
#print(f"resources is now: {resources}")

# TODO: If everything is good, then make the drink and deduct the ingredients from the resources dictionary
def make_drink(drink_name):
    """
    Assuming there is enough of the resources and the customer put in enough money.
    This function deducts the ingredients from the resources dictionary
    """
    # first store the needed amounts of each ingredient
    needed_water = drink_name.get("ingredients").get("water")
    needed_milk = drink_name.get("ingredients").get("milk")
    needed_coffee = drink_name.get("ingredients").get("coffee")
    
    # next deduct them from the values in resources
    resources["water"] -= needed_water
    resources["milk"] -= needed_milk
    resources["coffee"] -= needed_coffee
    return 

def make_coffee(drink_name, order_ingredients):
    print(f"drink name is {drink_name}")
    print((f"order ingredients is {order_ingredients}"))
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}!")
#print("Resources before making drink is\n")
#print_report()
#print(make_drink(MENU.get("latte")))
#print("Resources after making drink is\n")
#print_report()

# all the subfuntions have been completed, now they will be organized into a coffeemachine function to call
def coffee_machine():
    # First get the users drink choice
    choice = get_user_choice()
    print(choice)
    # handle the special inputs
    if choice == "off":
        print("choice was off")
        return
    if choice == "report":
        print_report()

    # user enters their coins
    user_money = get_coins()

    # Find the drink in the dictionary of drinks
    if choice not in MENU.keys():
        print("Not a valid menu option")
        return

    choice = MENU.get(choice)

    # Check that they put in enough money and there's enough resources
    if is_enough_money(choice) and sufficent_resources(choice):
        make_drink(choice)

    coffee_machine()
    return

def is_resource_sufficent(drink_ingredients):
    print("In is resource sufficent")
    for item in drink_ingredients:
        if drink_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


is_on = True
while is_on:
    choice = get_user_choice()
    if choice == "off":
        is_on = False
    elif choice ==  "report":
        print_report()
    else:
        drink = MENU[choice]
        print(drink)
        print(is_resource_sufficent(drink["ingredients"]))
        if is_resource_sufficent(drink["ingredients"]):
            payment = get_coins()
            #print(enough_money(payment, drink["cost"]))
            if enough_money(input_money=payment, drink_cost=drink["cost"]):
                make_coffee(choice, drink["ingredients"])

