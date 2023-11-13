#!/usr/bin/python3
def print_last_digit(number: int):
    """prints the last digit of number

    Args:
        number: The number

    Return:
        The last number
    """
    if number < 0:
        number = -number
    number = number % 10
    print(number, end='')
    return number
