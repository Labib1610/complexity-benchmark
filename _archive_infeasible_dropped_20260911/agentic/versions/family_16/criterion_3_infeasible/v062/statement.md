# Problem C — System Timeout: Impossibility Proof

Time limit: 2 s   Memory limit: 256 MB

## Description

A cloud architecture executes $j$ background jobs. The processing pipeline consists of two single-threaded microservices: the Decryption service (service 1) and the Analysis service (service 2). Each job must first pass through Decryption. Only after a job's decryption is entirely finished can the Analysis service begin processing it. For each job, you are given the exact time required by each service. Neither service can process multiple jobs concurrently.

There is a hard timeout $T$: all jobs must be fully analyzed by time $T$.

For all test cases, the timeout $T$ is mathematically impossible to satisfy, regardless of the execution order. Your task is not to find an optimal schedule, but to output a simple proof of this impossibility. Exactly one of the following reasons will always apply. Print the one that holds:

- **Individual job violation:** A single job's sequential processing time (Decryption plus Analysis) is strictly greater than $T$. Output `JOB i` where $i$ is the 1-based index of such a job.
- **Service saturation:** Because a service is single-threaded, it must be active for at least the sum of its required times across all jobs. If the total time required by service 1 or service 2 is strictly greater than $T$, the timeout cannot be met. Output `LOAD c` where $c \in \{1, 2\}$ is a service whose total required time exceeds $T$.

## Input

The first line contains two integers $j$ and $T$ ($1 \le j \le 200,000$, $1 \le T \le 1,000,000,000$).
The following $j$ lines each contain two integers $p_1$ and $p_2$ ($1 \le p_1, p_2 \le 1,000,000$), representing the time required by service 1 and service 2 respectively for that job.

## Output

Print a single line containing either `JOB i` (for a job whose $p_1 + p_2 > T$) or `LOAD c` (for a service $c$ whose total required processing time exceeds $T$).

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

In Example 1, job 1 requires $70 + 60 = 130 > 100$ time units sequentially, so `JOB 1` proves the timeout is impossible. In Example 2, no single job exceeds 150 time units, but service 1 must run for $50+50+50+50 = 200 > 150$ time units in total, so `LOAD 1` is the certificate.
