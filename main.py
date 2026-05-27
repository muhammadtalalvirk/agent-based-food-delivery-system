# backend/main.py

import time
from messaging.message_bus import MessageBus
from agents.customer import CustomerAgent
from agents.matchmaking import MatchingAgent
from agents.resturant import RestaurantAgent
from agents.delivery_agent import DeliveryAgent

bus = MessageBus()

customer = CustomerAgent("CustomerAgent", bus)

restaurants = [
    RestaurantAgent("RestaurantAgent1", bus),
    RestaurantAgent("RestaurantAgent2", bus)
]

matching = MatchingAgent("MatchingAgent", bus,
                         ["RestaurantAgent1", "RestaurantAgent2"])

delivery = DeliveryAgent("DeliveryAgent", bus)

customer.place_order(1, "Burger")

agents = [customer, matching, delivery] + restaurants

while True:
    for agent in agents:
        agent.step()
    time.sleep(0.5)
