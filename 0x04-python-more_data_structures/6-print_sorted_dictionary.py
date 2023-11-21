#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """
    Prints dictionary by ordered keys

    Args:
        a_dictionary: The dictionary

    Return:
            None Automatically
    """
    for entry in sorted(a_dictionary):
        print(entry, ": ", a_dictionary[entry], sep='')
