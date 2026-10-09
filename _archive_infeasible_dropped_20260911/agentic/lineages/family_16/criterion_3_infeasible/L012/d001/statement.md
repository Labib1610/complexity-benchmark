# Problem C — Impossible Window: Certify It

Time limit: 2 s   Memory limit: 256 MB

## Description

You are auditing $j$ data-transfer routines (referred to as "jobs"). Each job consists of transmitting a header via Channel 1, followed by transmitting its payload via Channel 2. A channel can only handle one transmission at a time, and a job's payload transmission cannot begin until its header transmission has completely finished.

There is a strict operational window of $T$ microseconds. All jobs must fully complete both of their transmissions within this window.

For every input in this problem, it is guaranteed that the time window is too small, regardless of the order in which the jobs are executed. Your task is to output a short text code that proves this impossibility.

Exactly one of the following two bottleneck types will apply. Print the corresponding code:

- `JOB i` (where $i$ is the 1-based index of a violating job): The window is too short to accommodate this specific job's sequence of operations, even if it were the only job in the system.
- `LOAD c` (where $c$ is 1 or 2): The window is too short to accommodate the total active time required by Channel $c$, even if we ignore all dependencies between headers and payloads.

## Input

The first line contains two integers $j$ and $T$ ($1 \le j \le 200000$, $1 \le T \le 1000000000$).
Each of the next $j$ lines contains two integers $p_1$ and $p_2$ ($1 \le p_1, p_2 \le 1000000$): the duration in microseconds for the job's header on Channel 1 and its payload on Channel 2, respectively.

## Output

Print a single line containing either `JOB i` (if job $i$'s sequence alone violates the window) or `LOAD c` (if Channel $c$'s required workload alone violates the window).

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

In Example 1, the first job requires 70 microseconds on Channel 1 and then 60 microseconds on Channel 2 sequentially. It cannot complete its own sequence within the 100-microsecond window, making `JOB 1` a valid proof of impossibility. 

In Example 2, no individual job's sequence violates the 150-microsecond window. However, Channel 1 is assigned four header transmissions of 50 microseconds each. Since a channel operates on only one transmission at a time, it cannot complete its assigned workload within the window, making `LOAD 1` the valid proof.