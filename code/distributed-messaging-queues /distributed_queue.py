import threading
import queue
import time
import random

class MessageBroker:
    def __init__(self, name):
        self.name = name
        self.queue = queue.Queue()

    def publish(self, message):
        self.queue.put(message)
        print(f"[{self.name}] Published: {message}")

    def consume(self):
        while True:
            if not self.queue.empty():
                msg = self.queue.get()
                print(f"[{self.name}] Consumed: {msg}")
            time.sleep(0.5)

# Primary-Secondary setup
class PrimarySecondaryCluster:
    def __init__(self):
        self.primary = MessageBroker("Primary")
        self.secondary = MessageBroker("Secondary")

    def publish(self, message):
        self.primary.publish(message)
        self.secondary.publish(f"[Replica] {message}")

    def consume_all(self):
        threading.Thread(target=self.primary.consume, daemon=True).start()
        threading.Thread(target=self.secondary.consume, daemon=True).start()

# Independent Broker Cluster
class BrokerCluster:
    def __init__(self, brokers):
        self.brokers = brokers

    def publish(self, message):
        broker = random.choice(self.brokers)
        broker.publish(message)

    def consume_all(self):
        for broker in self.brokers:
            threading.Thread(target=broker.consume, daemon=True).start()

# Run demo
if __name__ == "__main__":
    print("=== Primary-Secondary Cluster ===")
    cluster = PrimarySecondaryCluster()
    cluster.consume_all()
    cluster.publish("Order Created")
    cluster.publish("Payment Processed")
    time.sleep(3)

    print("\n=== Independent Broker Cluster ===")
    broker1 = MessageBroker("Broker1")
    broker2 = MessageBroker("Broker2")
    broker3 = MessageBroker("Broker3")

    cluster2 = BrokerCluster([broker1, broker2, broker3])
    cluster2.consume_all()
    cluster2.publish("Inventory Update")
    cluster2.publish("Shipping Label Created")
    time.sleep(3)
