# db_autoinc_sim.py
class AutoIncrementDB:
    def __init__(self):
        self.counter = 0

    def generate_id(self):
        self.counter += 1
        return self.counter

db = AutoIncrementDB()
print("Auto-incremented ID:", db.generate_id())
