#!/usr/bin/python3
"""
Module base_geometry

Ce module définit la classe `BaseGeometry`, destinée à servir de classe de base
pour des formes géométriques.

La classe inclut une méthode `area()` qui n’est pas implémentée et qui lève
une exception. Cela sert à indiquer que les sous-classes doivent redéfinir
cette méthode pour fournir une implémentation spécifique.
"""


class BaseGeometry:
    """
    Classe de base pour les formes géométriques.

    Cette classe fournit une interface commune pour les classes dérivées.
    La méthode `area` est définie mais volontairement non implémentée,
    afin de forcer les sous-classes à fournir leur propre implémentation.
    """

    def area(self):
        """
        Calcule la surface de la forme géométrique.

        Cette méthode n'est pas implémentée dans la classe de base
        et doit être surchargée par les classes dérivées.

        Raises:
            Exception: toujours levée avec le message "area() is
            not implemented"
        """
        raise Exception("area() is not implemented")
