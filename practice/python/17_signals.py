"""
Тема: OOM killer и сигналы, graceful shutdown (см. theory/python.md → «OOM Killer и сигналы»).

Задача: реализовать graceful shutdown для «воркера», который в цикле обрабатывает
задачи. По SIGTERM воркер должен:
- НЕ бросать текущую задачу на середине;
- перестать брать новые задачи;
- корректно завершиться (вернуть/залогировать, сколько успел обработать).

Реализуй Worker.run(): установить обработчик SIGTERM, который взводит флаг
остановки, и крутить цикл, проверяя флаг между задачами.

Ответь себе: почему SIGKILL перехватить нельзя и чем он отличается от SIGTERM,
и как это связано с OOM killer (какой сигнал шлёт ядро при overcommit).
"""

import signal
import time


class Worker:
    def __init__(self):
        self._stopping = False
        self.processed = 0

    def _handle_sigterm(self, signum, frame):
        raise NotImplemented  # todo: взвести флаг остановки

    def process_one(self) -> None:
        time.sleep(0.5)  # эмуляция работы над задачей
        self.processed += 1

    def run(self) -> None:
        # todo: зарегистрировать обработчик SIGTERM и крутить цикл,
        # проверяя self._stopping между задачами
        raise NotImplemented


if __name__ == '__main__':
    # запусти, затем в другом терминале: kill -TERM <pid>
    # ожидаем: текущая задача дорабатывается, новые не берутся, процесс выходит чисто
    Worker().run()
