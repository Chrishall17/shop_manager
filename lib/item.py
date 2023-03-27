class Item:
    def __init__(self, id, name, unit_price, quantity):
        self.id = id
        self.name = name
        self.unit_price = unit_price
        self.quantity = quantity

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"#{self.id} {self.name} - Unit price: {self.unit_price} - Quantity: {self.quantity}"
