# backend/messaging/message_bus.py

class MessageBus:
    def __init__(self):
        self.agents = {}

    def register_agent(self, agent):
        self.agents[agent.name] = agent
        print(f"[MessageBus] Registered {agent.name}")

    def send(self, sender, receiver, message):
        if receiver in self.agents:
            message["sender"] = sender
            self.agents[receiver].inbox.append(message)
            print(f"[MessageBus] {sender} → {receiver} | {message['type']}")
        else:
            print(f"[MessageBus] ERROR: {receiver} not found")
