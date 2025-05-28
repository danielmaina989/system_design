from scheduler import task_queue
import threading

def worker_loop():
    print("Worker running...")
    while True:
        task_func, args, kwargs = task_queue.get()
        print(f"Executing task: {task_func.__name__}")
        try:
            task_func(*args, **kwargs)
        except Exception as e:
            print(f"Task {task_func.__name__} failed: {e}")
