# Problem C — Unmeetable Quota: The Evidence

Time limit: 2 s
Memory limit: 256 MB

## Description

A manufacturing plant must fulfill $j$ work orders. Every order requires two distinct operations: a preparation phase (phase 1) followed by a finishing phase (phase 2). For any given order, its finishing phase cannot begin until its preparation phase has completely concluded. The plant has dedicated equipment for each phase, meaning it can perform preparation on at most one order at any given moment, and similarly can perform finishing on at most one order at any given moment.

There is a strict operational deadline of $T$ time units. Every single order must have both of its phases completed before this deadline.

For all test cases in this problem, it is guaranteed that meeting the deadline $T$ is impossible, regardless of the sequence in which the orders are processed. Your objective is not to attempt to schedule them, but to output a short, verifiable piece of evidence proving why the deadline cannot be met.

Based on the operational rules, exactly one of the following two reasons will apply to the input. You must print the one that holds:

- **Individual order duration:** An order's two phases cannot be executed simultaneously. If the combined time required for phase 1 and phase 2 of a specific order is strictly greater than $T$, that order alone cannot be completed in time.
  Print: `JOB i` (where $i$ is the 1-based index of the order).

- **Total phase load:** The equipment for a given phase handles only one order at a time. Therefore, the minimum time required to complete a phase for all orders is the sum of their durations for that phase. If the total time required for phase 1 (or phase 2) across all orders is strictly greater than $T$, the deadline is impossible.
  Print: `LOAD c` (where $c$ is 1 or 2, representing the phase whose total duration exceeds $T$).

## Input

The first line of the input contains two integers $j$ and $T$ ($1 \le j \le 200000$, $1 \le T \le 1000000000$).
The following $j$ lines each contain two integers $p_1$ and $p_2$ ($1 \le p_1, p_2 \le 1000000$). These represent the time required for phase 1 and phase 2 of the order, respectively.

## Output

Print a single line containing either `JOB i` (if order $i$'s total duration exceeds $T$) or `LOAD c` (if the total workload for phase $c$ exceeds $T$).

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

In Example 1, the first order requires $70 + 60 = 130$ time units. Since $130 > 100$, and the phases cannot overlap for a single order, `JOB 1` is the evidence that the deadline is unmeetable. 

In Example 2, no individual order exceeds $150$ time units. However, the preparation equipment (phase 1) must be active for $50+50+50+50 = 200$ time units. Since it can only process one order at a time, $200 > 150$ proves the deadline is unmeetable, so `LOAD 1` is the evidence.
