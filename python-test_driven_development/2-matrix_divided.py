#!/usr/bin/python3
"""
This module provides a function to divide all elements
of a matrix by a given number.
It includes the matrix_divided function that validates the matrix and divisor,
performs the division, and returns a new matrix with the results
rounded to 2 decimal places.
No external modules are used.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor.

    Args:
        matrix (list of lists): A matrix of integers or floats.
        div (int or float): The divisor.

    Returns:
        list of lists: A new matrix with each element divided by div,
        rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats.
        TypeError: If each row of the matrix is not of the same size.
        TypeError: If div is not a number (int or float).
        ZeroDivisionError: If div is zero.
    """
    if matrix == []:
        return []

    if not isinstance(matrix, list) or not all(
        isinstance(row, list) for row in matrix
    ):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
            )

    for row in matrix:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) \
                    of integers/floats"
                )

    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
    if not all(isinstance(element, (int, float)) for element in row):
        raise TypeError(
            "matrix must be a matrix (list of lists) \
            of integers/floats"
            )
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(element / div, 2) for element in row] for row in matrix]
