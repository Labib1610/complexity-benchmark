# Problem C — Habitat Allocation Veto

Time limit: 2 s   Memory limit: 256 MB

A conservation park is preparing to house $n$ rescued animal species, numbered 1 through $n$. The veterinary team has compiled a list of $m$ specific pairs of species that exhibit severe territorial aggression. If two species appear together as a pair on this list, they are forbidden from sharing the same habitat enclosure. 

The park management initially proposed constructing exactly two large enclosures to house all the species. However, this proposal is fundamentally unworkable. The behavioral data guarantees the existence of a structural contradiction: a subset of exactly three species that inherently requires at least three enclosures. This occurs because the veterinary list explicitly forbids sharing an enclosure for every possible pair formed from this subset.

To finalize the veto of the two-enclosure proposal, you must provide a formal certificate of its failure by identifying one such subset of three species.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 2 \cdot 10^5)$).
The following $m$ lines each contain two integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$), representing a pair of species that are forbidden from sharing an enclosure. Each pair is listed at most once.
It is guaranteed that at least one such subset of three species exists.

## Output
Print three integers $a$, $b$, and $c$ on a single line, separated by spaces, representing the numbers of the three species in the subset. The numbers must be printed in ascending order ($a < b < c$).
If there are multiple such subsets, you must output the one that is lexicographically smallest. That is, minimize $a$; if there is a tie, minimize $b$; and if there is still a tie, minimize $c$.

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