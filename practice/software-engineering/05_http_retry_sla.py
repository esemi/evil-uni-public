"""
Тема: HTTP-идемпотентность + retry, SLA/SLO/error budget
(см. theory/software-engineering.md → «Работа с сетью», «SLA / SLO»).

Задача A. request_with_retry(method, call): ретраить вызов при сбое, НО безопасно:
- ретраить только ИДЕМПОТЕНТНЫЕ методы (GET, PUT, DELETE, HEAD, OPTIONS);
  для неидемпотентных (POST, PATCH) — не ретраить (риск двойного эффекта);
- ретраить только на временных ошибках: коды 429, 500, 502, 503, 504 или
  TransientError; на 4xx (кроме 429) не ретраить — это не починится повтором;
- максимум MAX_RETRIES попыток, экспоненциальный backoff (см. _sleep — его мокнём).
call() возвращает код ответа или бросает TransientError.

Задача B. error_budget(slo: float, total: int) -> int: сколько запросов В МЕСЯЦ
можно "потерять" (ошибки), не нарушив SLO. Напр. SLO 99.9% при 1_000_000 запросов
-> бюджет 1000. Подумай: почему SLA=100% не делают.
"""

MAX_RETRIES = 3
IDEMPOTENT = {'GET', 'PUT', 'DELETE', 'HEAD', 'OPTIONS'}
RETRIABLE_CODES = {429, 500, 502, 503, 504}


class TransientError(Exception):
    pass


def _sleep(attempt: int) -> None:
    """Backoff. В тестах мокается, чтобы не ждать по-настоящему."""
    import time
    time.sleep(2 ** attempt * 0.1)


def request_with_retry(method: str, call) -> int:
    """call() -> int (HTTP-код) либо бросает TransientError. Вернуть финальный код."""
    raise NotImplemented


def error_budget(slo: float, total: int) -> int:
    """slo — доля успеха (0.999 = 99.9%). Вернуть допустимое число ошибок."""
    raise NotImplemented


if __name__ == '__main__':
    # A: временный сбой на GET -> ретраим и добиваем успех
    attempts = {'n': 0}
    def flaky_get():
        attempts['n'] += 1
        if attempts['n'] < 3:
            return 503
        return 200
    assert request_with_retry('GET', flaky_get) == 200
    assert attempts['n'] == 3

    # A: POST не ретраим даже на 503 (неидемпотентно)
    post_calls = {'n': 0}
    def flaky_post():
        post_calls['n'] += 1
        return 503
    assert request_with_retry('POST', flaky_post) == 503
    assert post_calls['n'] == 1, 'POST не должен ретраиться'

    # B: error budget
    assert error_budget(0.999, 1_000_000) == 1000
    print('ok')
