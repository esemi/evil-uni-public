"""
Приёмник вебхуков от платёжного провайдера: провайдер шлёт POST при смене статуса,
мы обновляем заказ и дёргаем колбэк-URL из payload. Публичная ручка в интернете.
"""

import requests
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()

    order_id = data["order_id"]
    status = data["status"]

    update_order(order_id, status)

    callback_url = data["callback_url"]
    requests.get(callback_url)

    process_heavy_analytics(data)

    return jsonify({"ok": True})


def update_order(order_id, status):
    ...


def process_heavy_analytics(data):
    time_consuming_stuff(data)


def time_consuming_stuff(data):
    ...
