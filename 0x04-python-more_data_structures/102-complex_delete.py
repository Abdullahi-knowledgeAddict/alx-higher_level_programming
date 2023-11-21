#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """
        Deletes all occurence of a value in a list
    Args:
        a_dictionary: The dictionary
               value: The value to be deleted

    Return:
         The modified list:
    """
    copy_dictionary = a_dictionary.copy()
    for key, val in copy_dictionary.items():
        if val == value:
            del a_dictionary[key]
    return a_dictionary
