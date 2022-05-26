from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#
# menu_object = Menu()
# menu_item_object = MenuItem()
# money_mcn_object = MoneyMachine()
# coffee_mkr_object = CoffeeMaker()


def test1():
    pass


def test2():
    pass


def get_input(menu_obj):
    # correct_choice = False
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    available_choices = menu_obj.get_items()
    if choice in available_choices or choice in ["report", "off", "refill"]:
        return choice
    else:
        print("The choice is not correct, please insert a new one")
        get_input()


def main_process():
    keep_coffee = True
    # Initialise the Menu
    menu_object = Menu()
    coffee_mkr_object = CoffeeMaker()
    money_mcn_object = MoneyMachine()
    while keep_coffee:
        # Get input from the user
        choice = get_input(menu_object)
        drink = menu_object.find_drink(choice)
        # Do different things depending on choices
        if choice == "off":
            keep_coffee = False
        elif choice == "report":
            coffee_mkr_object.report()
        elif choice == "refill":
            coffee_mkr_object = CoffeeMaker()
        else:
            if coffee_mkr_object.is_resource_sufficient(drink):
                cost = drink.cost
                if money_mcn_object.make_payment(cost):
                    coffee_mkr_object.make_coffee(drink)


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    main_process()


# 1) Prompt what would you like to have
# - check from MENu OO
# 2) if "off" exit
# 3) print report
#     coffee_mkr.report()
# 4) Check if resources are suffficient
# coffee_mkr.is_resource_sufficient(drink)
#
# 5) process coins
#
# 6) Make coffee
# coffee_mkr.make_coffee()
