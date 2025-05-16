#!/usr/bin/python3
"""This module provides basic arithmetic functions.
It includes add_integer to add two numbers as integers.
Inputs are validated and exceptions are raised if invalid.
This helps ensure reliable and safe operations.
Documentation meets the project requirements."""


def add_integer(a, b=98):
    """
    Args:a (int or float)b (int or float): The second number, default is 98.
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return (a + b)
