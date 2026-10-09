# Problem C — Proof of Impossibility

Time limit: 2 s   Memory limit: 256 MB

At a manufacturing plant, a workforce of $n$ individuals is subject to $m$ incompatibility constraints. Each constraint specifies a pair of workers who cannot be assigned to the same operational shift. The plant operates using exactly two shifts.

It is a verified property of this specific workforce that no valid assignment to the two shifts can be made without violating at least one constraint. The root cause of this failure is guaranteed to be the presence of at least one triad of workers who are completely mutually incompatible—meaning every worker in the triad has a constraint with both of the other two members of the triad.

To formally demonstrate to management why the two-shift schedule is failing, your task is to pinpoint one such triad.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$), representing the number of workers and the number of incompatibility constraints, respectively. Workers are numbered from $1$ to $n$.
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$), indicating that worker $u$ and worker $v$ cannot share a shift. Each pair is listed at most once.
It is guaranteed that at least one mutually incompatible triad exists.

## Output
Print three integers $a$, $b$, and $c$ on a single line, separated by spaces, representing the workers in the triad. You must format your output such that $a < b < c$. If there are multiple valid triads, output the one that is lexicographically smallest (i.e., minimize $a$; in case of a tie, minimize $b$; in case of a further tie, minimize $c$).

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
