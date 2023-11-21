#!/usr/bin/python3
def common_elements(set_1, set_2):
    """
        Gets a set of common element in two sets

    Args:
        set_1: As the name implies
        set_2: Also as the name implies

    Return:
            The intersection of the set
    """
    # Note this can also be done with (set_1 &  set_2)
    return {id_1 for id_1 in set_1 if id_1 in set_2}
