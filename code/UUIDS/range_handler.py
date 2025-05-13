# range_handler.py
class RangeHandler:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def generate_id(self):
        if self.current > self.end:
            raise ValueError("ID range exhausted")
        val = self.current
        self.current += 1
        return val

node1 = RangeHandler(1000, 1999)
node2 = RangeHandler(2000, 2999)

print("Node 1 ID:", node1.generate_id())
print("Node 2 ID:", node2.generate_id())
