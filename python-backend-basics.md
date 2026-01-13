Харды на питониста-разраба (обязательный минимум для резюме)
---
- Python: asyncio, FastApi, SQLAlchemy, Pytest
- Databases: PostgreSQL, NoSQL (на выбор, но лучше ClickHouse)
- Infra: Kubernetes, Docker, GCP (или AWS или яндекс.облако), Gitlab CI (или Github Actions)

Харды на питониста-разраба (опциональные для резюме)
---
- Python: Django, Django ORM, DRF, Starlette, Selenium
- Infra: Helm, Grafana, Splunk


Как работать с топиками ниже
---
- открываете бесплатную версию ChatGPT
- задаёте контекст промтом вида "я готовлюсь к собеседованию на python разработчика. У меня есть список тем для подготовки, я буду тебе их присылать. Отвечай на них краткой brief-выжимкой"
- каждый топик ниже отправляете в чат и читаете выжимку. Если непонятно - просите раскрыть более полно
- как правило все указанные темы он брифает без глюков (это не какие-то специфические малоизвестные особенности). Но если чувствуете что что-то не то - записываете в блокнотик и когда блокнот накопится - шлёте вопросы ментору.


Общие топики для собеседования бекенд-питониста
---

## Что нового в Python за последние годы (~3.8+)

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

```python
funcs = []
for i in range(3):
    funcs.append(lambda: i)
```
- Почему все функции вернут одно и то же?


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

## Выбор БД под задачу
- CAP theorem
- OLTP vs OLAP
- SQL vs NoSQL
- Почему не всё в PostgreSQL?


## Как делал миграции
- Управление схемой БД как кодом
- Zero-downtime миграции
- Rollback-и и обратная совместимость
- Миграции != deploy
- schema migration vs data migration
- Как вы деплоите миграции без простоя?


## Индексы
- Индекс = ускорение чтения за счёт кеша
- [B-tree по умолчанию](https://postgrespro.ru/docs/postgrespro/15/indexes)
- read-heavy vs write-heavy
- composite indexes
- covering index
- Индексы вредят при write-heavy нагрузке и при низкой селективности
- EXPLAIN (ANALYZE)
- Почему индекс есть, а запрос медленный?


## Дедлоки — что это и как готовить
- Взаимная блокировка транзакций
- Lock graph
- Deadlock detection
- Причины: разный порядок обновления строк | длинные транзакции
- SELECT ... FOR UPDATE
- единый порядок захвата ресурсов
- короткие транзакции
- retry

## SLA / SLO — что это
- Язык бизнеса
- Измеряемые цели
- Error budget
- SLA — договорное обязательство
- SLO — внутренняя цель
- SLI — метрика
- Почему нельзя делать SLA 100?


## ACK / NOACK в очередях
- At-least-once delivery
- Exactly-once — почти миф
- Consumer responsibility
- ACK → сообщение обработано
- NOACK / timeout → requeue
- Типовые решения: RabbitMQ, SQS, Kafka
- Что будет если consumer упал после обработки, но до ACK?


## Минимальный CI/CD для веб-API
- CI != CD
- Цель — быстро и безопасно доставить код в прод
- Минимум != примитив
- Минимальный pipeline CI: Checkout -> Install deps -> Linters -> Tests -> Build -> Push image
- Минимальный pipeline CD: Deploy (rolling / blue-green) -> Smoke check -> Rollback при ошибке

## Линтеры — конкретика и причины выбора
- Linters != форматирование
- Автоматизация code review
- Python stack (типовой senior-набор): ruff — быстрый all-in-one, black — форматирование, mypy — типы, bandit — security, vulture - stale code, WPS (harder than ruff)


## [Dockerfile: Один RUN или много](https://docs.docker.com/build/concepts/dockerfile/)
- Docker layers
- Cache invalidation
- один RUN: меньше слоёв & меньше образ
- несколько RUN: разные cache boundaries & dev vs prod stages


## Оптимизация времени сборки Docker
- правильный порядок инструкций
- multi-stage builds
- .dockerignore
- кеш pip / poetry
- buildkit
- Почему изменение кода ломает кэш зависимостей?

## [Security Docker build](https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html)
- Image != VM
- Supply chain attacks

### Практики:
- non-root user
- минимальный base image (slim, distroless)
- pinned versions
- secrets != ARG
- scan images


## Сущности Kubernetes для веб-API в проде
- Deployment
- Service
- ConfigMap
- Secret
- Ingress
- HPA
- Deployment — управляет репликами
- Service — стабильная точка доступа внутри кластера
- Ingress — вход снаружи кластера
- Можно ли жить без Ingress? (конечно)

## [HPA](https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/)
- scale по CPU / memory / custom metrics
- Какие проблемы HPA не решит?

## [Affinity / Anti-Affinity](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/)
- контроль размещения pod-ов по нодам
- fault domains
- не класть все pod’ы на один node
- spread по зонам
- Зачем anti-affinity если есть HPA?