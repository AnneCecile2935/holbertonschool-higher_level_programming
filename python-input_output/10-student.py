#!/usr/bin/python3
"""
Module Student

Ce module contient la définition de la classe Student qui modélise un étudiant
avec les attributs first_name, last_name et age, ainsi qu'une méthode pour
obtenir une représentation JSON partielle ou complète de l'objet.

Classes:
    Student: représente un étudiant avec ses informations de base.
"""


class Student:
    """
    Classe Student représentant un étudiant avec des attributs publics.

    Attributs publics:
        first_name (str): prénom de l'étudiant
        last_name (str): nom de famille de l'étudiant
        age (int): âge de l'étudiant

    Méthodes:
        to_json(attrs=None): retourne un dictionnaire contenant les attributs
        de l'instance, filtrés si une liste est passée en paramètre.
    """
    def __init__(self, first_name, last_name, age):
        """
        Initialise une nouvelle instance de Student.

        Args:
            first_name (str): prénom de l'étudiant
            last_name (str): nom de famille de l'étudiant
            age (int): âge de l'étudiant
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retourne le dictionnaire des attributs de l'instance Student.

        Si attrs est une liste de chaînes, seuls les attributs listés
        sont inclus dans le dictionnaire retourné. Sinon, tous les
        attributs de l'objet sont retournés.

        Args:
            attrs (list, optional): liste des noms d'attributs à inclure.

        Returns:
            dict: dictionnaire contenant les attributs sélectionnés.
        """
        if (
            isinstance(attrs, list) and
            all(isinstance(attr, str) for attr in attrs)
        ):
            return {
                attr: getattr(self, attr)
                for attr in attrs if hasattr(self, attr)
            }
        return self.__dict__
