#!/usr/bin/python3
"""
Definition du modèle State pour SQLAlchemy ORM.

Ce module définit la classe `State`, qui est mappée à la table `states`
dans une base de données MySQL.
Elle permet de manipuler des enregistrements de la table `states`
en utilisant SQLAlchemy.

Classes:
    State: classe représentant un état avec un identifiant et un nom.

Attributs:
    Base: instance de la classe declarative_base utilisée pour la
    déclaration du modèle ORM.
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class State(Base):
    """
    Classe `State` liée à la table `states` dans la base de données.

    Attributs:
        id (int): Clé primaire de la table, auto-incrémentée et non nulle.
        name (str): Nom de l'état, chaîne de caractères non nulle de longueur
        maximale 128.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
# establish one-to-many relationship
    cities = relationship(
        "City",
        backref='state',
        order_by='City.id',
        cascade='all, delete'
    )
