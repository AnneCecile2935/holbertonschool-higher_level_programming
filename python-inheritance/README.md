# 📘 Python Inheritance

Ce projet fait partie du programme Holberton School et vise à maîtriser les concepts de l'héritage en Python, y compris l’héritage multiple, la redéfinition de méthodes, la validation de types, et la construction de classes plus complexes à partir de classes de base.

---

## 🧠 Objectifs pédagogiques

À la fin de ce projet, vous serez capable de :

- Définir une classe parente (superclass/baseclass) et une classe enfant (subclass).
- Lister tous les attributs et méthodes d'une classe ou instance.
- Créer des attributs dynamiquement pour une instance.
- Hériter d'une ou plusieurs classes.
- Comprendre la classe parente par défaut (`object`).
- Redéfinir une méthode ou un attribut hérité.
- Utiliser `isinstance()`, `issubclass()`, `type()` et `super()` efficacement.
- Comprendre l’intérêt de l’héritage pour réutiliser du code.

---

## ⚙️ Environnement

- **OS**: Ubuntu 20.04 LTS
- **Python version**: Python 3.8.5
- **Style guide**: [pycodestyle 2.7.\*](https://pypi.org/project/pycodestyle/)
- **Exécution des tests**: `python3 -m doctest ./tests/*`

---

## 🗃️ Contenu du projet

| Fichier | Description |
|--------|-------------|
| `0-lookup.py` | Fonction `lookup(obj)` listant attributs et méthodes. |
| `1-my_list.py` | Classe `MyList` héritant de `list` avec tri personnalisé. |
| `2-is_same_class.py` | Vérifie si un objet est **exactement** une instance d'une classe. |
| `3-is_kind_of_class.py` | Vérifie si un objet est une instance **ou hérite** d'une classe donnée. |
| `4-inherits_from.py` | Vérifie si un objet hérite **exclusivement** d’une classe. |
| `5-base_geometry.py` | Classe vide `BaseGeometry`. |
| `6-base_geometry.py` | Ajout de la méthode `area()` (non implémentée). |
| `7-base_geometry.py` | Ajout de la méthode `integer_validator()`. |
| `8-rectangle.py` | Classe `Rectangle` héritant de `BaseGeometry`, avec validation. |
| `9-rectangle.py` | Implémentation de `area()` et affichage `[Rectangle] w/h`. |
| `10-square.py` | Classe `Square` héritant de `Rectangle`, zone carrée. |
| `11-square.py` | Affichage personnalisé `[Square] w/h`. |
| `100-my_int.py` | Classe `MyInt` inversant les opérateurs `==` et `!=`. |

---

## 🧪 Structure des tests

- Tous les tests se trouvent dans le dossier `tests/`.
- Fichiers de tests au format `.txt` compatibles avec `doctest`.
- Exemple d'exécution :
```bash
python3 -m doctest ./tests/*

---

## Author

Anne-Cécile Colléter
