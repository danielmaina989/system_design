# Simulated Inverted Index (Shard)
class Shard:
    def __init__(self, id):
        self.id = id
        self.index = {}

    def add_document(self, doc_id, text):
        for word in text.lower().split():
            self.index.setdefault(word, set()).add(doc_id)

    def search(self, word):
        return self.index.get(word.lower(), set())

# Coordinator to search multiple shards
class SearchCoordinator:
    def __init__(self, shards):
        # Validate that all elements are instances of Shard
        if not all(isinstance(shard, Shard) for shard in shards):
            raise ValueError("All elements in shards must be instances of Shard")
        self.shards = shards

    def search(self, word):
        results = set()
        for shard in self.shards:
            results.update(shard.search(word))
        return results

# Setup
shard1 = Shard("Shard1")
shard2 = Shard("Shard2")

shard1.add_document(1, "Distributed systems are powerful")
shard2.add_document(2, "Search engines use inverted indexes")

coordinator = SearchCoordinator([shard1, shard2])
print("Search results for 'inverted':", coordinator.search("inverted"))
