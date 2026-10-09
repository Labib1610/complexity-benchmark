# Chemical Storage

Time limit: 1 s   Memory limit: 256 MB

A laboratory is organizing a collection of $n$ chemical reagents, numbered from 1 to $n$. The facility has exactly two containment units, designated by the identifiers 1 and 2. Every reagent must be placed into exactly one of these two units.

The laboratory has identified $m$ reactive pairs among the reagents. Placing both reagents of a reactive pair into the same containment unit will result in a hazardous reaction. Therefore, the two reagents in any reactive pair must be separated into different units.

Your task is to determine if there is a safe way to distribute all $n$ reagents into the two units. If there are multiple safe distributions, you must select the one that resolves ties by prioritizing unit 1 as early as possible. Specifically, among all safe distributions, find those that assign the smallest possible unit identifier to reagent 1. If there is more than one such distribution, narrow them down to those that also assign the smallest possible identifier to reagent 2, and continue this sequential elimination up to reagent $n$.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), representing a reactive pair of reagents.

## Output
If there is no safe way to distribute the reagents, output a single line containing `NO`.
Otherwise, output `YES` on the first line. On the second line, output $n$ integers separated by spaces, where the $i$-th integer (either 1 or 2) is the unit assigned to the $i$-th reagent in your chosen distribution.

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
