#!/usr/bin/python3
"""
Prints the State object with the name passed as argument from the database.

Usage:
    ./7-model_state_fetch_all.py <username> <password> <database> <state_name>

Arguments:
    <username>   : MySQL username
    <password>   : MySQL password
    <database>   : MySQL database name
    <state_name> : Name of the state to search for (exact match)

This script connects to a MySQL server running on localhost at port 3306
and uses SQLAlchemy ORM to retrieve the first State record matching the
given name.

If a matching state is found, its id is printed.
If no matching state is found, it prints "Not found".
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

    state_name = sys.argv[4]
    state = (session.query(State).filter(State.name == state_name).first())

    if state:
        print(f"{state.id}")
    else:
        print("Not found")
    session.close()
