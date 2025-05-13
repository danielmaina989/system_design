# snowflake_sim.py
import time

EPOCH = 1650000000000  # Custom epoch (ms)
machine_id = 1  # Unique per node

sequence = 0
last_timestamp = -1

def get_timestamp():
    return int(time.time() * 1000)

def wait_next_millis(last_ts):
    ts = get_timestamp()
    while ts <= last_ts:
        ts = get_timestamp()
    return ts

def snowflake_id():
    global last_timestamp, sequence
    ts = get_timestamp()
    if ts == last_timestamp:
        sequence += 1
        if sequence > 4095:
            ts = wait_next_millis(last_timestamp)
            sequence = 0
    else:
        sequence = 0
    last_timestamp = ts

    # 41 bits timestamp | 10 bits machine_id | 12 bits sequence
    id = ((ts - EPOCH) << 22) | (machine_id << 12) | sequence
    return id

print("Snowflake-like ID:", snowflake_id())
