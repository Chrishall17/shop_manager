class Order:
    def __init__(self, id, customer, order_date):
        self.id = id
        self.customer = customer
        self.order_date = order_date

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"{self.id} - {self.customer}, placed order on: {self.order_date}"