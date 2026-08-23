# Vault Allocation

Time limit: 2 s   Memory limit: 256 MB

A chemical research facility houses $n$ sensitive compounds, numbered $1$ through $n$. The facility has three isolated storage vaults labeled $1$, $2$, and $3$. Certain pairs of compounds are chemically volatile when stored together and must not be placed into the same vault.

You must assign every compound to exactly one vault such that no volatile pair shares a vault, or determine that no safe arrangement exists.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$) — the number of chemical compounds and the number of incompatible pairs.
Each of the next $m$ lines contains two integers $u$ and $v$ — indicating that compound $u$ and compound $v$ cannot be stored in the same vault.

## Output
If no valid vault assignment exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1 s_2 \dots s_n$ (where each $s_i \in \{1, 2, 3\}$), representing the vault assignment for each compound $i$. If there are multiple valid assignments, output the one that is lexicographically smallest (comparing $s_1$ first, then $s_2$, and so on).

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
