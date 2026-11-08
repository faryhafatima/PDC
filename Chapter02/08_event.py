# 08_event.py
# Topic: Thread synchronization using an Event
# Scenario: Students enter the exam hall at different times, but nobody
# may start writing until the invigilator announces "Exam starts".
# An Event is a flag: wait() blocks until set() is called.

import threading
import time

exam_started = threading.Event()   # OFF = exam not started, ON = exam started
START = time.perf_counter()        # to show a time line in the output


def now():
    # Seconds since the program started.
    return f"t={time.perf_counter() - START:3.1f}s"


def invigilator(wait_seconds):
    # This thread announces the start of the exam.
    print(f"{now()}  Invigilator: handing out question papers...\n", end="")
    time.sleep(wait_seconds)
    print(f"{now()}  Invigilator: EXAM STARTS NOW!\n", end="")
    exam_started.set()              # flag ON -> ALL waiting students are released


def student(name, arrives_at):
    time.sleep(arrives_at)          # student enters the hall at his own time
    if exam_started.is_set():
        print(f"{now()}  {name} arrived LATE, exam already started, starts writing\n", end="")
    else:
        print(f"{now()}  {name} arrived and is waiting for the exam to start\n", end="")
        exam_started.wait()         # blocked here until the invigilator calls set()
        print(f"{now()}  {name} starts writing\n", end="")


# Our own data: (student name, arrival time in seconds)
students = [("Ayesha", 0.5), ("Bilal", 1.0), ("Chaman", 1.5),
            ("Dua", 2.0), ("Eesha", 4.0)]   # Eesha comes after the exam has started

threads = [threading.Thread(target=invigilator, args=(3,))]
threads += [threading.Thread(target=student, args=s) for s in students]

for t in threads:
    t.start()
for t in threads:
    t.join()

print("\nAll students are writing the exam.")