#!/usr/bin/python3
"""
Module 4-print_square
Defines a function `print_square(size)` that prints a square
using the `#` character.

The function takes an integer `size` as its parameter. If `size
is not an integer
or if it is less than 0, appropriate exceptions will be raised.

Example:
    >>> print_square(3)
    ###
    ###
    ###
"""


def print_square(size):
    """
    Prints a square with the character '#'.

    Args:
        size (int): The size of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
