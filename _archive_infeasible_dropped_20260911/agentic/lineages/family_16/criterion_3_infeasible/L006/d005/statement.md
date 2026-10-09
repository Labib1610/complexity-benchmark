# SLA Rejection Certificate

Time limit: 2 s   Memory limit: 256 MB

## Description

A cloud computing platform uses a two-stage pipeline to process client requests. A batch of $j$ jobs has been submitted. Every job must be processed on machine 1 and then on machine 2. Each machine processes one job at a time without preemption. A job can only begin on machine 2 after it has completely finished on machine 1.

The client requires all $j$ jobs to be completely finished by a deadline of $T$ milliseconds. 

For every input provided, it is impossible to meet this deadline. The input guarantees that exactly one of the two following limitation categories applies. You must print a short rejection certificate from the applicable category:

- **Sequential Bottleneck:** A job cannot begin on machine 2 until it has completely finished on machine 1. For a job $i$, if $T - p_{1,i} < p_{2,i}$, it cannot complete within the deadline. If this category applies, print `JOB i` (where $i$ is the 1-based index). If multiple jobs satisfy this inequality, printing any one of them is acceptable.

- **Machine Capacity Limit:** Each machine processes one job at a time without preemption. For a machine $c \in \{1, 2\}$, if $T < \sum_{i=1}^j p_{c,i}$, the machine cannot clear all its assigned tasks within the deadline. If this category applies, print `LOAD c`. If both machines satisfy this inequality, printing either is acceptable.

Output must be consistent with the unique applicable limitation category guaranteed by the input.

## Input

The first line contains two integers $j$ and $T$ ($1 \le j \le 200000$, $1 \le T \le 1000000000$).
Each of the next $j$ lines contains two integers $p_1$ and $p_2$ ($1 \le p_1, p_2 \le 1000000$): the processing times of a job on machine 1 and machine 2, respectively.

## Output

Print a single line containing either `JOB i` (for a job qualifying under the Sequential Bottleneck) or `LOAD c` (for a machine qualifying under the Machine Capacity Limit). The output must be consistent with the unique applicable limitation category guaranteed by the input.

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

In Example 1, for job 1, $p_{1,1} = 70$ and $p_{2,1} = 60$. We check the Sequential Bottleneck inequality: $100 - 70 < 60$ is $30 < 60$, which is true. This category applies, so `JOB 1` is a valid rejection certificate.

In Example 2, no job satisfies the Sequential Bottleneck inequality. However, for machine 1, the sum of processing times is $50 + 50 + 50 + 50 = 200$. We check the Machine Capacity Limit inequality: $150 < 200$ is true. This category applies, so `LOAD 1` is a valid rejection certificate.