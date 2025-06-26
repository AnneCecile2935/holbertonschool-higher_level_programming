#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa.

The script takes 3 arguments:
    - mysql username
    - mysql password
    - database name

It connects to a MySQL server running on localhost at port 3306,
retrieves all cities along with their corresponding state names,
and displays them sorted by city id in ascending order.

Usage:
    ./4-cities_by_state.py <mysql_username> <mysql_password> <database_name>

Example:
    ./4-cities_by_state.py root root hbtn_0e_4_usa

Output format:
    (city_id, city_name, state_name)
"""
import sys
import MySQLdb

if __name__ == "__main__":

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3])

    cursor = db.cursor()
    query = (
        "SELECT cities.id, cities.name, states.name "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "ORDER BY cities.id;"
    )
    cursor.execute(query)
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
