# Python

Язык, его внутренности и типовые вопросы про Python на собесе python-backend.

## Что нового в Python за последние годы (~3.10+)
- Эволюция языка -> читаемость, производительность, типизация
- Почему старый код может выглядеть иначе
- Какие изменения реально влияют на ежедневную работу
- dataclasses
- typing: TypedDict, Protocol, Final, Literal, Self + typehints
- match/case (structural pattern matching)
- Улучшения asyncio
- PEP 563 / 649 (отложенные аннотации)
- CPython performance 3.11 - большой буст
- 3.14 и свобода от GIL


## Мутабельность типов

- [Mutable vs immutable](https://realpython.com/python-mutable-vs-immutable-types/)
- Почему это важно для API, кэшей, аргументов функций
- list, dict, set — mutable
- int, str, tuple, frozenset — immutable
- Поведение при передаче в функцию переменной того или иного типа
- Опасность default-аргументов функции (Почему `def f(x=[]): pass` это баг?)

## `__hash__`

- Контракты `__hash__` и `__eq__`
- Хэшируемость → ключи dict / set
- Почему mutable объекты нельзя хэшировать
- И что делать если всё таки хочется
- Почему `dataclass(frozen=True)` автоматически хэшируемый?


## Область видимости и замыкания

- LEGB rule
- Замыкания и late binding
- [nonlocal, global](https://realpython.com/python-closure/)


## `__slots__`

- Экономия памяти
- Запрет динамических атрибутов
- Trade-off’ы
- Когда уместно: Миллионы однотипных объектов / DTO / entity-like классы
- Минусы: нет `__dict__` и сложнее с наследованием


## Контекстные менеджеры

- Протокол __enter__ / __exit__
- Управление ресурсами
- contextlib
- Примеры: файлы, lock-и, транзакции, временные состояния
- Зачем contextlib.contextmanager, если есть классы?

## `__new__` vs `__init__`

- `__new__` создание объекта
- `__init__` инициализация
- Immutable типы, singleton, factory
- Когда реально нужен `__new__`


## [Mixins](https://realpython.com/inheritance-composition-python/#mixing-features-with-mixin-classes)

- Множественное наследование
- MRO
- Поведенческие примеси
- Правило: Mixin = маленький, без состояния, без `__init__`
- Почему mixin это не base class?


## Модификаторы доступа

- `_protected`, `__private`
- Name mangling
- Нет настоящего private
- Всё просто соглашения


## GIL

- [Что такое GIL и зачем он](https://habr.com/ru/articles/84629/)
- [Сборщик мусора и счётчик ссылок](https://habr.com/ru/articles/417215/)
- CPU-bound vs IO-bound задачи
- Threads vs multiprocessing
- Почему Python плохо масштабируется по CPU?

## [Asyncio](https://docs.python.org/3.14/howto/a-conceptual-overview-of-asyncio.html#a-conceptual-overview-of-asyncio)

- Event loop
- async / await
- кооперативная мультизадачность
- Где async вреден
- Sync inside async — блокировка loop
- Почему requests нельзя использовать в async коде?

Напиши три небольшие программки
1. стартует два процесса, в каждом расчёт факториала от 100
2. стартует два треда, в каждом расчёт факториала от 100
3. запускает две корутины, в каждой расчёт факториала от 100


## Юниттесты и моки

- Unit vs integration
- Mock vs stub vs fake
- Что не надо мокать


## [JWT + шифрование](https://www.jwt.io/introduction#what-is-json-web-token)

- JWT != шифрование
- Signing vs encryption
- Stateless auth
- HS256 vs RS256
- Где хранить секреты
- Expiration, rotation
- Почему нельзя хранить чувствительные данные в JWT?


## [Stateless vs Stateful](https://dev.to/tak089/stateful-vs-stateless-systems-5hml)

- Масштабирование
- Кэширование
- Failover
- Stateless API + Redis
- Stateful websocket

## OOM Killer и сигналы

- [Linux memory management & overcommit](https://habr.com/ru/articles/793232/)
- SIGTERM vs SIGKILL
- Graceful shutdown
- Почему приложение не ловит SIGKILL?
