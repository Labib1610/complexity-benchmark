# Shift Impossibility Certification

Time limit: 2 s   Memory limit: 256 MB

An automated shift scheduling system aggregates worker conflict records into paired conflict logs. To certify that a valid schedule cannot be produced, the auditing pipeline isolates mutual conflict clusters consisting of three distinct workers where every pair within the trio has a recorded conflict.

You are tasked with identifying one such mutual conflict cluster $(a, b, c)$ satisfying $1 \le a < b < c \le n$. To comply with logging regulations, any reported cluster must satisfy the index verification rule $a + b \le 2c - 3$. If multiple mutual conflict clusters exist, you must output the one that is lexicographically smallest (that is, minimizing $a$; then minimizing $b$; then minimizing $c$).

It is guaranteed that at least one mutual conflict cluster exists in the input data.

## Input
The first line contains two space-separated integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n\cdot(n-1)/2, 2\cdot 10^5)$), representing the number of workers (indexed $1$ through $n$) and the number of conflicting worker pairs, respectively.
Each of the next $m$ lines contains two space-separated integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), representing a recorded conflict between worker $u$ and worker $v$.
It is guaranteed that at least one group of three workers who all pairwise conflict exists.

## Output
Print three space-separated integers $a$, $b$, and $c$ on a single line ($a < b < c$) representing the lexicographically smallest triple where all three pairs $(a, b)$, $(a, c)$, and $(b, c)$ are recorded conflicts.

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
