# Chapter 2 – Thread-Based Parallelism

Python `threading` examples built around one theme:
**University Online Examination Management System**.
Every program is standalone and has easy comments explaining each step.

## Requirements

- Python 3.8 or newer (standard library only, nothing to install)

## How to run

Open a terminal in the `PDC` folder and run any file:

```bash
python Chapter-2/01_defining_thread.py
```

## Programs

| #  | File                    | Concept                 | Exam-system scenario                    |
|----|-------------------------|-------------------------|-----------------------------------------|
| 01 | `01_defining_thread.py` | `Thread`, `start`, `join` | 5 students submit assignments together |
| 02 | `02_current_thread.py`  | `current_thread().name` | Registration, Grading, Result jobs      |
| 03 | `03_thread_subclass.py` | Thread subclass         | Students solving a paper                |
| 04 | `04_lock.py`            | `Lock`                  | Shared submission record (race condition) |
| 05 | `05_rlock.py`           | `RLock`                 | Teachers saving marks in a gradebook    |
| 06 | `06_semaphore.py`       | `Semaphore`             | Lab with only 3 computers               |
| 07 | `07_condition.py`       | `Condition`             | Submission desk with limited space      |
| 08 | `08_event.py`           | `Event`                 | Students wait for the exam to start     |
| 09 | `09_barrier.py`         | `Barrier`               | Teachers finish marking together        |
| 10 | `10_queue.py`           | `Queue`, `PriorityQueue` | Assignment submission and grading      |

## Sample output (`04_lock.py`)

```text
WITHOUT lock -> expected 200, got 51
WITH lock    -> expected 200, got 200
```

The "without lock" number changes every run. This is the race condition.