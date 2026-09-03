"""
Репозиторий заказов поверх SQLAlchemy. Дёргается из ручек API,
отдаёт заказы с позициями и суммами. Тут и N+1, и работа с сессией.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql://user:password@localhost/shop")
Session = sessionmaker(bind=engine)
session = Session()


def get_orders_with_totals(user_id):
    orders = session.query(Order).filter(Order.user_id == user_id).all()

    result = []
    for order in orders:
        total = 0
        for item in order.items:
            product = session.query(Product).filter(Product.id == item.product_id).first()
            total += product.price * item.qty
        result.append({"id": order.id, "total": total})

    return result


def search_orders(query):
    sql = "SELECT * FROM orders WHERE comment LIKE '%" + query + "%'"
    return session.execute(sql).fetchall()


def get_all_orders():
    return session.query(Order).all()
