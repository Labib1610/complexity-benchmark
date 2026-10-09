# Problem A — Laboratory Execution

Time limit: 5 s   Memory limit: 256 MB

## Description

A laboratory has **m** analyzers and must execute **j** protocols. Each protocol consists of a strict sequence of phases. Every phase must be executed on a specific analyzer for a predetermined number of cycles.

The laboratory must adhere to the following physical restrictions:
- Within any single protocol, a phase cannot begin until the immediately preceding phase in its sequence has completely finished.
- An analyzer is capable of performing only one phase at any given moment.
- A phase cannot be paused or interrupted once it has commenced; it occupies its analyzer for its full duration.

Your task is to organize the execution of all phases to minimize the cycle at which the final phase concludes.

Additionally, the following guarantees apply to all configurations:
- The sum of the durations of all phases across all protocols is at most 50,000.
- No single protocol contains more than 50 phases.

## Input

The first line contains two integers **j** and **m** (1 ≤ j ≤ 10, 1 ≤ m ≤ 10).
Each of the next **j** lines describes one protocol: an integer **o** (the number of phases) followed by **o** pairs of integers `analyzer duration` (1 ≤ analyzer ≤ m, 1 ≤ duration ≤ 1000), listing the protocol's phases in order.
The total number of phases across all protocols is at most 50.

## Output

Print a single integer: the earliest possible cycle at which all protocols are finished.

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

In Example 1, two identical protocols each pass through analyzers 1, 2, and 3 (requiring 2 cycles each); the second protocol follows the first through the sequence and concludes at cycle 8. In Example 3, the two protocols utilize distinct analyzers and execute simultaneously, concluding at cycle 4.
