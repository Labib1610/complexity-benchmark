# Factory Shift Audit Protocol

Time limit: 2 s   Memory limit: 256 MB

## Description
In a manufacturing plant, $n$ staff members (indexed $1$ through $n$) are assigned to operational shifts. The plant tracks $m$ recorded operational incompatibilities. Each incompatibility involves two distinct staff members and is mutual, meaning neither member can be scheduled alongside the other on the same shift.

When three staff members are all mutually incompatible with one another, any attempt to schedule all three together creates a severe operational deadlock. Internal compliance guidelines require auditing these deadlocks. Due to plant safety regulations, every triple of staff members $(a, b, c)$ evaluated for audit must have valid individual indexes bounded by $1 \le a < b < c \le n$, which naturally guarantees that $a + b + c \le 3n - 3$. 

Your task is to identify a mutually incompatible group of three distinct staff members. Specifically, among all valid triplets $(a, b, c)$ with $1 \le a < b < c \le n$ where $a$ is incompatible with $b$, $a$ is incompatible with $c$, and $b$ is incompatible with $c$, you must find and report the one that is lexicographically smallest (minimizing $a$, then $b$, then $c$).

## Input
The first line contains two space-separated integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 2\cdot 10^5)$) — the number of staff members and the number of documented mutual incompatibilities, respectively.
Each of the next $m$ lines contains two space-separated integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), representing a mutual incompatibility between staff member $u$ and staff member $v$.
It is guaranteed that at least one group of three mutually incompatible staff members exists.

## Output
Print three space-separated integers $a$, $b$, and $c$ on a single line, with $1 \le a < b < c \le n$, representing the lexicographically smallest triplet of staff members who are all pairwise incompatible.

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
