"""
Скрипт выгрузки отчёта: читает список заказов из CSV, считает сумму по каждому
клиенту и пишет результат в новый файл. Запускается по крону раз в сутки.
Лежит в scripts/daily_report.py.
"""

import csv


def build_report(input_path, output_path):
    f = open(input_path)
    reader = csv.reader(f)

    totals = {}
    for row in reader:
        client = row[0]
        amount = row[2]
        if client in totals:
            totals[client] = totals[client] + amount
        else:
            totals[client] = amount

    out = open(output_path, "w")
    for client in totals:
        out.write(client + ";" + totals[client] + "\n")
    out.close()

    print("Report done, {} clients".format(len(totals)))


if __name__ == "__main__":
    build_report("orders.csv", "report.csv")
