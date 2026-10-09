# Frequency Allocation Certificate

Time limit: 2 s   Memory limit: 256 MB

A telecommunications provider operates $n$ radio towers, identified by integers from 1 to $n$. A recent survey mapped $m$ specific pairs of towers with overlapping broadcast ranges. To prevent signal collision, any two towers with overlapping ranges must be assigned distinct operating frequencies.

The infrastructure team planned to deploy exactly two distinct frequencies across the entire network. However, this deployment strategy is invalid. The survey data guarantees the presence of at least one triad of towers where each tower's range overlaps with the ranges of the other two. Because all three towers mutually overlap, they require three distinct frequencies, making a two-frequency deployment impossible.

To formally document why the two-frequency plan was rejected, you must identify one such triad of mutually overlapping towers.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 2 \cdot 10^5)$).
The following $m$ lines each contain two integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$), specifying that tower $u$ and tower $v$ have overlapping broadcast ranges. Each overlapping pair is recorded at most once.
It is guaranteed that at least one triad of mutually overlapping towers exists.

## Output
Print three integers $a$, $b$, and $c$ on a single line, separated by spaces, representing the identifiers of three towers that form a mutually overlapping triad. The identifiers must be printed in ascending order ($a < b < c$).
If there are multiple such triads, output the one that is lexicographically smallest. That is, minimize $a$; if there is a tie, minimize $b$; and if there is still a tie, minimize $c$.

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
