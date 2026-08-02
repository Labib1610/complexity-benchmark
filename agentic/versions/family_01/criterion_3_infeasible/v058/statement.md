# Operation Resource Conflict Audit

Time limit: 2 s   Memory limit: 256 MB

## Description
An enterprise execution engine manages $n$ operations, indexed $1$ through $n$. Due to shared resource constraints, certain pairs of operations cannot run simultaneously. The system logs $m$ distinct pairwise operational conflicts. Each conflict record involves two distinct operations, and conflicts are inherently mutual.

To document an operational bottleneck, the system auditor needs to pinpoint a group of three distinct operations where every pair within the group shares a logged conflict. It is guaranteed that at least one such group of three mutually conflicting operations exists in the dataset.

To ensure consistent logging, among all candidate triplets $(a, b, c)$ satisfying $1 \le a < b < c \le n$ where $a$ conflicts with $b$, $a$ conflicts with $c$, and $b$ conflicts with $c$, you must report the lexicographically smallest triplet (that is, the one that minimizes $a$, then minimizes $b$, then minimizes $c$). Additionally, compliance rules dictate that any reported triplet must satisfy $a + b < 2n$.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 2\cdot 10^5)$) — the number of operations and the number of recorded pairwise conflicts, respectively.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n, u \neq v$), representing a pairwise conflict between operation $u$ and operation $v$.
It is guaranteed that at least one mutually conflicting group of three operations exists.

## Output
Print three space-separated integers $a$, $b$, and $c$ on a single line ($a < b < c$), representing the lexicographically smallest triplet of mutually conflicting operations.

## Example 1
Input:
```
4 5
1 2
1 3
2 3
2 4
3 4
```
Output:
```
1 2 3
```

## Example 2
Input:
```
5 6
1 2
1 4
2 4
3 4
3 5
4 5
```
Output:
```
1 2 4
```
