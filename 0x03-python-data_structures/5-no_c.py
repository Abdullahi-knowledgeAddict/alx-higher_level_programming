#!/usr/bin/python3
def no_c(my_string):
    """
        Generate a new_string from my_string
        removing 'C' and 'c' from the string if present

        Args:
            my_string: The original string

        Return:
            new_string
    """
    new_string = ""
    for c in my_string:
        if c not in 'Cc':
            new_string += c
    return new_string
