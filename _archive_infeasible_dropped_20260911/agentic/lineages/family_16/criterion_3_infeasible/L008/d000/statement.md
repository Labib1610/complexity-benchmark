# Problem C — Telemetry Window: Diagnostic Code

Time limit: 2 s   Memory limit: 256 MB

## Description

An orbital satellite is scheduled to execute **j** observation jobs before it passes out of communication range in exactly **T** milliseconds.

Each observation job requires two sequential phases:
1. First, the targeting gimbal (Subsystem 1) must orient to the correct coordinates. This takes **p1** milliseconds.
2. Afterward, the imaging sensor (Subsystem 2) must expose the frame. This takes **p2** milliseconds.

The satellite's hardware constraints dictate that:
- The targeting gimbal can only orient for one job at a time.
- The imaging sensor can only expose for one job at a time.
- For any given job, the imaging sensor cannot begin its exposure until the gimbal has completely finished orienting for that specific job.

Mission control has determined that completing all **j** jobs within the **T** millisecond window is impossible, regardless of the execution order. Your task is not to attempt a schedule, but to output a diagnostic code proving why the sequence cannot be completed. The certificate can be checked directly against the input.

Exactly one of the following diagnostic conditions always applies. Print the code for the one that holds:

- **An individual job is too lengthy.** If a single observation job's combined orientation and exposure times exceed the total window **T**, it alone proves the failure (gimbal then sensor, in sequence, cannot finish within **T**).
  Print: `JOB i` — where **i** (1-based) is such an observation job.

- **A subsystem is overloaded.** Because each subsystem operates serially, the total active time required by a subsystem cannot exceed the window **T**. If the sum of all orientation times exceeds **T**, or the sum of all exposure times exceeds **T**, the window is impossible to meet.
  Print: `LOAD c` — where **c** is the subsystem number (1 or 2) whose total load exceeds **T**.

## Input

The first line contains two integers **j** and **T** (1 ≤ j ≤ 200000, 1 ≤ T ≤ 1000000000).
Each of the next **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000): the orientation time on Subsystem 1 and the exposure time on Subsystem 2 for that observation job.

## Output

Print a single line: `JOB i` (an observation job whose p1 + p2 exceeds T) or `LOAD c` (a subsystem c whose total load exceeds T).

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

In Example 1, observation job 1 requires 70 + 60 = 130 > 100 milliseconds in sequence, so `JOB 1` proves the window is impossible. In Example 2, no single job exceeds 150 milliseconds, but Subsystem 1 must operate for 50+50+50+50 = 200 > 150 milliseconds in total, so `LOAD 1` is the correct diagnostic code.
