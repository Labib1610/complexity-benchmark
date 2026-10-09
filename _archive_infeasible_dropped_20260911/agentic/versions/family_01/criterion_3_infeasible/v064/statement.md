# Problem C — Safety Audit Configuration

Time limit: 2 s   Memory limit: 256 MB

A chemical storage facility is reviewing its safety protocols. The facility manages $n$ distinct chemical compounds. Extensive testing has produced a catalog of $m$ specific pairs of these compounds that undergo an exothermic reaction when combined.

You are tasked with finding a critical configuration to demonstrate the inadequacy of a proposed two-container isolation system. A critical configuration is a subset of exactly $k=3$ distinct compounds such that all $\binom{k}{2}$ pairs formed by its elements are present in the catalog of reactions.

Given that $n$ can be up to 2000, the configuration space contains over a billion possible 3-compound subsets. You must search this space to identify a valid critical configuration. To ensure standardized reporting, if multiple valid configurations exist, you must output the one that is lexicographically first based on the compounds' numerical identifiers. A lexicographically first configuration $(a, b, c)$ with $a < b < c$ minimizes $a$, then minimizes $b$ in the event of a tie, and finally $c$.

It is strictly guaranteed that the catalog allows for at least one such configuration.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 2\cdot 10^5)$).
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$) — a pair of compounds in the catalog. Unordered pairs are not repeated.
It is guaranteed that at least one valid critical configuration exists.

## Output
Print three integers $a$, $b$, and $c$ on a single line with $a < b < c$, representing the compounds in the lexicographically first critical configuration.

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
