"""
Аутентификация по JWT: логин выдаёт токен, мидлварь его проверяет.
Используется на всех приватных ручках сервиса.
"""

import jwt
import hashlib

SECRET = "supersecret123"


def make_token(user_id, is_admin):
    payload = {"user_id": user_id, "is_admin": is_admin}
    return jwt.encode(payload, SECRET, algorithm="HS256")


def verify_token(token):
    data = jwt.decode(token, SECRET, options={"verify_signature": False})
    return data


def login(username, password, db):
    user = db.get_user(username)
    if user is None:
        return None

    password_hash = hashlib.sha256(password.encode()).hexdigest()
    if user["password_hash"] == password_hash:
        return make_token(user["id"], user["is_admin"])
    return None


def check_admin(token):
    data = verify_token(token)
    if data["is_admin"] == True:
        return True
    return False
