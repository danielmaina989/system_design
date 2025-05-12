class VectorClock:
    def __init__(self):
        self.clock = {}

    def increment(self, node_id):
        self.clock[node_id] = self.clock.get(node_id, 0) + 1

    def update(self, other_clock):
        for node, counter in other_clock.items():
            self.clock[node] = max(self.clock.get(node, 0), counter)

    def get(self):
        return self.clock

    def __repr__(self):
        return str(self.clock)
