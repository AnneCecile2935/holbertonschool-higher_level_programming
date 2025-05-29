#!/usr/bin/python3
"""
Module myint

Ce module contient la définition de la classe MyInt, une sous-classe
personnalisée de int qui inverse le comportement des opérateurs d'égalité
(==) et d'inégalité (!=).

Fonctionnalités :
- L'opérateur == retourne True lorsque les valeurs sont différentes.
- L'opérateur != retourne True lorsque les valeurs sont égales.
"""


class MyInt(int):
    """
    Sous-classe de int avec opérateurs == et != inversés.

    Cette classe modifie le comportement des comparaisons d'égalité et
    d'inégalité pour que :

      - a == b retourne True si a et b sont différents,
      - a != b retourne True si a et b sont égaux.

    Cela permet d'utiliser MyInt comme un entier "rebelle".

    Méthodes
    --------
    __ne__(self, other)
        Retourne True si self est égal à other (inverse de !=).

    __eq__(self, other)
        Retourne True si self est différent de other (inverse de ==).
    """

    def __ne__(self, other):
        """
        Redéfinit l'opérateur d'inégalité (!=).

        Inverse la logique de la classe parente int.__ne__ en appelant
        int.__eq__ pour déterminer l'égalité.

        Paramètres:
        -----------
        other : objet à comparer

        Retour:
        -------
        bool
            True si self est égal à other, False sinon.
        """
        return super().__eq__(other)

    def __eq__(self, other):
        """
        Redéfinit l'opérateur d'égalité (==).

        Inverse la logique de la classe parente int.__eq__ en appelant
        int.__ne__ pour déterminer l'inégalité.

        Paramètres:
        -----------
        other : objet à comparer

        Retour:
        -------
        bool
            True si self est différent de other, False sinon.
        """
        return super().__ne__(other)
