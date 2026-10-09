# Problem B — Orbital Array

Time limit: 1 s
Memory limit: 256 MB

An orbital array consists of $n$ satellites, numbered 1 through $n$. Each satellite must be configured with a deployment mode, which is set using either the integer 1 or the integer 2. 

The control system has identified $m$ critical operational constraints. Each constraint involves two specific satellites. Whenever a constraint exists between two satellites, their deployment modes must be chosen such that the sum of their mode values is exactly 3.

Determine a valid configuration for all $n$ satellites that satisfies every constraint. If multiple valid configurations exist, you must output the one that is lexicographically smallest. If no such configuration is possible, the system must report a failure.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ — the identifiers of two satellites that share a critical operational constraint.

## Output
If it is impossible to configure the array without violating a constraint, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1 \dots s_n$ (each being 1 or 2), representing the deployment modes of the satellites 1 through $n$ in the lexicographically smallest valid configuration.

## Example 1
Input:
```
4 4
1 2
2 3
3 4
1 4
```
Output:
```
YES
1 2 1 2
```

## Example 2
Input:
```
3 3
1 2
1 3
2 3
```
Output:
```
NO
```
