from lib.database_connection import DatabaseConnection
from lib.order_repository import OrderRepository
from lib.item_repository import ItemRepository
from lib.item import Item

class Application():
    def __init__(self):    
        # Connect to the database
        self._connection = DatabaseConnection()
        self._connection.connect()
        # Seed with some seed data
        self._connection.seed("seeds/items_orders.sql")

    def run(self):
        print("Welcome to the music library manager!")
        print("")
        print("What would yo u like to do?")
        print("  1 = list all shop items")
        print("  2 = create a new item")
        print("  3 = list all orders")
        print("  4 = create a new order")
        print("")

        value = input("Enter your value:\n")
        value = int(value)

        item_repository = ItemRepository(self._connection)
        items = item_repository.all()
        order_repository = OrderRepository(self._connection)
        orders = order_repository.all()
        
        if value == 1:
            print("")
            print("Here is the list of items:")
            for item in items:
                print(item)
        elif value == 2:
            print("")
            name = str(input("Enter your item:\n"))
            price = int(input("Enter your price:\n"))
            quantity = int(input("Enter your quantity:\n"))
            item = Item(None, name, price, quantity)
            item_repository.create(item)
            print("Your item has been added!")
        elif value == 3:
            print("")
            print("Here is the list of orders:")
            for order in orders:
                print(order)
        elif value == 4:
            pass


if __name__ == '__main__':
    app = Application()
    app.run()