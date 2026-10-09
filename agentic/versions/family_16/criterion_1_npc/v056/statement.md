# Problem A — System Coordination

Time limit: 5 s   Memory limit: 256 MB

## Description

A computing cluster consists of **m** distinct processors. It receives a batch of **j** jobs. Each job requires executing a predefined sequence of tasks. Each task specifies which processor must execute it and exactly how many clock cycles it takes.

The execution must adhere to the following strict rules:
- Tasks within the same job must be executed strictly in the order they are provided. A task cannot begin until the immediately preceding task in the same job has fully completed.
- A processor can execute at most one task at any given moment.
- Once a processor begins a task, it must process it continuously until the task is finished (no preemption).

Additionally, it is guaranteed that no single job contains more than 50 tasks, and the sum of the cycle durations for all tasks across all jobs is at most 50,000.

Your objective is to determine a valid execution timeline for all tasks such that the entire batch of jobs is finished as early as possible. Output the smallest possible clock cycle at which the final task among all jobs completes.

## Input

The first line provides two integers **j** and **m** (1 ≤ j ≤ 10, 1 ≤ m ≤ 10), representing the number of jobs and processors, respectively.
The following **j** lines each detail a single job. A job is described by an integer **o** (the number of tasks for this job), followed by **o** pairs of integers. Each pair `p c` (1 ≤ p ≤ m, 1 ≤ c ≤ 1000) indicates that the task must run on processor **p** for **c** clock cycles. The pairs are listed in the required execution order for that job. 

The total number of tasks across all jobs is at most 50.

## Output

Print a single integer: the earliest possible clock cycle when all tasks of all jobs are completely finished.

## Examples

### Example 1

**Input**
```
2 3
3 1 2 2 2 3 2
3 1 2 2 2 3 2
```

**Output**
```
8
```

### Example 2

**Input**
```
1 3
3 1 5 2 3 3 2
```

**Output**
```
10
```

### Example 3

**Input**
```
2 3
1 1 4
1 2 3
```

**Output**
```
4
```
