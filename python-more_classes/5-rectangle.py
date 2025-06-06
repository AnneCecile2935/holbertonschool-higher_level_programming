#!/usr/bin/python3
"""
This module defines the Rectangle class.

The Rectangle class represents a geometric rectangle and provides
mechanisms for setting and validating its width and height, as well
as calculating its area and perimeter. It also defines how the
rectangle is represented as a string and includes cleanup behavior
upon object deletion.
"""


class Rectangle:
    """"
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

        __str__(self):
            Returns a printable string made of '#' characters
            representing the rectangle.

        __repr__(self):
            Returns an unambiguous string representation of the
            rectangle that can be used to recreate the object.

        __del__(self):
            Prints a message when the rectangle instance is deleted.
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

    def __str__(self):
        """
        Returns a string representation of the rectangle using the
        '#' character.

        If either the width or the height is 0, returns an empty string.

        Returns:
        str: A string made of lines of '#' characters representing
        the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

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
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __repr__(self):
        """
        Return an official string representation of the Rectangle object.

        The returned string is formatted as 'Rectangle(width, height)' and is
        intended to be unambiguous. This representation can be used to
        recreate the object using eval(), assuming the Rectangle class
        is in scope.

        Returns:
        str: A string that represents the Rectangle object.
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Called when the Rectangle instance is about to be destroyed.

        Prints a farewell message to indicate that the object is being deleted.
        """
        print("Bye rectangle...")
