#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    Calcule le carré de chaque élément dans une matrice donnée.

    Cette fonction prend en entrée une matrice représentée
    sous forme de liste de listes
    et renvoie une nouvelle matrice où chaque élément
    est le carré de l'élément correspondant
    dans la matrice d'origine.

    Paramètres:
    - matrix (list): Liste de listes contenant des entiers ou des flottants.

    Retourne:
    - list: Nouvelle matrice où chaque élément est
    le carré de l'élément d'origine.
    """
    return [[x**2 for x in row] for row in matrix]
