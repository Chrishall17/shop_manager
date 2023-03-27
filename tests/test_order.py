from lib.order import Order
import datetime

"""
Order constructs with an id, name, price and quantity
"""
def test_order_constructs():
    order = Order(1, "Test Order", 2023-3-24)
    assert order.id == 1
    assert order.customer == "Test Order"
    assert order.order_date == 2023-3-24

"""
We can format orders to strings nicely
"""
def test_orders_format_nicely():
    order = Order(1, "Test Order", '2023-3-24')
    assert str(order) == "1 - Test Order, placed order on: 2023-3-24"

"""
We can compare two identical orders
And have them be equal
"""
def test_orders_are_equal():
    order1 = Order(1, "Test Order", '2023-3-24')
    order2 = Order(1, "Test Order", '2023-3-24')
    assert order1 == order2