#!/usr/bin/python3
class MyInt(int):
    """
    Classe MyInt qui hérite de int avec les opérateurs == et != inversés.

    Description:
    ------------
    MyInt est une sous-classe de int où :
    - l'opérateur d'égalité (==) utilise la logique inverse de int.__eq__,
      c'est-à-dire qu'il retourne True si les valeurs sont différentes.
    - l'opérateur d'inégalité (!=) utilise la logique inverse de int.__ne__,
      c'est-à-dire qu'il retourne True si les valeurs sont égales.

    Cela signifie que les comparaisons == et != sont inversées par rapport
    au comportement standard des entiers en Python.

    Méthodes redéfinies:
    --------------------
    __ne__(self, other)
        Utilise la méthode __eq__ de la classe parent (int) pour inverser
        le résultat de l'inégalité.

    __eq__(self, other)
        Utilise la méthode __ne__ de la classe parent (int) pour inverser
        le résultat de l'égalité.

    Exemple d'utilisation:
    ----------------------
    >>> a = MyInt(5)
    >>> b = MyInt(5)
    >>> c = MyInt(3)

    >>> a == b
    False  # Valeurs égales, mais == est inversé

    >>> a != b
    True   # Valeurs égales, mais != est inversé

    >>> a == c
    True   # Valeurs différentes, == retourne True (inversé)

    >>> a != c
    False  # Valeurs différentes, != retourne False (inversé)
    """

    def __ne__(self, other):
        return super().__eq__(other)

    def __eq__(self, other):
        return super().__ne__(other)
