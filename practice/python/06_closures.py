"""
Тема: замыкания, LEGB, late binding (см. theory/python.md → «Область видимости и замыкания»).

Задача A. Код ниже создаёт три функции, но все они возвращают 2 (late binding —
i захватывается по ссылке, а не по значению). Почини make_funcs так, чтобы
funcs[0]() == 0, funcs[1]() == 1, funcs[2]() == 2.

Задача B. Реализуй counter() — фабрику, возвращающую функцию-счётчик:
каждый её вызов возвращает следующее число (0, 1, 2, ...). Используй замыкание
и nonlocal, без глобальных переменных и без атрибутов функции.
"""


def make_funcs():
    funcs = []
    for i in range(3):
        funcs.append(lambda: i)  # todo: пофиксить late binding
    return funcs


def counter():
    raise NotImplemented


# A
fs = make_funcs()
assert [f() for f in fs] == [0, 1, 2], 'late binding: каждая функция должна помнить своё i'

# B
c = counter()
assert [c(), c(), c()] == [0, 1, 2]
assert counter()() == 0, 'новый счётчик независим'
print('ok')
