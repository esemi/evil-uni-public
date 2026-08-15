"""
Тема: asyncio, IO-bound (см. theory/python.md → «Asyncio»).

Дано: функция, эмулирующая сбор данных с сайтов в синхронном варианте
(ожидание ответа = time.sleep).
Задача: переписать load_responses_async так, чтобы все ожидания шли
конкурентно через asyncio, а суммарное время ≈ времени самого долгого сайта,
а не сумме всех.

Подумай: почему здесь нельзя использовать time.sleep внутри корутины
и почему requests не подходит для async-кода?
"""

import asyncio
import time


def load_responses_sync(sites: list[tuple[str, float]]) -> list[str]:
    responses = []
    for site, timeout in sites:
        time.sleep(timeout)  # fake wait for response
        responses.append(f'{site} OK')
    return responses


async def load_responses_async(sites: list[tuple[str, float]]) -> list[str]:
    raise NotImplemented


# Тестирование
WEBSITES = [
    ("google.com", 1.5),
    ("github.com", 5.2),
    ("stackoverflow.com", 10.8),
    ("python.org", 8.5),
    ("wikipedia.org", 10.0),
    ("reddit.com", 5.0),
    ("medium.com", 4.5),
    ("dev.to", 10.8),
]
print('benchmark', load_responses_sync(WEBSITES))
print('async', asyncio.run(load_responses_async(WEBSITES)))
