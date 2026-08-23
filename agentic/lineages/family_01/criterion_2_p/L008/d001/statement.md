# Botanical Treatments

Time limit: 1 s   Memory limit: 256 MB

A botanical research facility is cultivating $n$ distinct plant species, numbered 1 through $n$. The head botanist must assign exactly one of two available nutrient blends, designated as 1 and 2, to each species.

The facility has $m$ shared hydroponic tubes. Each tube connects exactly two specific species. Due to the chemical interactions of the roots, if two species connected by a tube receive the same nutrient blend, a toxic reaction will ruin the water supply. Consequently, any two species that share a tube must be assigned different nutrient blends.

Determine if it is possible to assign a nutrient blend to all $n$ species without causing any toxic reactions.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$) — a pair of species connected by a hydroponic tube.

## Output
If no safe assignment exists, print a single line `NO`.
Otherwise print `YES`, then a second line with $n$ integers $s_1 \dots s_n$ (each in $\{1,2\}$), the lexicographically smallest valid assignment.

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