# Distributed Shard Design with Redis

This project demonstrates a simple sharding mechanism using Python and Redis to distribute data across multiple nodes.

## 🔧 Setup

1. Install Redis:
2. Run multiple Redis servers on different ports:
```bash
redis-server --port 6379
redis-server --port 6380
```
3. Install Python dependencies:
```bash
pip install redis
```
4. Clone this repository and navigate to the project directory.

## 🚀 Usage

- Update the configuration to list your Redis node addresses and ports.
- Run the sharding script to start distributing data.

## 📁 Project Structure

- `shard.py` — Main sharding logic.
- `config.py` — Configuration for Redis nodes.
- `README.md` — Project documentation.

## 📝 Notes

- Ensure all Redis servers are running before starting the sharding script.
- This is a basic demonstration and not production-ready.

## 📚 References

- [Redis Documentation](https://redis.io/documentation)
- [Python Redis Client](https://pypi.org/project/redis/)