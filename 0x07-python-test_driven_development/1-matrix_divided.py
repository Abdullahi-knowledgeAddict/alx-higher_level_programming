#!/usr/bin/python3

""" A simple module containing a function that divides a matrix
"""


def matrix_divided(matrix, div):
    """Divides a given matrix

    Args:
        matrix: The matrix to be divided (A list of lists with constant length)
        div: The divider for the whole list

    Returns:
        A new list of which is the result of the division of the original list
        else:
            an exception indicating a specific error Indicated

    """

    if div is None or type(div) not in [int, float]:
        raise TypeError('div must be a number')

    elif div == 0:
        raise ZeroDivisionError('division by zero')
    if None in matrix:
        raise TypeError('matrix must be a matrix (list of lists) of ' +
                        'integers/floats')

    length = len(matrix[0])
    new_matrix = []

    for row in matrix:
        if length != len(row):
            raise TypeError('Each row of the matrix must have the same size')
        new_row = []
        # The loop to generate new row
        for column in row:
            if type(column) not in [int, float]:
                raise TypeError('matrix must be a matrix (list of lists) of ' +
                                'integers/floats')
            new_row.append(round(column/div, 2))
        # Now adding the new row to the new matrix
        new_matrix.append(new_row)

    return new_matrix
