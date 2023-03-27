from lib.item import Item

"""
Item constructs with an id, name, price and quantity
"""
def test_item_constructs():
    item = Item(1, "Test Item", 99, 30)
    assert item.id == 1
    assert item.name == "Test Item"
    assert item.unit_price == 99
    assert item.quantity == 30

"""
We can format items to strings nicely
"""
def test_items_format_nicely():
    item = Item(1, "Test Item", 99, 30)
    assert str(item) == "#1 Test Item - Unit price: 99 - Quantity: 30"

"""
We can compare two identical items
And have them be equal
"""
def test_items_are_equal():
    item1 = Item(1, "Test Item", 99, 30)
    item2 = Item(1, "Test Item", 99, 30)
    assert item1 == item2
