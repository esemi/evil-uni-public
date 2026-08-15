"""
Тема: __hash__ (см. theory/python.md → «__hash__»).

Сделай так, чтобы код ниже не бросал исключение — экземпляры CustomDict
должны быть пригодны как ключи словаря.

Подумай: dict по умолчанию нехэшируемый (mutable). Что нужно определить,
чтобы объект стал хэшируемым, и какой контракт связывает __hash__ и __eq__?
"""


class CustomDict(dict):
    # todo
    pass


first = CustomDict(key='first value')
second = CustomDict(key='second value')

counter_with_dict_keys = {
    first: 3,
    second: 103,
}
print(counter_with_dict_keys)
# >>> {{'key': 'first value'}: 3, {'key': 'second value'}: 103}
