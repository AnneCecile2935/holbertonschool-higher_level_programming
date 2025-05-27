#!/usr/bin/python3
'''Module for Rectangle class.'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Classe représentant un rectangle.

    Hérite de BaseGeometry et valide la largeur et la hauteur
    à l’aide de la méthode integer_validator.

    Attributes:
        __width (int): Largeur du rectangle (privé).
        __height (int): Hauteur du rectangle (privé).
    """

    def __init__(self, width, height):
        """
        Initialise un rectangle avec une largeur et une hauteur données.

        Args:
            width (int): La largeur du rectangle.
            height (int): La hauteur du rectangle.

        Raises:
            TypeError: Si width ou height ne sont pas des entiers.
            ValueError: Si width ou height sont inférieurs ou égaux à 0.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
