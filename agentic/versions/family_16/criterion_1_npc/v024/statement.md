# Problem A — Chemical Laboratory Protocols

Time limit: 5 s   Memory limit: 256 MB

## Description

A chemical testing laboratory must process **j** samples using **m** unique analytical instruments. Each sample is accompanied by a protocol that dictates a sequence of tests. Each test in a protocol requires a specific instrument for a predetermined duration.

The laboratory operates under the following constraints:
- The tests for any single sample must be performed in the exact sequence specified by its protocol. A test cannot begin until the preceding test for that sample has fully concluded.
- Each analytical instrument can process at most one test at a time.
- Once an instrument begins a test, it must run that test continuously until completion; the process cannot be paused, interrupted, or switched to another sample.

All samples and instruments are available at time zero. Determine the earliest possible time at which every test for all samples is entirely finished.

## Input

The first line contains two integers **j** and **m** (1 ≤ j ≤ 10, 1 ≤ m ≤ 10), representing the number of samples and the number of instruments, respectively.
Each of the next **j** lines describes the protocol for one sample. A protocol begins with an integer **o** (the number of tests for the sample), followed by **o** pairs of integers. Each pair provides the `instrument` (1 ≤ instrument ≤ m) and the `duration` (1 ≤ duration ≤ 1000) for a test, listed in the order they must be performed.
The total number of tests across all samples combined is at most 50.

## Output

Print a single integer: the earliest possible time at which all samples have completed their testing protocols.

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

In Example 1, two identical samples each require instruments 1, 2, and 3 in that order (taking 2 time units per test). The second sample follows the first through the instruments, finishing its final test at time 8. In Example 3, the two samples require different instruments and can be tested simultaneously, finishing at time 4.
