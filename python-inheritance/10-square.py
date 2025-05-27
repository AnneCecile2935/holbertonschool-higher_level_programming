#!/usr/bin/python3

"""
Module square

Ce module définit la classe Square, qui hérite de Rectangle.

La classe Square représente un carré, une forme géométrique particulière
où la largeur et la hauteur sont égales. Elle hérite de la classe Rectangle
et utilise l’héritage pour valider et stocker sa dimension unique :
la taille (`size`).

Fonctionnalités :
- Validation de la taille à l’aide de integer_validator
(héritée de BaseGeometry)
- Calcul de l’aire du carré
- Représentation lisible via __str__
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Classe représentant un carré, héritant de Rectangle.

    Attributs privés :
        __size (int): Taille du côté du carré (strictement positif).

    Méthodes :
        __init__(self, size): Initialise un carré avec une taille donnée.
        area(self): Retourne l'aire du carré.
        __str__(self): Retourne une description formatée du carré.
    """
    def __init__(self, size):
        """
        Initialise un carré avec une taille donnée.

        Valide que `size` est un entier strictement positif en utilisant
        la méthode integer_validator héritée.

        Args:
            size (int): La taille du côté du carré.

        Raises:
            TypeError: Si size n’est pas un entier.
            ValueError: Si size est inférieur ou égal à 0.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """
        Calcule et retourne l'aire du carré.

        Returns:
            int: Aire du carré (size * size).
        """
        return self.__size * self.__size

    def __str__(self):
        """
        Retourne une représentation formatée du carré.

        Format :
            [Square] <size> / <size>

        Returns:
            str: Description lisible du carré.
        """
        return "[Square] {} / {}".format(self.__size, self.__size)
