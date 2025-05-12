import hashlib

class MerkleTree:
    def __init__(self, values):
        self.tree = self.build_tree([self.hash(v) for v in values])

    def hash(self, value):
        return hashlib.sha256(str(value).encode()).hexdigest()

    def build_tree(self, hashes):
        if len(hashes) == 1:
            return hashes[0]
        new_level = []
        for i in range(0, len(hashes), 2):
            left = hashes[i]
            right = hashes[i + 1] if i + 1 < len(hashes) else left
            new_level.append(self.hash(left + right))
        return self.build_tree(new_level)

    def root(self):
        return self.tree
