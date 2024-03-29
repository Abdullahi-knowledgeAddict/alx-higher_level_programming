#!/usr/bin/python3

""" A Simple module containing a simple function that says my_name
"""


def say_my_name(first_name, last_name=""):
    """ A function that says "My name is <first name> <last name>"

    Args:
        first_name: As implied
        last_name:  As Implied

    """

    # Checking user input
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    elif type(last_name) != str:
        raise TypeError("last_name must be a string")
    elif first_name == "":
        raise ValueError("first_name can't be an empty string")

    # Since user input passed
    print(f"My name is {first_name} {last_name}")
