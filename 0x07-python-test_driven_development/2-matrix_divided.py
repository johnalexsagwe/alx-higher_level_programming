#!/usr/bin/python3
"""
Module matrix_divided
Divides each element of a matrix of numbers by a number
Returns a new matrix
"""


def matrix_divided(matrix, div):
    """
    Returns new matrix with dividends
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list or len(matrix) == 0 or len(matrix[0]) == 0:
        raise TypeError(msg)

    new_matrix = []
    samelen = len(matrix[0])
    for lists in matrix:
        if type(lists) is not list:
            raise TypeError(msg)
        if len(lists) != samelen:
            raise TypeError("Each row of the matrix must have the same size")
        newlist = []
        for i in lists:
            if not isinstance(i, (int, float)):
                raise TypeError(msg)
            newlist.append(round(i/div, 2))
        new_matrix.append(newlist)
    return new_matrix
