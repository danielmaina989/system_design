import threading
import time
from collections import defaultdict

class PubSubBroker:
    def __init__(self):
        self.subscribers = defaultdict(list)

    def subscribe(self, topic, callback):
        self.subscribers[topic].append(callback)
        print(f"🔔 Subscribed to topic: {topic}")

    def publish(self, topic, message):
        print(f"\n📢 Publishing to {topic}: {message}")
        for callback in self.subscribers[topic]:
            threading.Thread(target=callback, args=(message,), daemon=True).start()

# Sample subscriber function
def send_email_alert(msg):
    print(f"[Email Alert] 📩 {msg}")

def log_to_database(msg):
    print(f"[DB Logger] 💾 {msg}")

def push_to_dashboard(msg):
    print(f"[Dashboard] 📊 {msg}")

# Demo
if __name__ == "__main__":
    broker = PubSubBroker()
    
    # Subscribing consumers
    broker.subscribe("order_created", send_email_alert)
    broker.subscribe("order_created", log_to_database)
    broker.subscribe("inventory_update", push_to_dashboard)

    # Publishing events
    broker.publish("order_created", "Order #567 has been placed.")
    broker.publish("inventory_update", "Stock updated for item #123.")

    time.sleep(2)
