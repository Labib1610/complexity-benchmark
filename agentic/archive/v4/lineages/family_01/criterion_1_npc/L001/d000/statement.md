# Vault Preservation Allocation

Time limit: 2 s   Memory limit: 256 MB

A museum is relocating $n$ fragile artifacts (numbered $1$ through $n$) into three specialized storage vaults, designated as Vault 1, Vault 2, and Vault 3.

Certain pairs of artifacts produce chemical vapors that interact destructively if placed in the same environment. Therefore, two artifacts involved in such an incompatible pair must never be assigned to the same vault.

Determine whether it is possible to assign every artifact to exactly one vault without placing any incompatible pair together. If multiple valid placement plans exist, select the plan that yields the lexicographically smallest sequence of vault numbers $s_1, s_2, \dots, s_n$ (that is, comparing $s_1$ first, then $s_2$, and so on).

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le \frac{n(n-1)}{2}$), representing the number of artifacts and the number of incompatible pairs, respectively.
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating that artifact $u$ and artifact $v$ cannot be stored in the same vault.

## Output
If no valid vault assignment exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1, s_2, \dots, s_n$ ($s_i \in \{1, 2, 3\}$), where $s_i$ denotes the vault assigned to artifact $i$, choosing the lexicographically smallest sequence.

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
