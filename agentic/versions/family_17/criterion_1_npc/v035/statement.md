# Problem A — Full-Coverage Cell Deployment for the Regional Drill

Time limit: 5 s   Memory limit: 256 MB

## Description
The regional emergency directorate is preparing a full-scale readiness drill. Every certified operator on the active roster must be committed to the exercise — leadership has been explicit that a drill in which any operator sits idle is treated as a planning failure, and equally that no operator may be counted in more than one place at the same moment. The roster is fixed for the duration of the drill and consists of exactly $3q$ operators, with unique badge numbers running consecutively from 1 to $3q$.

Because the total roster size is a perfect multiple of three, the deployment structure is strictly uniform. Operators are only ever fielded in cells of exactly three. Over the years, particular trios have completed joint certification together, and standing policy permits command to field a cell if and only if that precise three-person trio appears on the pre-cleared list. Every pre-cleared trio contains exactly three distinct operators.

A deployment plan is simply an activation of exactly $q$ of these cleared trios. Because $q$ trios of size 3 yield exactly $3q$ positions, a plan is acceptable if and only if the $q$ chosen trios share no operators among them. This perfectly balanced uniformity means you do not need to optimize the number of cells or handle variable capacities; you simply need to ensure that each of the $3q$ operators appears in exactly one activated cell, tiling the roster with no gaps and no overlaps.

Your task is to decide whether the pre-cleared list contains $q$ disjoint trios that perfectly tile the roster, and if they do, to produce one acceptable deployment plan. If the cleared list cannot cover the roster under these uniform rules, report that no acceptable plan exists.

## Input
The first line contains two integers **q** and **t** (1 ≤ q ≤ 200, 0 ≤ t ≤ 20000).
Each of the next **t** lines contains three integers a b c (1 ≤ a < b < c ≤ 3q): an allowed triple.

## Output
If a valid selection exists, print `YES`, then q lines each with the three items of one chosen triple.
Otherwise print `NO`.

## Examples
### Example 1
Input:
```
2 3
1 2 3
4 5 6
1 4 5
```
Output:
```
YES
1 2 3
4 5 6
```
