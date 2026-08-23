# Zone Allocation Protocol

Time limit: 2 s   Memory limit: 256 MB

A cloud architecture manages $n$ software modules, numbered $1$ to $n$. Every module must be deployed to exactly one of three available execution domains, represented by the integers 1, 2, and 3.

Due to hardware interference constraints, certain pairs of modules are incompatible and cannot be placed in the same execution domain.

Determine whether there exists a valid domain placement for all $n$ modules such that no incompatible pair shares an execution domain. If multiple valid placements exist, find the one that yields the lexicographically smallest sequence of domain identifiers $s_1, s_2, \dots, s_n$ (comparing $s_1$ first, then $s_2$, and so on).

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le \frac{n(n-1)}{2}$) — the number of modules and the number of incompatibility rules.
Each of the next $m$ lines contains two integers $u$ and $v$ — an incompatible pair of modules.

## Output
If no valid deployment exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1, s_2, \dots, s_n$ (each $s_i \in \{1, 2, 3\}$), representing the domain assigned to each module.

## Example 1
Input:
```
4 5
1 2
1 3
2 3
1 4
2 4
```
Output:
```
YES
1 2 3 3
```

## Example 2
Input:
```
4 6
1 2
1 3
1 4
2 3
2 4
3 4
```
Output:
```
NO
```
