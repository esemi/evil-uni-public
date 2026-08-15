"""
Тема: ACK / NOACK в очередях, at-least-once (см. theory/software-engineering.md → «ACK / NOACK»).

Дано: простейшая in-memory очередь с семантикой брокера:
- get() выдаёт сообщение, но НЕ удаляет его — держит "in-flight";
- ack(msg) удаляет обработанное сообщение;
- если consumer упал ПОСЛЕ обработки, но ДО ack — сообщение вернётся в очередь
  (requeue) и придёт снова. Отсюда at-least-once: возможны повторы (дубликаты).

Задача: реализовать consume(queue, handler, process), который:
1) берёт сообщения, обрабатывает через process(msg) и делает ack ТОЛЬКО после
   успешной обработки (иначе — не ack, пусть requeue);
2) идемпотентен: одно и то же сообщение (по msg['id']) должно применяться к
   handler РОВНО один раз, даже если очередь доставит его дважды.

Проверка внизу эмулирует падение до ack (первая попытка кидает исключение) и
дубликат — итог должен быть без повторного эффекта.
"""


class Queue:
    def __init__(self, messages: list[dict]):
        self._pending = list(messages)
        self._inflight: dict[int, dict] = {}

    def get(self) -> dict | None:
        if not self._pending:
            return None
        msg = self._pending.pop(0)
        self._inflight[msg['id']] = msg
        return msg

    def ack(self, msg: dict) -> None:
        self._inflight.pop(msg['id'], None)

    def requeue_inflight(self) -> None:
        """Эмуляция таймаута/падения: всё необработанное (без ack) вернуть в очередь."""
        self._pending.extend(self._inflight.values())
        self._inflight.clear()

    def is_empty(self) -> bool:
        return not self._pending and not self._inflight


def consume(queue: Queue, handler: dict, process) -> None:
    """
    handler — состояние приёмника (напр. {'balance': 0, 'applied': set()}).
    process(msg) — бизнес-обработка, может бросить исключение (значит НЕ ack).
    """
    raise NotImplemented


if __name__ == '__main__':
    handler = {'balance': 0, 'applied': set()}

    calls = {'n': 0}
    def process(msg):
        # первая обработка первого сообщения падает ДО ack -> requeue
        calls['n'] += 1
        if msg['id'] == 1 and calls['n'] == 1:
            raise RuntimeError('boom before ack')
        handler['balance'] += msg['amount']

    q = Queue([
        {'id': 1, 'amount': 100},
        {'id': 1, 'amount': 100},  # дубликат доставки того же события
        {'id': 2, 'amount': 50},
    ])

    consume(q, handler, process)

    assert q.is_empty(), 'все сообщения должны быть в итоге обработаны и заакнуты'
    assert handler['balance'] == 150, f'эффект ровно один раз на id: ожидали 150, получили {handler["balance"]}'
    print('ok, balance =', handler['balance'])
