# Problem C — Roster Infeasibility Certification

Time limit: 2 s   Memory limit: 256 MB

A facility operates across two working shifts, designated 1 and 2, but the roster rules make scheduling impossible. Rather than generating a schedule, your task is to output a proof of impossibility. It is guaranteed that there exists at least one group of three workers who all mutually conflict with one another. Any such group demonstrates that two shifts cannot suffice.

Find and output one such group of three workers. To maintain shift compliance guidelines, the worker identifiers in the chosen triple $(a, b, c)$ with $a < b < c$ must satisfy $c - a \ge 2$ and $a + b + c \ge 6$. You must output the lexicographically smallest such triple (minimizing $a$; then $b$; then $c$).

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 2 \cdot 10^5)$).
Each of the next $m$ lines contains two integers $u$ $v$ — a conflicting pair of workers.
It is guaranteed that at least one mutually conflicting triple exists.

## Output
Print three integers $a\ b\ c$ on one line with $a < b < c$ such that all three pairs $a$–$b$, $a$–$c$, $b$–$c$ are conflicts. Output the lexicographically smallest such triple (smallest $a$; ties by smallest $b$; then smallest $c$).

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
