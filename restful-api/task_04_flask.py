#!/usr/bin/python3

from flask import Flask
from flask import jsonify
from flask import request
from markupsafe import escape
app = Flask(__name__)

users = {
    "jane": {
        "username": "jane",
        "name": "Jane",
        "age": 28,
        "city": "Los Angeles"
        },
    "john": {
        "username": "john",
        "name": "John",
        "age": 30,
        "city": "New York"
        }
}


@app.route('/')
def home():
    return 'Welcome to the Flask API!'


@app.route('/data')
def get_users():
    return jsonify(list(users.keys()))


@app.route('/status')
def get_status():
    return 'OK'


@app.route('/users/<username>')
def get_user(username):
    requete_username = escape(username)
    requete_user = {"username": requete_username}
    if requete_username in users:
        requete_user.update(
            {key: value for key, value in users[requete_username].items()}
        )
        return jsonify(requete_user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def post_add_user():
    data = request.get_json()
    if not data or 'username' not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data['username']
    if username in users:
        return jsonify({"error": "User already exists"}), 409

    allowed_fields = {'name', 'age', 'city'}
    user_info = {'username' :username}
    for key in allowed_fields:
        if key in data:
            user_info[key]= data[key]
    users[username] = user_info

    return jsonify({
        "message": "User added", "user": user_info}), 201


if __name__ == '__main__':
    app.run(debug=True)
