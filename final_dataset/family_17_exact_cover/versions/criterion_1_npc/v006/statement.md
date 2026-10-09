# Problem A — Full-Coverage Cell Deployment for the Regional Drill

Time limit: 5 s
Memory limit: 256 MB

## Description
You are scheduling a regional emergency readiness drill. Because the audit requires a complete accounting of personnel, every operator on the active roster must participate. Since an operator cannot physically be in two places at once, no operator may be assigned to multiple cells. The roster consists of $3q$ operators, each identified by a unique badge number from $1$ to $3q$.

Due to vehicle capacity limits, operators must be deployed in response cells of exactly three people. To ensure team cohesion, a cell may only be formed if its exact three-person combination appears on a pre-cleared list of certified trios. You are provided with this list of $t$ allowed trios.

Your task is to choose a subset of the pre-cleared trios to form a deployment plan. A plan is valid if and only if every operator on the roster appears in exactly one chosen trio. If such a deployment plan exists, you must output one; otherwise, report that no valid plan can be formed.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 200$, $0 \le t \le 20000$), where $3q$ is the total number of operators and $t$ is the number of pre-cleared trios.
Each of the next $t$ lines contains three integers $a$, $b$, and $c$ ($1 \le a < b < c \le 3q$), representing the badge numbers of the operators in one pre-cleared trio.

## Output
If a valid deployment plan exists, print `YES`, followed by $q$ lines each containing the three badge numbers of a chosen trio.
Otherwise, print `NO`.

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
