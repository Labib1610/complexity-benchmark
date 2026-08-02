# Problem B — Sector Assignment

Time limit: 1 s   Memory limit: 256 MB

A manufacturing plant operates two non-overlapping work sectors, labeled 1 and 2. The plant employs $n$ personnel, indexed from $1$ to $n$. Due to safety regulations and supervisory constraints, certain pairs of personnel are designated as mutually exclusive and cannot be assigned to the same sector.

You must assign every employee to exactly one sector (1 or 2) such that no mutually exclusive pair is placed in the same sector. If multiple valid assignments exist, choose the one that yields the lexicographically smallest sequence of assignments $(s_1, s_2, \dots, s_n)$, where $s_i$ is the sector assigned to employee $i$. A sequence $A = (a_1, \dots, a_n)$ is lexicographically smaller than $B = (b_1, \dots, b_n)$ if at the first index $k$ where $a_k \neq b_k$, $a_k < b_k$.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$) — the total number of employees and the number of mutually exclusive pairs, respectively.

Each of the next $m$ lines contains two space-separated integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), representing a pair of employees who cannot share a sector.

## Output
If no valid assignment exists, print a single line containing `NO`.

Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1, s_2, \dots, s_n$ ($s_i \in \{1, 2\}$), denoting the lexicographically smallest valid assignment.

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
