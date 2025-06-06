#!/usr/bin/env python3
"""
Module pour convertir un fichier CSV en fichier JSON.

La fonction principale lit un fichier CSV, convertit chaque ligne
en dictionnaire,
puis écrit l'ensemble sous forme de liste JSON dans un fichier `data.json`.
Chaque dictionnaire est écrit sur une seule ligne avec une indentation
personnalisée.
"""


import csv
import json


def convert_csv_to_json(csv_file):
    """
    Convertit un fichier CSV en un fichier JSON nommé `data.json`.

    Lit le fichier CSV spécifié, convertit chaque ligne en dictionnaire,
    et écrit la liste de dictionnaires dans un fichier JSON avec la structure
    suivante :
    - Une liste encadrée par des crochets `[ ]`
    - Chaque dictionnaire sur une seule ligne, indenté de 4 espaces
    - Virgules entre les dictionnaires sauf après le dernier

    Args:
        csv_file (str): Le chemin du fichier CSV à convertir.

    Returns:
        bool: True si la conversion a réussi, False en cas d'erreur.

    Exemple:
        >>> convert_csv_to_json('data.csv')
        True

    En cas d'erreur (fichier manquant, permission, etc.), la fonction affiche
    l'erreur
    et retourne False.
    """
    try:
        with open(csv_file, "r", newline='') as f:
            dict_reader = csv.DictReader(f)
            data = list(dict_reader)

        with open("data.json", "w") as d:
            d.write("[\n")
            for i, entry in enumerate(data):
                json_line = json.dumps(entry, separators=(',', ':'))
                d.write("    " + json_line)
                if i < len(data) - 1:
                    d.write(",\n")
                else:
                    d.write("\n")
            d.write("]\n")

        return True

    except Exception as e:
        print(f"Erreur : {e}")
        return False
