# Problem A — Full-Coverage Cell Deployment for the Regional Drill

Time limit: 5 s   Memory limit: 256 MB

## Description
For an upcoming readiness drill, the regional emergency directorate must deploy its entire active roster to evaluate full-scale response capabilities. The roster contains exactly $3q$ certified operators, who are identified by consecutive badge numbers from $1$ to $3q$.

During the drill, operators must be deployed in distinct response cells, with each cell strictly mandated to contain exactly three operators. Because cell members must communicate seamlessly, a cell may only be activated if its exact three-person lineup appears on a pre-cleared list maintained by the training division. This pre-cleared list represents all combinations of operators who have previously completed joint certification.

A valid deployment plan must activate a subset of these pre-cleared cells such that every single operator on the roster is assigned to exactly one activated cell, ensuring no operator is left idle and no operator is double-booked.

Your task is to determine if a valid deployment plan exists for the given roster and pre-cleared list, and if so, output the specific cells to activate.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 200$, $0 \le t \le 20000$), where $q$ is the target number of response cells to activate and $t$ is the number of pre-cleared combinations.

Each of the next $t$ lines contains three integers $a$, $b$, and $c$ ($1 \le a < b < c \le 3q$), representing the badge numbers of three operators who form a pre-cleared cell.

## Output
If a valid deployment plan exists, print `YES` on the first line. Then, print $q$ lines, each containing the three badge numbers of an activated cell. 
If no valid deployment plan is possible, print `NO`.

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
