# Problem C — Proof of Impossibility

Time limit: 2 s   Memory limit: 256 MB

The manufacturing plant is trying to assign each of its employees to one of two production lines. However, certain pairs of employees have incompatible schedules and cannot be placed on the same line. 

The situation is known to be unresolvable. Your task is not to create an assignment, but to provide evidence of this failure. It is guaranteed that the provided data contains at least one group of three employees where every individual in the group has an incompatible schedule with the other two. Any such group demonstrates that two production lines cannot suffice. Output one such group.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of employees with incompatible schedules.
It is guaranteed that at least one such group of three exists.

## Output
Print three integers $a$, $b$, and $c$ on one line with $a < b < c$ such that all three pairs $a$–$b$, $a$–$c$, and $b$–$c$ are incompatible. Output the lexicographically smallest such group (smallest $a$; ties broken by smallest $b$; then smallest $c$).

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
