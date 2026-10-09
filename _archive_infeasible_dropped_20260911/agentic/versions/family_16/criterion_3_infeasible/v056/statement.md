# Pipeline Optimization: Diagnostic Certification

Time limit: 2 s   Memory limit: 256 MB

## Description

You oversee a two-stage sequential manufacturing system. A set of jobs must be processed first by an assembly station (Node 1) and then by a testing station (Node 2). Both nodes are strictly single-tasking; they can only handle one job at a time. Furthermore, a job cannot begin at Node 2 until it has fully completed its time at Node 1.

You are given a strict deadline, and you want to order the jobs such that the final job finishes at Node 2 before or exactly at the deadline. The system allows jobs to overlap across different nodes (for example, Node 2 can test one job while Node 1 assembles the next). 

However, for all configurations provided to your system, no such ordering exists. The deadline is physically impossible to meet. Your task is not to search for a valid schedule, but rather to analyze the configuration and output a diagnostic code proving why the deadline cannot be met.

Exactly one of the following two diagnostic certificates will apply to any given input. You must output the one that holds:

- **Individual Job Bound:** A specific job requires a combined duration on Node 1 and Node 2 that strictly exceeds the deadline. Because a single job must be processed sequentially across the two nodes, this job alone makes the deadline impossible, regardless of how other jobs are arranged.
  Print: `JOB i` — where **i** (1-based index) is the job that exceeds the deadline.

- **Node Saturation:** The total time required by all jobs on a single node strictly exceeds the deadline. Because each node can only process one job at a time, the pipeline cannot possibly clear this node's workload before the deadline.
  Print: `LOAD c` — where **c** is the node number (1 or 2) whose total workload exceeds the deadline.

## Input

The first line contains two integers: the total number of jobs and the deadline. The facility's loading dock can accommodate anywhere from a single job up to its maximum capacity of 200,000 jobs. The deadline is enforced by a countdown timer that can be set from 1 up to 1,000,000,000 ticks.

Each of the following lines corresponds to a job (in order from 1 to the total number of jobs) and contains two integers: the duration required on Node 1 and the duration required on Node 2. Each node's operational mechanism requires a minimum of 1 tick per job, and physical wear limits any single node operation to a maximum of 1,000,000 ticks.

## Output

Print a single line containing either `JOB i` (if job **i**'s combined duration exceeds the deadline) or `LOAD c` (if Node **c**'s total workload exceeds the deadline).

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

In Example 1, job 1 requires 70 + 60 = 130 ticks. Since 130 > 100, this job alone proves the deadline is impossible, so `JOB 1` is the correct certificate. 
In Example 2, no single job's combined time exceeds 150. However, Node 1 must process 50 + 50 + 50 + 50 = 200 ticks of work sequentially. Since 200 > 150, `LOAD 1` is the correct certificate.
