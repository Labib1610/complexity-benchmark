# Problem A — Factory Scheduling

Time limit: 5 s   Memory limit: 256 MB

## Description

A factory contains **m** machines and is tasked with completing **j** jobs. Each job is defined as a strict sequence of operations. For every operation, there is a designated machine it must use and a specific duration it will take in time units.

The execution of operations must adhere to the following strict rules:
- Within any single job, operations must be performed in their given order. A subsequent operation can only commence after the prior operation for that job has entirely finished.
- A single machine can only be occupied by one operation at any given time.
- Once an operation begins on a machine, it must continue without interruption until its required duration is met.

Your objective is to determine a valid arrangement of all operations. Calculate and report the earliest possible time at which all operations across all jobs can be completely finished.

## Input

The first line provides two integers **j** and **m** (1 ≤ j ≤ 10, 1 ≤ m ≤ 10).
The following **j** lines each detail a single job. A line begins with an integer **o** (the total number of operations for this job), followed by **o** pairs of integers formatted as `machine duration` (1 ≤ machine ≤ m, 1 ≤ duration ≤ 1000). These pairs list the job's operations in their required sequential order.
The total number of operations across all jobs combined will not exceed 50.

## Output

Output a single integer representing the minimum possible time at which every job is fully completed.

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

## Note

In Example 1, two identical jobs both require machines 1, 2, and 3 in sequence (taking 2 time units on each). The second job follows the first through the sequence and completes at time 8. In Example 3, the two jobs utilize different machines and can be processed simultaneously, allowing them to finish at time 4.
