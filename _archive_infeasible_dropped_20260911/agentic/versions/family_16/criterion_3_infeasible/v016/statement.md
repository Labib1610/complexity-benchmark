# Problem C — Inevitable Failure Certification

Time limit: 2 s   Memory limit: 256 MB

## Description

A processing facility must execute **j** jobs through two sequential phases. Every job must complete Phase 1 before it is permitted to begin Phase 2. Each phase can only work on a single job at any given moment.

Management has mandated a strict shutdown time **T**. Every single job must be completely finished by this time.

For every scenario provided, it is guaranteed that meeting the shutdown time is physically impossible, regardless of how the jobs are ordered. Your task is not to attempt scheduling, but to provide a specific proof of failure that can be verified instantly against the raw data.

Exactly one of the following two failure conditions will always apply. You must identify and print the one that holds:

- **Sequential Impossibility:** If the combined duration of Phase 1 and Phase 2 for a specific job exceeds **T**, that job alone cannot finish before the shutdown time.
  Print: `JOB i` — where **i** (1-based index) is such a job.

- **Phase Bottleneck:** Because each phase operates on one job at a time, it must remain active for the sum of all its assigned durations. If the total required time for all jobs in Phase 1 (or Phase 2) exceeds **T**, the shutdown time is impossible.
  Print: `LOAD c` — where **c** is 1 or 2 and the total duration on phase **c** exceeds **T**.

## Input

The first line contains two integers **j** and **T**. The facility's tracking system requires at least one job, and has a maximum capacity of two hundred thousand job slots. The countdown timer supports a shutdown time of at least one second, up to a maximum of one billion seconds.

Each of the subsequent **j** lines contains two integers **p1** and **p2**: the duration of the job in Phase 1 and Phase 2, respectively. A phase requires a duration of at least one second, and the machinery's safety shutoff limits any single phase duration to a maximum of one million seconds.

## Output

Print a single line: `JOB i` (a job whose combined Phase 1 and Phase 2 duration exceeds **T**) or `LOAD c` (a phase **c** whose total duration across all jobs exceeds **T**).

## Examples

### Example 1

**Input**
```
3 100
70 60
2 2
3 4
```

**Output**
```
JOB 1
```

### Example 2

**Input**
```
4 150
50 1
50 1
50 1
50 1
```

**Output**
```
LOAD 1
```

## Note

In Example 1, job 1 requires 70 + 60 = 130 time units in sequence. Since 130 > 100, `JOB 1` proves the shutdown time cannot be met. In Example 2, no individual job's sequential time exceeds 150, but Phase 1 must remain active for 50 + 50 + 50 + 50 = 200 total units of work. Since 200 > 150, `LOAD 1` is the correct proof of failure.
