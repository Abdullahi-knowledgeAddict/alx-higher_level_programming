#!/usr/bin/python3

""" A simple module containing that prints a square
"""


def print_square(size):
    """prints a square using '#'s for every given unit

    Args:
        size: The length or Breadth of the square

    """

    # checking input
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    # Printing The Square
    copy = size
    while size > 0:
        print('#' * copy)
        size -= 1
