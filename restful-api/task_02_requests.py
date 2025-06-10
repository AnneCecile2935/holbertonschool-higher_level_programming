#!/usr/bin/python3
"""
Module pour interagir avec l'API JSONPlaceholder.
Ce module contient deux fonctions principales :
- fetch_and_print_posts() : récupère et affiche les titres des posts.
- fetch_and_save_posts() : récupère les posts et les sauvegarde dans
un fichier CSV.
"""


import requests
import csv


def fetch_and_print_posts():
    """
    Récupère tous les posts depuis JSONPlaceholder et affiche les titres.

    Envoie une requête GET à l'API JSONPlaceholder pour obtenir la liste
    des posts.
    Affiche le code de statut de la réponse.
    Si la requête réussit (status code 200), affiche le titre de chaque post.
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status Code : {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])


def fetch_and_save_posts():
    """
    Récupère tous les posts depuis JSONPlaceholder et sauvegarde les données
      dans un fichier CSV.

    Envoie une requête GET à l'API JSONPlaceholder pour obtenir la liste
    des posts.
    Si la requête réussit (status code 200), crée une liste de dictionnaires
    contenant
    les clés 'id', 'title' et 'body' pour chaque post.
    Ensuite, écrit ces données dans un fichier CSV nommé 'posts.csv'
    avec les colonnes correspondantes.
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        data = [
            {"id": post['id'], "title": post['title'], "body": post['body']}
            for post in posts
        ]
        fieldnames = ['id', 'title', 'body']
        with open("posts.csv", 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        print("Data has been successfully written to posts.csv")
