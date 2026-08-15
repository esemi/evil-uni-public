"""
Тема: мутабельность типов и опасность default-аргументов
(см. theory/python.md → «Мутабельность типов»).

Задача A. Функция append_item ниже содержит классический баг мутабельного дефолта:
список «запоминается» между вызовами. Почини так, чтобы каждый вызов без явного
bucket начинал с пустого списка.

Задача B. Реализуй freeze(obj): вернуть immutable-эквивалент для list/set/dict
(list->tuple, set->frozenset, dict->frozenset пар), рекурсивно. Нужно, чтобы
результат можно было положить в set (т.е. он должен быть хэшируемым).
"""


def append_item(item, bucket=[]):  # todo: убрать мутабельный дефолт
    bucket.append(item)
    return bucket


def freeze(obj):
    raise NotImplemented


# A
assert append_item(1) == [1]
assert append_item(2) == [2], 'дефолтный список не должен накапливать значения между вызовами'

# B
frozen = freeze({'a': [1, 2], 'b': {3, 4}})
assert isinstance(frozen, frozenset)
_ = {frozen}  # должно быть хэшируемым
print('ok')
