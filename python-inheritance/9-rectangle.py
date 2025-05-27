#!/usr/bin/python3
"""
Module rectangle

Ce module définit la classe Rectangle qui hérite de BaseGeometry.

La classe Rectangle permet de créer un rectangle défini par sa largeur
et sa hauteur, tous deux des entiers strictement positifs validés via
la méthode integer_validator héritée de BaseGeometry.

La classe implémente également une méthode pour calculer l'aire et
redéfinit la représentation en chaîne pour un affichage personnalisé.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Classe représentant un rectangle.

    Attributs privés:
        __width (int): Largeur du rectangle.
        __height (int): Hauteur du rectangle.

    Hérite de:
        BaseGeometry: pour la validation des entiers.

    Méthodes:
        __init__(self, width, height): Initialise la largeur et la hauteur
            après validation.
        area(self): Retourne l'aire du rectangle.
        __str__(self): Retourne la description formatée du rectangle.
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

    def area(self):
        """
        Calcule et retourne l'aire du rectangle.

        Returns:
            int: Aire calculée (width * height).
        """
        return (self.__width * self.__height)

    def __str__(self):
        """
        Retourne une représentation formatée du rectangle.

        Format:
            [Rectangle] <width>/<height>

        Returns:
            str: Description du rectangle.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
