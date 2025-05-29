# Python OOP – Abstract Classes, Interfaces, Subclassing

## Introduction

Ce projet est une série d’exercices conçus pour renforcer la compréhension et l’application des concepts de Programmation Orientée Objet (POO) en Python. Les concepts couverts incluent les classes abstraites, les interfaces, le duck typing, l’héritage multiple, les mixins, et l’extension de classes de base Python.

## Objectifs pédagogiques

- **Classes abstraites** : Définir des interfaces communes et forcer l’implémentation de méthodes clés.
- **Interfaces et Duck Typing** : Travailler avec des objets selon leurs comportements plutôt que leurs types.
- **Extension de classes standard** : Hériter de classes Python intégrées comme `list`, `dict`, ou les itérateurs.
- **Surcharge de méthodes** : Modifier ou enrichir le comportement hérité.
- **Héritage multiple** : Comprendre la résolution d’ordre de méthode (MRO) et les implications de l’héritage multiple.
- **Mixins** : Ajouter des comportements spécifiques de manière modulaire.

## Ressources recommandées

- [Python 3 Object-Oriented Programming (livre)](https://www.packtpub.com/product/python-3-object-oriented-programming/9781789615852)
- [Documentation officielle sur `abc`](https://docs.python.org/3/library/abc.html)
- [Real Python – OOP in Python 3](https://realpython.com/python3-object-oriented-programming/)
- [Corey Schafer – OOP Python YouTube Playlist](https://www.youtube.com/playlist?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc)
- [sentdex – Python OOP Tutorial](https://www.youtube.com/watch?v=JeznW_7DlB0)

---

## Contenu du projet

### 0. Abstract Animal Class and Subclasses

- Implémentation d’une classe abstraite `Animal` avec une méthode `sound`.
- Sous-classes concrètes : `Dog` et `Cat`, chacune avec sa propre implémentation de `sound`.

### 1. Shapes, Interfaces, and Duck Typing

- Classe abstraite `Shape` avec méthodes `area` et `perimeter`.
- Classes concrètes `Circle` et `Rectangle`.
- Fonction `shape_info` qui utilise le duck typing pour afficher l’aire et le périmètre.

### 2. Extending the Python List with Notifications

- Classe `VerboseList` qui hérite de `list`.
- Surcharge de méthodes (`append`, `extend`, `remove`, `pop`) avec messages explicites.

### 3. CountedIterator – Suivi d’itération

- Classe `CountedIterator` pour suivre le nombre d’éléments itérés via `__next__`.
- Méthode `get_count()` pour afficher le nombre d’itérations effectuées.

### 4. FlyingFish – Héritage multiple

- Classe `FlyingFish` héritant de `Fish` et `Bird`.
- Méthodes `swim`, `fly`, et `habitat` redéfinies.
- Exploration de l’ordre de résolution des méthodes via `mro()`.

### 5. Dragon – Utilisation de Mixins

- `SwimMixin` et `FlyMixin` fournissent les capacités de nager et voler.
- `Dragon` combine ces comportements et ajoute une méthode `roar`.

---

## Exécution

Chaque fichier `main_*.py` contient un script de test indépendant. Pour tester chaque tâche :

```bash
$ ./main_00_abc.py
$ ./main_01_duck_typing.py
...
$ ./main_05_dragon.py


---

## Author

Anne-Cécile Colléter
