# Практика — Python

По одной задаче-заготовке на каждую тему из [`../../theory/python.md`](../../theory/python.md).
Формат: рабочий скелет с дырами (`raise NotImplemented`, `# todo`), условие — в докстринге,
самопроверка (`assert` / ожидаемый вывод) — внизу файла. Файлы пронумерованы в порядке теории.

## Задачи

| # | Файл | Тема теории |
|---|------|-------------|
| 01 | [`01_dataclasses.py`](01_dataclasses.py) | Новинки: dataclasses |
| 02 | [`02_match_case.py`](02_match_case.py) | Новинки: match/case (structural pattern matching) |
| 03 | [`03_typing.py`](03_typing.py) | Новинки: typing (TypedDict, Protocol, Literal, Self) |
| 04 | [`04_mutability.py`](04_mutability.py) | Мутабельность типов + опасность default-аргументов |
| 05 | [`05_hash.py`](05_hash.py) | `__hash__` / `__eq__`, хэшируемость |
| 06 | [`06_closures.py`](06_closures.py) | Область видимости (LEGB), замыкания, late binding |
| 07 | [`07_slots.py`](07_slots.py) | `__slots__`, экономия памяти |
| 08 | [`08_context_managers.py`](08_context_managers.py) | Контекстные менеджеры (sync + async) |
| 09 | [`09_new_vs_init.py`](09_new_vs_init.py) | `__new__` vs `__init__` (singleton) |
| 10 | [`10_mixins.py`](10_mixins.py) | Mixins, множественное наследование, MRO |
| 11 | [`11_access_modifiers.py`](11_access_modifiers.py) | Модификаторы доступа, name mangling |
| 12 | [`12_gil_primes.py`](12_gil_primes.py) | GIL: треды vs процессы (CPU-bound) |
| 13 | [`13_asyncio_io.py`](13_asyncio_io.py) | Asyncio (IO-bound, конкурентные ожидания) |
| 14 | [`14_pytest.py`](14_pytest.py) | Юниттесты и моки (pytest) |
| 15 | [`15_jwt.py`](15_jwt.py) | JWT + подпись, stateless auth |
| 16 | [`16_stateless.py`](16_stateless.py) | Stateless vs stateful, масштабирование |
| 17 | [`17_signals.py`](17_signals.py) | OOM killer и сигналы, graceful shutdown |

## Как заниматься

1. Открываешь файл по номеру, читаешь условие в докстринге.
2. Закрываешь дыры (`# todo`, `raise NotImplemented`).
3. Запускаешь файл (`python NN_*.py`) — внизу самопроверка. Для `03_typing.py`
   ещё и `mypy --strict`, для `14_pytest.py` — пишешь тесты и гоняешь `pytest`.
