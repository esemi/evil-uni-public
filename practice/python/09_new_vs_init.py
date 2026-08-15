"""
Тема: __new__ vs __init__ (см. theory/python.md → «__new__ vs __init__»).

Реализуй Singleton через __new__ так, чтобы сколько бы раз ни создавали экземпляр,
это был один и тот же объект (одинаковый id), а состояние не перезатиралось при
повторных «созданиях».

Подумай: почему это делается в __new__, а не в __init__, и когда __new__
реально необходим (immutable-типы, singleton, factory).
"""


class Singleton:
    # todo: сделать так, чтобы всегда возвращался один и тот же экземпляр
    def __init__(self, value):
        self.value = value


a = Singleton('first')
b = Singleton('second')

assert a is b, 'должен быть один и тот же объект'
assert a.value == 'first', 'состояние не должно перезатираться повторным вызовом'
print('ok')
