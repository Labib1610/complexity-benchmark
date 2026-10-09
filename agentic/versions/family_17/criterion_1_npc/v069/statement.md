# Problem A — Operation Checksum: Full-Roster Deployment

Time limit: 5 s
Memory limit: 256 MB

## Description
The regional emergency directorate is finalizing the deployment schedule for a readiness drill. The active roster consists of exactly $3q$ certified operators, each uniquely identified by a badge number from $1$ to $3q$. 

Every operating cell must consist of exactly three members. The directorate has a historical database containing $t$ pre-cleared trios of operators who have trained together. Deployment policy restricts the drill exclusively to these pre-cleared trios.

Your objective is to select exactly $q$ trios from the database such that every single operator on the roster is deployed in exactly one cell. No operator may be left behind, and no operator may be assigned to multiple cells. 

To ensure the integrity of the deployment plan, the audit department has imposed two mandatory checksum constraints on any valid schedule:
1. **Local Cell Checksum**: For every deployed cell, the sum of the three operators' badge numbers must be at least $6$ and no greater than $9q - 3$.
2. **Global Roster Checksum**: The grand total of all operators' badge numbers across the $q$ chosen cells must sum exactly to $\frac{3q(3q+1)}{2}$.

If a deployment schedule can be formed that satisfies the exact assignment requirement and both checksum constraints, it is considered a perfect plan. If the historical data does not contain a set of trios that achieves this exact balance, report that no acceptable plan exists.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 200$, $0 \le t \le 20000$). The total number of operators on the roster is $3q$.
Each of the following $t$ lines contains three integers $a$, $b$, and $c$ ($1 \le a < b < c \le 3q$), representing the badge numbers of one pre-cleared trio.

## Output
If a perfect deployment schedule can be extracted, print `YES` on the first line. Then, print $q$ lines, each containing the three operators of one chosen trio.
If no such schedule can be formed, print `NO`.

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
