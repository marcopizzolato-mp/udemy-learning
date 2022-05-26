import pytest

from coffee_machine import (
    fill_resources,
    check_resources,
    deduct_resources,
    check_amount,
)

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


def test_fill_resources():
    test_resources = {"water": 300, "milk": 200, "coffee": 100, "money": 0}
    resources = fill_resources()
    assert resources == test_resources


@pytest.mark.parametrize(
    "session_resources,ingredients,result",
    [
        (
            {"water": 250, "milk": 100, "coffee": 24},
            {"water": 250, "milk": 100, "coffee": 24},
            True,
        ),
        (
            {"water": 250, "milk": 100, "coffee": 23},
            {"water": 250, "milk": 100, "coffee": 24},
            False,
        ),
        (
            {"water": 250, "milk": 100, "coffee": 24},
            {"water": 250, "milk": 100, "coffee": 23},
            True,
        ),
    ],
)
def test_check_resources(session_resources, ingredients, result):
    flag = check_resources(session_resources, ingredients)
    assert result == flag


@pytest.mark.parametrize(
    "session_resources,ingredients,result",
    [
        (
            {"water": 250, "milk": 100, "coffee": 24},
            {"water": 250, "milk": 100, "coffee": 24},
            {"water": 0, "milk": 0, "coffee": 0},
        ),
        (
            {"water": 250, "milk": 100, "coffee": 24},
            {"water": 249, "milk": 99, "coffee": 23},
            {"water": 1, "milk": 1, "coffee": 1},
        ),
    ],
)
def test_deduct_resources(session_resources, ingredients, result):
    result_deduct = deduct_resources(session_resources, ingredients)
    assert result == result_deduct


@pytest.mark.parametrize(
    "choice,total_amount,result",
    [
        (1.5, 1, False),
        (1.5, 4, True),
        (1.5, 1.5, True),
    ],
)
def test_check_amount(choice, total_amount, result):
    flag_mount = check_amount(choice, total_amount)
    assert result == flag_mount
