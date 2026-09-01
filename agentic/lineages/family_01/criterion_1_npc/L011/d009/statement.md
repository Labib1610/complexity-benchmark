# Problem A — System State Configuration

Time limit: 2 s   Memory limit: 256 MB

You are configuring a system with $n$ components, indexed from $1$ to $n$. Each component $i$ must be assigned a discrete state vector $V_i$, chosen from exactly one of three available vectors: $A = (1, 1, 0)$, $B = (1, 0, 1)$, or $C = (0, 1, 1)$.

The system is subject to $m$ interference constraints. Each constraint specifies a pair of components $u$ and $v$ that interact. To ensure system stability, the state vectors assigned to any interacting pair must have a dot product of exactly 1. That is, the assignment must satisfy the condition $V_u \cdot V_v = 1$.

For reporting purposes, the complete configuration of the system is represented by a sequence of $n$ integers $c_1, c_2, \ldots, c_n$. The value of $c_i$ is determined by the state vector assigned to component $i$:
- $c_i = 1$ if $V_i = (1, 1, 0)$
- $c_i = 2$ if $V_i = (1, 0, 1)$
- $c_i = 3$ if $V_i = (0, 1, 1)$

If there are multiple stable configurations, you must select the one whose configuration sequence $c_1, c_2, \ldots, c_n$ is lexicographically smallest. That is, when comparing two valid sequences, the one with the smaller integer value at the first index where they differ is strictly preferred.

Determine if a stable configuration exists, and if so, output the optimal configuration sequence.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$), representing the number of components and the number of interference constraints.
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating that component $u$ and component $v$ interact and their assigned state vectors must satisfy the dot product condition.

## Output
If no stable configuration is possible, print a single line containing `NO`.
If a stable configuration is possible, print `YES` on the first line. On the second line, print exactly $n$ integers $c_1, c_2, \ldots, c_n$, where $c_i \in \{1, 2, 3\}$ is the integer representation of the state vector assigned to component $i$. Among all stable configurations, you must output the lexicographically smallest sequence $c_1, c_2, \ldots, c_n$ (compare $c_1$ first, then $c_2$, etc.).

## Example 1
Input:
```
4 5
1 2
1 3
2 3
1 4
2 4
```
Output:
```
YES
1 2 3 3
```

## Example 2
Input:
```
4 6
1 2
1 3
1 4
2 3
2 4
3 4
```
Output:
```
NO
```