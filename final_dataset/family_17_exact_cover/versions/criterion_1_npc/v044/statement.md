# Problem A — Regional Drill Deployment Plan

Time limit: 5 s   Memory limit: 256 MB

## Description
The regional emergency directorate is finalizing its readiness drill. The active roster contains exactly $3q$ responders, with ID codes assigned sequentially from $1$ to $3q$. The objective is to organize the entire roster into exactly $q$ response triads, where each triad consists of exactly three responders.

Command maintains a database of $t$ certified triplet protocols. Each protocol specifies three ID codes that have passed joint certification. Responders may only be deployed together if their exact three-person group appears in this database. 

Because the total capacity of $q$ triads is exactly $3q$ responders, this assignment simplifies to finding a set of exactly $q$ non-overlapping protocols. While individual protocols in the database may overlap and share responders, your final selected set must be entirely disjoint. Furthermore, since the database provides these protocols as strictly increasing sequences ($a < b < c$), you can systematically assign responders starting from ID $1$ up to $3q$ without needing to process arbitrary orderings. An allocation is valid if and only if every ID code from $1$ to $3q$ is included in exactly one activated protocol.

You must determine whether the database contains a combination of protocols that yields a valid allocation. If a valid allocation exists, output the protocols that form it. Otherwise, report that it is impossible.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 200$, $0 \le t \le 20000$), representing the target number of response triads and the number of certified protocols in the database.
The following $t$ lines each contain three integers $a$, $b$, and $c$ ($1 \le a < b < c \le 3q$). These are the ID codes comprising one certified protocol.

## Output
If a valid allocation exists, print `YES` on the first line. On the following $q$ lines, print the three ID codes for each protocol activated in the plan.
If no such allocation can be formed from the database, print `NO`.

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
