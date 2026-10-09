# Problem B — Cargo Inspection

Time limit: 1 s   Memory limit: 256 MB

## Description

A port authority is evaluating the risk profile of **j** vessels arriving for cargo inspection. Each vessel is associated with two time metrics: a Local inspection duration (**p1**) and a Federal inspection duration (**p2**).

You must arrange the fleet into a single sequence $S = (s_1, s_2, \dots, s_j)$. 

To evaluate the efficiency of your sequence, an independent auditor will select exactly one vessel at some position $k$ ($1 \le k \le j$) to act as the "transfer point". The delay penalty for a chosen transfer point $k$ is calculated as the sum of the Local durations for all vessels from the beginning of the sequence up to position $k$, plus the sum of the Federal durations for all vessels from position $k$ to the end of the sequence. 

Formally, for a given sequence $S$ and a chosen transfer point $k$, the penalty is:
$$ \text{Penalty}(k) = \sum_{i=1}^k p_1(s_i) + \sum_{i=k}^j p_2(s_i) $$

The auditor is adversarial and will always select the transfer point $k$ that maximizes this delay penalty. The overall clearance time of your sequence is defined as this maximum possible penalty.

Your goal is to choose the sequence $S$ that minimizes the overall clearance time. Output this minimum possible value.

## Input

The first line contains a single integer **j** (1 ≤ j ≤ 200000).
Each of the next **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000): the Local inspection duration and the Federal inspection duration for that vessel, respectively.

## Output

Print a single integer: the smallest possible overall clearance time across all valid sequences.

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

In Example 1, one optimal sequence is to place the third vessel, then the second, then the first.
The sequence of (Local, Federal) times is:
- $s_1$: (1, 3)
- $s_2$: (2, 4)
- $s_3$: (3, 2)

We evaluate the penalty for all possible transfer points $k$:
- If $k=1$: Local sum = 1. Federal sum = 3 + 4 + 2 = 9. Penalty = 10.
- If $k=2$: Local sum = 1 + 2 = 3. Federal sum = 4 + 2 = 6. Penalty = 9.
- If $k=3$: Local sum = 1 + 2 + 3 = 6. Federal sum = 2. Penalty = 8.

The auditor chooses $k=1$ to maximize the penalty, making the overall clearance time 10. No other sequence can achieve a lower maximum penalty.

In Example 2, the only vessel is placed at $s_1$. For $k=1$, the Local sum is 5 and the Federal sum is 3. The penalty is 8.