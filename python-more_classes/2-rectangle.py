#!/usr/bin/python3
"""
This module defines the Rectangle class.

The Rectangle class represents a geometric rectangle and provides
mechanisms for setting and validating its width and height, as well
as calculating its area and perimeter.
"""


class Rectangle:
    """
    A class to represent a rectangle.

    Attributes:
        width (int): The width of the rectangle (default is 0).
        height (int): The height of the rectangle (default is 0).

    Methods:
        __init__(self, width=0, height=0):
            Initializes a new Rectangle instance with optional width
            and height.

        width(self):
            Retrieves the width of the rectangle.

        width(self, value):
            Sets the width of the rectangle, validating the input.

        height(self):
            Retrieves the height of the rectangle.

        height(self, value):
            Sets the height of the rectangle, validating the input.

        area(self):
            Returns the area of the rectangle.

        perimeter(self):
            Returns the perimeter of the rectangle, or 0 if width
            or height is 0.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance.

        Args:
            width (int): The width of the rectangle. Must be an integer >= 0.
            height (int): The height of the rectangle. Must be an integer >= 0.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter for the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width of the rectangle.

        Args:
            value (int): The width value to set. Must be an integer >= 0.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter for the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height of the rectangle.

        Args:
            value (int): The height value to set. Must be an integer >= 0.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: The area (width * height) of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle, or 0 if width or height is 0.
        """
        if self.width < 0 or self.height < 0:
            perimeter = 0
        return (self.__width + self.height) * 2
