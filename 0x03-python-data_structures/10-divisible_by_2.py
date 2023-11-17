#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """
        Finds all multiple of 2 in a list.

        Args:
            my_list: The list

        Return:
                A new list with True or False depending on whether the
                integer at the same position in the original list is a
                multiple of 2
    """
    result_list = []
    for elem in my_list:
        if elem % 2 == 0:
            result_list.append(True)
        else:
            result_list.append(False)
    return result_list
