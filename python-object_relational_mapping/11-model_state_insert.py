#!/usr/bin/python3
"""
Inserts a new State object with the name 'Louisiana' into the database.

Usage:
    ./7-model_state_fetch_all.py <username> <password> <database>

Arguments:
    <username>   : MySQL username
    <password>   : MySQL password
    <database>   : MySQL database name

This script connects to a MySQL server running on localhost at port 3306
and uses SQLAlchemy ORM to insert a new State record with the name 'Louisiana'
into the specified database.

After insertion, it prints the id of the newly added State.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://"
        f"{sys.argv[1]}:{sys.argv[2]}"
        "@localhost:3306/"
        f"{sys.argv[3]}",
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()

    print(f"{new_state.id}")

    session.close()
