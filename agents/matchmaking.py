# backend/agents/matching_agent.py

from agents.base_agent import BaseAgent
import random

class MatchingAgent(BaseAgent):
    def __init__(self, name, bus, restaurants):
        super().__init__(name, bus)
        self.restaurants = restaurants
        self.pending_orders = {}

    def step(self):
        msg = self.receive()
        if not msg:
            return

        order = msg["order"]

        if msg["type"] == "ORDER_REQUEST":
            self.pending_orders[order.id] = order
            self.try_restaurant(order)

        elif msg["type"] == "ORDER_REJECTED":
            print(f"[Matching] Retrying order {order.id}")
            self.try_restaurant(order)

        elif msg["type"] == "ORDER_ACCEPTED":
            order.restaurant = msg["restaurant"]
            self.send("DeliveryAgent", {
                "type": "DELIVERY_ASSIGN",
                "order": order
            })

        elif msg["type"] == "ORDER_DELIVERED":
            self.send("CustomerAgent", {
                "type": "ORDER_COMPLETED",
                "order": order
            })

    def try_restaurant(self, order):
        restaurant = random.choice(self.restaurants)
        print(f"[Matching] Sending order {order.id} to {restaurant}")
        self.send(restaurant, {
            "type": "ORDER_REQUEST",
            "order": order
        })
