# backend/agents/delivery_agent.py

from agents.base_agent import BaseAgent
import time
import random

class DeliveryAgent(BaseAgent):
    def step(self):
        msg = self.receive()
        if msg and msg["type"] == "DELIVERY_ASSIGN":
            self.state = "DELIVERING"
            order = msg["order"]
            print(f"[Delivery] Delivering order {order.id}")
            time.sleep(random.randint(1, 3))
            self.send("MatchingAgent", {
                "type": "ORDER_DELIVERED",
                "order": order
            })
