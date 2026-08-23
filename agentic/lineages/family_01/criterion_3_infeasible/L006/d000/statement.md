# Problem C — Vault Impossibility Certificate

Time limit: 2 s   Memory limit: 256 MB

You are tasked with storing $n$ delicate historical artifacts, numbered 1 through $n$, into exactly two climate-controlled vaults. Due to their varied material compositions, certain pairs of artifacts require mutually exclusive atmospheric conditions and cannot be placed in the same vault.

The provided list of incompatible pairs makes it impossible to divide all artifacts into just two vaults. Your task is to extract a direct proof of this impossibility. Specifically, you must identify a group of exactly three artifacts such that every artifact in the group is incompatible with both of the others. Because there are only two vaults available, any such group guarantees that at least two of the three artifacts would be forced into the same vault, which is forbidden. Output one such group.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$), representing the number of artifacts and the number of incompatible pairs.
Each of the next $m$ lines contains two integers $u$ and $v$ — an incompatible pair.
It is guaranteed that at least one group of three mutually incompatible artifacts exists.

## Output
Print three integers $a$, $b$, and $c$ on one line with $a < b < c$ such that all three pairs $a$–$b$, $a$–$c$, and $b$–$c$ are incompatible. Output the lexicographically smallest such group (smallest $a$; ties by smallest $b$; then smallest $c$).

## Example 1
Input:
```
4 5
1 2
1 3
2 3
2 4
3 4
```
Output:
```
1 2 3
```

## Example 2
Input:
```
5 6
1 2
1 4
2 4
3 4
3 5
4 5
```
Output:
```
1 2 4
```
