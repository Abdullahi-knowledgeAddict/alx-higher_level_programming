#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """prints integers in a list

        Args:
            my_list: The list

        Return:
                Automatically None
    """
    for numb in my_list:
        print("{:d}".format(numb))
