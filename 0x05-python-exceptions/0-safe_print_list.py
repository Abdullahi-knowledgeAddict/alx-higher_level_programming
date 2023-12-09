#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):

    """Safely prints elements of given list till a certain index

        Args:
            my_list: The list of element
                  x: The number of elmnt to be printed from the list

        Return:
            the number of elements printed
    """
    i = 0

    try:
        while (i < x):
            print(my_list[i], end="")
            i += 1
        return i
    except IndexError:
        return i
    finally:
        print()
