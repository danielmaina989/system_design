# 📬 Distributed Messaging Queue (Python Simulation)

This project simulates basic distributed messaging queue models used in system design, including:

- Primary-Secondary replication
- A cluster of independent brokers

## ✨ Features

- Simulated message publishing and consuming
- Support for both replicated and sharded broker models
- Multithreaded consumers for real-time simulation

## 🧠 Concepts Covered

- Decoupling microservices using messaging
- Durability through replication (Primary-Secondary)
- Load distribution with clustered brokers
- High availability and eventual consistency

## 📚 What is a Distributed Messaging Queue?

A **distributed messaging queue** is a system that enables asynchronous communication between different components or services, often across multiple servers or data centers. It provides a reliable way to send, store, and receive messages, ensuring that messages are not lost even if parts of the system fail.

### Key Benefits

- **Scalability:** Easily handle increased load by adding more brokers or consumers.
- **Fault Tolerance:** Replication and clustering ensure the system remains available even if some nodes fail.
- **Loose Coupling:** Producers and consumers do not need to interact directly, allowing independent scaling and deployment.
- **Durability:** Messages are persisted to prevent data loss.

### Common Use Cases

- Microservices communication
- Event-driven architectures
- Task queues and background processing
- Data pipeline buffering

## 🚀 Getting Started

```bash
python distributed_queue.py
```

## 🛠️ How It Works

- **Primary-Secondary Replication:** One broker acts as the primary, handling all writes, while secondary brokers replicate the data for durability.
- **Clustered Brokers:** Multiple brokers operate independently, and messages are distributed (sharded) among them for load balancing.

## 📦 Example Technologies

Real-world distributed messaging queues include:
- Apache Kafka
- RabbitMQ
- Amazon SQS
- NATS

---

Feel free to explore the code and experiment with different configurations to deepen your understanding of distributed messaging systems!
