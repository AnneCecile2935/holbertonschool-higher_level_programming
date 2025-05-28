#!/usr/bin/env python3
"""
Module verbose_list

Ce module définit une classe VerboseList qui hérite de la classe built-in list.
Cette classe surchage certaines méthodes pour afficher un message chaque fois
qu'un élément est ajouté ou retiré de la liste.

Classes:
    VerboseList: Liste avec notifications lors des modifications.

Usage:
    Instanciez VerboseList et utilisez les méthodes append, extend, remove, pop.
    Des messages seront automatiquement affichés lors des appels.
"""
class VerboseList(list):
    """
    Liste personnalisée qui affiche des messages lorsque des éléments
    sont ajoutés ou retirés.

    Méthodes surchargées:
        append(item): Ajoute un élément et affiche un message.
        extend(iterable): Étend la liste avec plusieurs éléments et affiche un message.
        remove(item): Supprime un élément et affiche un message.
        pop(index=-1): Supprime et retourne un élément à un index donné (par défaut le dernier),
                       et affiche un message.
    """

    def append(self, item):
        """
        Ajoute un élément à la liste et affiche un message.

        Args:
            item: L'élément à ajouter.
        """
        super().append(item)
        print(f"Added [{item}] to the list")

    def extend(self, iterable):
        """
        Étend la liste avec les éléments fournis et affiche un message.

        Args:
            iterable: Une séquence d'éléments à ajouter.
        """
        super().extend(iterable)
        print(f"Extended the list with [{len(iterable)}] items.")

    def remove(self, item):
        """
        Supprime le premier élément égal à item et affiche un message.

        Args:
            item: L'élément à retirer.
        """
        super().remove(item)
        print(f"Removed [{item}] from the list.")

    def pop(self, index=-1):
        """
        Supprime et retourne l'élément à l'index donné, affiche un message.

        Args:
            index (int, optional): L'index de l'élément à retirer. Par défaut -1 (dernier).

        Returns:
            L'élément retiré.
        """
        item = super().pop(index)
        print(f"Popped [{item}] from the list.")
        return item


if __name__ == "__main__":
    my_list = VerboseList()
    my_list.append("Bonjour")
    print(my_list)
    my_list.extend(["Bonjour", "Aurevoir"])
    print(my_list)
    my_list.remove("Bonjour")
    print(my_list)
    my_list.pop()
    print(my_list)
