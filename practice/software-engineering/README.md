# Практика — Программная инженерия

Задачи на backend-инженерию вокруг Python: БД, очереди, сеть, инфра. Зеркалит теорию из
[`../../theory/software-engineering.md`](../../theory/software-engineering.md).
Задачи 01–05 — код-заготовки (рабочий скелет с дырами `raise NotImplemented` / `# todo`,
самопроверка внизу; SQL-темы — скрипты с пошаговыми комментариями под `psql`).
Задачи 06–08 — операционные: пошаговое задание в README, инфру поднимаешь сам.

## Задачи

| # | Файл | Тема теории |
|---|------|-------------|
| 01 | [`01_indexing.sql`](01_indexing.sql) | Индексы, `EXPLAIN (ANALYZE)`, оптимизация запросов |
| 02 | [`02_n_plus_1.py`](02_n_plus_1.py) | N+1 проблема, батчинг запросов |
| 03 | [`03_deadlocks.sql`](03_deadlocks.sql) | Дедлоки: воспроизвести и починить (порядок захвата, retry) |
| 04 | [`04_queue_ack.py`](04_queue_ack.py) | Очереди, ACK/NOACK, at-least-once + идемпотентность |
| 05 | [`05_http_retry_sla.py`](05_http_retry_sla.py) | HTTP-идемпотентность + retry/backoff, SLA/SLO и error budget |
| 06 | [`06_k8s/`](06_k8s/) | Kubernetes: hello-world FastAPI → Docker → манифесты → minikube |
| 07 | [`07_linters.md`](07_linters.md) | Линтеры: ruff + vulture + mypy до «зелёного» |
| 08 | [`08_ci.md`](08_ci.md) | CI/CD: GitHub Actions — линтеры на каждый push в master |

`01` и `03` требуют PostgreSQL (`psql`), `03` — две сессии. `06` — Docker + minikube,
`08` — репозиторий на GitHub. `02`, `04`, `05` — чистый Python без внешних сервисов.
Задачи 06→07→08 идут связкой над одной апишкой ([`06_k8s/app.py`](06_k8s/app.py)):
завернул в docker/k8s → прогнал линтерами → повесил их в CI.

## Ещё нет задач (из теории)

Темы, оставленные под теорию (нужна отдельная возня с БД/деплоем):
миграции схемы (zero-downtime, rollback), оптимизация времени сборки Docker,
HPA и affinity/anti-affinity.
