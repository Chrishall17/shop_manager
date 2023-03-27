from lib.order_repository import OrderRepository
from lib.order import Order
import datetime

"""
When we call OrderRepository#all
We get a list of Order objects reflecting the seed data.
"""
def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/items_orders.sql") # Seed our database with some test data
    repository = OrderRepository(db_connection) # Create a new OrderRepository

    orders = repository.all() # Get all orders

    # Assert on the results
    assert orders == [
        Order(1, 'Chris', datetime.date(2023, 3, 24))
    ]

"""
When we call OrderRepository#find
We get a single Order object reflecting the seed data.
"""
def test_get_single_record(db_connection):
    db_connection.seed("seeds/items_orders.sql")
    repository = OrderRepository(db_connection)

    order = repository.find(1)
    assert order == Order(1, 'Chris', datetime.date(2023, 3, 24))

"""
When we call OrderRepository#create
We get a new record in the database.
"""
def test_create_record(db_connection):
    db_connection.seed("seeds/items_orders.sql")
    repository = OrderRepository(db_connection)

    repository.create(Order(None, 'Jack', datetime.date(2023, 3, 24)))

    result = repository.all()
    assert result == [
        Order(1, 'Chris', datetime.date(2023, 3, 24)),
        Order(2, 'Jack', datetime.date(2023, 3, 24))
    ]

"""
When we call OrderRepository#delete
We remove a record from the database.
"""
def test_delete_record(db_connection):
    db_connection.seed("seeds/items_orders.sql")
    repository = OrderRepository(db_connection)
    repository.delete(1) 

    result = repository.all()
    assert result == [

    ]
