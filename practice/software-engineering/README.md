# Практика — Программная инженерия

Задачи на backend-инженерию вокруг Python: БД, очереди, инфра. Зеркалит теорию из
[`../../theory/software-engineering.md`](../../theory/software-engineering.md).

## Задачи

| Файл | Задачи | Темы теории |
|------|--------|-------------|
| [`indexing.sql`](indexing.sql) | Песочница PostgreSQL (генерятся таблицы `employees`/`sex`) + запросы, которые нужно оптимизировать индексами. Смотри `EXPLAIN (ANALYZE)`. | индексы, выбор БД, N+1 |

## Ещё нет задач (из теории)

Темы из [`software-engineering.md`](../../theory/software-engineering.md), под которые пока нет заготовок:
миграции схемы (zero-downtime, rollback), дедлоки (`SELECT ... FOR UPDATE`, retry, порядок захвата),
SLA/SLO/SLI и error budget, очереди и ACK/NOACK (at-least-once, requeue), минимальный CI/CD,
линтеры, работа с сетью (HTTP-идемпотентность, TCP, keep-alive), Dockerfile и оптимизация сборки,
сущности Kubernetes (Deployment/Service/Ingress/ConfigMap, HPA, affinity).
