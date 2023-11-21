#!/usr/bin/python3
def best_score(a_dictionary):
    """
        Search for the key with the biggest integer value

    Args:
        a_dictionary: The dictionary

    Return: The value with the biggest key
            or None if dictionary is empty or None
    """
    if a_dictionary == {} or a_dictionary is None:
        return None
    b_score = 0
    b_person = ""
    for key, value in a_dictionary.items():
        if value > b_score:
            b_score = value
            b_person = key
    return b_person
