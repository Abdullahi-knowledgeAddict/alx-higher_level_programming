#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
        Adds all element uniquely in a list(only once for each integer)

    Args:
        my_list: The list

    Return: The Sum
    """
    total = 0
    for x in set(my_list):
        total += x
    return total
