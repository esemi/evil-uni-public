"""
Парсер логов nginx: считает, сколько раз встретился каждый статус-код
за файл, и возвращает топ ошибок. Дёргается из CLI-утилиты анализа логов.
Лежит в tools/logparse/parser.py.
"""

import re


def parse_logs(path):
    pattern = re.compile('.* (\d{3}) \d+ ".*"')

    result = {}
    lines = open(path).readlines()
    for line in lines:
        match = re.match(pattern, line)
        status = match.group(1)
        if status in result.keys():
            result[status] += 1
        else:
            result[status] = 1

    errors = {}
    for status in result:
        if int(status) >= 400:
            errors[status] = result[status]

    top = sorted(errors.items(), key=lambda x: x[1])[-5:]
    return top


def print_report(path):
    top = parse_logs(path)
    print("Top errors:")
    for status, count in top:
        print(status, count)
