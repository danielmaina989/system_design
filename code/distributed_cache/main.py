import time
import threading
import hashlib

# Simulate a Redis-like node
class CacheNode:
    def __init__(self, name):
        self.name = name
        self.store = {}

    def get(self, key):
        return self.store.get(key)

    def set(self, key, value):
        self.store[key] = value

    def __str__(self):
        return f"Node {self.name} → {self.store}"

# Basic consistent hashing for distribution
class DistributedCache:
    def __init__(self, nodes):
        self.nodes = nodes

    def _get_node(self, key):
        hash_val = int(hashlib.sha256(key.encode()).hexdigest(), 16)
        return self.nodes[hash_val % len(self.nodes)]

    def set(self, key, value):
        node = self._get_node(key)
        node.set(key, value)
        print(f"[SET] {key}={value} → {node.name}")

    def get(self, key):
        node = self._get_node(key)
        value = node.get(key)
        print(f"[GET] {key} → {value} (from {node.name})")
        return value

# Usage
if __name__ == "__main__":
    nodeA = CacheNode("A")
    nodeB = CacheNode("B")
    nodeC = CacheNode("C")

    cache = DistributedCache([nodeA, nodeB, nodeC])
    cache.set("user:1", "Alice")
    cache.set("user:2", "Bob")
    cache.set("user:3", "Charlie")

    cache.get("user:1")
    cache.get("user:3")
