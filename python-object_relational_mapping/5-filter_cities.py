#!/usr/bin/python3
"""
Script sécurisé contre les injections SQL.

Ce script se connecte à une base MySQL et affiche les noms des villes
de la table `cities` appartenant à un état donné (sensible à la casse),
triés par ID croissant.

Les noms des villes sont affichés sur une seule ligne, séparés par des
virgules.

Arguments :
    <username>      : nom d'utilisateur MySQL
    <password>      : mot de passe MySQL
    <database_name> : nom de la base de données
    <state_name>    : nom exact de l'état à rechercher (sensible à la casse)

Exemple d'utilisation :
    ./3-my_safe_filter_states.py root root hbtn_0e_4_usa 'Arizona'

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
    query = (
        "SELECT cities.name "
        "FROM cities "
        "JOIN states "
        "ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC;"
        )
    cursor.execute(query, (sys.argv[4],))
    rows = cursor.fetchall()

    city_names = [row[0] for row in rows]
    print(", ".join(city_names))

    cursor.close()
    db.close()
