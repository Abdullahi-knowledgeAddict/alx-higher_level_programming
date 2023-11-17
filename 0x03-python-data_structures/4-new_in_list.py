#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """
        Replaces an element in a list at specific position
        without modifying the original list

        Args:
            my_list: The list
            element: The new element
                idx: The index it will be placed
        Return:
                a copy of my_list; modified if idx is valid
    """
    cp_list = [x for x in my_list]
    if (idx >= 0 and idx < len(my_list)):
        cp_list[idx] = element
    return cp_list
