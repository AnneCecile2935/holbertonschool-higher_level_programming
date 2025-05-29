#!/usr/bin/env python3
"""
Module: flyingfish

Ce module illustre l'héritage multiple en Python à l'aide des classes Fish,
Bird et FlyingFish.
La classe FlyingFish hérite à la fois des comportements des poissons et
des oiseaux, et redéfinit certaines méthodes pour refléter ses capacités
uniques.
"""


class Fish:
    """
    Classe représentant un poisson.

    Méthodes :
        swim() : Affiche un message indiquant que le poisson nage.
        habitat() : Affiche l'habitat typique d'un poisson.
    """
    def swim(self):
        """Affiche que le poisson nage."""
        print("The fish is swimming")

    def habitat(self):
        """Affiche que le poisson vit dans l'eau."""
        print("The fish lives in water")


class Bird:
    """
    Classe représentant un oiseau.

    Méthodes :
        fly() : Affiche un message indiquant que l'oiseau vole.
        habitat() : Affiche l'habitat typique d'un oiseau.
    """
    def fly(self):
        """Affiche que l'oiseau vole."""
        print("The bird is flying")

    def habitat(self):
        """Affiche que l'oiseau vit dans le ciel."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    Classe représentant un poisson volant, qui hérite de Fish et Bird.

    Méthodes redéfinies :
        fly() : Affiche que le poisson volant plane.
        swim() : Affiche que le poisson volant nage.
        habitat() : Affiche que le poisson volant vit à la fois
        dans l'eau et dans le ciel.
    """
    def fly(self):
        """Affiche que le poisson volant plane."""
        print("The flying fish is soaring!")

    def swim(self):
        """Affiche que le poisson volant nage."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Affiche que le poisson volant vit à la fois dans l'eau
        et dans le ciel."""
        print("The flying fish lives both in water and the sky!")


if __name__ == "__main__":
    flyfish = FlyingFish()
    flyfish.fly()
    flyfish.swim()
    flyfish.habitat()
    print(FlyingFish.mro())
