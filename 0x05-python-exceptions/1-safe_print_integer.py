#!/usr/bin/python3
def safe_print_integer(value):

    """Safely prints an integer, Handlin exceptions

        Args:
            value: The value to be printed

        Return:
            True if value has been correctly printed
            else False.
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
