# 01_defining_thread.py
# Topic: Defining a Thread
# Scenario: 5 students submit their assignments at the same time.
# Each submission runs in its own thread, so nobody waits for the others.

import threading
import time


def submit_assignment(student_name, roll_no):
    # This is the work each thread will do.
    print(f"{student_name} (Roll {roll_no}) started submitting")
    time.sleep(2)  # pretend the upload takes 2 seconds
    print(f"{student_name} (Roll {roll_no}) finished submitting")


# Our own data: (student name, roll number)
students = [("Ayesha", 101), ("Bilal", 102), ("Chaman", 103),
            ("Dua", 104), ("Eesha", 105)]

threads = []

# Step 1: create one thread for each student and start it
for name, roll in students:
    t = threading.Thread(target=submit_assignment, args=(name, roll))
    threads.append(t)
    t.start()  # the thread begins working now

# Step 2: wait until all threads are finished
for t in threads:
    t.join()

print("All assignments submitted!")
