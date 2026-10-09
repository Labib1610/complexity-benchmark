# Problem B — Environment Deployment

Time limit: 1 s
Memory limit: 256 MB

A software architecture contains $n$ distinct modules, numbered $1$ through $n$. You are tasked with migrating these modules into a new infrastructure that features exactly two execution environments, designated as 1 and 2. Every module must be assigned to exactly one of these two environments.

During testing, it was discovered that $m$ specific pairs of modules experience race conditions if they are placed in the same environment. To ensure system stability, you must allocate the modules such that no two modules involved in a race condition end up in the same environment. 

Furthermore, the following conditions are guaranteed to hold for all test cases:
- The maximum number of race conditions any single module is involved in is at most $m$.
- The combined total of modules and race conditions ($n + m$) is at most $400,000$.

Determine if a stable allocation exists. If it does, and there are multiple ways to allocate the modules, you must select the one that is lexicographically smallest when the assignments for modules $1$ to $n$ are written as a sequence of $1$s and $2$s.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$), indicating that module $u$ and module $v$ have a race condition. 

## Output
If it is impossible to separate all conflicting modules into the two environments, output a single line containing `NO`.
If it is possible, output `YES` on the first line. On the second line, output $n$ space-separated integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{1, 2\}$), representing the lexicographically smallest valid environment assignment.

## Example 1
**Input:**
```
4 4
1 2
2 3
3 4
1 4
```
**Output:**
```
YES
1 2 1 2
```

## Example 2
**Input:**
```
3 3
1 2
1 3
2 3
```
**Output:**
```
NO
```
