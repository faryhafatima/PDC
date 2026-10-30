# 03_thread_subclass.py
# Topic: Defining a Thread subclass
# Scenario: Four students solve their exam paper at different speeds.
# Each Student is a thread. We create our OWN class that inherits
# from threading.Thread and put the work inside its run() method.

import threading
import time


def log(message):
    # Print the whole line in one go so lines do not get mixed up.
    print(message + "\n", end="")


class Student(threading.Thread):
    # One Student object = one thread.

    def __init__(self, student_name, solving_time):
        # First call the parent class constructor and give the thread a name.
        super().__init__(name=student_name)
        self.solving_time = solving_time  # data that belongs to this thread
        self.finished_at = None           # we will fill this when done

    def run(self):
        # run() is called automatically when we write student.start()
        log(f"{self.name} started the paper ({self.solving_time}s needed)")
        time.sleep(self.solving_time)     # student is solving the paper
        self.finished_at = self.solving_time
        log(f"{self.name} SUBMITTED the paper")


# Our own data: (student name, time needed in seconds)
students = [
    Student("Hassan", 3),
    Student("Maryam", 1),
    Student("Talha", 4),
    Student("Noor", 2),
]

# Start all threads
for s in students:
    s.start()

# Wait for all of them to finish
for s in students:
    s.join()

# Because Student is OUR class, we can read its data after the work is done
topper = min(students, key=lambda s: s.finished_at)
log(f"\nFirst to submit: {topper.name} ({topper.finished_at}s)")
