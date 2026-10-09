# Problem A — Regional Readiness Drill Deployment

Time limit: 5 s   Memory limit: 256 MB

## Description
The regional emergency directorate is coordinating a comprehensive simulation. The active roster has a total staff count equal to three times a base factor $q$. Personnel are identified by badges numbered $1$ through $3q$. The simulation's mandate requires full operational efficiency: no individual may remain on standby, and no individual may be assigned to multiple concurrent duties.

Personnel are deployed exclusively in specialized teams of three. Due to strict interoperability standards, command will only authorize a team if those specific three individuals have previously completed joint certification. You are provided with a catalog of $t$ historically vetted teams. An individual might be part of several distinct vetted teams in the catalog, but command must authorize a specific collection of these teams to run the simulation.

Your objective is to determine whether it is possible to authorize a collection of vetted teams that perfectly fulfills the mandate—deploying the entire roster with zero idle personnel and zero overlapping assignments. If such a deployment is achievable, provide the teams to be authorized. If the catalog cannot support the mandate, report that it is impossible.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 200$, $0 \le t \le 20000$).
Each of the following $t$ lines contains three integers $a$, $b$, and $c$ ($1 \le a < b < c \le 3q$), representing the badge numbers of the individuals in one vetted team.

## Output
If a valid collection can be authorized, print `YES`, followed by $q$ lines, each listing the three individuals of an authorized team. 
If no such collection is possible, print `NO`.

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
