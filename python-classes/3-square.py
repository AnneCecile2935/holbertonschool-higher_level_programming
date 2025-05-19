#!/usr/bin/python3
"""
This module defines the Square class.
The Square class has a private instance attribute: size,
and provides a method to calculate the area of the square.
"""


class Square:
    """
    A class to represent a square.

    Attributes:
        __size (int): The size of the square. This attribute is private.

    Methods:
        __init__(size=0): Initializes a new Square instance
        with the given size.
        area(): Calculates and returns the area of the square.
    """
    def __init__(self, size=0):
        """
        Initializes a new Square instance with the given size.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size
