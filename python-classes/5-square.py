#!/usr/bin/python3
"""
This module defines the Square class.
The Square class manages the size of a square and provides
methods to calculate its area and print the square.
"""


class Square:
    """
    A class to represent a square.

    Attributes:
        __size (int): The size of the square. This attribute is private.

    Methods:
        __init__(size=0): Initializes a new Square instance
        with the given size.
        size(): Retrieves the size of the square (getter).
        size(value): Sets the size of the square with validation (setter).
        area(): Calculates and returns the area of the square.
        my_print(): Prints the square using the character '#'.
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
        self.size = size

    @property
    def size(self):
        """
        Getter for the size attribute.

        Returns:
            int: The current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for the size attribute with validation.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            int: The area of the square, calculated as size^2.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Print the square using the character '#'.
        If the size is 0, it prints an empty line.
        Otherwise, it prints size lines of size '#' characters.
        """
        if self.size == 0:
            print("")
        else:
            for i in (range(self.size)):
                print("#" * self.size)
