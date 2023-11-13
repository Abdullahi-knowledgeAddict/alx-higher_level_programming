#!/usr/bin/python3
def remove_char_at(str, n):

    """
        Remove character at the given index of a string.

        Parameters:
        - str: The string
        - n: index of the char to be removed

        Returns:
        The modified string.

        """

    index = 0
    copy_str = str
    str = ''
    for char in copy_str:
        if index != n:
            str += char
        index += 1
    return str
