# Problem A — Grid Management Upgrade

Time limit: 5 s
Memory limit: 256 MB

## Description
A regional energy provider is upgrading its grid management system. This upgrade is executed in three distinct phases:

**Phase 1 (Surveying):** Field engineers have mapped out $n$ power substations (numbered 1 to $n$) and identified $m$ viable corridors where fiber-optic links can be installed. They have assessed the exact installation expense for each corridor.

**Phase 2 (Synthesis):** This is your responsibility. Among the $n$ substations, exactly $t$ have been designated as primary control centers. Your task is to design a unified communication backbone that ensures all $t$ primary control centers can exchange data with one another (meaning they must all be part of the same connected network). Messages can be routed through any sequence of installed fiber links, utilizing any of the non-primary substations as passive relays if it reduces the overall expense. You must calculate the minimum possible total expense required to achieve this connectivity among the primary control centers.

**Phase 3 (Deployment):** The minimum expense figure you compute will be submitted to the finance committee. Once the budget is approved, procurement and installation crews will be dispatched to lay the fiber in the chosen corridors.

Write a program to execute Phase 2: given the survey data from Phase 1, output the required budget for Phase 3.

## Input
The first line contains three integers $n$, $m$, and $t$ ($1 \le t \le 10$, $1 \le n \le 100$, $0 \le m \le n(n-1)/2$).
The second line contains $t$ distinct integers: the IDs of the primary control centers.
Each of the next $m$ lines contains three integers $u$, $v$, and $w$ ($1 \le u, v \le n$, $u \neq v$, $1 \le w \le 1000000$), representing a viable corridor between substation $u$ and substation $v$ with an installation expense of $w$.
It is guaranteed that the surveyed corridors are sufficient to connect all primary control centers.

## Output
Print a single integer: the minimum total expense to ensure all primary control centers are connected.

## Examples

### Example 1

**Input**
```
4 6 3
1 2 3
1 4 1
2 4 1
3 4 1
1 2 2
2 3 2
1 3 2
```

**Output**
```
3
```

### Example 2

**Input**
```
4 4 3
1 2 3
1 2 1
2 3 1
1 4 10
3 4 10
```

**Output**
```
2
```

### Example 3

**Input**
```
3 2 1
1
1 2 5
2 3 5
```

**Output**
```
0
```

## Note
In Example 1, routing the fiber through the passive relay substation 4 (which costs 1+1+1 = 3) is cheaper than linking the three primary control centers directly to each other (which would cost 4). 
In Example 3, there is only one primary control center, so no fiber links need to be installed.
