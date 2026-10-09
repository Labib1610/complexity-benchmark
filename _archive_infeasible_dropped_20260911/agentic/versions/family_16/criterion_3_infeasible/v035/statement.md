# Problem C — System Bottleneck Certification

Time limit: 2 s   Memory limit: 256 MB

## Description

You are given **j** jobs to be executed in a dual-component environment. Each job has a duration on Component 1, followed sequentially by a duration on Component 2. Components are strictly serial and process one job at a time. A job transitions to Component 2 only after its Component 1 phase concludes.

To find an optimal execution plan, one would typically explore the **j!** possible orderings of jobs, scheduling them as early as possible on the components to minimize the final completion time. Your objective is to determine if there exists any permutation of jobs such that the entire workload finishes by a strict threshold **T**.

Because the space of **j!** permutations is vast, analyzing every sequence might seem required. However, in all provided test cases, no valid permutation exists—the threshold **T** is always breached regardless of the schedule. Rather than searching the configuration space, your program must identify the structural bottleneck that prevents any arrangement from succeeding.

The test cases are designed such that exactly one of the following fundamental bottlenecks is responsible for the failure. Print the one that holds:

- **Isolated Job Duration.** The sequential dependency of a single job makes it too long. Print `JOB i`, where **i** (1-based) is a job whose combined duration on Component 1 and Component 2 strictly exceeds **T**.
- **Component Saturation.** The cumulative active time required by a single component breaches the threshold. Print `LOAD c`, where **c** is the component index (1 or 2) whose sum of durations across all **j** jobs strictly exceeds **T**.

## Input

The first line contains two integers **j** and **T** (1 ≤ j ≤ 200000, 1 ≤ T ≤ 1000000000).
Each of the next **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000): the durations of a job on Component 1 and Component 2.

## Output

Print a single line: `JOB i` (for a job whose p1 + p2 exceeds T) or `LOAD c` (for a component c whose total required time exceeds T).

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

In Example 1, analyzing all 6 permutations is unnecessary because job 1 alone requires 70 + 60 = 130 > 100 time units in sequence, making any arrangement breach the threshold. Thus, `JOB 1` is the bottleneck. In Example 2, no single job exceeds 150, but Component 1 must process 50+50+50+50 = 200 > 150 units of work in total regardless of ordering, so `LOAD 1` is the bottleneck.
