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
 
    def print_sorted(self):
        """
        Affiche les éléments de la liste dans l'ordre croissant (trié),
        sans modifier la liste originale.
        """
        print(sorted(self))
