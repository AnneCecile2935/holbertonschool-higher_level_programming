#!/usr/bin/env python3
"""
Module animal

Ce module définit une hiérarchie de classes pour représenter des animaux
en utilisant la programmation orientée objet avec des classes abstraites.

Il inclut :
- Une classe abstraite `Animal` qui impose la définition d'une méthode
`sound()`.
- Deux sous-classes concrètes : `Dog` et `Cat`, représentant respectivement
un chien et un chat,
  chacune implémentant sa propre version de la méthode `sound()`.

Ce modèle permet d'encapsuler le comportement spécifique de chaque type
'animal,
tout en garantissant que tous les animaux implémentent la méthode `sound`.

Classes :
    - Animal (ABC) : Classe de base abstraite.
    - Dog (Animal) : Classe représentant un chien.
    - Cat (Animal) : Classe représentant un chat.

Exemple d'utilisation :
    d = Dog()
    print(d.sound())  # Affiche "Bark"

    c = Cat()
    print(c.sound())  # Affiche "Meow"
"""


from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Classe abstraite représentant un animal.

    Méthodes abstraites :
        - sound() : Doit être implémentée dans chaque sous-classe.
    """

    @abstractmethod
    def sound(self):
        """
        Retourne le son que fait l’animal.

        Cette méthode doit être redéfinie dans toute classe fille.
        """
        pass


class Dog(Animal):
    """
    Classe représentant un chien.

    Hérite de :
        - Animal

    Méthodes :
        - sound() : Retourne "Bark"
    """

    def sound(self):
        return "Bark"


class Cat(Animal):
    """
    Classe représentant un chat.

    Hérite de :
        - Animal

    Méthodes :
        - sound() : Retourne "Meow"
    """

    def sound(self):
        return "Meow"
