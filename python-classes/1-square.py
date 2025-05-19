#!/usr/bin/python3
"""
This module defines the Square class.
The Square class has a private instance attribute: size.
"""


class Square:
    """
    A class to represent a square.

    Attributes:
        __size (int): The size of the square. This attribute is private.
    """
    def __init__(self, size):
        """
        Initializes a new Square instance with the given size.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
