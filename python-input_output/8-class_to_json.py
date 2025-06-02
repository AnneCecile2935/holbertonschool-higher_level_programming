#!/usr/bin/python3
"""
Module contenant une fonction pour convertir une instance de classe
en dictionnaire simple, prêt pour la sérialisation JSON.

Fonctions :
    - class_to_json(obj): Retourne un dictionnaire des attributs de l'objet.
"""


import json


def class_to_json(obj):
    """
    Returns the dictionary representation of a class instance's attributes
    suitable for JSON serialization.

    Args:
        obj (object): An instance of a class.

    Returns:
        dict: A dictionary containing all the attributes of the instance
        with their values, assuming they are simple data types (list, dict,
        string, int, bool) compatible with JSON serialization.
    """
    return obj.__dict__
