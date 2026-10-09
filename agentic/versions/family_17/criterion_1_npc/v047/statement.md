# Problem A — Comprehensive Squad Allocation for the Readiness Simulation

Time limit: 5 s
Memory limit: 256 MB

## Description
The Disaster Response Agency is organizing a comprehensive readiness simulation. The active personnel roster consists of exactly $3q$ responders, who are assigned unique badge numbers sequentially from 1 to $3q$. 

Agency protocol requires a rigid deployment structure. Every operational squad must contain exactly three responders. Since the roster size is a multiple of three, exactly $q$ squads are required to field the entire roster. The agency mandates that every single responder must be assigned to exactly one squad, with no responder left unassigned or placed in multiple squads.

Due to strict compatibility requirements, responders can only be deployed in specific three-person teams that have previously completed joint certification. The agency's archives contain a list of $t$ such certified teams. The simulation must be built exclusively from these $t$ available teams. 

Furthermore, you are guaranteed that the archive satisfies two compliance constraints:
1. For any certified team, the sum of the badge numbers of its three members is strictly less than 1800.
2. For any certified team, the difference between the highest and lowest badge numbers among its members is strictly less than 600.

Your objective is to select exactly $q$ mutually exclusive teams from the $t$ certified options such that all $3q$ responders are deployed. If the provided archive does not contain a combination of teams that achieves this perfect allocation, you must report that no valid deployment exists.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 200$, $0 \le t \le 20000$). The total number of responders is $3q$.
Each of the following $t$ lines contains three integers $a$, $b$, and $c$ ($1 \le a < b < c \le 3q$), representing the badge numbers of responders in one certified team.

## Output
If a valid deployment can be formed, print `YES` on the first line. Then, output $q$ lines, each containing the three badge numbers of a selected team.
If no such deployment is possible, print `NO`.

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
