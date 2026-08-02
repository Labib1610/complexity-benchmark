# Vault Allocation Security

Time limit: 2 s   Memory limit: 256 MB

A chemical containment facility must store $n$ distinct materials, numbered 1 through $n$, across 3 isolated containment vaults labeled 1, 2, and 3.

Certain pairs of materials are chemically incompatible and will cause a dangerous reaction if placed inside the same vault. Every material must be assigned to exactly one vault, and no incompatible pair may share a vault.

Determine if there exists a valid vault assignment for all $n$ materials. If valid assignments exist, find the one that yields the lexicographically smallest sequence of vault labels $s_1\ s_2\ \dots\ s_n$, where $s_i$ is the vault assigned to material $i$.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le \frac{n(n-1)}{2}$) — the number of materials and the number of incompatible pairs.
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of materials that cannot share a vault.

## Output
If no valid assignment exists, print a single line `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1\ s_2\ \dots\ s_n$ (each in $\{1, 2, 3\}$), where $s_i$ is the vault assigned to material $i$. Among all valid assignments, output the lexicographically smallest sequence (compare $s_1$ first, then $s_2$, and so on).

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