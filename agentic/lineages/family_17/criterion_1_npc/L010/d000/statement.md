# Problem A — Routine Drill Scheduling

Time limit: 5 s   Memory limit: 256 MB

## Description
The regional emergency directorate is generating a routine schedule for an upcoming readiness drill. The active roster contains $3q$ certified operators, numbered sequentially from $1$ to $3q$. 

To maintain standard operational protocols, operators are deployed in response units. A response unit is always formed by three specific operators who have previously completed joint certification. The directorate has provided a comprehensive catalog of $t$ pre-cleared unit configurations, compiled from recent training cycles. Because these configurations reflect standard training cohorts, the data is highly structured and many operators share multiple joint certifications.

A deployment schedule is considered valid only if it is fully balanced. This means every operator on the active roster must be assigned to an active unit, and no operator may be scheduled for more than one unit simultaneously. In other words, you must select a collection of units from the catalog such that each operator from $1$ to $3q$ is accounted for exactly once. 

Your task is to process the historical catalog of configurations and determine whether a valid, non-conflicting schedule can be formed. If a balanced schedule is possible, you must also provide one such assignment.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 200$, $0 \le t \le 20000$), where $3q$ represents the total number of operators on the active roster, and $t$ is the number of pre-cleared unit configurations.

Each of the following $t$ lines contains three integers $a$, $b$, and $c$ ($1 \le a < b < c \le 3q$), representing the badge numbers of the operators in one pre-cleared configuration.

## Output
If a valid schedule can be formed, print `YES` on the first line. On the next $q$ lines, print the three operators for each selected unit in your schedule. If no such schedule is possible, print `NO`.

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
