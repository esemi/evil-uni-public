"""
Тема: mixins, множественное наследование, MRO (см. theory/python.md → «Mixins»).

Задача A. Реализуй два поведенческих миксина (маленькие, без состояния, без __init__):
- JsonMixin.to_json() -> JSON-строка из self.__dict__;
- ReprMixin.__repr__() -> "<ClassName field=val ...>" из self.__dict__.
Примешай их к User так, чтобы проверки внизу прошли.

Задача B. Ответь себе (комментарием в коде) на вопрос: в каком порядке Python
ищет метод в User(JsonMixin, ReprMixin) — выведи User.__mro__ и объясни почему
такой порядок (правило C3 / линеаризация).
"""

import json


class JsonMixin:
    # todo: to_json()
    pass


class ReprMixin:
    # todo: __repr__()
    pass


class User(JsonMixin, ReprMixin):
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


u = User('Alex', 30)
assert json.loads(u.to_json()) == {'name': 'Alex', 'age': 30}
assert repr(u) == '<User name=Alex age=30>'
print(User.__mro__)  # B: объясни порядок
print('ok')
