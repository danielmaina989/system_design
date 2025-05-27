# 📝 Distributed Logging Demo

This project is a minimal example of a distributed logging system using Python. It demonstrates:

- A log agent that sends logs to a central ingestion API.
- A central ingestion service that receives logs.
- A stream processor that consumes and processes logs in real-time.

---

## 📂 Project Structure

distributed_logging_demo/
├── log_agent/
│   └── log_agent.py   # Log generator and sender
├── ingestion_api/
│   └── app.py         # Flask API that receives logs
├── stream_processor/
│   └── consumer.py    # Consumer that processes logs
└── README.md          # This file

---

## 🚀 How It Works

1. **Log Agent** (`log_agent.py`): Simulates client applications generating logs and sending them to the ingestion API via HTTP POST.
2. **Ingestion API** (`app.py`): A Flask app that receives logs and stores them in a queue (simulating a Kafka broker).
3. **Stream Processor** (`consumer.py`): Reads from the queue and processes each log (prints to console, but could do more).

---

## ⚙️ Setup Instructions

### Prerequisites

- Python 3.7+
- pip

### Install dependencies

```bash
pip install flask requests
```

---

## 🏃‍♂️ Running the Demo

1. **Start the Ingestion API**  
    In one terminal:
    ```bash
    cd ingestion_api
    python app.py
    ```

2. **Start the Stream Processor**  
    In another terminal:
    ```bash
    cd stream_processor
    python consumer.py
    ```

3. **Run the Log Agent**  
    In a third terminal:
    ```bash
    cd log_agent
    python log_agent.py
    ```

---

## 🧩 Extending the Demo

- Replace the in-memory queue with a real message broker (e.g., Kafka, RabbitMQ).
- Add authentication and error handling to the ingestion API.
- Enhance the stream processor to store logs in a database or trigger alerts.

---

## 📖 References

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Python Requests](https://docs.python-requests.org/)

---

## 📝 License

This project is licensed under the MIT License.
