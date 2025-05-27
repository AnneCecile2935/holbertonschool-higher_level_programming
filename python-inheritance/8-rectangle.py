#!/usr/bin/python3
"""
Module base_geometry

Ce module définit une hiérarchie de classes pour des formes géométriques.

Il contient :
- une classe de base `BaseGeometry`, qui fournit une interface générique
  pour des formes géométriques, incluant une méthode à implémenter (`area`)
  et une méthode utilitaire de validation (`integer_validator`),
- une sous-classe `Rectangle`, représentant un rectangle avec largeur
  et hauteur validées.
"""


class BaseGeometry:
    """
    Classe de base pour des formes géométriques.

    Fournit une interface commune et des méthodes de validation,
    destinée à être héritée par d'autres classes géométriques.
    """

    def area(self):
        """
        Méthode non implémentée, à surcharger dans les sous-classes.

        Raises:
            Exception: Toujours levée pour indiquer que la méthode
            n'est pas encore implémentée.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Valide que `value` est un entier strictement positif.

        Args:
            name (str): Le nom de l'attribut (utilisé dans les messages
            d'erreur).
            value (int): La valeur à valider.

        Raises:
            TypeError: Si value n'est pas un entier.
            ValueError: Si value est inférieur ou égal à 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


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
