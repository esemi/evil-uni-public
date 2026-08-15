"""
Тема: __slots__ (см. theory/python.md → «__slots__»).

Сделай так, чтобы MemoryOptimized занимал меньше памяти, чем Default,
но при этом код ниже не бросал исключение.

Подумай: за счёт чего __slots__ экономит память и какой ценой
(что запрещает, как влияет на наследование).
"""


class Default:
    pass


class MemoryOptimized:
    # todo
    pass


default = Default()
default.key = 'value'

optimized = MemoryOptimized()
optimized.key = 'value'

from sys import getsizeof

print(getsizeof(default), getsizeof(optimized))
# >>> 48 40
assert getsizeof(default) > getsizeof(optimized)
