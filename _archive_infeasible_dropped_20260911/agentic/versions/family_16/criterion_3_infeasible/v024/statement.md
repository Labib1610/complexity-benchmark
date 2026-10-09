# Pipeline Optimization: Diagnostic Certification

Time limit: 2 s   Memory limit: 256 MB

## Description

You are tasked with optimizing a two-stage sequential pipeline. You are given a set of **j** computational workloads. Each workload must be processed by Node 1 and then by Node 2. Node 1 and Node 2 are strictly serial processors; neither can process more than one workload simultaneously. Furthermore, a workload cannot commence processing on Node 2 until it has entirely completed processing on Node 1.

The goal of the pipeline optimization is to determine a processing permutation—an exact sequence in which the workloads are fed into the pipeline—such that the total makespan (the time when the final workload completes on Node 2) is less than or equal to a critical threshold **T**. Because the workloads can be interleaved (e.g., workload A on Node 2 while workload B is on Node 1), the scheduling space consists of **j!** possible orderings. Evaluating these orderings to minimize idle time and find a sequence that meets the threshold **T** is the primary operational objective. It is guaranteed that for all provided inputs the deadline cannot be met by any permutation. Your system is not expected to find a working schedule, but rather to output a precise diagnostic certificate proving why the configuration cannot be scheduled within the limit.

Exactly one of the following two certificates will apply to any given input. You must print the one that holds:

- **Individual Workload Bound:** A specific workload requires more time on Node 1 and Node 2 combined than the entire threshold **T**. Since it must run sequentially, this workload alone proves the threshold is impossible regardless of interleaving.
  Print: `JOB i` — where **i** (1-based) is such a workload.

- **Sequential Node Saturation:** One of the nodes is assigned a total sum of processing times across all **j** workloads that strictly exceeds **T**. Since the node processes serially, the pipeline cannot possibly clear this node within **T**.
  Print: `LOAD c` — where **c** is 1 or 2 and the total processing time on Node **c** exceeds **T**.

## Input

The first line specifies two integers **j** and **T** (1 ≤ j ≤ 200000, 1 ≤ T ≤ 1000000000).
Each of the subsequent **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000): the processing times of a workload on Node 1 and Node 2.

## Output

Print a single line: `JOB i` (a workload whose p1 + p2 exceeds T) or `LOAD c` (a Node c whose total load exceeds T).

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

In Example 1, workload 1 requires 70 + 60 = 130 > 100 time units in absolute sequence, so `JOB 1` proves the threshold is impossible. In Example 2, no single workload exceeds 150, but Node 1 must process 50+50+50+50 = 200 > 150 units of work sequentially, so `LOAD 1` is the certificate.
