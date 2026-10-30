# 02_current_thread.py
# Topic: Determining the current thread
# Scenario: In the exam system, three jobs run at the same time:
# Registration, Grading and Result. Every message in the log
# should show WHICH thread (job) printed it.

import threading
import time


def log(message):
    # threading.current_thread().name gives the name of the thread
    # that is running this line right now.
    # We add "\n" inside the text and use end="" so the whole line
    # is printed in one go (otherwise lines can get mixed up).
    print(f"[{threading.current_thread().name}] {message}\n", end="")


def registration():
    log("checking student ID cards...")
    time.sleep(1)
    log("all students verified")


def grading():
    log("checking answer sheets...")
    time.sleep(2)
    log("marks calculated")


def result():
    log("preparing result sheet...")
    time.sleep(3)
    log("result published")


# Two threads get our own names. The third has no name,
# so Python gives it a default name like "Thread-1".
t1 = threading.Thread(name="Registration", target=registration)
t2 = threading.Thread(name="Grading", target=grading)
t3 = threading.Thread(target=result)

for t in (t1, t2, t3):
    t.start()

for t in (t1, t2, t3):
    t.join()

# This line runs in the main thread (the program itself)
log("all jobs finished")