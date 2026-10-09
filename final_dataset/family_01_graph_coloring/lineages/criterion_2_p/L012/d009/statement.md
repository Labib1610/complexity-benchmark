# Problem B — Boolean Configuration

Time limit: 1 s
Memory limit: 256 MB

You are given $n$ boolean variables, $x_1, x_2, \dots, x_n$. Each variable must be assigned a truth value of either True or False.

You must satisfy $m$ constraints. Each constraint is given as a pair of indices $u$ and $v$, which enforces exactly two boolean clauses that must both be satisfied:
1. $(x_u \lor x_v)$
2. $(\neg x_u \lor \neg x_v)$

Your task is to determine if there exists a satisfying assignment for all variables such that every constraint is met. If a valid assignment exists, you must output it. In your output, represent True as `1` and False as `2`.

If there are multiple valid assignments, you must output the one that is lexicographically smallest when represented as a sequence of integers $h_1, h_2, \dots, h_n$ (where each $h_i \in \{1, 2\}$). A sequence $A$ is lexicographically smaller than sequence $B$ if, at the first index $i$ where they differ, the value in $A$ is strictly less than the value in $B$.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), representing a constraint between variables $x_u$ and $x_v$.

## Output
If there is no satisfying assignment, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $h_1, h_2, \dots, h_n$ (each either `1` or `2`), representing the lexicographically smallest valid assignment.

## Example 1
Input:
```
4 4
1 2
2 3
3 4
1 4
```
Output:
```
YES
1 2 1 2
```

## Example 2
Input:
```
3 3
1 2
1 3
2 3
```
Output:
```
NO
```