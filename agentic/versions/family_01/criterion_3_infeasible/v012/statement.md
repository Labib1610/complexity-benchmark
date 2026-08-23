# Problem C — Critical Triad

Time limit: 2 s
Memory limit: 256 MB

In a hazardous materials storage facility, certain pairs of chemical compounds are highly reactive when placed in close proximity. While the facility can manage isolated pairs of reactive compounds using specialized dual-containment bins, this system completely fails if there is a "critical triad"—a set of three separate compounds where every single pair among the three is reactive.

Your task is to identify a critical triad to demonstrate that the current storage protocols are insufficient. You are given a list of all reactive pairs. It is guaranteed that the inventory contains at least one critical triad.

## Input
The first line contains two integers n and m (3 ≤ n ≤ 2000, 3 ≤ m ≤ min(n·(n−1)/2, 2·10⁵)), representing the number of compounds and the number of reactive pairs, respectively. Compounds are numbered from 1 to n.
Each of the following m lines contains two integers u and v (1 ≤ u, v ≤ n, u ≠ v), indicating that compound u and compound v are reactive.
It is guaranteed that at least one critical triad exists.

## Output
Print three integers a, b, and c on a single line, separated by spaces, representing the identifiers of the compounds in a critical triad. The identifiers must be printed in increasing order (a < b < c).
If there are multiple critical triads, output the one that is lexicographically smallest (i.e., minimize a; in case of a tie, minimize b; and if still tied, minimize c).

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
