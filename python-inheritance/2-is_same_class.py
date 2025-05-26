#!/usr/bin/python3
"""
Module is_same_class

Ce module contient la fonction is_same_class qui permet de vérifier
si un objet est exactement une instance d'une classe donnée.

Fonction:
    is_same_class(obj, a_class): Retourne True si obj est une instance
    exacte de a_class, sinon False.
"""


def is_same_class(obj, a_class):
    """
    Vérifie si un objet est **exactement** une instance de la classe spécifiée.

    Args:
        obj (any): L'objet à tester.
        a_class (type): La classe à comparer avec l'objet.

    Returns:
        bool: True si obj est exactement une instance de a_class, sinon False.

    Exemple:
        >>> class A: pass
        >>> a = A()
        >>> is_same_class(a, A)
        True
        >>> is_same_class(a, object)
        False
    """

    if obj.__class__ is a_class:
        return True
    return False
