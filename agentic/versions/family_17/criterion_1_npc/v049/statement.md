# Phase 2: Full-Coverage Cell Deployment

Time limit: 5 s   Memory limit: 256 MB

## Description
During readiness drills, the regional emergency directorate relies on a master list of pre-cleared response units. The roster consists of operators assigned consecutive badge numbers from $1$ up to a total of $3q$. The master list provides a catalog of potential units, each comprising exactly three specific operators who have completed joint certification. Ad-hoc groupings outside of this catalog are strictly forbidden.

When a drill is initiated, the directorate enforces strict participation rules for any active schedule. First, overlapping deployments are prohibited: if an operator is assigned to one active unit, they cannot be assigned to any other. Second, the deployment must be comprehensive: no operator on the roster may be left idle. Because of these rules, the selected subset of units must collectively include every operator from $1$ to $3q$ exactly once.

Your software is responsible for the deployment planning phase. Given the target parameter $q$ and the master list of pre-cleared units, you must select a subset of these units that satisfies all of the directorate's participation rules. You must either produce a schedule that perfectly meets these conditions or determine that the provided master list makes it impossible to do so.

## Input
The first line provides two integers $q$ and $t$ ($1 \le q \le 200$, $0 \le t \le 20000$). The value $q$ determines the total roster size of $3q$ operators, and $t$ is the number of pre-cleared units on the master list.
Each of the subsequent $t$ lines contains three integers $a$, $b$, and $c$ ($1 \le a < b < c \le 3q$), representing the badge numbers of the operators in a single pre-cleared unit.

## Output
If a valid deployment plan can be formed, print `YES` on the first line. Then, output $q$ lines, each containing the three badge numbers of an activated unit in your schedule. If no such plan is possible, print `NO`.

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
