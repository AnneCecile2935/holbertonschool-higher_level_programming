#!/usr/bin/python3
"""
Module inherits_from

Ce module contient la fonction inherits_from qui permet de vérifier
si un objet est une instance d'une classe héritée directement ou indirectement
d'une classe donnée.
"""


def inherits_from(obj, a_class):
    """
    Vérifie si l'objet est une instance d'une classe héritée directement ou
    indirectement

    Args:
        obj (object): L'objet à tester.
        a_class (type): La classe à comparer.

    Returns:
        bool: True si obj est une instance de a_class héritée directement
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
    if cls is not a_class and issubclass(cls, a_class):
        return True
    return False
