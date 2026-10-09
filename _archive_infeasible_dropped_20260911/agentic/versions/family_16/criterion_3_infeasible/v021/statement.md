# Problem C — Impossible Window: Certify It

Time limit: 2 s   Memory limit: 256 MB

## Description

You are auditing $j$ data-transfer routines (referred to as "jobs"). Each job consists of transmitting a header via Channel 1, followed by transmitting its payload via Channel 2. A channel can only handle one transmission at a time, and a job's payload transmission cannot begin until its header transmission has completely finished.

There is a strict operational window of $T$ microseconds. All jobs must fully complete both of their transmissions within this window.

For every input in this problem, it is guaranteed that the time window is too small, regardless of the order in which the jobs are executed. Your task is to output a short text code that proves this impossibility.

Exactly one of the following two evidence types will apply. Print the one that holds:

- **An individual job is too lengthy.** If a job's header transmission time plus its payload transmission time strictly exceeds $T$, that job alone cannot finish within the window. Print `JOB i` — where $i$ (1-based) is such a job.

- **A channel is saturated.** Because a channel operates on one transmission at a time, it must be active for at least the sum of all durations assigned to it. If the sum of all header transmission times (on Channel 1) or the sum of all payload transmission times (on Channel 2) strictly exceeds $T$, the window is impossible to meet. Print `LOAD c` — where $c$ is 1 or 2, identifying a channel whose total required time exceeds $T$.

## Input

The first line contains two integers $j$ and $T$ ($1 \le j \le 200000$, $1 \le T \le 1000000000$).
Each of the next $j$ lines contains two integers $p_1$ and $p_2$ ($1 \le p_1, p_2 \le 1000000$): the duration in microseconds for the job's header on Channel 1 and its payload on Channel 2.

## Output

Print a single line containing either `JOB i` (if job $i$'s combined duration exceeds $T$) or `LOAD c` (if Channel $c$'s total required time exceeds $T$).

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

In Example 1, the first job requires 70 + 60 = 130 microseconds in sequence. Since 130 > 100, it cannot complete within the window, making `JOB 1` the valid evidence. 

In Example 2, no individual job exceeds 150 microseconds. However, Channel 1 must be active for a total of 50 + 50 + 50 + 50 = 200 microseconds. Since 200 > 150, `LOAD 1` is the valid evidence.
