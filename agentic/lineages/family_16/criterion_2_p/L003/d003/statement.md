# Problem B — Order Fulfillment

Time limit: 1 s   Memory limit: 256 MB

## Description

A system must evaluate a batch of **j** independent tasks. Each task requires two evaluation steps: the Alpha step and the Beta step.

You must define a single global sequence for the tasks. The scheduling of these steps follows strict timing rules:
- The Alpha steps are evaluated in your chosen sequence. The first task's Alpha step begins at time 0. The Alpha step for each subsequent task begins exactly at the moment the previous task's Alpha step ends.
- The Beta steps are evaluated in the exact same sequence.
- A task's Beta step cannot begin until both of the following conditions are met:
  1. The task's own Alpha step has ended.
  2. The Beta step of the previous task in your sequence has ended (this condition does not apply to the first task in the sequence).
- Each task's Beta step begins at the earliest possible moment that satisfies both conditions.

Given the duration **p1** required for the Alpha step and the duration **p2** required for the Beta step for each task, determine the optimal sequence. Your objective is to minimize the time at which the final task's Beta step ends. Output this minimum possible time.

## Input

The first line contains a single integer **j** (1 ≤ j ≤ 200000).
Each of the next **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000): the durations required for a task's Alpha step and Beta step, respectively.

## Output

Print a single integer: the smallest possible time at which the final task completes its Beta step.

## Examples

### Example 1

**Input**
```
3
3 2
2 4
1 3
```

**Output**
```
10
```

### Example 2

**Input**
```
1
5 3
```

**Output**
```
8
```

### Example 3

**Input**
```
3
2 2
2 2
2 2
```

**Output**
```
8
```

## Note

In Example 2, the single task takes 5 for the Alpha step and 3 for the Beta step, finishing its Beta step at time 8.