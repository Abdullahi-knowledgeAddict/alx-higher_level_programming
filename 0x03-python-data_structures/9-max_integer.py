#!/usr/bin/python3
def max_integer(my_list=[]):
    """
        Evaluate a list for the biggest integer

        Args:
            my_list: The list to be evaluated

        Returns:
                The biggest integer in the list or None if list
                is zero in size, None.
    """

    if not my_list:
        return None
    biggest = my_list[0]
    for element in my_list:
        if element > biggest:
            biggest = element
    return biggest
