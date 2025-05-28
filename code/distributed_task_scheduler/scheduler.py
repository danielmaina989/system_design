import queue
import threading
import time
from tasks import example_task

task_queue = queue.Queue()

def schedule_task(task_func, delay=0, *args, **kwargs):
    def delayed_enqueue():
        time.sleep(delay)
        task_queue.put((task_func, args, kwargs))
        print(f"Task scheduled: {task_func.__name__}")
    threading.Thread(target=delayed_enqueue).start()

def dispatcher():
    print("Scheduler started...")
    while True:
        task_func, args, kwargs = task_queue.get()
        print(f"Dispatching task: {task_func.__name__}")
        threading.Thread(target=task_func, args=args, kwargs=kwargs).start()
