#!/usr/bin/python3
def safe_print_division(a, b):
    """Divides and prints the result of 2 ints safely

    Args:
        a: dividend
        b: divisor

    Return:
            quotient or None
    """
    try:
        quotient = a / b
    except (ZeroDivisionError, TypeError, ValueError):
        quotient = None
    finally:
        print("Inside result: {}".format(quotient))
        return quotient
