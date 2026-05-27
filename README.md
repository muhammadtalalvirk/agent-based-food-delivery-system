# Agent-Based Online Food Delivery System 🚀🍕

An implementation of an online food delivery platform designed using **Agent-Based Software Engineering (ABSE)** principles. Instead of a traditional centralized monolithic architecture, this system models every entity as an autonomous, intelligent agent capable of making independent decisions and communicating via a decentralized messaging protocol.

---

## 🏗️ System Architecture

The system is composed of four core intelligent agents:

1. **Customer Agent:** Places orders based on preferences, budget, and location. It evaluates offers from Restaurant Agents.
2. **Restaurant Agent:** Manages menus, calculates food preparation times, accepts/rejects orders based on kitchen capacity, and requests couriers.
3. **Driver (Courier) Agent:** Autonomous delivery units that track their own location, fuel/battery status, and bid on delivery jobs based on proximity and payout.
4. **Delivery Coordinator Agent (The Broker):** Facilitates communication, handles yellow-page lookups (matching drivers to restaurants), and logs system analytics.

---

## 🛠️ Tech Stack & Tools

* **Language:** Python 3.10+
* **Agent Framework:** `mesa` (or `spade` / `jade` for multi-agent systems)
* **Communication Protocol:** JSON-RPC / ACL (Agent Communication Language)
* **Visualization:** Mesa Canvas / Pygame (Optional UI)

---

