#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """Prints integers in a list upto index X

    Args:
        my_list: The list
              x: The index to stop (Excluding it)
    Return:
        The number of reall integers printed
    """
    i = 0
    y = 0
    int_count = 0

    while (i < x):
        try:
            print("{:d}".format(my_list[i]), end="")
        except (TypeError, ValueError):
            pass
        else:
            int_count += 1
        i += 1
    print()
    return int_count
