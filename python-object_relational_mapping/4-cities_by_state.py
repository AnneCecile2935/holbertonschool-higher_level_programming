#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa, sorted by cities.id ASC.

Usage:
    ./4-cities_by_state.py <mysql_username> <mysql_password> <database_name>
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()
    query = (
        "SELECT cities.id, cities.name, states.name "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "ORDER BY cities.id ASC"
    )
    cursor.execute(query)
    
    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()
