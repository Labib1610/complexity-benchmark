# Problem C — Proof of Impossibility

Time limit: 2 s   Memory limit: 256 MB

The manufacturing plant requires all personnel to be assigned to either the morning schedule or the evening schedule. Certain pairs of employees have filed grievances against each other and cannot be placed on the same schedule. 

Management already knows that a valid assignment for everyone is unachievable. Your job is not to attempt an assignment, but to produce the documentation proving it will fail. You are guaranteed that there exists at least one group of three employees where every individual in the group has a grievance with both of the other two. Any such group demonstrates the impossibility of using only two schedules. You must identify one such group.

## Input
The first line contains two integers $n$ and $m$. The headcount $n$ is at least 3 and at most the facility's maximum capacity of 2000. The grievance count $m$ is at least 3, and is capped at the system limit of 200000 or the maximum possible number of distinct pairs among the personnel, whichever is smaller.

Each of the following $m$ lines contains two integers $u$ and $v$ — the ID numbers of a pair of employees who cannot share a schedule. Employees are numbered from 1 to $n$.

It is guaranteed that at least one mutually incompatible group of three exists.

## Output
Print three integers $a$, $b$, and $c$ on a single line with $a < b < c$, such that the pairs $a$ and $b$, $a$ and $c$, as well as $b$ and $c$ all have grievances with each other. If there are multiple valid groups, output the one with the smallest value for $a$; in case of a tie, the smallest value for $b$; and if still tied, the smallest value for $c$.

## Example 1
Input:
```
4 5
1 2
1 3
2 3
2 4
3 4
```
Output:
```
1 2 3
```

## Example 2
Input:
```
5 6
1 2
1 4
2 4
3 4
3 5
4 5
```
Output:
```
1 2 4
```
