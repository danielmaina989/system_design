# Distributed Cache

A distributed cache is a system that stores data across multiple nodes to provide fast, scalable, and reliable access to frequently used data.

## Features

- **Scalability:** Easily add or remove nodes to handle varying loads.
- **Fault Tolerance:** Data replication ensures high availability.
- **Consistency:** Configurable consistency models (eventual, strong).
- **Eviction Policies:** Supports LRU, LFU, and custom policies.
- **APIs:** Simple RESTful and/or gRPC interfaces for integration.

## Architecture

```
+-----------+      +-----------+      +-----------+
|  Client   | <--> |  Cache    | <--> |  Storage  |
+-----------+      +-----------+      +-----------+
         \        /         \        /
        +-----------+      +-----------+
        |  Cache    |      |  Cache    |
        +-----------+      +-----------+
```

- **Clients** interact with the cache cluster.
- **Cache Nodes** store and replicate data.
- **Storage** (optional) for persistence.

## Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-org/distributed-cache.git
   cd distributed-cache
   ```

2. **Run the cache nodes:**
   ```bash
   docker-compose up
   ```

3. **Use the API:**
   ```bash
   curl -X PUT http://localhost:8080/cache/mykey -d 'myvalue'
   curl http://localhost:8080/cache/mykey
   ```

## Configuration

- `CACHE_SIZE`: Maximum items per node.
- `REPLICATION_FACTOR`: Number of replicas.
- `EVICTION_POLICY`: LRU, LFU, etc.

## Contributing

Contributions are welcome! Please open issues or submit pull requests.

## License

MIT License
