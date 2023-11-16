#!/usr/bin/python3

def element_at(my_list, idx):
    """
        Retrieve element at a give index

        Args:
            my_list: The list containing elements
                idx: The index of the element
        Return:
            None, if the index doesn't exist
            else:
                the element retrieved
    """
    if (idx >= 0 and idx < len(my_list)):
        return my_list[idx]
    return
