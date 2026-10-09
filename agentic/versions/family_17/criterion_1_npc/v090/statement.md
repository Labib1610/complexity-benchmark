# Problem A — Phase 3: Mobilization Assignment

Time limit: 5 s
Memory limit: 256 MB

## Description
The regional emergency directorate has initiated Phase 3 of its annual readiness drill. The goal of this phase is to finalize the mobilization of $q$ deployment units.

The active personnel roster consists of $3q$ individuals, who are identified by sequential tracking numbers from $1$ to $3q$. During the earlier synergy testing phase, various potential units—each comprising three individuals—were put through a communication simulator. The units that successfully completed the simulation were logged in the clearance database.

Your software must process these logs to finalize the deployment. You are required to approve exactly $q$ units from the database. To maintain strict operational constraints, no individual tracking number may appear more than once across your approved units.

Determine whether a valid mobilization can be formed under these rules, and if so, output the specific units to be dispatched.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 200$, $0 \le t \le 20000$), where $q$ is the target number of deployment units, and $t$ is the number of units logged in the clearance database.

Each of the next $t$ lines contains three integers $a$, $b$, and $c$ ($1 \le a < b < c \le 3q$), representing the tracking numbers of the personnel in a successfully logged unit.

## Output
If a valid mobilization can be formed, print `YES` on the first line. Following that, print $q$ lines, each containing the three tracking numbers of an approved unit. 
If no such mobilization is possible, print `NO`.

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
