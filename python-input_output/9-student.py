#!/usr/bin/python3
"""
Module Student

Ce module contient la définition de la classe Student qui modélise un étudiant
avec les attributs first_name, last_name et age, ainsi qu'une méthode pour
obtenir une représentation JSON de l'objet.

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
        to_json(): retourne un dictionnaire contenant tous les attributs
        de l'instance, prêt pour la sérialisation JSON.
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

    def to_json(self):
        """
        Retourne le dictionnaire des attributs de l'instance.

        Returns:
            dict: un dictionnaire contenant les attributs et valeurs
            de l'objet Student.
        """
        return self.__dict__
