# Problem A — Curating the Grand Exhibition

Time limit: 5 s   Memory limit: 256 MB

## Description
A museum is organizing a temporary exhibition featuring exactly $3q$ selected artifacts. The artifacts are identified by integers from 1 to $3q$. 

The exhibition floor plan consists of custom display cases, each designed to hold exactly three artifacts. The conservation department has compiled a list of approved three-artifact groups that can safely share a display case's microclimate. A display case can only be populated using one of these approved groups.

The exhibition must include every single artifact from the selection. Since each artifact is a unique physical object, it can be placed in at most one display case. You must determine if it is possible to select a set of approved groups such that every artifact from 1 to $3q$ is displayed exactly once. If a valid selection exists, you must output the groups chosen for the display cases.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 200$, $0 \le t \le 20000$).
Each of the following $t$ lines contains three integers $a$, $b$, and $c$ ($1 \le a < b < c \le 3q$), representing the IDs of the artifacts that make up one approved group.

## Output
If a valid selection of groups can be formed, print `YES` on the first line. Then, output $q$ lines, each containing the three artifact IDs of a chosen group.
If no such selection is possible, print `NO`.

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
