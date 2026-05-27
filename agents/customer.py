# backend/agents/customer_agent.py

from agents.base_agent import BaseAgent
from services.order_Service import Order

class CustomerAgent(BaseAgent):
    def place_order(self, order_id, item):
        self.order = Order(order_id, item)
        self.state = "ORDER_PLACED"
        print(f"[Customer] Placed order {order_id}")
        self.send("MatchingAgent", {
            "type": "ORDER_REQUEST",
            "order": self.order
        })

    def step(self):
        msg = self.receive()
        if msg and msg["type"] == "ORDER_COMPLETED":
            self.state = "COMPLETED"
            print(f"[Customer] Order {msg['order'].id} delivered ")
