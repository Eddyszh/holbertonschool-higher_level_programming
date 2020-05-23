#!/usr/bin/python3
"""
    Matrix module
    Function:
        matrix_divided: divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    Args:
        matrix: List of list
        div: number to divide
    Raise:
        TypeError, ZeroDivision
    Returns:
        a new matrix
    """
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    elif div is 0:
        raise ZeroDivisionError("division by zero")
    typeEr = "matrix must be a matrix (list of lists) of integers/floats"
    sizeEr = "Each row of the matrix must have the same size"
    if matrix is None or matrix is 0 or matrix[0] is 0:
        raise TypeError(typeEr)
    new = []
    old = len(matrix[0])
    for count, m in enumerate(matrix):
        if not isinstance(m, list):
            raise TypeError(typeEr)
        if len(m) != old:
            raise TypeError(sizeEr)
        old = len(m)
        new.append(m[:])
        for count2, item in enumerate(m):
            if not isinstance(item, (int, float)):
                raise TypeError(typeEr)
            new[count][count2] = round(item / div, 2)
    else:
        return new
