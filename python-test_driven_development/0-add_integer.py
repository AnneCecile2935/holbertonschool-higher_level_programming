#!/usr/bin/python3
"""This module provides basic arithmetic functions.
It includes add_integer to add two numbers as integers.
Inputs are validated and exceptions are raised if invalid.
This helps ensure reliable and safe operations.
Documentation meets the project requirements."""


def add_integer(a, b=98):
    """
    Adds two integers or floats and returns their sum as an integer.
    Args:
        a (int or float): The first number.
        b (int or float): The second number, default is 98.
    Raises:
        TypeError: If a or b is not an integer or a float.
    Returns:
        int: The sum of a and b as an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if a != a:
        raise TypeError("a must be a number")
    if b != b:
        raise TypeError("b must be a number")

    if a in [float('inf'), float('-inf')]:
        raise TypeError("a must be a number")
    if b in [float('inf'), float('-inf')]:
        raise TypeError("b must be a number")

    return int(a) + int(b)
