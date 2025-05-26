#!/usr/bin/python3
"""
Module base_geometry

Ce module définit une classe BaseGeometry avec des méthodes de base pour
la géométrie. Elle est destinée à être étendue par des sous-classes.
"""


class BaseGeometry:
    """
    Classe de base pour des formes géométriques.

    Fournit une interface commune et des méthodes de validation.
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
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
