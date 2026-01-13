Топики для "архитектурного мяса"
---

## Нефункциональные требования (NFR)
- latency / throughput
- SLA / SLO / availability
- scalability (вертикальная vs горизонтальная)
- consistency vs availability (CAP)
- cost awareness
- security & compliance


## API & контракты
- REST vs GraphQL vs gRPC
- версионирование API
- идемпотентность
- пагинация (offset vs cursor)
- rate limiting / throttling
- backward compatibility
 

## Кэширование
- где кэшировать: CDN / reverse proxy / app / DB
- write-through / write-back / cache-aside
- инвалидация кэша
- Redis vs Memcached


## Асинхронщина и фоновые задачи
- когда синхрон, когда async
- очереди vs event streaming
- exactly-once / at-least-once
- дедупликация задач
- идемпотентные воркеры


## Надёжность и отказоустойчивость
- retries с backoff + jitter
- circuit breaker
- timeouts
- graceful degradation
- bulkheads


## Observability
- structured logs
- метрики (RED / USE)
- трассировка
- алерты: когда и на что


## Миграции и эволюция системы
- zero-downtime migrations
- feature flags
- blue/green vs canary
- как менять схему БД без даунтайма


## Архитектурные подходы (DDD, TDD и т.п.)
- не «что это», а когда применять
- DDD != везде

1. Когда DDD — оверхед?
2. Как bounded context ложится на микросервисы?
3. Что делать, если бизнес-логика простая?
4. Как TDD влияет на архитектуру?

## Базы данных
- OLTP vs OLAP
- read-heavy vs write-heavy
- когда индексы вредят
- composite indexes
- hot keys
- реплика лаг и его последствия
- шардинг: по чему и какие проблемы

## Очереди
Главное — модель мышления, а не список отличий.

- queue vs log
- ordering
- retention
- replay
- consumer groups
- exactly-once (почему почти никогда нет)

1. «У тебя события оплаты и уведомления. Что куда и почему?»


## Kubernetes

- зачем вообще k8s
- pod vs deployment vs statefulset
- config & secrets
- liveness / readiness
- scaling стратегии
- как сервисы находят друг друга

1. Почему нельзя просто увеличить replicas и всё станет хорошо?


## Облака

- managed vs self-hosted
- vendor lock-in
- стоимость
- сети (VPC, private/public)
- IAM и безопасность

1. Что ты возьмёшь managed, а что оставишь самописным — и почему?


Универсальный фрейм для любого вопроса
---
- Уточнение контекста
- нагрузка
- тип данных
- SLA
- команда / сроки

1. Простое базовое решение
2. Проблемы базового решения
3. Улучшения по мере роста
4. Трейдофы
