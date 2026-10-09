# Problem B — Two-Stage Assembly

Time limit: 1 s   Memory limit: 256 MB

## Description

A manufacturing plant is fulfilling a batch of $j$ custom orders. You must arrange the $j$ orders into a single sequence $O_1, O_2, \dots, O_j$ (a permutation of the given orders).

Each order requires a preparation phase and an assembly phase. For each order, you are given its preparation duration, $p_1$, and its assembly duration, $p_2$. Let $p_1(O_k)$ and $p_2(O_k)$ denote the respective durations for the order placed at position $k$ in your sequence.

You must assign a preparation start time $S_k$ and an assembly start time $A_k$ for each position $k$ ($1 \le k \le j$). To be valid, the schedule must satisfy the following conditions:
- Preparation for $O_{k+1}$ cannot start until preparation for $O_k$ is complete: $S_{k+1} \ge S_k + p_1(O_k)$ for $1 \le k < j$.
- Assembly for $O_k$ cannot start until its own preparation is complete: $A_k \ge S_k + p_1(O_k)$ for $1 \le k \le j$.
- Assembly for $O_{k+1}$ cannot start until assembly for $O_k$ is complete: $A_{k+1} \ge A_k + p_2(O_k)$ for $1 \le k < j$.

Assume $S_1 \ge 0$. Find a sequence of the $j$ orders and a valid schedule that minimizes the completion time of the final assembly, which is $A_j + p_2(O_j)$. Report this smallest possible completion time.

## Input

The first line contains a single integer **j** (1 ≤ j ≤ 200000).
Each of the next **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000): the preparation duration and assembly duration of an order.

## Output

Print a single integer: the smallest possible completion time of the final assembly.

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

In Example 2, there is only one order with $p_1 = 5$ and $p_2 = 3$. We can set $S_1 = 0$, so its preparation completes at 5. We then set $A_1 = 5$, and its assembly completes at $5 + 3 = 8$.