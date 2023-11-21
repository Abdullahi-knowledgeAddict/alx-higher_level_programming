#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """
        generate a set of elements only present in one set

        Args:
            set_1: Implies the name
            set_2: Implies the name

        Return:
                A new set containing the elements present
                in either set not both
    """
    # This could be done using nested two loop and the add() method
    return set_1 ^ set_2
