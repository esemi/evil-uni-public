"""
Декоратор ретраев для нестабильных сетевых вызовов. Оборачивает функции,
которые ходят во внешние сервисы. Лежит в common/retry.py.
"""

import time


def retry(times=3, delay=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempt = 0
            while attempt < times:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempt += 1
                    print("Attempt {} failed: {}".format(attempt, e))
                    time.sleep(delay)
        return wrapper
    return decorator


@retry(times=5)
def fetch_data(client, url):
    return client.get(url)


@retry()
def charge_card(gateway, card, amount):
    return gateway.charge(card, amount)
