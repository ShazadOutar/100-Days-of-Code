from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
my_coffee_maker = CoffeeMaker()
my_menu = Menu()
process_money = MoneyMachine()
# print("Latte info is")
# print(my_menu.find_drink("latte").ingredients)
# print(my_menu.find_drink("latte").cost)

# my_item = MenuItem(
#     name="latte",
#     water=my_menu.find_drink("latte").ingredients["water"],
#     milk=my_menu.find_drink("latte").ingredients["milk"],
#     coffee=my_menu.find_drink("latte").ingredients["coffee"],
#     cost=my_menu.find_drink("latte").cost
# )
# print(my_item.ingredients)
# print(my_item.cost)
while is_on:
    # Get the users drink choice
    choice = input(f"What would you like? ({my_menu.get_items()})? ").lower()
    if choice == "off":
        # turn off the machine
        print("Machine off")
        is_on = False
    elif choice == "report":
        # print the report
        my_coffee_maker.report()
    else:
        # if not off or report, assume it's a drink
        # check resources sufficent
        #print(f"Choice is {choice}")
        menu_choice = my_menu.find_drink(choice)
        # check that it's a valid menu option
        if menu_choice: # check if it doesn't return none
            # check if resources sufficient
            # print(menu_choice)
            # print(menu_choice.ingredients)
            milk_cost = menu_choice.ingredients["milk"]
            water_cost = menu_choice.ingredients["water"]
            coffee_cost = menu_choice.ingredients["coffee"]
            # print(menu_choice.cost)
            money_cost = menu_choice.cost
            # for key in menu_choice.ingredients:
            #     print(key)
            # for value in menu_choice.ingredients.values():
            #     print(value)
            my_item = MenuItem(name=choice, water=water_cost, milk=milk_cost, coffee=coffee_cost, cost=money_cost)
            # check if there are sufficient resources
            if my_coffee_maker.is_resource_sufficient(my_item):
                # if there are enough resources, start processing the input money
                # if true then the payment was accepted
                if process_money.make_payment(money_cost):
                    # after payment is accepted make the coffee
                    my_coffee_maker.make_coffee(my_item)