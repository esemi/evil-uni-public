"""
Скрипт выгрузки отчёта: читает список заказов из CSV, считает сумму по каждому
клиенту и пишет результат в новый файл. Запускается по крону раз в сутки.
Лежит в scripts/daily_report.py.
"""

import csv


def build_report(input_path, output_path):# fixme нет типов
    # fixme нет валидации путей - туда можно и внутренние пути на серваке пробросить и привет
    f = open(input_path) # fixme нет контекстного манагера
    reader = csv.reader(f)

    totals = {} # fixme проще решить через встроенный Counter
    for row in reader:
        client = row[0] # fixme завязка ни индексы == беда беда
        amount = row[2]
        if client in totals: # fixme тоже каунтер порешал бы проще
            totals[client] = totals[client] + amount
        else:
            totals[client] = amount

    out = open(output_path, "w") # fixme тоже нет закрытия дескриптора при исключении
    for client in totals: # fixme for client, counter in totals.items()
        out.write(client + ";" + totals[client] + "\n") # fixme ну хотя бы формат, если уж не готовый райтер csv
    out.close()

    print("Report done, {} clients".format(len(totals))) # fixme логгинг


if __name__ == "__main__":
    # fixme не лишним бы сигналы прерывания ловить если файлы большие?
    # fixme да и пути бы как аргументы cli лучше?
    build_report("orders.csv", "report.csv")  # fixme не нравятся относительные пути тут
