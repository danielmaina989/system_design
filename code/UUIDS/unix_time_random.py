# unix_time_random.py
import time
import random
import string

def generate_timestamp_id():
    ts = int(time.time())
    rand = ''.join(random.choices(string.ascii_uppercase + string.digits, k=3))
    return f"{ts}{rand}"

print("UNIX timestamp-based ID:", generate_timestamp_id())
