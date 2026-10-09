# Problem A — Resource Alignment

Time limit: 5 s   Memory limit: 256 MB

## Description

A facility operates with a perfectly symmetric resource pool: exactly **k** operators, **k** hardware terminals, and **k** duty shifts. All resources are numbered 1 through **k**. The facility must deploy exactly **k** independent work units. Each work unit combines exactly one operator, one terminal, and one shift.

To streamline the process, the system has already filtered out all incompatible combinations. You are provided with a clean, pre-processed list of **t** fully compatible operational profiles. Each profile `(x, y, z)` indicates that operator **x**, terminal **y**, and shift **z** function together flawlessly. 

Your task is to finalize the deployment. Because the required number of work units matches the available resources perfectly, and all provided profiles are already known to be internally valid, you simply need to select exactly **k** profiles from the list such that there are no resource overlaps. Specifically, every single operator must be deployed exactly once, every terminal utilized exactly once, and every shift filled exactly once.

Determine whether such a perfectly balanced, non-overlapping selection can be extracted from the pre-processed list, and if so, report one valid configuration.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 22, 0 ≤ t ≤ k·k·k): the size of each resource pool and the number of pre-processed operational profiles.
Each of the next **t** lines contains three integers **x**, **y**, **z** (1 ≤ x, y, z ≤ k), representing a compatible profile consisting of operator **x**, terminal **y**, and shift **z**. All listed profiles are distinct.

## Output

If a valid deployment of **k** work units exists, print `YES` on the first line. Then, print **k** lines, each containing the three integers `x y z` of one selected profile. Any valid selection that perfectly utilizes all resources exactly once is accepted; the chosen profiles may be printed in any order.

If no such deployment is possible, print `NO`.

## Examples

### Example 1

**Input**
```
2 3
1 1 1
1 2 2
2 2 2
```

**Output**
```
YES
1 1 1
2 2 2
```

### Example 2

**Input**
```
2 2
1 1 1
2 1 2
```

**Output**
```
NO
```

### Example 3

**Input**
```
1 1
1 1 1
```

**Output**
```
YES
1 1 1
```

## Note

In Example 2, both compatible profiles require terminal 1, meaning terminal 2 can never be utilized.
