# timestamp_random_id.py
import time
import random
import string

def generate_id():
    ts = int(time.time() * 1000)
    rand = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    return f"{ts}{rand}"

print("Timestamped ID:", generate_id())
