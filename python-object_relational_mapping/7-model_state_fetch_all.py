#!/usr/bin/python3
"""
Lists all State objects from the database hbtn_0e_6_usa.

Usage:
    ./7-model_state_fetch_all.py <username> <password> <database>

Arguments:
    <username>   : MySQL username
    <password>   : MySQL password
    <database>   : MySQL database name

This script connects to a MySQL server running on localhost at port 3306
and uses SQLAlchemy ORM to fetch and display all State records,
sorted by ascending state.id.
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

    states = session.query(State).order_by(State.id).all()
    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()
