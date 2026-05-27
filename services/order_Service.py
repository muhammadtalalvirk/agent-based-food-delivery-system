# backend/entities/order.py

class Order:
    def __init__(self, order_id, item):
        self.id = order_id
        self.item = item
        self.status = "CREATED"
        self.restaurant = None
