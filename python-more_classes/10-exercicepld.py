#!/usr/bin/python3
# Exercice Python - Classes et Baguettes Magiques de Harry Potter

"""
OBJECTIF: Créer une classe BaguetteMagique qui modélise les baguettes magiques du monde de Harry Potter.

CONSIGNES:
1. Implémentez la classe BaguetteMagique avec les attributs de classe et d'instance spécifiés
2. Implémentez les méthodes demandées
3. Testez votre code avec les exemples fournis à la fin de l'exercice

"""

import random

class BaguetteMagique:
    # Attributs de classe
    boiserie = ["Hêtre", "Chêne", "Acajou", "If", "Houx", "Vigne", "Saule", "Aubépine", "Sureau", "Prunellier"]
    coeurs = ["Crin de licorne", "Ventricule de dragon", "Plume de phénix", "Crin de Sombral", "Cheveu de Vélane"]
    baguettes = {}  # Dictionnaire pour stocker les baguettes créées

    def __init__(self, maison, proprietaire):
        """
        Constructeur de la classe BaguetteMagique

        Paramètres:
        - maison: str - La maison de Poudlard du propriétaire (Gryffondor, Poufsouffle, Serdaigle, Serpentard)
        - proprietaire: str - Le nom du propriétaire de la baguette

        Attributs d'instance à initialiser:
        - proprietaire: le nom du propriétaire (paramètre)
        - maison: la maison de Poudlard (paramètre)
        - bois: choisi aléatoirement dans la liste 'bois' de la classe
        - coeur: choisi aléatoirement dans la liste 'coeurs' de la classe
        - longueur: nombre aléatoire entre 22 et 35 (cm)

        Tous les attributs doivent être privés et utiliser des getter et setter
        """
        self.maison = maison
        self.proprietaire = proprietaire
        self.__bois = random.choice(BaguetteMagique.boiserie)
        self.__coeur = random.choice(BaguetteMagique.coeurs)
        self.__longueur = random.randint(22, 35)

    @property
    def maison(self):
        return self.__maison

    @maison.setter
    def maison(self, value):
        if not isinstance(value, str):
            raise TypeError("Maison doit être un string")
        self.__maison = value

    @property
    def proprietaire(self):
        return self.__proprietaire

    @proprietaire.setter
    def proprietaire(self, value):
        if not isinstance(value, str):
            raise TypeError("Proprietaire doit être un string")
        self.__proprietaire = value

    @property
    def coeur(self):
        return self.__coeur

    @coeur.setter
    def coeur(self, value):
        self.__coeur = value

    @property
    def bois(self):
        return self.__bois

    @bois.setter
    def bois(self, value):
        self.__bois = value

    def expelliarmus(self):
        """
        Méthode qui simule le sort Expelliarmus
        Affiche simplement "Expelliarmus !"
        """
        print("Expelliarmus!")

    def avada_kedavra(self):
        """
        Méthode qui simule le sort Avada Kedavra
        Vérifie si la baguette appartient à un sorcier de Serpentard
        Si oui, affiche "Avada Kedavra !"
        Si non, lève une exception avec un message approprié
        """
        if self.maison != "Serpentard":
            raise TypeError("La baguette n'appartient pas à un Serpentard")
        else:
            print("Avada Kedavra")

    def enregistrer_baguette(self):
        """
        Méthode qui enregistre les informations de la baguette dans le dictionnaire de classe 'baguettes'
        Utilise le nom du propriétaire comme clé
        La valeur doit être un dictionnaire contenant toutes les informations de la baguette
        (maison, bois, coeur, longueur)
        """
        self.baguettes[self.proprietaire] = {
        "maison": self.maison,
        "bois": self.__bois,
        "coeur": self.__coeur,
        "longueur": self.__longueur
    }



if __name__ == "__main__":
    # Création de quelques baguettes magiques
    baguette_harry = BaguetteMagique("Gryffondor", "Harry Potter")
    baguette_drago = BaguetteMagique("Serpentard", "Drago Malefoy")
    baguette_luna = BaguetteMagique("Serdaigle", "Luna Lovegood")

    # Enregistrement des baguettes
    baguette_harry.enregistrer_baguette()
    baguette_drago.enregistrer_baguette()
    baguette_luna.enregistrer_baguette()

    # Affichage des baguettes enregistrées
    print("Baguettes enregistrées:")
    for proprietaire, infos in BaguetteMagique.baguettes.items():
        print(f"Baguette de {proprietaire}: {infos}")

    # Test des sorts
    print("\nTest des sorts:")
    baguette_harry.expelliarmus()

    try:
        baguette_harry.avada_kedavra()  # Devrait lever une exception
    except Exception as e:
        print(f"Exception: {e}")

    baguette_drago.avada_kedavra()
