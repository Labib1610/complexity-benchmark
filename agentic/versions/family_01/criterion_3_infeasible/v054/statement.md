# Problem C — Roster Audit

Time limit: 2 s
Memory limit: 256 MB

The factory operates two shifts, 1 and 2. Management needs to assign each of the $n$ workers to one of these shifts. The HR department has compiled a log of mutual grievances between workers; if two workers share a mutual grievance, they cannot be assigned to the same shift.

When auditing a roster for shift assignment, HR must identify subsets of workers that are entirely mutually incompatible. We define an "irreducible conflict" as a subset of workers where every single worker in the subset has a logged mutual grievance with every other worker in that same subset.

Evaluating the combinatorial space of all $2^n$ possible worker subsets to find irreducible conflicts is a vast task. An irreducible conflict could theoretically involve any number of workers, and verifying one requires cross-checking all pairs within the chosen subset. 

For the current compliance cycle, your objective is to search this space and isolate an irreducible conflict. The specific regulatory requirement for this audit restricts your search to finding a subset that contains exactly three workers. It is guaranteed that the grievance log contains at least one such subset.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n - 1) / 2, 2 \cdot 10^5)$), representing the number of workers and the number of grievance records. Workers are identified by integers from $1$ to $n$.

Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), representing a mutual grievance between worker $u$ and worker $v$. Each pair of workers appears at most once in the log. It is guaranteed that at least one irreducible conflict of the required size exists.

## Output
Print three integers $a$, $b$, and $c$ on a single line with $a < b < c$, representing the IDs of the workers in the irreducible conflict.

If there are multiple valid subsets of the required size, output the one that is lexicographically smallest. This means you should prioritize finding the subset with the smallest possible value for $a$; if there is a tie, minimize the value for $b$; and if there is still a tie, minimize the value for $c$.

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
