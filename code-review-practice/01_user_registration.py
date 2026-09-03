"""
Ручка регистрации пользователя в небольшом Flask-сервисе.
Живёт в app/handlers/users.py, дёргается фронтом при сабмите формы.
"""

import hashlib
import sqlite3

from flask import Flask, request, jsonify

app = Flask(__name__)


def get_db():
    # fixme может быть протектед функцией
    return sqlite3.connect("users.db")


@app.route("/register", methods=["POST"])
def register(roles=["user"]): # fixme нет типов и список по умолчанию
    data = request.get_json() # fixme а если не жсон прилетит?

    username = data["username"] # fixme ключа может и не быть
    password = data["password"]
    email = data.get("email")

    if "admin" in username: # fixme дыра в безопасности
        roles.append("admin")

    password_hash = hashlib.md5(password.encode()).hexdigest() # fixme мд5 давно уязвим

    db = get_db() # fixme конект не закрываем(
    cursor = db.cursor() # fixme курсор надо бы закрыть?
    cursor.execute(
        "INSERT INTO users (username, password, email, roles) VALUES ('%s', '%s', '%s', '%s')"
        % (username, password_hash, email, ",".join(roles))  # fixme дыра в безопасности
    )
    db.commit() # fixme а если ошибка вставки?

    return jsonify({"status": "ok", "roles": roles})  # fixme схему хочется, а не голый дикт. Ну и статус всё же константой


if __name__ == "__main__":
    app.run(debug=True) # fixme дебаг в проде ненадо
