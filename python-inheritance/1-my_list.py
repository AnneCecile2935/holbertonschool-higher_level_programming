#!/usr/bin/python3
"""
Module 1-my_list

Ce module contient la classe `MyList`, une sous-classe de `list`
qui ajoute une méthode pour afficher la liste triée.
Il vérifie également que tous les éléments ajoutés sont des entiers.
"""


class MyList(list):
    """
    Classe dérivée de `list` qui impose que tous les éléments soient
    des entiers et ajoute une méthode `print_sorted` pour afficher
    la liste triée.
    """
    def __init__(self, entier=None):
        """
        Initialise une nouvelle instance de MyList.

        Args:
            entier (list, optional): Liste d'entiers à initialiser.
                                     Par défaut, une liste vide est utilisée.

        Raises:
            TypeError: Si un ou plusieurs éléments de la liste ne sont
            pas des entiers.
        """
        if entier is None:
            entier = []
        if not all(isinstance(value, int) for value in entier):
            raise TypeError("Elements must be integers")
        super().__init__(entier)

    def print_sorted(self):
        """
        Affiche les éléments de la liste dans l'ordre croissant (trié),
        sans modifier la liste originale.
        """
        print(sorted(self))
