# 🧠 Distributed Key-Value Store Simulation

This project demonstrates fundamental concepts behind key-value stores used in distributed systems.

## 🔍 Concepts Demonstrated

- **Virtual Nodes**: Simulated by randomly selecting nodes to store data.
- **Replication**: Each key is stored on two nodes (replication factor = 2).
- **Data Versioning**: Managed via vector clocks to resolve updates.
- **Vector Clocks**: Track causality across nodes and clients.
- **Anti-Entropy**: Simplified with Merkle Trees to compare dataset consistency.

## 📂 Project Structure

keyvalue_store/
├── main.py # Entry point of the simulation
├── vector_clock.py # Vector Clock implementation
├── merkle.py # Merkle Tree for anti-entropy checks
└── README.md


## ▶️ How to Run

```bash
cd keyvalue_store
python main.py
