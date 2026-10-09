# Problem C — Shift Validation Failure

Time limit: 2 s
Memory limit: 256 MB

A manufacturing plant operates exactly two daily shifts. A list of worker pairs is provided; if a pair is listed, those two workers have a documented grievance and cannot be assigned to the same shift. The current list of grievances makes a valid two-shift assignment impossible.

Your task is to isolate a specific configuration of workers that proves this impossibility. Consider a verification process that selects three distinct workers. The process checks the grievance list for the interactions between these three individuals. If the records show that the first worker has a grievance with the second, the second has a grievance with the third, and the first also has a grievance with the third, the process halts and rejects the shift plan. This happens because placing them into just two shifts will always force at least one pair with a grievance to work together. 

You must find three workers that will cause this process to halt. It is guaranteed that the records contain at least one such trio.

## Input
The first line contains the number of workers $n$ ($3 \le n \le 2000$) and the number of grievance records $m$ ($3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$).
The following $m$ lines each contain two integers $u$ and $v$ — representing a grievance between worker $u$ and worker $v$.
It is guaranteed that at least one trio of workers satisfying the halting condition exists.

## Output
Print three integers $a$, $b$, and $c$ on a single line, separated by spaces, representing the three workers.
The output must satisfy $a < b < c$. If there are multiple such trios, output the one that is lexicographically smallest (the one with the smallest $a$; in case of a tie, the one with the smallest $b$; and if still tied, the smallest $c$).

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
