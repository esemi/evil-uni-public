"""
Тема: typing — TypedDict, Protocol, Literal, Self (см. theory/python.md → «Что нового в Python»).

Задача — расставить типы так, чтобы mypy (strict) был доволен, а рантайм работал.

1. UserDict — TypedDict с полями id: int, name: str, role: Literal['admin', 'user'].
2. SupportsPing — Protocol с методом ping(self) -> str (structural typing).
3. QueryBuilder.where(...) должен возвращать Self (чтобы чейнинг типизировался
   корректно и в наследниках).

Проверь себя: `mypy --strict 03_typing.py` без ошибок.
"""

from typing import TypedDict, Protocol, Literal, Self


class UserDict(TypedDict):
    ...  # todo: id, name, role


class SupportsPing(Protocol):
    ...  # todo: ping(self) -> str


class QueryBuilder:
    def __init__(self) -> None:
        self._filters: list[str] = []

    def where(self, expr: str):  # todo: аннотировать возврат как Self
        self._filters.append(expr)
        return self


def greet(u: UserDict) -> str:
    return f"{u['name']} ({u['role']})"


def ping_all(items: list[SupportsPing]) -> list[str]:
    return [item.ping() for item in items]


if __name__ == '__main__':
    print(greet({'id': 1, 'name': 'Alex', 'role': 'admin'}))
    print(QueryBuilder().where('a = 1').where('b = 2')._filters)
