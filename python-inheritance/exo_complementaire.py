#!/usr/bin/python3

"""
Exercice : Gestion des personnages dans l’univers Harry Potter
 Contexte
Tu dois modéliser différents types de personnages dans l’univers Harry Potter.
Certains sont des sorciers, d’autres des moldus, et certains sorciers
maîtrisent des pouvoirs spéciaux comme le vol sur balai ou la métamorphose.

### Objectifs
Créer une classe abstraite Personnage avec des méthodes et attributs communs.

Créer des interfaces (classes abstraites) représentant des capacités spéciales.

Implémenter des classes concrètes héritant de ces classes abstraites et
interfaces.

Manipuler ces objets dans un scénario simple.

Instructions détaillées

Créer une classe abstraite Personnage

Attribut en lecture seule : nom (string)

Méthode abstraite se_presenter() qui affiche une phrase de présentation.

Créer deux interfaces (classes abstraites) :

PeutVoler avec méthode abstraite voler() (affiche par exemple « {nom} vole
sur son balai. »).

PeutSeMetamorphoser avec méthode abstraite se_metamorphoser()
(affiche par exemple « {nom} se transforme en animal. »).

Créer les classes concrètes suivantes :

Moldu hérite de Personnage.

Implémente se_presenter() pour dire « Je suis {nom}, un moldu. »

Sorciere hérite de Personnage et PeutVoler.

Implémente se_presenter() pour dire « Je suis {nom}, une sorcière. »

Implémente voler().

Animagus hérite de Personnage et PeutSeMetamorphoser.

Implémente se_presenter() pour dire « Je suis {nom}, un animagus. »

Implémente se_metamorphoser().

HarryPotter hérite de Personnage, PeutVoler et PeutSeMetamorphoser.

Implémente se_presenter() pour dire « Je suis Harry Potter,
le célèbre sorcier. »

Implémente voler() et se_metamorphoser().

Tester

Instancier un Moldu, une Sorciere, un Animagus, et HarryPotter.

Appeler leurs méthodes de présentation et capacités spécifiques.

Exemple d’utilisation attendue
python
Copier
Modifier
moldu = Moldu("John")
moldu.se_presenter()  # Je suis John, un moldu.

sorciere = Sorciere("Hermione")
sorciere.se_presenter()  # Je suis Hermione, une sorcière.
sorciere.voler()         # Hermione vole sur son balai.

animagus = Animagus("Sirius")
animagus.se_presenter()      # Je suis Sirius, un animagus.
animagus.se_metamorphoser()  # Sirius se transforme en animal.

harry = HarryPotter()
harry.se_presenter()         # Je suis Harry Potter, le célèbre sorcier.
harry.voler()                # Harry Potter vole sur son balai.
harry.se_metamorphoser()     # Harry Potter se transforme en animal.
"""


from abc import ABC, abstractmethod

class Personnage(ABC):
    def __init__(self, nom):
        self._nom = nom

    @property
    def nom(self):
        return self._nom

    @abstractmethod
    def se_presenter(self):
        print (f"Je me présente, je m'appelle {self.nom}")

class PeutVoler(ABC):
    @abstractmethod
    def voler(self):
        pass

class PeutSeMetamorphoser(ABC):
     @abstractmethod
     def se_metamorphoser(self):
       pass

class Moldu(Personnage):
     def se_presenter(self):
        print(f"Je suis {self.nom}, un moldu")

class Sorciere(Personnage, PeutVoler):
    def se_presenter(self):
        print(f"Je suis {self.nom}, une sorcière")

    def voler(self):
        print(f"{self.nom} vole sur son balai")

class Animagus(Personnage, PeutSeMetamorphoser):
    def se_presenter(self):
        print(f"Je suis {self.nom}, un animagus")

    def se_metamorphoser(self):
        print(f"{self.nom} se transforme en animal")

class HarryPotter(Personnage, PeutVoler, PeutSeMetamorphoser):

    def __init__(self):
        super().__init__("Harry Potter")
    def se_presenter(self):
        print(f"Je suis {self.nom}, le célèbre sorcier")

    def voler(self):
        print(f"{self.nom} vole sur son balai")

    def se_metamorphoser(self):
        print(f"{self.nom} se transforme en animal")


moldu = Moldu("John")
moldu.se_presenter()
sorciere = Sorciere("Avidaga")
sorciere.se_presenter()
sorciere.voler()
animagus = Animagus("oltor")
animagus.se_presenter()
animagus.se_metamorphoser()
harry_potter = HarryPotter()
harry_potter.se_presenter()
harry_potter.se_metamorphoser()
harry_potter.voler()
