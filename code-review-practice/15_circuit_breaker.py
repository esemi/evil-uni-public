"""
Клиент к внешнему сервису с «предохранителем» (circuit breaker) и ретраями.
Оборачивает вызовы к flaky-зависимости, чтобы не долбить упавший сервис.
"""

import time

import requests

FAILURES = 0
OPEN_UNTIL = 0


def call_service(payload):
    global FAILURES, OPEN_UNTIL

    if time.time() < OPEN_UNTIL:
        return None

    for attempt in range(5):
        try:
            resp = requests.post("http://service.internal/api", json=payload)
            if resp.status_code == 200:
                FAILURES = 0
                return resp.json()
        except Exception:
            FAILURES += 1

        time.sleep(1)

    if FAILURES > 3:
        OPEN_UNTIL = time.time() + 30

    return None


def charge_and_call(payload):
    return call_service(payload)
