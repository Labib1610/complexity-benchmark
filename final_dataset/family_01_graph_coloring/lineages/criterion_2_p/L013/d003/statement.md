# Problem B — Asset Hedging

Time limit: 1 s   Memory limit: 256 MB

A financial institution is allocating a portfolio of $n$ assets into two separate investment pools, labeled as Vehicle 1 and Vehicle 2. Every single asset must be placed into exactly one of these two vehicles.

Due to extreme market correlation, risk analysts have identified $m$ specific pairs of assets that require careful handling. To comply with the institution's hedging policy, every flagged pair must be split: exactly one asset from each such pair must be placed into Vehicle 1.

Your objective is to find a complete allocation of the $n$ assets that strictly respects all $m$ hedging policies. If such an allocation is possible, you must output it. In cases where multiple valid allocations exist, you must choose the one that yields the lexicographically smallest sequence of $n$ vehicle identifiers (using 1s and 2s).

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$), indicating the total number of assets and the number of flagged asset pairs. The assets are indexed from 1 to $n$.
The following $m$ lines each contain two integers $u$ and $v$, specifying a pair of assets that falls under the hedging policy.

## Output
If no allocation can satisfy all hedging policies, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, output $n$ integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{1, 2\}$) denoting the assigned vehicles for assets 1 through $n$. If there are multiple valid allocations, output the sequence that is lexicographically smallest.

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