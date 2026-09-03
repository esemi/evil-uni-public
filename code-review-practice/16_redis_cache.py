"""
Кэш «cache-aside» поверх Redis: читаем из кэша, при промахе идём в БД и кладём обратно.
Плюс инвалидация при обновлении. Дёргается из горячих ручек каталога.
"""

import pickle

import redis

r = redis.Redis(host="localhost", port=6379)


def get_product(product_id, db):
    key = "product:" + str(product_id)
    cached = r.get(key)
    if cached:
        return pickle.loads(cached)

    product = db.get_product(product_id)
    r.set(key, pickle.dumps(product))
    return product


def update_product(product_id, data, db):
    db.update_product(product_id, data)
    r.delete("product:" + str(product_id))


def clear_all_products():
    for key in r.keys("product:*"):
        r.delete(key)
