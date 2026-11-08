# 04_lock.py
# Topic: Thread synchronization using a Lock
# Scenario: The exam portal has 4 submission counters. Each counter
# records 50 submissions in ONE shared total (the "submission record").
# Correct final total = 4 x 50 = 200.
#
# We run the same job twice:
#   1) WITHOUT a lock -> wrong total (race condition)
#   2) WITH a lock    -> correct total

import threading
import time

COUNTERS = 4                 # number of threads
SUBMISSIONS_PER_COUNTER = 50


class SubmissionRecord:
    def __init__(self, use_lock):
        self.total = 0                   # shared data: total submissions
        self.use_lock = use_lock
        self.lock = threading.Lock()     # the lock protects 'total'

    def _add_one(self):
        # This is the critical section: read -> add -> write.
        current = self.total             # 1) read the total
        time.sleep(0.0001)               # 2) small delay: another thread can enter here!
        self.total = current + 1         # 3) write back (may overwrite another thread's work)

    def add_submission(self):
        if self.use_lock:
            with self.lock:              # only ONE thread can be inside at a time
                self._add_one()
        else:
            self._add_one()              # no protection -> race condition


def counter(record):
    # Work done by one counter (one thread).
    for _ in range(SUBMISSIONS_PER_COUNTER):
        record.add_submission()


def run_experiment(use_lock):
    record = SubmissionRecord(use_lock)
    threads = [threading.Thread(target=counter, args=(record,))
               for _ in range(COUNTERS)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    return record.total


expected = COUNTERS * SUBMISSIONS_PER_COUNTER

without_lock = run_experiment(use_lock=False)
print(f"WITHOUT lock -> expected {expected}, got {without_lock}")

with_lock = run_experiment(use_lock=True)
print(f"WITH lock    -> expected {expected}, got {with_lock}")