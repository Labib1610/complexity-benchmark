# Vault Storage Assignment for Reactive Compounds

Time limit: 1 s   Memory limit: 256 MB

A chemical laboratory needs to partition $n$ distinct chemical compounds, indexed from $1$ to $n$, into two isolated storage vaults (Vault 1 and Vault 2).

Due to dangerous cross-reactivity, certain pairs of compounds cannot be safely placed in the same vault. Every compound must be assigned to exactly one vault ($1$ or $2$) such that no pair of mutually reactive compounds shares a vault.

If there are multiple safe vault assignments, you must determine the one that yields the lexicographically smallest sequence of vault choices $s_1, s_2, \ldots, s_n$. If no safe assignment is possible, report that the partition cannot be accomplished.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 200\,000$, $0 \le m \le 200\,000$), representing the total number of chemical compounds and the total number of cross-reactivity constraints, respectively.

Each of the next $m$ lines contains two space-separated integers $u$ and $v$ ($1 \le u, v \le n, u \neq v$), indicating that compound $u$ and compound $v$ cannot share the same storage vault.

## Output
If no safe vault assignment exists, print a single line containing `NO`.

Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1, s_2, \ldots, s_n$ (where each $s_i \in \{1, 2\}$), representing the lexicographically smallest valid assignment sequence.

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
