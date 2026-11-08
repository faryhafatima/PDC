# 09_barrier.py
# Topic: Thread synchronization using a Barrier
# Scenario: 4 teachers mark different sections of the same exam.
# Stage 1: every teacher marks his own section (different speeds).
# Stage 2: moderation starts ONLY after all 4 have finished marking.
# A Barrier makes all threads wait for each other at a meeting point.

import threading
import time

TEACHERS = 4
stage_number = 0   # counts completed stages (changed only by the barrier action)


def stage_finished():
    # The barrier calls this function ONCE, when the last thread arrives.
    global stage_number
    stage_number += 1
    print(f"*** All {TEACHERS} teachers are ready: stage {stage_number} complete ***\n", end="")


# Barrier(4): the first 3 threads wait until the 4th one arrives.
# 'action' runs once every time the barrier opens.
meeting_point = threading.Barrier(TEACHERS, action=stage_finished)


def teacher(name, marking_time, moderation_time):
    # ----- Stage 1: marking the answer sheets -----
    print(f"{name} started marking ({marking_time}s)...\n", end="")
    time.sleep(marking_time)
    print(f"{name} finished marking, waiting for the others\n", end="")
    meeting_point.wait()          # blocks until all 4 teachers reach this line

    # ----- Stage 2: moderation (the SAME barrier is used again) -----
    print(f"{name} started moderation ({moderation_time}s)...\n", end="")
    time.sleep(moderation_time)
    meeting_point.wait()          # second meeting point

    print(f"{name}: results are ready to publish\n", end="")


# Our own data: (teacher name, marking time, moderation time) in seconds
teachers = [("Sir Zain", 1, 1), ("Miss Yusra", 3, 1),
            ("Sir Waqar", 2, 2), ("Miss Rida", 1, 3)]

threads = [threading.Thread(target=teacher, args=t) for t in teachers]
for t in threads:
    t.start()
for t in threads:
    t.join()

print("\nResults published.")