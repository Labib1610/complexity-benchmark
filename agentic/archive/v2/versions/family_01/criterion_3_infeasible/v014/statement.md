# Factory Shift Incompatibility Certification

Time limit: 2 s   Memory limit: 256 MB

A manufacturing plant operates on a rigid schedule of two shifts. However, operational frictions prohibit certain pairs of personnel from being assigned to the same shift. When scheduling fails, engineers generate a certificate demonstrating that no valid two-shift assignment exists.

Evaluating every possible grouping among thousands of workers would require searching an extensive space of personnel combinations. However, a schedule failure can be definitively certified by locating a single triplet of workers where every pair within the triplet suffers from operational friction. Your task is to analyze the registered personnel restrictions and output the lexicographically earliest such diagnostic triplet.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 2 \cdot 10^5)$), indicating the total number of workers (numbered $1$ through $n$) and the total number of recorded pairwise friction restrictions.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), specifying that worker $u$ and worker $v$ cannot be on the same shift.
It is guaranteed that at least one triplet of mutually incompatible workers exists in the input.

## Output
Print three space-separated integers $a$, $b$, $c$ on a single line such that $1 \le a < b < c \le n$ and all three pairs $(a, b)$, $(a, c)$, and $(b, c)$ are recorded pairwise friction restrictions. Output the lexicographically smallest such triple (minimizing $a$; breaking ties by minimizing $b$; then $c$).

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
