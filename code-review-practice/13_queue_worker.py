"""
Воркер очереди: читает задачи из RabbitMQ-подобного брокера, обрабатывает,
шлёт результат в БД. Крутится демоном в проде, должен переживать падения.
"""

import json
import time


def process_message(body):
    task = json.loads(body)
    result = do_heavy_work(task["payload"])
    save_to_db(task["id"], result)


def run_worker(channel):
    while True:
        method, properties, body = channel.basic_get(queue="tasks")
        if body is None:
            time.sleep(0.1)
            continue

        channel.basic_ack(method.delivery_tag)

        try:
            process_message(body)
        except Exception:
            pass


def do_heavy_work(payload):
    return {"processed": payload}


def save_to_db(task_id, result):
    ...
