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
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name_searched = sys.argv[4]
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database_name
        )
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC;".format(
        state_name_searched)
    cursor.execute(query)
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
