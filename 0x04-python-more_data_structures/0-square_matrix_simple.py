#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
        Computes the square value for all the integer
        of a square matrix

        Args:
            matrix: A list containing other list

        Return:
                a new matrix of same size
    """
    return [list(map(lambda entry: entry*entry, row)) for row in matrix]
