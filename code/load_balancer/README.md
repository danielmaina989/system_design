# ⚖️ Load Balancer Simulation

A simple Python simulation that demonstrates how a load balancer distributes incoming traffic to multiple backend servers using a **round-robin** strategy.

## 📦 What It Demonstrates

- Backend servers handling requests
- Load balancer evenly distributing client traffic
- Round-robin algorithm in action

## 🔄 Load Balancing Strategy

**Round Robin**: Each incoming request is forwarded to the next available server in rotation, ensuring an even spread of traffic.

## 📁 Project Structure


## ▶️ Run the Simulation

```bash
cd code/load_balancer

# Run simple DNS resolution
python main.py

➡️  Distributing request 1 to server S1
✅ Server S1 handled request 1
➡️  Distributing request 2 to server S2
✅ Server S2 handled request 2
➡️  Distributing request 3 to server S3
✅ Server S3 handled request 3
...


