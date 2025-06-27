#!/usr/bin/python3
"""
Deletes all State objects containing the letter 'a' from the database.

Usage:
    ./7-model_state_fetch_all.py <username> <password> <database>

Arguments:
    <username>   : MySQL username
    <password>   : MySQL password
    <database>   : MySQL database name

This script connects to a MySQL server running on localhost at port 3306
and uses SQLAlchemy ORM to locate all State objects whose name contains
the letter 'a'. All matching State records are deleted from the database.

Note:
    - If no matching State is found, no deletion occurs.
    - The deletion is committed to the database.
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

    state_del_a = session.query(State).filter(State.name.like('%a%')).all()
    for state in state_del_a:
        session.delete(state)
    session.commit()

    remaining_states = session.query(State).order_by(State.id).all()
    for state in remaining_states:
        print(f"{state.id}: {state.name}")

    session.close()
