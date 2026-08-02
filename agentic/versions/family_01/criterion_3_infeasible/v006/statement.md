# Problem C — Certificate of Conflict

Time limit: 2 s   Memory limit: 256 MB

A factory attempts to assign its personnel to two work shifts, but the roster is known to be impossible due to worker incompatibilities. To certify this impossibility, you must find three workers who are mutually incompatible with each other—meaning every pair among the three has a recorded conflict. Any such group demonstrates that two shifts cannot prevent conflicting workers from sharing a shift. Output the lexicographically smallest such triple.

## Input
The first line contains two integers $n$ and $m$. The headcount $n$ is at least 3 and does not exceed the facility capacity of 2000 ($3 \le n \le 2000$). The number of recorded conflicts $m$ is at least 3 and bounded by the maximum possible worker pairings up to two hundred thousand ($3 \le m \le \min(n(n-1)/2, 2 \cdot 10^5)$).

Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$), indicating a conflict between worker $u$ and worker $v$.

It is guaranteed that at least one set of three mutually conflicting workers exists.

## Output
Print three integers $a$, $b$, $c$ on a single line with $a < b < c$ such that all three pairs $a$–$b$, $a$–$c$, and $b$–$c$ are recorded conflicts. If there are multiple such triples, output the lexicographically smallest one (the one with the smallest $a$; breaking ties with the smallest $b$; then smallest $c$).

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
