# 06_semaphore.py
# Topic: Thread synchronization using a Semaphore
# Scenario: The exam lab has only 3 computers, but 7 students arrive.
# A Semaphore(3) lets only 3 students inside at the same time.
# The other students wait until someone finishes and leaves.

import threading
import time

COMPUTERS = 3

# The counter starts at 3. Each student takes 1, and gives it back when done.
lab = threading.Semaphore(COMPUTERS)

in_use = 0                      # how many computers are busy right now
in_use_lock = threading.Lock()  # protects the 'in_use' counter


def student(name, arrives_after, exam_time):
    time.sleep(arrives_after)   # student reaches the lab a bit later
    print(f"{name} arrived and is waiting for a computer\n", end="")

    with lab:                   # take one computer (waits if all 3 are busy)
        global in_use
        with in_use_lock:
            in_use += 1
            print(f"   {name} STARTED exam   (computers busy: {in_use}/{COMPUTERS})\n", end="")

        time.sleep(exam_time)   # student is writing the exam

        with in_use_lock:
            in_use -= 1
            print(f"   {name} FINISHED exam  (computers busy: {in_use}/{COMPUTERS})\n", end="")
    # leaving the "with" block gives the computer back to the next student


# Our own data: (name, arrives after seconds, exam time in seconds)
students = [
    ("Ali", 0.0, 2), ("Bushra", 0.2, 2), ("Cyrus", 0.4, 2),
    ("Dania", 0.6, 1), ("Emaan", 0.8, 1), ("Fahad", 1.0, 1),
    ("Gul", 1.2, 1),
]

threads = [threading.Thread(target=student, args=s) for s in students]
for t in threads:
    t.start()
for t in threads:
    t.join()

print("\nLab closed. Never more than 3 students used computers at once.")