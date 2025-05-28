#!/usr/bin/env python3

class CountedIterator:
    """
    Classe qui encapsule un itérateur et compte le nombre d'éléments
    itérés.

    Attributs:
        iterator (iterator): L'itérateur sous-jacent sur lequel la classe
        s'appuie.
        counter (int): Le compteur du nombre d'éléments déjà retournés.

    Méthodes:
        __iter__(): Retourne l'objet itérateur lui-même.
        __next__(): Retourne le prochain élément de l'itérateur et
        incrémente le compteur.
        get_count(): Retourne le nombre d'éléments déjà itérés.
    """
    def __init__(self, iterable):
        """
        Initialise un CountedIterator à partir d'un iterable.

        Args:
            iterable: Un objet itérable (liste, tuple, etc.) à itérer.
        """
        self.iterator = iter(iterable)
        self.counter = 0

    def __next__(self):
        """
        Retourne le prochain élément de l'itérateur et incrémente le compteur.

        Raises:
            StopIteration: Lorsque l'itérateur est épuisé.

        Returns:
            L'élément suivant de l'itérateur.
        """
        try:
            item = next(self.iterator)
            self.counter += 1
            return item

        except StopIteration:
            raise StopIteration

    def get_count(self):
        """
        Retourne le nombre d'éléments déjà itérés.

        Returns:
            int: Le nombre d'éléments retournés via __next__().
        """
        return self.counter

    def __iter__(self):
        """
        Retourne l'objet itérateur lui-même pour prise en charge
        dans une boucle.

        Returns:
            self: L'objet CountedIterator.
        """
        return self


if __name__ == "__main__":
    count_iterator = CountedIterator([1, 2, 3, 4, 5])
    for item in count_iterator:
        print(item)
    print("Total items iterated :", count_iterator.get_count())
