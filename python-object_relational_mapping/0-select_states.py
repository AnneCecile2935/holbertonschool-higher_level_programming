#!/usr/bin/python3
"""
Script qui se connecte à une base de données MySQL et affiche toutes
les entrées
de la table `states` triées par ordre croissant selon leur `id`.

Le script prend en arguments la connexion MySQL (nom d'utilisateur,
mot de passe,
nom de la base de données) et affiche chaque ligne de la table `states`.

Usage:
    ./0-select_states.py <username> <password> <database_name>

Exemple:
    ./0-select_states.py root mypassword hbtn_0e_0_usa
"""
import sys
import MySQLdb
if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
        )
    print(username, password, db_name)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC;")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
