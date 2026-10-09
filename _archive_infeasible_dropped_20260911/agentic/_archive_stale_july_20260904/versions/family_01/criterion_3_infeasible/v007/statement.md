# Problem C — Shift Roster Audit

Time limit: 2 s   Memory limit: 256 MB

An auditor is reviewing a factory's shift schedule. The factory operates with exactly two shifts, but the proposed roster is known to be unworkable due to interpersonal conflicts. Your task is to provide the auditor with a concrete certificate of this impossibility. It is guaranteed that the provided list of incompatible worker pairs contains at least one group of three workers where every worker in the group conflicts with the other two. Any such group proves that two shifts are insufficient to separate all conflicting workers. Output one such group.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$), representing the number of workers and the number of incompatible pairs.
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of workers who cannot be on the same shift.
It is guaranteed that at least one group of three mutually incompatible workers exists.

## Output
Print three integers $a$, $b$, and $c$ on one line with $a < b < c$ such that all three pairs $a$–$b$, $a$–$c$, and $b$–$c$ are incompatible. Output the lexicographically smallest such group (smallest $a$; ties by smallest $b$; then smallest $c$).

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
