Общие топики для подготовки к собеседованию на python-backend
---

## Как работать с топиками ниже
- открываете бесплатную версию ChatGPT
- задаёте контекст промтом вида "я готовлюсь к собеседованию на python разработчика. У меня есть список тем для подготовки, я буду тебе их присылать. Отвечай на них краткой brief-выжимкой"
- каждый топик ниже отправляете в чат и читаете выжимку. Если непонятно - просите раскрыть более полно
- как правило все указанные темы он брифает без глюков (это не какие-то специфические малоизвестные особенности). Но если чувствуете что что-то не то - записываете в блокнотик и когда блокнот накопится - шлёте вопросы ментору.


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

```python
from collections import defaultdict

class Foo(dict):
    name: str

alex = Foo()
alex.name = 'Alex'

mar = Foo()
mar.name = 'Mar'

counter: dict[Foo, int] = defaultdict(int)

counter[alex] += 1
counter[mar] += 1

print(counter)
```


## Область видимости и замыкания

- LEGB rule
- Замыкания и late binding
- [nonlocal, global](https://realpython.com/python-closure/)

```python
funcs = [
    lambda: i
    for i in range(3)
]
for f in funcs:
    print(f())
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

## Выбор БД под задачу
- https://system-design.space/chapter/database-selection-framework
- CAP theorem
- OLTP vs OLAP
- SQL vs NoSQL
- Почему не всё в PostgreSQL?
- ACID + уровни изоляции транзакций
- нормализация vs денормализация
- N+1 проблема


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
- Python stack (типовой senior-набор): ruff — быстрый all-in-one, black — форматирование, mypy — типы, bandit — security, vulture - stale code, WPS (суровей чем ruff)


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
Ставим миникуб и пишем хеловорд вебапишку на fastapi.
Тебе понадобится деплоймент, сервис, ингрес и конфигмап
Остальное можно просто почитать что и зачем.
https://minikube.sigs.k8s.io/docs/start/?arch=%2Flinux%2Fx86-64%2Fstable%2Fbinary+download

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

## Helm
- что происходит при helm upgrade и какие риски в проде?
- возможный downtime
- как организовать values для dev / stage / prod?
- в чём основные проблемы Helm в больших проектах?

## Terraform
- Зачем нужен
- Что такое Terraform state и что будет, если его потерять?
- Чем Terraform отличается от Helm по ответственности?

## Работа с сетью
- HTTP: методы, коды, идемпотентность
- REST vs RPC
- как работает TCP (в общих чертах)
- keep-alive, timeouts


## AWS — минимум для python-backend

### Как учить
- Завести free-tier аккаунт, поднять руками EC2 + S3 + RDS, чтобы пощупать
- Не лезть в 200+ сервисов — учить только то, что реально встречается в проде у обычного web-сервиса
- На собесе обычно спрашивают «какие сервисы использовал и зачем» + 1-2 глубоких вопроса. Цель — уметь объяснить trade-off’ы, а не зазубрить лимиты


## [Модель ответственности и регионы](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/global-infrastructure.html)
- Region vs Availability Zone vs Edge location
- Shared responsibility model: за что отвечает AWS, за что ты
- Почему мультизональный деплой ≠ мультирегиональный
- Latency и стоимость cross-AZ трафика


## [IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html)
- User vs Role vs Policy
- Принцип least privilege
- Assume role, STS, временные креды
- IAM Role для EC2/ECS/Lambda — почему не нужны access keys внутри инстанса
- Где НЕЛЬЗЯ хранить AWS access keys (привет, git)
- Почему `*:*` в policy — это плохо


## Compute: EC2 / ECS / Fargate / Lambda
- EC2 — виртуалка, ты сам ставишь ОС и софт
- ECS — оркестрация контейнеров (аналог Kubernetes от AWS)
- Fargate — serverless контейнеры (без управления нодами)
- Lambda — serverless functions, до 15 минут, pay-per-invocation
- Когда выбирать что:
  - постоянная нагрузка → EC2 / ECS на EC2
  - переменная нагрузка → Fargate
  - редкие события, event-driven → Lambda
- Cold start у Lambda — почему это боль для latency-sensitive API
- Почему long-running задачи нельзя в Lambda


## [S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)
- Object storage, не файловая система
- Bucket / key / versioning
- Storage classes: Standard / IA / Glacier — trade-off цена vs скорость
- Pre-signed URL — отдать клиенту прямой доступ без проксирования через бекенд
- Eventual consistency была раньше, теперь strong consistency
- Lifecycle policy — автоудаление/архивация
- Почему S3 нельзя использовать как файловую систему для random write


## RDS / Aurora / DynamoDB
- RDS — managed PostgreSQL/MySQL/etc. AWS делает бэкапы, патчи, failover
- Aurora — AWS-овый форк MySQL/Postgres с разделённым storage, быстрее и дороже
- DynamoDB — managed NoSQL key-value / document, single-digit ms latency
- Когда DynamoDB, а когда RDS:
  - известный access pattern, нужен горизонтальный scale → DynamoDB
  - сложные join-ы, аналитика, транзакции → RDS
- Read replicas — отдельный endpoint, eventual consistency
- Multi-AZ deployment — это про HA, не про scale
- Почему `SELECT *` в DynamoDB — это антипаттерн


## Очереди и стриминг: SQS / SNS / Kinesis / EventBridge
- SQS — pull-based очередь, at-least-once delivery
- SNS — pub/sub, push-based, fan-out
- SQS + SNS вместе — типовой fan-out паттерн (одно событие → много consumer’ов)
- Kinesis — стриминг данных, аналог Kafka, ordered shards
- EventBridge — event bus с фильтрацией, удобно для микросервисов
- Visibility timeout в SQS — почему он критичен (см. ACK/NOACK выше)
- Dead-letter queue — куда уходят сообщения, которые не смогли обработать
- Когда Kinesis, а когда SQS?


## VPC и сеть
- VPC = твоя виртуальная сеть в AWS
- Subnet: public vs private — где может торчать наружу
- Security Group (stateful) vs NACL (stateless)
- NAT Gateway — чтобы private subnet ходил в интернет
- VPC Endpoint — доступ к AWS-сервисам не через public интернет
- Почему RDS нельзя класть в public subnet


## Load balancing: ALB / NLB
- ALB — L7, HTTP/HTTPS, path/host routing
- NLB — L4, TCP/UDP, миллионы коннектов, низкая latency
- ALB умеет terminate TLS, sticky sessions, health checks
- Target group — куда роутить (EC2/ECS task/IP/Lambda)


## Observability: CloudWatch / X-Ray
- CloudWatch Logs — куда пишут все managed-сервисы и lambda по дефолту
- CloudWatch Metrics — стандартные + custom
- CloudWatch Alarms → SNS → PagerDuty/Slack
- X-Ray — distributed tracing (аналог Jaeger)
- Log Insights — query язык для логов
- Почему писать `print()` в Lambda — это нормально (и куда оно попадает)


## Деплой / IaC: CloudFormation / CDK / Terraform
- CloudFormation — родной IaC от AWS, YAML/JSON
- CDK — пишешь IaC на python/typescript, компилится в CloudFormation
- Terraform — multi-cloud, state хранится отдельно
- Terraform vs CloudFormation — про state и про vendor lock-in
- Stack vs Stack Set
- Drift — когда руками поменяли то, что управляется кодом


## Secrets: Secrets Manager / Parameter Store / KMS
- Secrets Manager — секреты с автоматической ротацией (дороже)
- SSM Parameter Store — параметры конфигурации + SecureString (дешевле)
- KMS — управление ключами шифрования, envelope encryption
- Почему секреты не хранят в env-переменных в plain text
- IAM role + Secrets Manager — стандартный паттерн доступа к БД из приложения


## Стоимость и типовые грабли
- Cross-AZ traffic — стоит денег, легко набежать
- NAT Gateway — дорогой, особенно по трафику
- Не выключенный EC2 / RDS — счёт месяцами
- S3 egress — выгрузка из AWS платная
- CloudWatch Logs retention по дефолту — бесконечно (= деньги)
- Reserved Instances vs Savings Plans vs On-Demand vs Spot
- Почему билл может неожиданно вырасти в 10 раз?


## Что почитать
- [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/) — официальный гид по best practices, 6 столпов
- [The Open Guide to AWS](https://github.com/open-guides/og-aws) — community-driven, без маркетингового мусора
- [AWS in Plain English](https://expeditedsecurity.com/aws-in-plain-english/) — что какой сервис делает на пальцах


## Практика на один день
1. Поднять EC2 в public subnet, зайти по SSH, поставить nginx, открыть наружу через Security Group
2. Создать S3 bucket, залить файл через CLI, сгенерировать pre-signed URL
3. Создать RDS PostgreSQL в private subnet, подключиться к нему с EC2
4. Написать lambda на python, которая по триггеру из S3 (новый файл) пишет запись в DynamoDB
5. Найти всё созданное в Cost Explorer и УДАЛИТЬ, пока не натикало на тысячи денег


## Лайвкод
- [нарешиваем минимум на литкоде](https://leetcode.com/studyplan/leetcode-75/)