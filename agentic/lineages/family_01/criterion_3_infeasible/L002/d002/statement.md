# Problem C — Volatile Complex

Time limit: 2 s   Memory limit: 256 MB

You are analyzing a sample of $n$ synthetic proteins. Your specialized assay has identified $m$ instances of stable binding affinity, where a specific pair of proteins are capable of bonding to each other.

A volatile "ternary complex" forms if three distinct proteins all share binding affinities with one another (each of the three can bond directly to the other two). The sample you are analyzing is guaranteed to contain at least one such three-protein complex. You must identify the components of this complex.

## Input
The first line provides $n$ and $m$ (3 ≤ n ≤ 2000, 3 ≤ m ≤ min(n·(n−1)/2, 2·10⁵)), representing the number of synthetic proteins and the number of bonding pairs, respectively.
The following $m$ lines each contain two integers $u$ and $v$, indicating that protein $u$ and protein $v$ share a stable binding affinity.
The input will always contain at least one ternary complex involving three proteins.

## Output
Output three integers $a$, $b$, and $c$ on a single line, separated by spaces, with $a < b < c$. These must represent a set where the bonding pairs $a$–$b$, $a$–$c$, and $b$–$c$ are all present in the input. If there are multiple such sets, provide the one that is lexicographically first (prioritizing the lowest value for $a$, then the lowest for $b$, and finally $c$).

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