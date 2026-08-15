"""
Тема: JWT, stateless auth (см. theory/python.md → «JWT + шифрование»).

Задача: реализовать выпуск и проверку JWT-токена (HS256) руками, чтобы понять,
что подпись != шифрование, а payload читается кем угодно.

- issue_token(user_id, secret, ttl_seconds): вернуть подписанный JWT с полями
  sub=user_id и exp=now+ttl.
- verify_token(token, secret): вернуть payload, если подпись валидна и токен не
  протух; иначе бросить ValueError.

Разрешено взять библиотеку PyJWT (pip install pyjwt) — тогда сфокусируйся на
корректной обработке exp и невалидной подписи. Ответь себе: почему в payload
нельзя класть чувствительные данные и когда брать RS256 вместо HS256.
"""

import jwt  # PyJWT


def issue_token(user_id: int, secret: str, ttl_seconds: int = 3600) -> str:
    raise NotImplemented


def verify_token(token: str, secret: str) -> dict:
    raise NotImplemented


if __name__ == '__main__':
    secret = 'super-secret'
    token = issue_token(42, secret, ttl_seconds=60)
    print('token:', token)

    payload = verify_token(token, secret)
    assert payload['sub'] == 42

    try:
        verify_token(token, 'wrong-secret')
    except ValueError:
        print('ok: невалидная подпись отклонена')
    else:
        raise AssertionError('подпись с чужим секретом должна отклоняться')
