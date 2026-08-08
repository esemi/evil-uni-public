"""
Простой in-memory кэш с TTL для дорогих вычислений. Используется в паре мест
сервиса, чтобы не пересчитывать одно и то же. Лежит в common/cache.py.
"""

import time


class TTLCache:
    def __init__(self, ttl=60):
        self.ttl = ttl
        self.store = {}

    def get(self, key):
        if key in self.store:
            value, expires_at = self.store[key]
            if time.time() < expires_at:
                return value
        return None

    def set(self, key, value):
        self.store[key] = (value, time.time() + self.ttl)


cache = TTLCache()


def get_user_profile(user_id, db):
    cached = cache.get(user_id)
    if cached:
        return cached

    profile = db.query("SELECT * FROM profiles WHERE user_id = " + str(user_id))
    cache.set(user_id, profile)
    return profile
