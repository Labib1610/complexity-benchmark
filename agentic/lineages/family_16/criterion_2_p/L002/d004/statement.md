# Problem B — Cargo Inspection

Time limit: 1 s   Memory limit: 256 MB

## Description

A port authority manages a fleet of **j** vessels arriving for cargo inspection. Each vessel requires two sequential phases of clearance: a Local phase (taking **p1** minutes) and a Federal phase (taking **p2** minutes).

You must arrange the fleet into a single sequence $S = (s_1, s_2, \dots, s_j)$. Both the Local authority and the Federal authority will process the vessels in this exact same sequence.

The completion times for each vessel are determined by the following strict operational rules, evaluated from the first vessel to the last:
- Let $L_k$ be the time the Local phase finishes for the $k$-th vessel in your sequence. The Local authority processes vessels continuously one after another starting at time 0. Therefore, $L_k$ is the sum of the Local durations for the first $k$ vessels:
  $L_k = \sum_{i=1}^k p_1(s_i)$
- Let $F_k$ be the time the Federal phase finishes for the $k$-th vessel in your sequence. The Federal authority processes vessels one at a time and can only begin the $k$-th vessel when two conditions are met: the Federal phase for the previous vessel is complete (at time $F_{k-1}$), and the Local phase for the current vessel is complete (at time $L_k$). Thus, the Federal completion time is calculated as:
  - For the first vessel ($k=1$): $F_1 = L_1 + p_2(s_1)$
  - For all subsequent vessels ($k > 1$): $F_k = \max(F_{k-1}, L_k) + p_2(s_k)$

Your goal is to choose the initial sequence $S$ that minimizes the time at which the final vessel finishes its Federal phase (the value of $F_j$). Output this minimum possible value.

## Input

The first line contains a single integer **j** (1 ≤ j ≤ 200000).
Each of the next **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000): the duration required for the Local phase and the Federal phase for that vessel, respectively.

## Output

Print a single integer: the smallest possible value for $F_j$ across all valid sequences.

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

In Example 1, one optimal sequence is to process the third vessel, then the second, then the first.
- $k=1$ (third vessel): $L_1 = 1$. $F_1 = 1 + 3 = 4$.
- $k=2$ (second vessel): $L_2 = 1 + 2 = 3$. $F_2 = \max(4, 3) + 4 = 8$.
- $k=3$ (first vessel): $L_3 = 3 + 3 = 6$. $F_3 = \max(8, 6) + 2 = 10$.
The final completion time $F_3$ is 10.

In Example 2, the single vessel finishes its Local phase at 5, so $L_1 = 5$. The Federal phase finishes at $F_1 = 5 + 3 = 8$.