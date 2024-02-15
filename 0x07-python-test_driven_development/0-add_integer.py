#!/usr/bin/python3

""" A module containing basic function definitions

"""


def add_integer(a, b=98):
    """ A function that adds two numbers together
    which both are either integers or floats


    Args:
        a: must be an integer or float
        b: must be an integer or float

    Return:
        The algebraic summation  of both numbers
        else: an error is raised, if any of the given arguments
        is not an integer or float
    """

    if type(a) not in [int, float]:
        raise TypeError('a must be an integer')
    if type(b) not in [int, float]:
        raise TypeError('b must be an integer')

    return a+b
