#!/usr/bin/python3
"""
This  a function that divides all elements of a matrix.
It takes two parameters: matrix and div, which are the numbers to be added.
Then returns the values
"""


def matrix_divided(matrix, div):
    """This is a function that returns the addition of 2 variables
    matrix (list of lists): the matrix
    div (int) or (float: the divisor number"""
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list):  # to check if matrix is a list
        raise TypeError(msg)

    for row in matrix:
        if not isinstance(row, list):
            # to check if matrix is a list of lists
            raise TypeError(msg)
        for cols in row:
            # to check if the elements are integers or floats
            if not isinstance(cols, int) and not isinstance(cols, float):
                raise TypeError(msg)

    row_len = {len(row) for row in matrix}
    if len(row_len) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return list(map(lambda row: list(map(lambda x:
                round(x / div, 2), row)), matrix))
