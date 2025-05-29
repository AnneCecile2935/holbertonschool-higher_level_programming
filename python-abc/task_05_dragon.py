#!/usr/bin/env python3
"""
Module: dragon_mixins

Ce module illustre l'utilisation des mixins et de l'héritage multiple
en Python.
Il définit des comportements réutilisables avec des classes `SwimMixin`
et `FlyMixin`,
et une classe `Dragon` qui hérite de ces deux comportements.

Classes:
    SwimMixin: Fournit une méthode `swim` pour les créatures aquatiques.
    FlyMixin: Fournit une méthode `fly` pour les créatures volantes.
    Dragon: Une créature mythique capable de nager, voler et rugir.
"""


class SwimMixin:
    """
    Mixin qui ajoute la capacité de nager à une classe.
    """
    def swim(self):
        """
        Affiche un message indiquant que la créature nage.
        """
        print("The creature swims!")


class FlyMixin:
    """
    Mixin qui ajoute la capacité de voler à une classe.
    """
    def fly(self):
        """
        Affiche un message indiquant que la créature vole.
        """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Classe représentant un dragon qui peut nager, voler et rugir.

    Hérite de:
        SwimMixin: pour la méthode swim().
        FlyMixin: pour la méthode fly().
    """
    def __init__(self):
        """
        Initialise une instance de Dragon.
        """
        super().__init__()

    def roar(self):
        """
        Affiche un rugissement du dragon.
        """
        print("The dragon roars!")


if __name__ == "__main__":
    Draco = Dragon()
    Draco.swim()
    Draco.fly()
    Draco.roar()
