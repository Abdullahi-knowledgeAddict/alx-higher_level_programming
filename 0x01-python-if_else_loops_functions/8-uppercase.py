#!/usr/bin/python3
def uppercase(str: str):
    """prints all elements str in uppercase

    Args:
        str: The str
    Returns:
        Nothing
    """
    for c in str:
        c = ord(c)
        if c >= 97 and c <= 122:
            c = c - 32
        print("{:c}".format(c), end='')
    print("{}".format(""))
