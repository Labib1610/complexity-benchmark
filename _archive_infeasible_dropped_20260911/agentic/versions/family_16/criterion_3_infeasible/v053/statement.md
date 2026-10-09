# Problem C — Impossible Window: Certify It

Time limit: 2 s   Memory limit: 256 MB

## Description

You are evaluating a proposed schedule for a batch of $j$ independent tasks (referred to as "jobs"). Each job requires a two-step procedure: it must first be processed by Unit 1 for a specific duration, and immediately upon completion there, it must be processed by Unit 2 for another specific duration. 

The processing units are subject to the following operational rules:
- A unit operates strictly sequentially, meaning it can only process one job at any given moment.
- A job cannot begin its processing at Unit 2 until it has entirely finished its required time at Unit 1.

The entire batch of $j$ jobs must be completely processed by both units within a strict timeframe of $T$ units.

For every input provided, the schedule is guaranteed to be impossible to complete within $T$, regardless of how the jobs are ordered. Your task is to output a short text code that proves this impossibility.

Exactly one of the following two structural bottlenecks will apply. Print the one that holds:

- **An individual job is too lengthy.** Even if a job were processed in isolation, its sequential nature means its time at Unit 1 plus its time at Unit 2 cannot be compressed. If this sum strictly exceeds $T$ for a job, that job alone proves the schedule impossible. Print `JOB i` — where $i$ (1-based) is such a job.

- **A processing unit is saturated.** Because a unit cannot process multiple jobs simultaneously, it must remain active for at least the sum of the durations of all jobs assigned to it. If the sum of all processing times at Unit 1 or the sum of all processing times at Unit 2 strictly exceeds $T$, the timeframe cannot be met. Print `LOAD c` — where $c$ is 1 or 2, identifying the unit whose total required time exceeds $T$.

## Input

The first line contains two integers $j$ and $T$ ($1 \le j \le 200000$, $1 \le T \le 1000000000$).
Each of the next $j$ lines contains two integers $p_1$ and $p_2$ ($1 \le p_1, p_2 \le 1000000$). These represent the required processing duration for the job at Unit 1 and Unit 2, respectively.

## Output

Print a single line containing either `JOB i` (if job $i$'s combined duration at both units exceeds $T$) or `LOAD c` (if Unit $c$'s total required processing time exceeds $T$).

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

In Example 1, the first job requires $70 + 60 = 130$ units of time in sequence. Since $130 > 100$, it cannot complete within the timeframe, making `JOB 1` the valid evidence. 

In Example 2, no individual job exceeds 150 units of time. However, Unit 1 must be active for a total of $50 + 50 + 50 + 50 = 200$ units of time. Since $200 > 150$, `LOAD 1` is the valid evidence.
