# Problem C — Pipeline Pre-Check

Time limit: 2 s
Memory limit: 256 MB

## Description

The automated data pipeline has three stages: Ingestion, Pre-Check, and Assignment. You are building the **Pre-Check** component.

During Ingestion, a user submits $j$ work orders and a maximum time limit $T$. Every order requires two consecutive steps: it must go through the Primary Workstation, and after that finishes, it must go through the Secondary Workstation. A workstation is capable of handling only one order at any given moment.

The purpose of the Pre-Check component is to quickly filter out submissions that cannot possibly finish within the time limit $T$, skipping the computationally intense Assignment stage. For this problem, every submitted set of orders is guaranteed to be impossible to complete. Your code must not try to find an exact assignment of start times; instead, it must produce a short proof showing why the submission is invalid.

Every submission will contain exactly one of the following two fundamental flaws. Your code must determine which flaw is present and output the corresponding proof code:

- **Single Order Impossibility:** An order's total required time (its duration on the Primary Workstation plus its duration on the Secondary Workstation) is strictly greater than the time limit $T$. Because the steps are consecutive, this order alone would exceed the limit even if no other orders existed.
  Output: `JOB i` (where `i` is the 1-based index of this order).

- **Workstation Overload:** Because a workstation handles only one order at any given moment, its total active time will be exactly the sum of its required durations for all orders. If this sum for the Primary Workstation (or the Secondary Workstation) is strictly greater than the limit $T$, the submission cannot finish in time.
  Output: `LOAD c` (where `c` is 1 if the Primary Workstation is overloaded, or 2 if the Secondary Workstation is overloaded).

## Input

The first line provides two integers $j$ and $T$ (1 ≤ $j$ ≤ 200000, 1 ≤ $T$ ≤ 1000000000), representing the number of work orders and the time limit, respectively.
Each of the following $j$ lines provides two integers $p_1$ and $p_2$ (1 ≤ $p_1, p_2$ ≤ 1000000). These are the required durations of the order on the Primary Workstation and the Secondary Workstation.

## Output

Print a single line containing the proof code: either `JOB i` (for an order whose combined duration $p_1 + p_2$ exceeds $T$) or `LOAD c` (for a workstation $c$ whose total sum of durations exceeds $T$).

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

In Example 1, the first order requires 70 + 60 = 130 time units across both workstations. Since 130 > 100, the order violates the limit on its own, so `JOB 1` is the correct proof code.
In Example 2, no individual order exceeds the limit of 150. However, the Primary Workstation must run for a total of 50 + 50 + 50 + 50 = 200 time units. Since 200 > 150, the Primary Workstation is overloaded, making `LOAD 1` the correct proof code.
