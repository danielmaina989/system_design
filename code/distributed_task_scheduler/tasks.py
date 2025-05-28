import time

def example_task(name, duration=2):
    print(f"Task {name} started, duration: {duration}s")
    time.sleep(duration)
    print(f"Task {name} completed")
