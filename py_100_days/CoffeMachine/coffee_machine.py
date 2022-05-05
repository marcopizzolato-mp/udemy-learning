# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


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
    },
}

RESOURCES = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# TODO 1: def get_input():
def get_input():
    # correct_choice = False
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    available_choices = MENU.keys()
    if choice in available_choices:
        # correct_choice = True
        return choice
    elif choice in ["report", "off", "refill"]:
        return choice
    else:
        get_input()


# TODO 2: def insert_coin():
def get_cash():
    coin_types = {"quarter": 0.25, "dimes": 0.1, "nickel": 0.05, "pennies": 0.01}
    total_amount = 0
    for coin in coin_types:
        amount = int(input(f"Please insert the number of {coin} in the machine: "))
        total_amount = total_amount + (amount * coin_types[coin])
    return total_amount


# TODO 3: def check amount():
def check_amount(choice_cost, total_amount):
    if choice_cost > total_amount:
        print(f"I'm sorry, the total amount inserted {total_amount} is not enough")
        print(f"Here is your change of: {total_amount}")
        return False
    elif choice_cost < total_amount:
        print(f"Your change is of: {total_amount - choice_cost}")
        return True
    else:
        return True


# TODO 4: def get_report():
def get_report(session_resources):
    """
    Function that prints the report
    :param session_resources: dictionary with the resources for that specific session
    :return: no return, print statements with the amount of ingredients
    """
    # Assumption: resources remain the same (water/milk/coffee)
    print(f"Water: {session_resources['water']} ml")
    print(f"Milk: {session_resources['milk']} ml")
    print(f"Coffee: {session_resources['coffee']} ml")
    print(f"Money: {session_resources['money']} dollars")
    return


# TODO 4: def fill_resources():
def fill_resources():
    """
    Function that takes no input. It initialises the resources in the machine (water, milk, coffee)
    :return:
    """
    # global resources
    session_resources = RESOURCES.copy()
    session_resources["money"] = 0
    return session_resources


def check_resources(session_resources, ingredients):
    for kk in ingredients:
        if ingredients[kk] > session_resources[kk]:
            print(f"Sorry there is not enough {kk}.")
            return False
    return True


def deduct_resources(session_resources, ingredients):
    # Deduct resources
    for kk in ingredients:
        session_resources[kk] = session_resources[kk] - ingredients[kk]
    return session_resources


def add_amount(session_resources, total_amount):
    session_resources["money"] = session_resources["money"] + total_amount
    return session_resources


def make_coffee(session_resources, choice):
    """
    :param: dictionary with the resources
    :return: returns the updated resources' dictionary after the coffee has been made
    """
    global MENU
    ingredients = MENU[choice]["ingredients"]
    choice_cost = MENU[choice]["cost"]
    resources_flag = check_resources(session_resources, ingredients)
    if not resources_flag:
        return False
    total_amount = get_cash()
    amount_flag = check_amount(choice_cost, total_amount)
    if not amount_flag:
        return True
    session_resources = add_amount(session_resources, choice_cost)
    session_resources = deduct_resources(session_resources, ingredients)
    print(session_resources)
    return True


def coffee_machine():
    # Initiate session resources
    session_resources = fill_resources()
    keep_coffee = True
    while keep_coffee:
        # Get input from the user
        choice = get_input()
        # Do different things depending on choices
        if choice == "off":
            keep_coffee = False
        elif choice == "report":
            get_report(session_resources)
        elif choice == "refill":
            fill_resources()
        else:
            keep_coffee = make_coffee(session_resources, choice)


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    coffee_machine()
