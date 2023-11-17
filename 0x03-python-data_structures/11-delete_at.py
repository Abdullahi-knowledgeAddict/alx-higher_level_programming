#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """
        Deletes an item at a specific position in list

        Args:
            my_list: The list
                idx: The index which 0 by default
        Return:
            The modified list, or the original if not modifiable
    """
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    my_list[:] = my_list[:idx] + my_list[idx + 1:]
    return my_list
