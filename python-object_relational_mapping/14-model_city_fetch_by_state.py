#!/usr/bin/python3
"""
Lists all City objects from the database hbtn_0e_14_usa
and displays them as <state name>: (<city id>) <city name>

Usage:
    ./14-model_city_fetch_by_state.py <mysql_username> <mysql_password>
    <database_name>

This script connects to a MySQL server running on localhost at port 3306,
performs an inner join between the cities and states tables using SQLAlchemy,
and displays the results ordered by City.id in ascending order.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

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

    result = (
        session.query(State.name, City.id, City.name)
        .join(City, City.state_id == State.id)
        .order_by(City.id).all()
    )
    for state_name, city_id, city_name in result:
        print(f"{state_name}: ({city_id}) {city_name}")

    session.close()
