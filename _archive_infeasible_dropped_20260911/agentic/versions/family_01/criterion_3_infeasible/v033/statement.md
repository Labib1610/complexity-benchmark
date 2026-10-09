# Inadequate Facilities

Time limit: 2 s   Memory limit: 256 MB

A manufacturing plant employs $n$ technicians. Management wants to divide them between Facility 1 and Facility 2. However, certain pairs of technicians have filed grievances against each other and cannot be assigned to the same facility.

The HR department has already determined that a valid division into two facilities is unachievable. Your task is to extract a simple proof of this failure: a group of exactly three technicians where every individual in the group has a grievance filed against every other individual in the group. Because there are only two facilities available, any such group of three technicians guarantees that at least two of them would be forced into the same facility.

You must output the ID numbers of these three technicians. It is guaranteed that the grievance logs contain at least one such group of three.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$), representing the number of technicians and the total number of grievances.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), representing a grievance between technician $u$ and technician $v$.

## Output
Print three integers $a$, $b$, and $c$ on a single line, separated by spaces, representing the chosen technicians. The IDs must be printed in increasing order ($a < b < c$).

If there are multiple valid groups of three, output the one that minimizes $a$. If there is still a tie, minimize $b$, and if a tie remains, minimize $c$.

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
