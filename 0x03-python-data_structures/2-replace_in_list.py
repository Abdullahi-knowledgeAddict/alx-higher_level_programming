#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """
        Replace element at a give index

        Args:
            my_list: The list containing elements
            element: The new element
                idx: The index of the element
        Return:
            Original list, if the index doesn't exist
            else:
                The original list
    """
    if (idx >= 0 and idx < len(my_list)):
        my_list[idx] = element
    return my_list
