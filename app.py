from tasks import easy_task, medium_task, hard_task
import time

print("Starting Study Scheduler Environment...\n")

while True:
    print("Easy:", easy_task())
    print("Medium:", medium_task())
    print("Hard:", hard_task())
    print("-" * 40)

    time.sleep(10)