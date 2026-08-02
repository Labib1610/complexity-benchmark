# Technician Crew Incompatibility Auditor

Time limit: 2 s   Memory limit: 256 MB

In an automated manufacturing facility, pairs of technicians are flagged as incompatible if they cannot work on the same assembly team. Quality managers need to document fundamental scheduling bottlenecks by finding three distinct technicians who are mutually incompatible—meaning every pair among the three has a recorded incompatibility.

Given the total number of technicians and the list of pairwise incompatibility records, your goal is to find three technicians $a, b, c$ with $1 \le a < b < c \le n$ such that $a$ and $b$ are incompatible, $a$ and $c$ are incompatible, and $b$ and $c$ are incompatible. If there are multiple such groups of three, output the one that is lexicographically smallest (i.e., minimizing $a$; then $b$; then $c$).

## Input
The first line contains two space-separated integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 2 \cdot 10^5)$), representing the number of technicians (indexed $1$ through $n$) and the number of recorded pairwise incompatibilities.
Each of the following $m$ lines contains two space-separated integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating that technician $u$ and technician $v$ are incompatible. Incompatibility is a symmetric relationship.
It is guaranteed that at least one mutually incompatible group of three technicians exists in the input.

## Output
Print three space-separated integers $a$, $b$, $c$ on a single line such that $1 \le a < b < c \le n$ and all three pairs $(a, b)$, $(a, c)$, and $(b, c)$ are recorded as incompatible. If there are multiple valid triples, output the lexicographically smallest one.

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
