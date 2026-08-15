"""
Тема: stateless vs stateful (см. theory/python.md → «Stateless vs Stateful»).

Дано: «сервис» с сессиями, который хранит состояние в памяти процесса (SESSIONS).
Проблема: при нескольких репликах за балансировщиком запрос пользователя может
попасть на другую реплику — и сессии там нет (нельзя горизонтально масштабировать).

Задача: сделать StatelessService — вынести хранение сессий во внешний стор
(эмулируй интерфейсом с get/set/delete, как у Redis), чтобы любой инстанс
сервиса видел одни и те же сессии.

Ответь себе: почему stateless-инстансы проще масштабировать и переживать failover.
"""


# --- было (stateful, состояние в памяти инстанса) ---
class StatefulService:
    def __init__(self):
        self.SESSIONS: dict[str, int] = {}

    def login(self, token: str, user_id: int) -> None:
        self.SESSIONS[token] = user_id

    def whoami(self, token: str) -> int | None:
        return self.SESSIONS.get(token)


# --- стало (stateless: состояние во внешнем сторе) ---
class StatelessService:
    def __init__(self, store):  # store — объект с get/set/delete, напр. Redis
        raise NotImplemented

    def login(self, token: str, user_id: int) -> None:
        raise NotImplemented

    def whoami(self, token: str) -> int | None:
        raise NotImplemented


if __name__ == '__main__':
    # простейший in-memory стор с интерфейсом Redis для проверки идеи
    class FakeStore:
        def __init__(self):
            self._d = {}
        def set(self, k, v): self._d[k] = v
        def get(self, k): return self._d.get(k)
        def delete(self, k): self._d.pop(k, None)

    store = FakeStore()
    # два независимых инстанса сервиса делят один стор
    a = StatelessService(store)
    b = StatelessService(store)
    a.login('tok', 7)
    assert b.whoami('tok') == 7, 'другой инстанс должен видеть сессию через общий стор'
    print('ok')
