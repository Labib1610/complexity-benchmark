# Pipeline Pre-execution Validator

Time limit: 2 s
Memory limit: 256 MB

## Description

You are implementing a pre-execution validator for a batch of $j$ computational jobs. The jobs are scheduled to run on a two-stage pipeline consisting of Node 1 and Node 2. Every job must be fully processed by Node 1 and subsequently by Node 2. Each node can only process a single job at a time, and a job can only begin on Node 2 after it has completed on Node 1.

The entire batch is subject to a strict operational window of $T$. If the batch is deployed, every job must complete its entire sequence before time $T$ elapses.

Before the system attempts to sequence the batch, your validator must evaluate the baseline requirements and output a rejection code. The system will halt and return a code if any of the following absolute thresholds are breached:

- **Sequential duration breach:** A job's own processing requirements across both nodes prevent it from completing within the window $T$, even if it were the only job in the system.
  Output: `JOB i` — where $i$ (1-based) is the index of such a job.

- **Node capacity breach:** A single node's total active time for the entire batch exceeds the available window $T$, which would prevent it from finishing its work regardless of the order of operations.
  Output: `LOAD c` — where $c$ is 1 or 2, representing a node whose total required time exceeds $T$.

You may assume that for every provided input, exactly one of these two types of breaches will occur. Your task is to output the correct rejection code.

## Input

The first line contains two integers $j$ and $T$ (1 ≤ $j$ ≤ 200,000, 1 ≤ $T$ ≤ 1,000,000,000).
Each of the next $j$ lines contains two integers $p_1$ and $p_2$ (1 ≤ $p_1, p_2$ ≤ 1,000,000), representing the processing times of a job on Node 1 and Node 2.

## Output

Print a single line containing either `JOB i` (for a job whose $p_1 + p_2$ exceeds $T$) or `LOAD c` (for a node $c$ whose total load exceeds $T$).

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

In Example 1, job 1 requires 70 + 60 = 130 time units in sequence. Since 130 > 100, it cannot complete within the window, so `JOB 1` is the rejection code.
In Example 2, no individual job exceeds the 150 time limit, but Node 1 must process 50 + 50 + 50 + 50 = 200 units of work in total. Since 200 > 150, `LOAD 1` is the rejection code.
