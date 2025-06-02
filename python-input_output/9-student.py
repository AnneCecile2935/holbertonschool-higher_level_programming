#!/usr/bin/python3

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
