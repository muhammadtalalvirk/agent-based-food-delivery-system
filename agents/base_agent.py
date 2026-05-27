# backend/agents/base_agent.py

class BaseAgent:
    def __init__(self, name, bus):
        self.name = name
        self.bus = bus
        self.inbox = []
        self.state = "IDLE"
        self.bus.register_agent(self)

    def send(self, receiver, message):
        self.bus.send(self.name, receiver, message)

    def receive(self):
        if self.inbox:
            return self.inbox.pop(0)
        return None

    def step(self):
        pass
