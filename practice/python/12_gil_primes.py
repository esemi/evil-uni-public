"""
Тема: GIL, треды vs процессы (см. theory/python.md → «GIL»).

Дано: функция вычисления простых чисел в диапазоне (CPU-bound).
Задача: ускорить вычисления с помощью потоков (find_primes_threading)
и с помощью процессов (find_primes_multiprocess).

Замерь время каждого варианта и объясни себе результат: почему threading
на CPU-bound не даёт ускорения, а multiprocessing даёт?
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
