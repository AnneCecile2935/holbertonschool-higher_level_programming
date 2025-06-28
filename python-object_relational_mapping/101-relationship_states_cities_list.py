#!/usr/bin/python3
"""
Lists all State objects and their linked City objects from a MySQL database.

Usage:
    ./101-relationship_states_cities_list.py <mysql_username> <mysql_password>
      <database_name>

This script:
- Connects to a MySQL server on localhost:3306 using SQLAlchemy.
- Uses a single query to fetch all State objects and preloads their cities via
 relationship().
- Displays the results sorted by states.id and cities.id (ascending).
- Prints the data in the following format:

    <state id>: <state name>
        <city id>: <city name>

Note:
    The relationship between State and City must be defined using SQLAlchemy's
    ORM
    with joined loading to avoid N+1 queries. Your State class must have a
    `cities` relationship to City.
"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from relationship_city import City
from relationship_state import State
from sqlalchemy.orm import selectinload

if __name__ == "__main__":
    # connect to MySQl server using SQLAlchemy
    engine = create_engine(
        "mysql+mysqldb://"
        f"{sys.argv[1]}:{sys.argv[2]}"
        "@localhost:3306/"
        f"{sys.argv[3]}",
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()
    # Query all States and preload their related cities in one query
    states = (
        session.query(State)
        .options(selectinload(State.cities))
        .order_by(State.id)
        .all()
        )
    # options(joined(state.cities = charge tous les objets State
    # en la relation cities avec un Join SQl,
    # requête qui combine State et City avec un JOIN

    # Iterate over states and their cities,
    # displaying them in the required format
    for state in states:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"\t{city.id}: {city.name}")

    session.close()
