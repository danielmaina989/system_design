import hashlib
import redis

class ShardManager:
    def __init__(self, shard_configs):
        self.shards = [redis.StrictRedis(host=conf["host"], port=conf["port"]) for conf in shard_configs]

    def _get_shard(self, key):
        hash_val = int(hashlib.md5(key.encode()).hexdigest(), 16)
        return self.shards[hash_val % len(self.shards)]

    def set(self, key, value):
        shard = self._get_shard(key)
        shard.set(key, value)

    def get(self, key):
        shard = self._get_shard(key)
        return shard.get(key)


if __name__ == "__main__":
    config = [
        {"host": "127.0.0.1", "port": 6379},
        {"host": "127.0.0.1", "port": 6380}
    ]

    manager = ShardManager(config)
    manager.set("user:1001", "Alice")
    print(manager.get("user:1001"))