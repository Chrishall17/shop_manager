from lib.item_repository import ItemRepository
from lib.item import Item

"""
When we call ItemRepository#all
We get a list of Item objects reflecting the seed data.
"""
def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/items_orders.sql") # Seed our database with some test data
    repository = ItemRepository(db_connection) # Create a new ItemRepository

    items = repository.all() # Get all items

    # Assert on the results
    assert items == [
        Item(1, 'Vacuum', 99, 30),
        Item(2, 'Coffee Machine', 69, 15),
        Item(3, 'Monopoly', 18, 20),
        Item(4, 'Prime', 12, 1)
    ]

"""
When we call ItemRepository#find
We get a single Item object reflecting the seed data.
"""
def test_get_single_record(db_connection):
    db_connection.seed("seeds/items_orders.sql")
    repository = ItemRepository(db_connection)

    item = repository.find(3)
    assert item == Item(3, 'Monopoly', 18, 20)

"""
When we call ItemRepository#create
We get a new record in the database.
"""
def test_create_record(db_connection):
    db_connection.seed("seeds/items_orders.sql")
    repository = ItemRepository(db_connection)

    repository.create(Item(None, 'Bible', 12, 10))

    result = repository.all()
    assert result == [
        Item(1, 'Vacuum', 99, 30),
        Item(2, 'Coffee Machine', 69, 15),
        Item(3, 'Monopoly', 18, 20),
        Item(4, 'Prime', 12, 1),
        Item(5, 'Bible', 12, 10)
    ]

"""
When we call ItemRepository#delete
We remove a record from the database.
"""
def test_delete_record(db_connection):
    db_connection.seed("seeds/items_orders.sql")
    repository = ItemRepository(db_connection)
    repository.delete(3) 

    result = repository.all()
    assert result == [
        Item(1, 'Vacuum', 99, 30),
        Item(2, 'Coffee Machine', 69, 15),
        Item(4, 'Prime', 12, 1)
    ]
