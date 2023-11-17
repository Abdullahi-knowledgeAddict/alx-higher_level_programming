#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """
        Generates new tuple adding together first element, and
        also second element

    Args:
        tuple_a: The first tuple
        tuple_b: The second tuple

    Return:
            A new tupple contain, the addition of first and addition
            of second elements of the two tupples
    """
    tuple_a = tuple_a + (0, 0)
    tuple_b = tuple_b + (0, 0)
    tuple_c = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return tuple_c
