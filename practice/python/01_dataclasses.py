"""
Тема: dataclasses (см. theory/python.md → «Что нового в Python»).

Перепиши класс Point ниже через @dataclass так, чтобы код-проверка внизу прошёл:
- поля x, y (int), tag (str) со значением по умолчанию 'origin';
- сравнение по значению (__eq__);
- экземпляр должен быть хэшируемым (пригоден как ключ set/dict);
- поле history: list[str] с дефолтом пустой список — но без бага мутабельного дефолта.

Подумай: почему dataclass(frozen=True) автоматически хэшируемый и зачем
field(default_factory=...) вместо default=[].
"""

from dataclasses import dataclass


class Point:  # todo: переписать через @dataclass
    pass


a = Point(1, 2)
b = Point(1, 2)
c = Point(3, 4, tag='corner')

assert a == b, 'сравнение по значению'
assert a != c
assert len({a, b, c}) == 2, 'должно быть хэшируемым и a == b'
assert c.tag == 'corner'
assert Point(0, 0).tag == 'origin'
assert Point(0, 0).history == [] and Point(0, 0).history is not Point(0, 0).history
print('ok')
