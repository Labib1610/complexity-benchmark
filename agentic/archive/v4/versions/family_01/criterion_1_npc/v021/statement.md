# Tier Allocation Protocol

Time limit: 2 s   Memory limit: 256 MB

A high-security database manages $n$ digital assets labeled $1, 2, \dots, n$. To ensure system stability, each asset must be assigned to one of three isolated memory zones, designated as $1$, $2$, and $3$.

Certain pairs of assets have operational cross-interference and must not be placed into the same memory zone.

Your task is to assign every asset to exactly one memory zone such that no interfering pair shares a zone. If multiple valid zone assignments exist, choose the assignment that forms the lexicographically smallest sequence of zone designations $(s_1, s_2, \dots, s_n)$. If no valid assignment is possible, report this result.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le \frac{n(n-1)}{2}$) — the number of assets and the number of interfering pairs.

Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$) specifying that asset $u$ and asset $v$ interfere with each other.

## Output
If no valid assignment exists, print a single line containing `NO`.

Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{1, 2, 3\}$), representing the memory zone assigned to asset $i$.

Among all valid assignments, output the one that is lexicographically smallest (comparing $s_1$ first, then $s_2$, and so on).

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
