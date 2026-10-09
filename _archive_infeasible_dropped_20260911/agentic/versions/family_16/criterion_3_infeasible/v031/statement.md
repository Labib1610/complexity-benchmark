# Unachievable Logistics: Provide the Evidence

Time limit: 2 s   Memory limit: 256 MB

## Description

A freight company is tasked with fulfilling **j** delivery jobs. Every job must first complete an overseas voyage (leg 1) and subsequently an overland route (leg 2). For each job, you are provided with its transit duration on leg 1 and on leg 2. The company operates a single vessel for leg 1 and a single train for leg 2; thus, each leg can only handle one job at a time. A job is only ready for leg 2 after its leg 1 transit concludes.

Management expects all deliveries to be finalized within a strict time window of **T** hours.

For every dataset evaluated, it is **certain that the target window cannot be satisfied**, regardless of the sequence in which the jobs are dispatched. You are not asked to find a dispatch sequence. Instead, you must **demonstrate** that the target is unachievable by providing a concise piece of evidence that can be immediately verified against the provided durations.

Exactly one of the following two scenarios always applies. Print the one that holds:

- **An individual job is too lengthy.** If a specific job's combined duration across both legs exceeds **T**, that job alone (leg 1 followed immediately by leg 2) cannot be completed within the window.
  Print: `JOB i` — where **i** (1-indexed) is the ID of such a job.

- **A transit leg is saturated.** Since each leg processes jobs sequentially, it requires an amount of time at least equal to the sum of all its assigned durations. If the aggregate transit time required for leg 1 (or leg 2) is strictly greater than **T**, the target is unachievable.
  Print: `LOAD c` — where **c** is 1 or 2, representing the leg whose total duration exceeds **T**.

## Input

The first line contains two integers **j** and **T** (1 ≤ j ≤ 200000, 1 ≤ T ≤ 1000000000).
Each of the next **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000): the transit durations of the job on leg 1 and leg 2, respectively.

## Output

Print a single line: `JOB i` (a job whose p1 + p2 exceeds T) or `LOAD c` (a leg c whose total duration exceeds T).

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

In Example 1, job 1 requires 70 + 60 = 130 hours in succession. Since 130 > 100, `JOB 1` demonstrates the target is unachievable. 
In Example 2, no individual job exceeds 150 hours. However, leg 1 must accommodate 50+50+50+50 = 200 hours of transit in total. Since 200 > 150, `LOAD 1` is the correct evidence.
