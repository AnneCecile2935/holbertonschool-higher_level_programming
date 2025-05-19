#!/usr/bin/python3
"""
This module defines the Square class.
The Square class manages the size of a square and provides
methods to calculate its area.
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

    def __eq__(self, other):
        """Check if two squares are equal in area."""
        if isinstance(other, Square):
            return self.area() == other.area()
        return Notimplemented

    def __ne__(self, other):
        """Check if two squares are not equal in area."""
        if isinstance(other, Square):
            return self.area() != other.area()
        return Notimplemented

    def __lt__(self, other):
        """Check if this square is smaller than another in area."""
        if isinstance(other, Square):
            return self.area() < other.area()
        return Notimplemented

    def __le__(self, other):
        """Check if this square is smaller than or equal to another
        in area.
        """
        if isinstance(other, Square):
            return self.area() <= other.area()
        return Notimplemented

    def __gt__(self, other):
        """Check if this square is greater than another in area."""
        if isinstance(other, Square):
            return self.area() > other.area()
        return Notimplemented

    def __ge__(self, other):
        """Check if this square is greater than or equal to another
        in area.
        """
        if isinstance(other, Square):
            return self.area() >= other.area()
        return Notimplemented
