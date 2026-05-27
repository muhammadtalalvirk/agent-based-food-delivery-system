# backend/agents/restaurant_agent.py

from agents.base_agent import BaseAgent
import random

class RestaurantAgent(BaseAgent):
    def __init__(self, name, bus):
        super().__init__(name, bus)
        self.capacity = 1

    def step(self):
        msg = self.receive()
        if not msg:
            return

        if msg["type"] == "ORDER_REQUEST":
            if random.choice([True, False]):
                print(f"[{self.name}] Accepted order {msg['order'].id}")
                self.send("MatchingAgent", {
                    "type": "ORDER_ACCEPTED",
                    "order": msg["order"],
                    "restaurant": self.name
                })
            else:
                print(f"[{self.name}] Rejected order {msg['order'].id}")
                self.send("MatchingAgent", {
                    "type": "ORDER_REJECTED",
                    "order": msg["order"],
                    "restaurant": self.name
                })
