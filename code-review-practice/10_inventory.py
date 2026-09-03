"""
Модуль учёта склада для маленького магазина: хранит остатки товаров,
списывает при заказе, считает суммарную стоимость. Дёргается из бизнес-логики
оформления заказа. Лежит в shop/inventory.py.
"""


class Inventory:
    def __init__(self, items):
        self.items = items  # {name: {"qty": int, "price": float}}

    def add_stock(self, name, qty):
        self.items[name]["qty"] += qty

    def remove_stock(self, name, qty):
        if self.items[name]["qty"] >= qty:
            self.items[name]["qty"] -= qty
            return True
        return False

    def total_value(self):
        total = 0
        for name in self.items:
            item = self.items[name]
            total += item["qty"] * item["price"]
        return total

    def low_stock(self, threshold=5):
        result = []
        for name in self.items:
            if self.items[name]["qty"] < threshold:
                result.append(name)
        return result


def process_order(inventory, order):
    for name, qty in order.items():
        inventory.remove_stock(name, qty)
    return "Order processed, total stock value: " + inventory.total_value()
