#!/usr/bin/python3
"""
Se connecte à une base MySQL et affiche les entrées de la table `states`.

Le script prend en arguments : nom d'utilisateur, mot de passe, nom de la base.

Il affiche les états dont le nom commence par 'N', triés par `id` croissant.

Usage:
    ./0-select_states.py <username> <password> <database_name>

Exemple:
    ./0-select_states.py root mypassword hbtn_0e_0_usa
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
    cursor.execute(
        "SELECT id, name "
        "FROM states "
        "WHERE UPPER(name) "
        "LIKE 'N%' "
        "ORDER BY id ASC;")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
