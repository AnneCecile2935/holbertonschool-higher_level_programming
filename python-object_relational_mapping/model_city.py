"""
Defines the City class mapped to the 'cities' table using SQLAlchemy ORM.
Each City has an id, a name, and a foreign key linking to a State.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """
    City class that represents a row in the 'cities' table.

    Attributes:
        id (int): Primary key, unique and auto-generated.
        name (str): Name of the city (max 128 characters), cannot be NULL.
        state_id (int): Foreign key referencing states.id, cannot be NULL.
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('state.id'), nullable=False)
