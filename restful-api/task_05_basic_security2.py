from flask import Flask
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity,
    get_jwt,
)
from flask import request, jsonify

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user",
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin",
    },
}

app = Flask(__name__)
auth = HTTPBasicAuth()


@auth.verify_password
def get_check_password(username, password):
    if username in users:
        user = users[username]
        if check_password_hash(user["password"], password):
            return username
    return None


@app.route("/basic-protected")
@auth.login_required
def get_basic_protected():
    return "Basic Auth : Access Granted"


app.config["JWT_SECRET_KEY"] = "une_cle_secrete_tres_forte"
jwt = JWTManager(app)


@app.route("/login", methods=["POST"])
def post_login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"msg": "Username and Password are required"}), 400

    user = users.get(username, None)
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(
        identity=username, additional_claims={"role": user["role"]}
    )
    return jsonify(access_token=access_token)


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def get_jwt_protected():
    current_user = get_jwt_identity()
    return jsonify(
        logged_in_as=current_user, message="JWT Auth: Access Granted"
        )


@app.route("/admin-only", methods=["GET"])
@jwt_required()
def get_admin_only():
    claims = get_jwt()
    if claims.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return jsonify(message="Admin Access: Granted")

jwt = JWTManager(app)

  @jwt.unauthorized_loader
  def handle_unauthorized_error(err):
      return jsonify({"error": "Missing or invalid token"}), 401

  @jwt.invalid_token_loader
  def handle_invalid_token_error(err):
      return jsonify({"error": "Invalid token"}), 401

  @jwt.expired_token_loader
  def handle_expired_token_error(err):
      return jsonify({"error": "Token has expired"}), 401

  @jwt.revoked_token_loader
  def handle_revoked_token_error(err):
      return jsonify({"error": "Token has been revoked"}), 401

  @jwt.needs_fresh_token_loader
  def handle_needs_fresh_token_error(err):
      return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run(debug=True)
