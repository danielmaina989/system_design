from scheduler import schedule_task, dispatcher
from tasks import example_task
import threading

if __name__ == "__main__":
    threading.Thread(target=dispatcher, daemon=True).start()

    # Schedule multiple tasks
    schedule_task(example_task, delay=1, name="Alpha", duration=2)
    schedule_task(example_task, delay=2, name="Beta", duration=3)
    schedule_task(example_task, delay=3, name="Gamma", duration=1)

    input("Press Enter to exit...\n")
