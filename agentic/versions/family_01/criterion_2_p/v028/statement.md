# Botanical Gardens

Time limit: 1 s   Memory limit: 256 MB

You are tasked with arranging $n$ rare plant species in a newly constructed botanical conservatory. The conservatory features a primary cultivation area, designated as Zone 1, and a secondary cultivation area, designated as Zone 2. Every species must be allocated to exactly one of these areas.

Extensive research has identified $m$ cases of allelopathy between specific pairs of species. If two species involved in such a case are placed in the same cultivation area, they will release biochemicals that inhibit each other's growth. To ensure the survival of all plants, your arrangement must separate every allelopathic pair into different areas.

Given the number of species and the list of allelopathic pairs, determine if a safe allocation is possible.

## Input
The first line provides the number of species, $n$, and the number of allelopathic cases, $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$). The species are indexed from $1$ to $n$.
Each of the subsequent $m$ lines contains two integers $u$ and $v$ — representing a pair of species that inhibit each other.

## Output
If no safe allocation can be achieved, output a single line containing `NO`.
Otherwise, output `YES` on the first line. On the second line, output $n$ space-separated integers $z_1, z_2, \dots, z_n$ (where each $z_i \in \{1, 2\}$) representing the area assigned to each species. If multiple safe allocations exist, output the one that is lexicographically smallest.

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
