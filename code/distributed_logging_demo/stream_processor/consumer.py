import time
from ingestion_api.app import get_log_queue

def process_log(log):
    # Simulate log enrichment or analysis
    print(f"[{log.get('level')}] - {log.get('message')}")

def start_consumer():
    log_queue = get_log_queue()
    print("Consumer started. Waiting for logs...")

    while True:
        if not log_queue.empty():
            log = log_queue.get()
            process_log(log)
        else:
            time.sleep(1)

if __name__ == "__main__":
    start_consumer()
