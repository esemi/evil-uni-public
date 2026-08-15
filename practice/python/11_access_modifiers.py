"""
Тема: модификаторы доступа, name mangling (см. theory/python.md → «Модификаторы доступа»).

В Python нет настоящего private — есть соглашения (_protected) и name mangling (__private).

Задача A. Достучись до «приватного» атрибута account.__balance СНАРУЖИ класса,
не меняя сам класс Account, и запиши баланс в переменную balance ниже.
Подсказка: как реально называется __balance после name mangling?

Задача B. Ответь себе комментарием: почему __private не является настоящей
защитой и чем _protected отличается от __private по механике.
"""


class Account:
    def __init__(self, balance: int):
        self.__balance = balance  # «приватное» поле

    def deposit(self, amount: int) -> None:
        self.__balance += amount


account = Account(100)

balance = None  # todo: получить сюда значение приватного __balance снаружи класса

assert balance == 100, 'достучись до значения через фактическое имя после name mangling'
print('ok')
