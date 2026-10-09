# Problem C — Vault Instability Certificate

Time limit: 2 s   Memory limit: 256 MB

A facility contains $n$ chemical components. The goal is to partition them into two isolated vaults. We have a list of $m$ highly reactive pairs; if two components form a reactive pair, they cannot be placed in the same vault.

Any subset of components that cannot be partitioned into two vaults serves as a certificate that the entire facility cannot be safely partitioned. The number of possible subsets of components is $2^n$, and a certificate could theoretically be of any size. To standardize the reporting process, you must output a certificate of exactly three components. It is guaranteed that the facility contains at least one subset of three components where every component in the subset reacts with the other two.

Find such a triplet. If there are multiple valid triplets, you must provide the one that comes first lexicographically (the triplet with the smallest first component; in case of a tie, the smallest second component; and finally the smallest third component, when each triplet is sorted in ascending order).

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n - 1) / 2, 2 \cdot 10^5)$).
Each of the next $m$ lines contains two integers $u$ and $v$ — representing a reactive pair of components.
It is guaranteed that at least one triplet of mutually reactive components exists.

## Output
Print three integers $a$, $b$, and $c$ on one line with $a < b < c$ such that the pairs $a$–$b$, $a$–$c$, and $b$–$c$ are all listed as reactive pairs. Output the lexicographically smallest such triplet.

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
