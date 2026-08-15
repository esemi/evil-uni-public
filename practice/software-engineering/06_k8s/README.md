# 06 — Kubernetes: FastAPI в minikube

Тема: сущности Kubernetes для веб-API (см. [`../../../theory/software-engineering.md`](../../../theory/software-engineering.md) → «Сущности Kubernetes»).

Задача целиком операционная: взять готовую hello-world апишку, завернуть её в Docker,
описать k8s-манифесты и поднять в minikube. Дано только [`app.py`](app.py) — всё
остальное пишешь сам.

## Что должно получиться

Запрос снаружи кластера доходит до пода с апишкой:

```
curl http://<minikube>/           -> {"message": "hello world"}
curl http://<minikube>/healthz    -> {"status": "ok"}
```

## Шаги

### 1. Docker-образ
- [ ] Напиши `Dockerfile` для `app.py` (base `python:3.12-slim`, ставит fastapi+uvicorn,
      запускает `uvicorn app:app --host 0.0.0.0 --port 8000`).
- [ ] Собери и проверь локально: `docker build -t hello-api:0.1 .` затем
      `docker run -p 8000:8000 hello-api:0.1` и `curl localhost:8000/`.

### 2. Завести minikube и образ в нём
- [ ] Поставь и запусти minikube: https://minikube.sigs.k8s.io/docs/start/
- [ ] Прокинь образ в кластер: `minikube image load hello-api:0.1`
      (или собери прямо в докере minikube через `eval $(minikube docker-env)`).

### 3. Манифесты
Опиши в `k8s/` (по файлу на объект или один multi-doc yaml):
- [ ] **Deployment** — 2 реплики, образ `hello-api:0.1`, `imagePullPolicy: IfNotPresent`,
      liveness/readiness пробы на `/healthz`.
- [ ] **ConfigMap** — переменная `GREETING`, прокинь её в контейнер через `envFrom`/`env`
      (проверь, что ответ `/` меняется на заданный текст).
- [ ] **Service** (`ClusterIP`) — стабильная точка доступа к подам внутри кластера.
- [ ] **Ingress** — вход снаружи; включи аддон `minikube addons enable ingress`.

Примени: `kubectl apply -f k8s/` и убедись, что поды `Running` (`kubectl get pods`).

### 4. Проверка
- [ ] `minikube ip` + правило ingress → `curl http://<ip>/` возвращает greeting.
- [ ] Убей под (`kubectl delete pod <name>`) — Deployment должен поднять новый,
      сервис остаётся доступен.

## Вопросы на подумать
- Зачем нужен Service, если у пода уже есть IP? Почему на него нельзя завязываться напрямую?
- Можно ли обойтись без Ingress? (да — как?) Чем он отличается от Service типа `NodePort`/`LoadBalancer`?
- Что даёт разделение liveness и readiness проб?
- Где здесь пригодился бы HPA и anti-affinity (см. теорию) — и почему в hello-world они избыточны?
