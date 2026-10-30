# 10_queue.py
# Topic: Thread communication using a Queue
# Scenario: Students submit assignments into a portal queue (size 4).
# Two teachers take assignments from the queue and grade them.
#   - Queue is full  -> the student waits
#   - Queue is empty -> the teacher waits
# Queue is THREAD-SAFE, so we do not need our own Lock.
# Part 2 uses a PriorityQueue: smaller number = graded FIRST.

import queue
import threading
import time

TEACHERS = 2
STOP = None   # special value that means: "no more assignments"


def log(message):
    # Print the whole line in one go so lines do not get mixed up.
    print(message + "\n", end="")


def portal(assignments, submissions):
    # PRODUCER: students put assignments into the queue.
    for name in assignments:
        submissions.put(name)   # waits here if the queue already has 4 items
        log(f"PORTAL : '{name}' submitted (in queue: {submissions.qsize()})")
        time.sleep(0.2)
    for _ in range(TEACHERS):   # one STOP signal for each teacher
        submissions.put(STOP)


def teacher(name, submissions):
    # CONSUMER: takes assignments from the queue and grades them.
    while True:
        work = submissions.get()          # waits here if the queue is empty
        if work is STOP:
            submissions.task_done()
            log(f"{name}: no more assignments, finished")
            return
        log(f"{name}: started grading '{work}'")
        time.sleep(1)                     # grading takes 1 second
        log(f"{name}: finished grading '{work}'")
        submissions.task_done()           # tell the queue this item is done


def part1_submission_portal():
    log("=== Part 1: Submission portal (Queue) ===")
    # Our own data
    assignments = ["Ayesha-Lab1", "Bilal-Lab1", "Chaman-Lab1", "Dua-Lab1",
                   "Eesha-Lab1", "Farhan-Lab1", "Gul-Lab1", "Hina-Lab1"]
    submissions = queue.Queue(maxsize=4)  # the portal holds at most 4 items

    threads = [threading.Thread(target=portal, args=(assignments, submissions))]
    threads += [threading.Thread(target=teacher, args=(f"Teacher-{i}", submissions))
                for i in range(1, TEACHERS + 1)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()


def part2_priority_grading():
    log("\n=== Part 2: Grading order (PriorityQueue) ===")
    pq = queue.PriorityQueue()
    # (priority, work): 1 = final exam, 2 = midterm, 3 = quiz
    pq.put((3, "Quiz of Ayesha"))
    pq.put((1, "Final exam of Bilal"))
    pq.put((2, "Midterm of Chaman"))
    pq.put((1, "Final exam of Dua"))
    while not pq.empty():
        priority, work = pq.get()          # always gives the smallest number first
        log(f"Teacher grades [priority {priority}] {work}")


part1_submission_portal()
part2_priority_grading()