#!/usr/bin/python3
"""
Script that takes in arguments and displays all values in states table
where name matches the argument.

Usage:
    ./2-my_filter_states.py <username> <password> <database_name> <state_name>

Example:
    ./2-my_filter_states.py root root hbtn_0e_0_usa 'Arizona'
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
    query = "SELECT * FROM states WHERE BINARY name = '{}' ".format(
        sys.argv[4])
    cursor.execute(query)
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
