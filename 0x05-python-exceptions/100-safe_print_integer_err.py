#!/usr/bin/python3
from sys import stderr


def safe_print_integer_err(value):
    """
        prints integer but reporst on stderr on failure

        Args:
            value: the parameter to be printed

        Return:
            True on Success, False on Failure
    """
    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        print("Exception:", e, file=stderr)
        return False
