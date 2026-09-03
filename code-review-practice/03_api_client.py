"""
Мини-клиент к внешнему платёжному API. Используется другими модулями сервиса
как обёртка над requests. Лежит в integrations/payments/client.py.
"""

import requests


class PaymentClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.payments.example.com"

    def get_payment(self, payment_id):
        url = self.base_url + "/payments/" + payment_id
        resp = requests.get(url, headers={"Authorization": self.api_key})
        return resp.json()

    def create_payment(self, amount, currency):
        data = {"amount": amount, "currency": currency}
        resp = requests.post(self.base_url + "/payments", data=data)
        if resp.status_code == 200:
            return resp.json()

    def list_payments(self, user_id):
        payments = []
        page = 1
        while True:
            resp = requests.get(
                self.base_url + "/payments?user=" + str(user_id) + "&page=" + str(page)
            )
            batch = resp.json()["items"]
            if batch == []:
                break
            payments = payments + batch
            page = page + 1
        return payments
