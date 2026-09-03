"""
Ручка регистрации пользователя в небольшом Flask-сервисе.
Живёт в app/handlers/users.py, дёргается фронтом при сабмите формы.
"""

import hashlib
import sqlite3

from flask import Flask, request, jsonify

app = Flask(__name__)


def get_db():
    return sqlite3.connect("users.db")


@app.route("/register", methods=["POST"])
def register(roles=["user"]):
    data = request.get_json()

    username = data["username"]
    password = data["password"]
    email = data.get("email")

    if "admin" in username:
        roles.append("admin")

    password_hash = hashlib.md5(password.encode()).hexdigest()

    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO users (username, password, email, roles) VALUES ('%s', '%s', '%s', '%s')"
        % (username, password_hash, email, ",".join(roles))
    )
    db.commit()

    return jsonify({"status": "ok", "roles": roles})


if __name__ == "__main__":
    app.run(debug=True)
