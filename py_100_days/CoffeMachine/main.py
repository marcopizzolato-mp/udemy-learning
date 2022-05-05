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

# TODO 3: def check amount():

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
    print(f"Money: {session_resources['money']} ml")
    return


# TODO 4: def get_report():


def fill_resources():
    """
    Function that takes no input. It initialises the resources in the machine (water, milk, coffee)
    :return:
    """
    # global resources
    session_resources = RESOURCES.copy()
    session_resources["money"] = 0
    return session_resources


def make_coffee(session_resources, choice):
    """
    :param: dictionary with the resources
    :return: returns the updated resources disctionary after the cofee has been made
    """
    global MENU
    ingredients = MENU[choice]["ingredients"]
    resources_flag = check_resources(session_resources, choice, ingredients)
    if not resources_flag:
        return
    session_resources = deduct_resources(session_resources, choice, ingredients)
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


def get_cash(choice):
    global MENU
    ingredients = MENU[choice]["ingredients"]


def CoffeeMachine():
    # Initiate session resources
    session_resources = fill_resources()
    # Get input from the user
    choice = get_input()

    if choice == "off":
        exit()
    elif choice == "report":
        get_report(session_resources)
    elif choice == "refill":
        fill_resources()
    else:
        session_resources = make_coffee(session_resources, choice)

    print(session_resources)


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    CoffeeMachine("CoffeeMachine!")
