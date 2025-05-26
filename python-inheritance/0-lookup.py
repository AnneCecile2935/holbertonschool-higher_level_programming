#!/usr/bin/python3
def lookup(obj):
    """
    Retourne la liste des attributs et méthodes disponibles
    pour un objet donné.

    Args:
        obj: L'objet à inspecter.

    Returns:
        list: Une liste de chaînes de caractères représentant les noms
        des attributs et méthodes accessibles via l'objet.

    Exemple:
        >>> lookup("hello")
        ['__add__', '__class__', ..., 'upper', 'zfill']
    """
    return dir(obj)
