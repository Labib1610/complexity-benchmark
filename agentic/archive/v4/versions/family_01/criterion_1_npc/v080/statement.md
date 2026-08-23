# Chemical Vault Allocation

Time limit: 2 s   Memory limit: 256 MB

A research facility must store $n$ distinct chemical compounds, indexed from $1$ to $n$. There are three isolated storage vaults available, designated by the integers $1$, $2$, and $3$. Each compound must be assigned to exactly one vault.

Safety logs specify $m$ hazardous interaction risks between pairs of compounds. If two compounds have an interaction risk listed, they cannot be placed in the same vault.

Determine whether it is possible to allocate every compound to a vault without placing any conflicting pair in the same vault. If a valid configuration exists, report `YES` followed by the lexicographically smallest list of vault choices $s_1, s_2, \dots, s_n$ (where $s_i \in \{1, 2, 3\}$ represents the vault for compound $i$). If no safe storage allocation exists, report `NO`.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le \frac{n(n-1)}{2}$) — the number of chemical compounds and the number of interaction risks.
Each of the following $m$ lines contains two space-separated integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$), indicating that compound $u$ and compound $v$ cannot share a vault.

## Output
If no safe vault assignment exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1, s_2, \dots, s_n$ ($s_i \in \{1, 2, 3\}$), representing the assigned vault for each compound $1$ through $n$. If multiple valid vault assignments exist, output the lexicographically smallest one.

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
