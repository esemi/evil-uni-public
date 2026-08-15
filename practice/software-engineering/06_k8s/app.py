"""
Hello-world FastAPI-апишка — подопытный для задач 06 (k8s), 07 (линтеры), 08 (CI/CD).

Запуск локально:
    pip install fastapi uvicorn
    uvicorn app:app --host 0.0.0.0 --port 8000

Проверка:
    curl localhost:8000/          -> {"message": "hello world"}
    curl localhost:8000/healthz   -> {"status": "ok"}
"""

import os

from fastapi import FastAPI

app = FastAPI()

# читается из ConfigMap в k8s-задаче — специально вынесено в env
GREETING = os.getenv("GREETING", "hello world")


@app.get("/")
def root() -> dict[str, str]:
    return {"message": GREETING}


@app.get("/healthz")
def healthz() -> dict[str, str]:
    return {"status": "ok"}
