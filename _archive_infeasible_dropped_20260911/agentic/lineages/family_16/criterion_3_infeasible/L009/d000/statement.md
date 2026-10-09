# Phase 1 Diagnostic

Time limit: 2 s   Memory limit: 256 MB

## Description

A factory processes $j$ work orders through exactly two stations. Every work order must be processed at Station 1 first, and then at Station 2. Each station can only process one work order at a time. The target completion time for the entire batch of orders is $T$.

You are developing the scheduling software for this factory. To optimize performance, the system runs a Phase 1 diagnostic check before proceeding to Phase 2 (the actual scheduling). 

The Phase 1 diagnostic evaluates the orders against the target time $T$ and flags structural bottlenecks. It checks for two specific conditions:

- **Individual Order Bottleneck:** If a single work order has a combined processing time (Station 1 + Station 2) that is strictly greater than $T$, output `JOB i` (where $i$ is the 1-based index of such a work order).
- **Station Bottleneck:** If the total processing time required by all work orders on Station 1 exceeds $T$, output `LOAD 1`. If the total processing time required by all work orders on Station 2 exceeds $T$, output `LOAD 2`.

For this problem, you only need to implement the Phase 1 diagnostic check. The test cases provided consist entirely of batches that trigger exactly one of these two bottleneck categories, meaning the system will always halt at Phase 1. Your program should simply output the corresponding diagnostic code.

## Input

The first line contains two integers $j$ and $T$ (1 ≤ $j$ ≤ 200,000, 1 ≤ $T$ ≤ 1,000,000,000).
Each of the next $j$ lines contains two integers $p_1$ and $p_2$ (1 ≤ $p_1, p_2$ ≤ 1,000,000): the processing times of a work order on Station 1 and Station 2.

## Output

Print a single line containing the diagnostic code: either `JOB i` (for a work order $i$ whose $p_1 + p_2$ exceeds $T$) or `LOAD c` (for a station $c$ whose total load exceeds $T$).

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

In Example 1, work order 1 requires 70 + 60 = 130 time units in sequence. Since 130 > 100, it triggers the Individual Order Bottleneck rule, resulting in `JOB 1`.
In Example 2, no single work order exceeds 150 time units. However, the sum of processing times on Station 1 is 50 + 50 + 50 + 50 = 200. Since 200 > 150, it triggers the Station Bottleneck rule, resulting in `LOAD 1`.
