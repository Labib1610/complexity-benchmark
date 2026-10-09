# Problem A — Structural Alloy Assignment

Time limit: 5 s   Memory limit: 256 MB

## Description
A structural framework is built from a set of hubs and a set of connecting rods. The topology of the framework is strictly regulated: every hub must serve as the junction for exactly three rods. 

Furthermore, the rods themselves are manufactured in three distinct material variants, identified as 1, 2, and 3. To prevent uneven thermal wear, a local constraint is enforced at every junction: the three rods converging at any single hub must each be made of a different material variant. 

Your objective is to evaluate a specific framework design and determine if it is possible to assign a material variant to every rod such that the thermal wear constraint is perfectly satisfied across all hubs.

## Input
The first line contains two integers **n** and **m** (n even, m = 3n/2, 2 ≤ n ≤ 2000), representing the number of hubs and rods, respectively.
Each of the following **m** lines contains two integers u and v (1 ≤ u < v ≤ n), indicating a rod connecting hub u and hub v.

## Output
If a valid material allocation exists, print `YES`, followed by a line with **m** integers from the set {1, 2, 3} — the material variant of the i-th rod, corresponding to the order the rods appear in the input. If no such allocation is possible, print `NO`.

## Example
Input:
```
4 6
1 2
1 3
1 4
2 3
2 4
3 4
```
Output:
```
YES
1 2 3 3 2 1
```
