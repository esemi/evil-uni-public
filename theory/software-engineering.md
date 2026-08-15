# Программная инженерия

Backend-инженерия вокруг Python: БД и данные, надёжность, очереди, CI/CD, Docker, Kubernetes, сеть.

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


## Работа с сетью
- HTTP: методы, коды, идемпотентность
- REST vs RPC
- как работает TCP (в общих чертах)
- keep-alive, timeouts


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
