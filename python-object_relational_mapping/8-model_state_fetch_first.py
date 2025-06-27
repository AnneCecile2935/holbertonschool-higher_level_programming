#!/usr/bin/python3
"""
Fetches and prints the first State object from the database hbtn_0e_6_usa.

Usage:
    ./7-model_state_fetch_all.py <username> <password> <database>

Arguments:
    <username>   : MySQL username
    <password>   : MySQL password
    <database>   : MySQL database name

This script connects to a MySQL server running on localhost at port 3306
and uses SQLAlchemy ORM to retrieve the first State record (ordered by id),
then prints its id and name in the format "<id>: <name>".

If the table 'states' is empty, it prints "Nothing".
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

    state = session.query(State).order_by(State.id).first()
    if state:
        print(f"{state.id}: {state.name}")
    else:
        print("Nothing")

    session.close()
