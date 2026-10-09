# Problem C — Shift Deadlock Identification

Time limit: 2 s
Memory limit: 256 MB

You are managing a roster of $n$ workers. Certain pairs of workers have filed mutual grievances, meaning they cannot be assigned to the same shift. You are given a log of $m$ such grievance pairs.

The company only operates two shifts. It has been determined that creating a valid two-shift schedule for all workers is impossible. Your task is to extract the core reason for this impossibility from the grievance log.

To prove that two shifts are not enough, you must identify a specific configuration of three workers. The requirement for this configuration is that if you select any two workers out of the three, there must be a grievance record between them. Because every individual in this trio refuses to share a shift with either of the other two, no two of them can be on the same shift, making it impossible to assign them to only two shifts.

It is guaranteed that the log contains at least one such configuration. You must search the grievance records to find it.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$), representing the number of workers and the number of grievance pairs.

The following $m$ lines each contain two integers $u$ and $v$, indicating that worker $u$ and worker $v$ have a mutual grievance. It is guaranteed that there exists at least one set of three workers where every pair among them has a grievance.

## Output
Print three integers $a$, $b$, and $c$ on a single line with $a < b < c$, representing the IDs of three workers who meet the condition (i.e., grievances exist between $a$ and $b$, between $a$ and $c$, and between $b$ and $c$). Output the lexicographically smallest such group (minimize $a$; in case of a tie, minimize $b$; then minimize $c$).

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
