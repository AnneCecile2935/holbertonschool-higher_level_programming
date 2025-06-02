#!/usr/bin/python3
"""
Module Pascal Triangle

Ce module contient une fonction qui génère le triangle de Pascal
sous forme de liste de listes.

Fonctions:
    pascal_triangle(n): retourne une liste de listes représentant
    le triangle de Pascal jusqu'à la n-ième ligne.
"""


def pascal_triangle(n):
    """
    Génère le triangle de Pascal jusqu'à la n-ième ligne.

    Chaque ligne du triangle est une liste d'entiers,
    où chaque élément est la somme des deux éléments situés
    juste au-dessus dans la ligne précédente.
    Les premiers et derniers éléments de chaque ligne sont toujours 1.

    Args:
        n (int): Le nombre de lignes du triangle à générer.

    Returns:
        list: Une liste de listes d'entiers représentant
        le triangle de Pascal. Si n <= 0, retourne une liste vide.
    """
    triangle = []
    for i in range(n):
        line = []
        for j in range(i + 1):
            if j == 0 or j == i:
                line.append(1)
            else:
                result = triangle[i - 1][j - 1] + triangle[i - 1][j]
                line.append(result)

        triangle.append(line)

    return triangle
