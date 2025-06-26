#!/usr/bin/python3
"""
Script sécurisé contre les injections SQL.

Ce script se connecte à une base MySQL et affiche les lignes de la table
`states` dont le nom correspond exactement à un nom donné (sensible à la
casse), en triant les résultats par ID croissant.

Arguments :
    <username>      : nom d'utilisateur MySQL
    <password>      : mot de passe MySQL
    <database_name> : nom de la base de données
    <state_name>    : nom de l'état à rechercher (sensible à la casse)

Exemple d'utilisation :
    ./3-my_safe_filter_states.py root root hbtn_0e_0_usa 'Arizona'

Ce script utilise des requêtes paramétrées (%s) pour éviter les injections SQL.
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
    query = "SELECT * FROM states WHERE BINARY name = %s ORDER BY id ASC;"
    cursor.execute(query, (sys.argv[4],))
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
