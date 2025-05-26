#!/usr/bin/python3
"""
Module is_kind_of_class

Ce module contient la fonction is_kind_of_class qui permet de vérifier
si un objet est une instance directe ou indirecte (via héritage) d'une classe
donnée.
"""


def is_kind_of_class(obj, a_class):
    """
    Vérifie si l'objet est une instance de la classe spécifiée ou
    d'une classe qui en hérite.

    Args:
        obj (object): L'objet à tester.
        a_class (type): La classe à comparer.

    Returns:
        bool: True si obj est une instance de a_class ou d'une classe héritée
        de a_class,
              False sinon.

    Exemple:
        >>> class A: pass
        >>> class B(A): pass
        >>> b = B()
        >>> is_kind_of_class(b, A)
        True
        >>> is_kind_of_class(b, B)
        True
        >>> is_kind_of_class(b, list)
        False
    """

    cls = obj.__class__
    if a_class in cls.__mro__:
        return True
    else:
        return False
