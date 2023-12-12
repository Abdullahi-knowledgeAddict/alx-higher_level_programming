#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    """Excutes a function safely

    Args:
        fct: The function
        arg: A tuple of argument for the function

    Return: What the function returns or None

    """
    try:
        return fct(*args)
    except Exception as werror:
        print(f"Exception: {werror}", file=stderr)
        return None
