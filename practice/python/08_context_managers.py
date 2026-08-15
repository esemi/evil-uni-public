"""
Тема: контекстные менеджеры (см. theory/python.md → «Контекстные менеджеры»).

Задача A. Реализуй Connector так, чтобы код ниже вывел:
```
open
Im here!
close
```

Задача B. Добавь async-протокол так, чтобы async-код ниже вывел:
```
async open
Im here!
async close
```

Подсказка: __enter__/__exit__ для sync, __aenter__/__aexit__ для async.
"""
import asyncio


class Connector:
    # todo
    pass


async def foo():
    async with Connector() as c:
        print('Im here!')


with Connector() as c:
    print('Im here!')

asyncio.run(foo())
