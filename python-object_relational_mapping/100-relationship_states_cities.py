#!/usr/bin/python3
"""
Creates the State 'California' with the City 'San Francisco' in the database
hbtn_0e_100_usa.

Usage:
    ./100-relationship_states_cities.py <mysql_username> <mysql_password>
    <database_name>

This script:
- Connects to a MySQL server on localhost at port 3306 using SQLAlchemy.
- Defines a relationship between State and City using the cities attribute.
- Uses the relationship to link a new City to a new State.
- Persists the new objects into the database.
"""
import sys
from sqlalchemy.orm import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import Base, City
from relationship_city import State


if __name__ == "__main__":
    # connect to MySQl server using SQLAlchemy
    engine = create_engine(
        "myslq+mysqldb://"
        f"{sys.argv[1]}:{sys.argv[2]}"
        "@localhost:3306"
        f"{sys.argv[3]}",
        pool_pre_ping=True
    )
    # Create all tables in the database (if not exist)
    Base.metadata.create_all(engine)
    # start a session
    Session = sessionmaker(bind=engine)
    session = Session()
    # Create a new state and associate city
    new_state = State(name='California')
    new_city = City(name='San Francisco')
    new_state.cities.append(new_city)
    # Add to the sessions and commit
    session.add(new_state)
    session.commit()
    # close the session
    session.close()
