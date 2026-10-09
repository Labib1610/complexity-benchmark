# Problem A — Research Coordination

Time limit: 5 s   Memory limit: 256 MB

## Description

An institute has **m** laboratory stations and is managing **j** research initiatives. Every initiative requires completing a strict sequence of experimental stages. Each stage must be conducted at a designated station for a specific number of hours. The following conditions apply:

- The stages within any single initiative must be executed in the exact order they are specified. A stage can only commence after the preceding stage for that initiative has fully concluded.
- A laboratory station can only host one stage at a time.
- Once a stage begins, it must continue without interruption until its required hours are fulfilled.

Determine the earliest possible hour by which all stages for all initiatives can be entirely completed.

## Input

The first line provides two integers **j** and **m** (1 ≤ j ≤ 10, 1 ≤ m ≤ 10).
Each of the subsequent **j** lines details one initiative. A line starts with an integer **o** (the number of stages for this initiative), followed by **o** pairs of integers `station hours` (1 ≤ station ≤ m, 1 ≤ hours ≤ 1000), representing the initiative's stages in their required chronological order.
The total number of stages across all initiatives combined will not exceed 50.

## Output

Print a single integer: the earliest possible hour when all initiatives are finished.

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

In Example 1, two identical initiatives each require stations 1, 2, and 3 (2 hours each); the second initiative follows the first through the sequence and concludes at hour 8. In Example 3, the two initiatives utilize different stations and advance simultaneously, concluding at hour 4.
