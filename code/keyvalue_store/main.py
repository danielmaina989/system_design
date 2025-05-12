from vector_clock import VectorClock
from merkle import MerkleTree
import random

class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.data = {}
        self.clock = {}

    def store(self, key, value, client_id):
        if key not in self.clock:
            self.clock[key] = VectorClock()
        self.clock[key].increment(client_id)
        self.data[key] = (value, self.clock[key].get())

    def retrieve(self, key):
        return self.data.get(key, (None, None))

    def merkle_root(self):
        keys = list(self.data.keys())
        return MerkleTree(keys).root()

# Simulate virtual nodes
nodes = [Node(f"node{i}") for i in range(3)]

# Simulate data replication (replication factor = 2)
def store_with_replication(key, value, client_id):
    chosen_nodes = random.sample(nodes, 2)
    for node in chosen_nodes:
        node.store(key, value, client_id)
        print(f"Stored '{key}' -> '{value}' on {node.node_id} with VC {node.clock[key]}")

# Demo
store_with_replication("user1", "Alice", "client1")
store_with_replication("user1", "Alice_v2", "client1")

# Retrieve from all nodes
for node in nodes:
    val, vc = node.retrieve("user1")
    print(f"{node.node_id} has: {val} | VC: {vc} | Merkle Root: {node.merkle_root()}")
