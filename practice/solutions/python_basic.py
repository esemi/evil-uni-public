import asyncio
import os


class Connector:
    pass

class SyncConnector(Connector):

    def __enter__(self):
        print("open")
        return "I'm here!"

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            raise exc_type(exc_val)
        print("close")


with SyncConnector() as c:
    print(c)

class AsyncConnector(Connector):

    async def __aenter__(self):
        print("async open")

        return "Im here!"

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            raise exc_type(exc_val)

        print("async close")

async def foo():
    async with AsyncConnector() as c:
        print(c)

asyncio.run(foo())

# -----------------------------------------
"""
Задача на параллельное вычисление простых чисел (процессы против тредов)

Дано: функция для вычисления простых чисел в диапазоне.
Задача: попробовать ускорить вычисления с помощью потоков (1) и с помощью процессов (2)
"""


import math
import time
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

def _find_primes_single(max_num: int) -> list[int]:
    """Найти простые числа в один процесс для сравнения"""
    return [
        i
        for i in range(max_num + 1)
        if _is_prime(i)
    ]

def _find_primes_in_range(start: int, max_num: int) -> list[int]:
    return [
        i
        for i in range(start, max_num + 1)
        if _is_prime(i)
    ]




def find_primes_single(max_num: int) -> float:
    start = time.time()

    _find_primes_single(max_num)

    return time.time() - start


def find_primes_threading(max_num: int) -> list[int]:
    """Найти простые числа используя мультитрединг"""
    num_threads = os.cpu_count()
    threads = []

    batch_size = max_num // num_threads

    start = time.time()
    for step in range(0, max_num, batch_size):
        t = threading.Thread(target=_find_primes_in_range, args=(step, step+batch_size))
        threads.append(t)
        t.start()


    for t in threads:
        t.join()

    return time.time() - start


def find_primes_multiprocess(max_num: int) -> list[int]:
    """Найти простые числа используя мультипроцессинг"""
    num_processes = mp.cpu_count()
    batch_size = max_num // num_processes
    pcs = []

    start = time.time()
    for step in range(0, max_num, batch_size):
        p = mp.Process(target=_find_primes_in_range, args=(step, step+batch_size))
        pcs.append(p)
        p.start()

    for p in pcs:
        p.join()

    return time.time() - start




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
    start = time.time()
    for site, timeout in sites:
        time.sleep(timeout)  # fake wait for response
        responses.append(f'{site} OK')
    return time.time() - start

async def _fetch_async(site: str, delay: float) -> str:
    await asyncio.sleep(delay)
    return f'{site} OK'

async def load_responses_async(sites: list[tuple[str, float]]) -> list[str]:
    start = time.time()

    tasks = [_fetch_async(site, delay) for site, delay in sites]

    await asyncio.gather(*tasks)

    return time.time() - start


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
print('sync', load_responses_sync(WEBSITES))
print('async', asyncio.run(load_responses_async(WEBSITES)))

# -----------------------------------------

