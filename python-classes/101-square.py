#!/usr/bin/python3
"""
This module defines the Square class.
The Square class manages the size and position of a square and provides
methods to calculate its area and print the square using the character '#'.
"""


class Square:
    """
    A class to represent a square.

    Attributes:
        __size (int): The size of the square. Must be a positive integer.
        __position (tuple): The position of the square represented as a tuple
        of two positive integers.

    Methods:
        __init__(size=0, position=(0, 0)): Initializes a new Square instance
        with the given size and position.
        size(): Retrieves the size of the square (getter).
        size(value): Sets the size of the square with validation (setter).
        position(): Retrieves the position of the square (getter).
        position(value): Sets the position of the square with validation
        (setter).
        area(): Calculates and returns the area of the square.
        my_print(): Prints the square using the character '#'.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square instance with the given size and position.

        Args:
            size (int): The size of the square. Default is 0.
            position (tuple): The position of the square as a tuple of
            two positive integers. Default is (0, 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
            TypeError: If position is not a tuple of two positive integers.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        elif size < 0:
            raise ValueError("size must be >= 0")
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Getter for the position attribute.

        Returns:
            tuple: The current position of the square as a tuple of
            two positive integers.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter for the position attribute with validation.

        Args:
            value (tuple): The new position of the square as a tuple
            of two positive integers.

        Raises:
            TypeError: If value is not a tuple of two positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
        The position is used to offset the square using spaces.
        """
        if self.size == 0:
            print()
            return
        for i in range(self.position[1]):
            print()

        for i in (range(self.size)):
            print(" " * self.position[0] + "#" * self.size)
