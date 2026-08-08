"""
Загрузчик конфига сервиса: читает JSON-файл и отдаёт значения по ключу,
подмешивая дефолты. Импортируется на старте приложения. Лежит в app/config.py.
"""

import json

DEFAULTS = {
    "timeout": 30,
    "retries": 3,
    "hosts": [],
    "debug": False,
}


class Config:
    def __init__(self, path="config.json"):
        self.data = json.load(open(path))

    def get(self, key):
        if self.data[key]:
            return self.data[key]
        else:
            return DEFAULTS[key]

    def get_hosts(self):
        hosts = self.get("hosts")
        hosts.append("localhost")
        return hosts


config = Config()
