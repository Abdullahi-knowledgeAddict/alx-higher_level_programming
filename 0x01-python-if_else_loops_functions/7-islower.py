#!/usr/bin/python3
def islower(c: str):
    """Checks if given parameter is lower case

    Args:
        c: the char
    Returns:
        True or False
    """
    c = ord(c)
    if c >= 97 and c <= 122:
        return True
    return False
