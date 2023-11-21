#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """
        Creates a new dictionary from a_dictionary
        but values are multiplied by two

    Args:
        a_dictionary: The original dictionary

    Return:
            The new dictionary
    """
    return {key: value*2 for key, value in a_dictionary.items()}
