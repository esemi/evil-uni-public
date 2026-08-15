# Практика — Программная инженерия

Небольшие задачи на backend-инженерию вокруг Python: БД, очереди, сеть. Зеркалит теорию из
[`../../theory/software-engineering.md`](../../theory/software-engineering.md).
Формат — как в python-блоке: рабочий скелет с дырами (`raise NotImplemented`, `# todo`),
условие в докстринге, самопроверка внизу. SQL-темы — скрипты с пошаговыми комментариями под `psql`.

## Задачи

| # | Файл | Тема теории |
|---|------|-------------|
| 01 | [`01_indexing.sql`](01_indexing.sql) | Индексы, `EXPLAIN (ANALYZE)`, оптимизация запросов |
| 02 | [`02_n_plus_1.py`](02_n_plus_1.py) | N+1 проблема, батчинг запросов |
| 03 | [`03_deadlocks.sql`](03_deadlocks.sql) | Дедлоки: воспроизвести и починить (порядок захвата, retry) |
| 04 | [`04_queue_ack.py`](04_queue_ack.py) | Очереди, ACK/NOACK, at-least-once + идемпотентность |
| 05 | [`05_http_retry_sla.py`](05_http_retry_sla.py) | HTTP-идемпотентность + retry/backoff, SLA/SLO и error budget |

`01` и `03` требуют PostgreSQL (`psql`), `03` — две сессии. Остальное — чистый Python, без внешних сервисов.

## Ещё нет задач (из теории)

Темы, которые не укладываются в «небольшую практику» — им нужна реальная инфра,
проходятся отдельно по инструкциям из [`software-engineering.md`](../../theory/software-engineering.md):
миграции схемы (zero-downtime, rollback), минимальный CI/CD, линтеры,
Dockerfile и оптимизация сборки, сущности Kubernetes (Deployment/Service/Ingress/ConfigMap, HPA, affinity).
