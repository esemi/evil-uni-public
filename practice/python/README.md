# Практика — Python

Задачи на язык и его внутренности. Зеркалит теорию из [`../../theory/python.md`](../../theory/python.md).
Формат: рабочий скелет с дырами (`raise NotImplemented`, `# todo`), условие — в докстринге,
самопроверка — внизу файла.

## Задачи

| Файл | Задачи | Темы теории |
|------|--------|-------------|
| [`python_basic.py`](python_basic.py) | Контекстные менеджеры (sync/async), простые числа через треды vs процессы, долгие ожидания через asyncio, `__hash__` для наследника `dict`, `__slots__` для экономии памяти. | контекстные менеджеры, GIL, asyncio, `__hash__`, `__slots__` |
| [`pytest.py`](pytest.py) | Функции `example_*` (в т.ч. async-запрос по HTTP и функция с `time.sleep`) — надо написать на них тесты на `pytest`, включая моки. | юниттесты и моки |

## Ещё нет задач (из теории)

Темы из [`python.md`](../../theory/python.md), под которые пока нет заготовок:
`__new__` vs `__init__`, mixins и MRO, замыкания и late binding, модификаторы доступа
(name mangling), JWT / stateless auth, OOM killer и сигналы (SIGTERM/SIGKILL, graceful shutdown),
новинки языка (dataclasses, `match/case`, typing).
