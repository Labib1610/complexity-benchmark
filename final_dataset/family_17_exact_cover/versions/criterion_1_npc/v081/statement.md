# Problem A — Readiness Drill Mobilization

Time limit: 5 s   Memory limit: 256 MB

## Description
The regional emergency directorate is preparing a mobilization plan for an upcoming readiness drill. The roster is built around a core requirement $q$, scaling up to a total of $3q$ personnel. These personnel hold badge numbers from $1$ to $3q$.

The drill requires personnel to act in coordinated deployment teams. Due to prior joint-certification requirements, a team always consists of three specific individuals. The directorate’s database contains $t$ pre-cleared teams. 

A mobilization plan is formed by activating some of these pre-cleared teams. To ensure comprehensive assessment without causing fatigue, the activation must be planned so that no person on the roster is left out of the drill, and no person is subjected to multiple deployments. 

Your task is to verify if the database allows for such a mobilization plan, and if so, to output the activated teams.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 200$, $0 \le t \le 20000$), where $3q$ represents the total number of personnel on the active roster, and $t$ is the number of pre-cleared teams.

Each of the following $t$ lines contains three integers $a$, $b$, and $c$ ($1 \le a < b < c \le 3q$), representing the badge numbers of the individuals in one pre-cleared team.

## Output
If a valid mobilization plan can be formed, print `YES` on the first line. On the next $q$ lines, print the three individuals for each activated team in your plan. If no such plan is possible, print `NO`.

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
