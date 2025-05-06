"""
A basic simulation of a Load Balancer distributing client requests to multiple backend servers using Round Robin strategy.
"""

import itertools
import random
import time

# Simulated backend servers
class BackendServer:
    def __init__(self, name):
        self.name = name

    def handle_request(self, request_id):
        print(f"✅ Server {self.name} handled request {request_id}")

# Round Robin Load Balancer
class LoadBalancer:
    def __init__(self, servers):
        self.servers = servers
        self.server_pool = itertools.cycle(self.servers)

    def distribute_request(self, request_id):
        server = next(self.server_pool)
        print(f"➡️  Distributing request {request_id} to server {server.name}")
        server.handle_request(request_id)

# Demo run
if __name__ == "__main__":
    server_list = [BackendServer(f"S{i+1}") for i in range(3)]  # e.g., S1, S2, S3
    lb = LoadBalancer(server_list)

    print("🔁 Simulating client requests...\n")
    for req_id in range(1, 11):  # Simulate 10 client requests
        lb.distribute_request(req_id)
        time.sleep(0.5)  # Simulated network delay
