# 05_rlock.py
# Topic: Thread synchronization using an RLock (re-entrant lock)
# Scenario: Two teachers save exam marks into ONE shared gradebook.
# record_batch() locks the gradebook and then calls record_mark(),
# which needs the SAME lock again (nested locking).
# A normal Lock would freeze here. An RLock allows it.

import threading
import time


def plain_lock_problem():
    # Small demo: a normal Lock cannot be taken twice by the same thread.
    lock = threading.Lock()
    lock.acquire()                    # first time: works
    got_it = lock.acquire(timeout=1)  # second time by the SAME thread
    print(f"Normal Lock, second acquire worked? {got_it}")
    print("(Without the timeout, the program would wait forever)\n")
    lock.release()


class GradeBook:
    def __init__(self):
        self.marks = {}                # student -> marks
        self.lock = threading.RLock()  # RLock: same thread may lock again

    def record_mark(self, student, mark):
        with self.lock:                # lock taken (2nd time when called from batch)
            self.marks[student] = mark
            print(f"   saved {student}: {mark}\n", end="")
            time.sleep(0.2)            # saving takes a little time

    def record_batch(self, teacher, papers):
        with self.lock:                # lock taken (1st time)
            print(f"{teacher} started saving {len(papers)} marks\n", end="")
            for student, mark in papers:
                self.record_mark(student, mark)  # needs the lock again -> RLock allows it
            print(f"{teacher} finished saving\n", end="")


plain_lock_problem()

book = GradeBook()

# Our own data: each teacher has a batch of (student, marks)
batch_1 = [("Ayesha", 85), ("Bilal", 72), ("Chaman", 90)]
batch_2 = [("Dua", 66), ("Eesha", 78), ("Farhan", 88)]

t1 = threading.Thread(target=book.record_batch, args=("Teacher Sara", batch_1))
t2 = threading.Thread(target=book.record_batch, args=("Teacher Omar", batch_2))

t1.start()
t2.start()
t1.join()
t2.join()

print(f"\nGradebook has {len(book.marks)} students: {book.marks}")