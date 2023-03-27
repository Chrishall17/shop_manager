from lib.order import Order

class OrderRepository:

    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all orders
    def all(self):
        rows = self._connection.execute('SELECT * from orders')
        orders = []
        for row in rows:
            order = Order(row["id"], row["customer"], row["order_date"])
            orders.append(order)
        return orders

    # Find a single order by their id
    def find(self, order_id):
        rows = self._connection.execute(
            'SELECT * from orders WHERE id = %s', [order_id])
        row = rows[0]
        return Order(row["id"], row["customer"], row["order_date"])

    # Create a new order
    # Do you want to get its id back? Look into RETURNING id;
    def create(self, order):
        self._connection.execute('INSERT INTO orders (customer, order_date) VALUES (%s, %s)', [
                                order.customer, order.order_date])
        return None

    # Delete an order by their id
    def delete(self, order_id):
        self._connection.execute(
            f"DELETE FROM orders WHERE id = '{order_id}'")
        return None
