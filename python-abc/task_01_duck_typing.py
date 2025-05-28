#!/usr/bin/env python3
"""
Module: shapes

Ce module définit une hiérarchie de classes pour représenter des formes
géométriques
utilisant la programmation orientée objet et le concept d’abstraction avec ABC.

Classes:
    Shape (classe abstraite): Définit l’interface des formes avec les méthodes
    `area` et `perimeter`.
    Circle: Représente un cercle, dérivé de Shape.
    Rectangle: Représente un rectangle, dérivé de Shape.

Fonctions:
    shape_info(shape): Affiche l’aire et le périmètre d’un objet Shape.
"""
from abc import ABC, abstractmethod


class Shape(ABC):
    """
    Classe abstraite représentant une forme géométrique.

    Méthodes abstraites:
        area(): Calcule et retourne l’aire de la forme.
        perimeter(): Calcule et retourne le périmètre de la forme.
    """

    @abstractmethod
    def area(self):
        """Retourne l'aire de la forme (à implémenter dans les
        sous-classes).
        """
        pass

    @abstractmethod
    def perimeter(self):
        """Retourne le périmètre de la forme (à implémenter dans
        les sous-classes).
        """
        pass


class Circle(Shape):
    """
    Représente un cercle avec un rayon donné.

    Attributs:
        radius (float): Le rayon du cercle.
    """
    def __init__(self, radius):
        """
        Initialise un objet Circle avec un rayon donné.

        Args:
            radius (float): Rayon du cercle.
        """
        self.radius = radius

    def area(self):
        """
        Calcule et retourne l'aire du cercle.

        Returns:
            float: Aire du cercle.
        """
        return 3.14 * self.radius ** 2

    def perimeter(self):
        """
        Calcule et retourne le périmètre du cercle.

        Returns:
            float: Périmètre du cercle.
        """
        return 2 * 3.14 * self.radius


class Rectangle(Shape):
    """
    Représente un rectangle avec une largeur et une hauteur.

    Attributs:
        width (float): Largeur du rectangle.
        height (float): Hauteur du rectangle.
    """

    def __init__(self, width, height):
        """
        Initialise un objet Rectangle avec une largeur et une hauteur.

        Args:
            width (float): Largeur du rectangle.
            height (float): Hauteur du rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Calcule et retourne l'aire du rectangle.

        Returns:
            float: Aire du rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calcule et retourne le périmètre du rectangle.

        Returns:
            float: Périmètre du rectangle.
        """
        return (self.width + self.height) * 2


def shape_info(shape):
    """
    Affiche l'aire et le périmètre d’un objet Shape.

    Args:
        shape (Shape): Une instance d’une classe dérivée de Shape.
    """
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
