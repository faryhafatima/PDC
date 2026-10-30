
# 07_condition.py
# Topic: Thread synchronization using a Condition
# Scenario: Students put answer papers on a submission desk that holds
# only 3 papers. Two teachers pick papers up from the desk.
#   - Desk FULL  -> the student has to WAIT
#   - Desk EMPTY -> the teachers have to WAIT
# A Condition lets threads wait and wakes them up when things change.

import threading
import time
from collections import deque

DESK_CAPACITY = 3

desk = deque()                      # papers currently on the desk
condition = threading.Condition()   # used for waiting and notifying
all_submitted = False               # becomes True when no more papers will come


def student_submissions(papers):
    # This thread puts papers on the desk one by one.
    global all_submitted
    for paper in papers:
        time.sleep(0.2)                       # student walks to the desk
        with condition:                       # take the condition's lock
            while len(desk) >= DESK_CAPACITY: # desk full? then wait
                print("Student: desk is full, waiting...\n", end="")
                condition.wait()              # sleep until a teacher takes a paper
            desk.append(paper)
            print(f"Student: put '{paper}' on desk  (papers on desk: {len(desk)})\n", end="")
            condition.notify_all()            # tell teachers: a new paper is here!

    with condition:
        all_submitted = True                  # no more papers will come
        condition.notify_all()                # wake teachers so they can finish


def teacher(name, checking_time):
    # Each teacher keeps taking papers until everything is done.
    while True:
        with condition:
            while not desk:                   # desk empty? then wait
                if all_submitted:             # nothing left and no more coming
                    print(f"{name}: no more papers, finished\n", end="")
                    return
                condition.wait()              # sleep until a paper arrives
            paper = desk.popleft()
            print(f"{name}: took '{paper}'   (papers on desk: {len(desk)})\n", end="")
            condition.notify_all()            # tell student: there is space now!
        time.sleep(checking_time)             # teacher checks the paper (outside the lock)


# Our own data: the papers to be submitted
papers = ["Ayesha-OS", "Bilal-OS", "Chaman-OS", "Dua-OS",
          "Eesha-OS", "Farhan-OS", "Gul-OS", "Hina-OS"]

threads = [
    threading.Thread(target=student_submissions, args=(papers,)),
    threading.Thread(target=teacher, args=("Teacher Sara", 2.0)),  # slow checking
    threading.Thread(target=teacher, args=("Teacher Omar", 2.0)),
]

for t in threads:
    t.start()
for t in threads:
    t.join()

print("\nAll papers were collected and checked.")