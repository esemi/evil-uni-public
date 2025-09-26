# -----------------------------------------
"""
Сделай так, чтобы код ниже вывел:
```
open
Im here!
close
```

"""
import asyncio
import time


class Connector:
    pass

with Connector as c:
    print(c)


"""
Сделай так, чтобы код ниже вывел:
```
async open
Im here!
async close
```

"""
async def foo():
    async with Connector as c:
        print(c)
asyncio.run(foo())

# -----------------------------------------
"""
Задача на параллельное вычисление простых чисел (процессы против тредов)

Дано: функция для вычисления простых чисел в диапазоне.
Задача: попробовать ускорить вычисления с помощью потоков (1) и с помощью процессов (2)
"""

import math
import multiprocessing as mp
import threading


def _is_prime(n):
    """Проверка числа на простоту"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def find_primes_single(max_num: int) -> list[int]:
    """Найти простые числа в один процесс для сравнения"""
    return [
        i
        for i in range(max_num + 1)
        if _is_prime(i)
    ]


def find_primes_threading(max_num: int) -> list[int]:
    """Найти простые числа используя мультитрединг"""
    raise NotImplemented


def find_primes_multiprocess(max_num: int) -> list[int]:
    """Найти простые числа используя мультипроцессинг"""
    num_processes = mp.cpu_count()
    raise NotImplemented


# Тестирование
MAX_NUM = 1000000
print('benchmark', find_primes_single(MAX_NUM))
print('processes', find_primes_multiprocess(MAX_NUM))
print('threads', find_primes_threading(MAX_NUM))


# -----------------------------------------
"""
Задача на долгие ожидания (процессы против асинкио)

Дано: функция эмулирующая сбор данных с сайта в синхронном варианте.
Задача: попробовать ускорить вычисления переписав её в asyncio-совместимом виде.
"""

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
    ("dev.to", 10.8)
]
print('benchmark', load_responses_sync(WEBSITES))
print('processes', load_responses_async(WEBSITES))

# -----------------------------------------