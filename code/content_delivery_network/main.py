# cdn_simulation.py

import random

# Simulated edge servers and origin
origin_server = {"index.html": "<html><body>Home Page</body></html>"}
edge_servers = {
    "edge_us": {},
    "edge_eu": {},
    "edge_asia": {}
}

# Simple cache-control mechanism
CACHE_TTL = 3  # in "requests"

# Tracks how long content is cached in edge servers
cache_tracker = {
    "edge_us": {},
    "edge_eu": {},
    "edge_asia": {}
}

def fetch_from_origin(file_name):
    print("📦 Fetching from origin...")
    return origin_server.get(file_name, "404 Not Found")

def fetch_from_cdn(file_name, region):
    server = edge_servers[region]
    tracker = cache_tracker[region]

    if file_name in server:
        tracker[file_name] += 1
        if tracker[file_name] <= CACHE_TTL:
            print(f"✅ Served from {region} edge cache.")
            return server[file_name]
        else:
            print(f"♻️ Cache expired on {region}. Refreshing...")
            del server[file_name]

    content = fetch_from_origin(file_name)
    server[file_name] = content
    tracker[file_name] = 1
    print(f"🆕 Cached on {region}.")
    return content

# Simulate some requests
regions = ["edge_us", "edge_eu", "edge_asia"]
for i in range(6):
    region = random.choice(regions)
    print(f"\n🌍 Request {i+1} from region: {region}")
    print(fetch_from_cdn("index.html", region))


# cdn_models.py

origin_server = {
    "style.css": "body { color: black; }",
    "app.js": "console.log('Hello')",
    "index.html": "<html><body>CDN Demo</body></html>"
}

# Edge servers
edge_us = {}
edge_eu = {}

# Push model: Preload files manually
def push_to_edge(file_name, edge_server):
    content = origin_server.get(file_name)
    if content:
        edge_server[file_name] = content
        print(f"✅ PUSHED '{file_name}' to edge.")
    else:
        print(f"❌ File '{file_name}' not found in origin.")

# Pull model: On-demand fetch
def pull_from_origin(file_name, edge_server):
    if file_name in edge_server:
        print(f"✅ SERVED from edge cache: {file_name}")
        return edge_server[file_name]
    else:
        print(f"📦 MISS - Fetching '{file_name}' from origin...")
        content = origin_server.get(file_name, "404 Not Found")
        if content != "404 Not Found":
            edge_server[file_name] = content
            print(f"🆕 Cached '{file_name}' on edge.")
        return content

# Simulation
print("\n--- PUSH CDN DEMO ---")
push_to_edge("style.css", edge_us)
print(edge_us)

print("\n--- PULL CDN DEMO ---")
pull_from_origin("index.html", edge_eu)
pull_from_origin("index.html", edge_eu)  # Served from cache now
