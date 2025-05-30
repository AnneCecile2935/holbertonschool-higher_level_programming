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
import math


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
        self.radius = abs(radius)

    def area(self):
        """
        Calcule et retourne l'aire du cercle.

        Returns:
            float: Aire du cercle.
        """
        return math.pi * self.radius ** 2

    def perimeter(self):
        """
        Calcule et retourne le périmètre du cercle.

        Returns:
            float: Périmètre du cercle.
        """
        return 2 * math.pi * self.radius


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
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Affiche l'aire et le périmètre d’un objet.

    Args:
        shape: Un objet qui possède les méthodes area() et perimeter().
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")


if __name__ == "__main__":
    circle = Circle(5)
    rectangle = Rectangle(4, 7)

    print("Circle:")
    shape_info(circle)

    print("\nRectangle:")
    shape_info(rectangle)
