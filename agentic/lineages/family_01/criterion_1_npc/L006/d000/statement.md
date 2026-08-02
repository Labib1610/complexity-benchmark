# Chemical Vault Partitioning

Time limit: 2 s   Memory limit: 256 MB

A research facility must store $n$ hazardous chemical substances, labeled from $1$ to $n$, across three isolated containment vaults designated as $1$, $2$, and $3$. Every substance must be assigned to exactly one vault.

Certain pairs of substances are chemically incompatible and cause unstable reactions if placed within the same vault. Thus, incompatible substances must always be assigned to different vaults.

Find an assignment of all $n$ substances to the three vaults such that no two incompatible substances occupy the same vault. If multiple valid vault assignments exist, choose the one that forms the lexicographically smallest sequence of vault numbers $(s_1, s_2, \dots, s_n)$, where $s_i$ denotes the vault assigned to substance $i$.

## Input
The first line contains two space-separated integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le \frac{n(n-1)}{2}$), representing the number of chemical substances and the number of incompatible pairs, respectively.

Each of the following $m$ lines contains two space-separated integers $u$ and $v$ ($1 \le u, v \le n, u \neq v$), indicating that substance $u$ and substance $v$ are incompatible.

## Output
If no valid vault assignment exists, print a single line containing `NO`.

Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1 s_2 \dots s_n$ (where each $s_i \in \{1, 2, 3\}$), representing the vault assigned to substance $i$. If multiple valid assignments exist, output the lexicographically smallest sequence.

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
