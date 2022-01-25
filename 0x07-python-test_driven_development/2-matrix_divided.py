#!/usr/bin/python3
"""
    Module 2-matrix_divided
    All elements of the matrix should be divided by div,
     rounded to 2 decimal places
    Returns a new matrix
    You are not allowed to import any module
"""


def matrix_divided(matrix, div):
    """
        matrix_divided
        Matrix must be a list of lists of integers
        or floats, otherwise raise a TypeError
        exception with the message matrix must be
        a matrix (list of lists) of integers/floats
        Each row of the matrix must be of the same size,
    """
    Error = "matrix must be a matrix (list of lists) of integers/floats"

    if isinstance(matrix, list) is not True:
        raise TypeError(Error)
    for i in range(len(matrix)):
        if type(matrix[i]) is not list:
            raise TypeError(Error)
        for j in range(len(matrix[i])):
            if isinstance((matrix[i][j]), (float, int)) is not True:
                raise TypeError(Error)

    for sub_list in matrix:
        if len(matrix[0]) != len(sub_list):
            raise TypeError("Each row of the matrix must have the same size")

    if isinstance(div, (int, float)) is not True:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    new_matriz = []

    for i in range(len(matrix)):
        tmp = []
        for j in range(len(matrix[i])):
            tmp.append(round(matrix[i][j] / div, 2))
        new_matriz.append(tmp)
    return new_matriz
