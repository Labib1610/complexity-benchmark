# Flow-Shop Sequence Feasibility

Time limit: 2 s   Memory limit: 256 MB

## Description

You are tasked with evaluating the feasibility of a production plan across **j!** possible execution sequences. A set of **j** items must be routed through a two-stage processing pipeline. The pipeline operates under strict constraints:
- Every item must undergo phase 1 processing followed immediately by phase 2 processing.
- Phase 1 and phase 2 are distinct processing units, and each unit can handle at most one item at any given moment.
- An item can only commence phase 2 processing once its phase 1 processing has fully concluded.

The primary objective in such environments is to discover an execution sequence of the **j** items such that the entire pipeline flushes (i.e., the final item completes phase 2) at or before a rigid time limit **T**. Because the number of possible item permutations grows factorially, evaluating all schedules is computationally demanding. For the datasets provided in this system, it is guaranteed that no valid sequence exists. Your task is to bypass the search space and directly generate a proof of infeasibility. The verification system requires a short rejection certificate that demonstrates why the deadline **T** is unachievable. You must output the appropriate certificate based on which of the following guaranteed conditions applies:

- **Item-level sequential constraint:** The total sequential duration of a single item (its phase 1 duration plus its phase 2 duration) strictly exceeds the time limit **T**. Output `JOB i`, where **i** is the 1-based index of such an item.
- **Unit-level capacity constraint:** The total accumulated active time required by one of the processing units, across all **j** items, strictly exceeds the time limit **T**. Output `LOAD c`, where **c** $\in \{1, 2\}$ is the index of the overloaded processing unit.

Exactly one of these two reasons always applies. Print the one that holds.

## Input

The first line contains two integers **j** and **T** (1 ≤ j ≤ 200000, 1 ≤ T ≤ 1000000000).
Each of the next **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000), representing the processing durations required by the item in phase 1 and phase 2, respectively.

## Output

Print a single line containing the rejection certificate: either `JOB i` (if item **i**'s total duration exceeds **T**) or `LOAD c` (if processing unit **c**'s total workload exceeds **T**).

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

In Example 1, evaluating the 6 possible schedules is unnecessary. Item 1 requires 70 + 60 = 130 time units sequentially, which is greater than the limit of 100. Thus, `JOB 1` proves the sequences are infeasible. 

In Example 2, no single item exceeds the limit of 150. However, phase 1 must process 50+50+50+50 = 200 units of work sequentially. Since 200 > 150, `LOAD 1` is the correct certificate.
