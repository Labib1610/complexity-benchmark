# Botanical Equilibrium

Time limit: 1 s   Memory limit: 256 MB

A botanical research facility is cultivating $n$ distinct plant species, numbered 1 through $n$. The head botanist must assign a nutrient dosage level to each species. The assigned dosage level for each species must be a positive integer not exceeding 2.

The facility features an irrigation network consisting of $m$ hydroponic tubes. Each tube forms a direct link between exactly two specific species. To maintain chemical equilibrium within the irrigation network, the product of the dosage levels assigned to the two species connected by any single tube must be exactly 2.

Determine if it is possible to assign a dosage level to all $n$ species such that chemical equilibrium is maintained across all tubes.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), representing a pair of species linked by a hydroponic tube.

## Output
If no valid assignment of dosage levels exists, output a single line containing `NO`.
Otherwise, output `YES` on the first line. On the second line, output $n$ integers $s_1 \dots s_n$, representing the lexicographically smallest valid assignment of dosage levels.

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