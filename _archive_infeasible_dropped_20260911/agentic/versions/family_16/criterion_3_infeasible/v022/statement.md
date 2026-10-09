# Problem C — Rift Seal: Denial Certificate

Time limit: 2 s   Memory limit: 256 MB

## Description

An arcane guild must complete **j** magical rituals (logged as **jobs**) to seal a dimensional rift. Every job requires two sequential steps: first, it must be channeled through the Earth Monolith (Focus 1), and subsequently through the Sky Monolith (Focus 2). For each job, you are given the channeling time required at Focus 1 and Focus 2. Each monolith can only channel one job at a time, and a job can only begin channeling at Focus 2 after its channeling at Focus 1 is completely finished.

The rift will fully open in exactly **T** seconds: every job must be entirely completed by time **T**.

For every input in this problem, it is **guaranteed that the time limit cannot be met**, regardless of the order in which the jobs are channeled. Your task is not to search for a valid order, but to **prove** the time limit is impossible to meet with a short certificate that can be checked directly against the input.

Exactly one of the following reasons always applies. Print the one that holds:

- **A single job takes too long.** If a job's two channeling times sum to more than **T**, that job alone (Focus 1 then Focus 2, in sequence) cannot finish by **T**.
  Print: `JOB i` — where **i** (1-based) is the index of such a job.

- **A monolith is overloaded.** A monolith channels jobs one at a time, so it must bear a continuous magical load for at least the sum of all its individual channeling times. If the total load on Focus 1 (or Focus 2) exceeds **T**, the time limit is impossible.
  Print: `LOAD c` — where **c** is 1 or 2 and the total channeling time on Focus **c** exceeds **T**.

## Input

The first line contains two integers **j** and **T** (1 ≤ j ≤ 200000, 1 ≤ T ≤ 1000000000).
Each of the next **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000): the channeling times of a job at Focus 1 and Focus 2.

## Output

Print a single line: `JOB i` (a job whose p1 + p2 exceeds T) or `LOAD c` (a Focus c whose total load exceeds T).

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

In Example 1, job 1 needs 70 + 60 = 130 > 100 seconds in sequence, so `JOB 1` proves the time limit is impossible. In Example 2 no single job exceeds 150, but Focus 1 must handle 50+50+50+50 = 200 > 150 seconds of load in total, so `LOAD 1` is the certificate.
