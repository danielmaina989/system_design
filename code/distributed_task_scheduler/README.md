# Distributed Task Scheduler (Demo)

A simple Python-based distributed task scheduler. Tasks are scheduled with optional delays and are executed by worker threads in parallel.

---

## 🏗️ High-Level Architecture

```text
+-------------+       +---------------+       +-------------+
|  Scheduler  |-----> |   Task Queue  |<----->|   Worker(s) |
+-------------+       +---------------+       +-------------+
                             |
                      (Thread-safe queue)
```

---

## ✨ Features

- Schedule tasks with optional delays
- Parallel execution using worker threads
- Thread-safe task queue
- Simple and extensible design

## 🚀 Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/distributed_task_scheduler.git
   cd distributed_task_scheduler
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the scheduler:**
   ```bash
   python scheduler.py
   ```

## 📂 Project Structure

```
.
├── scheduler.py        # Main scheduler logic
├── worker.py           # Worker implementation
├── queue.py            # Thread-safe task queue
└── README.md           # Project documentation
```

## 📝 License

This project is licensed under the MIT License.

