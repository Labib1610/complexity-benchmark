# Problem C — Proof of Impossibility

Time limit: 2 s   Memory limit: 256 MB

The factory administration needs to divide its workforce into two non-overlapping shifts: day and night. However, HR has logged a list of mutual incompatibilities between specific workers. When an incompatibility is logged for a pair of workers, they are barred from working the same shift.

It has been determined that creating a valid two-shift assignment for the entire workforce is impossible due to inherent contradictions in the incompatibility log. To officially close the scheduling attempt, you must provide a specific proof of this impossibility. Specifically, you need to find three distinct employees who form a complete deadlock. A complete deadlock occurs among three employees when the first is incompatible with the second, the second is incompatible with the third, and the third is incompatible with the first. The log is guaranteed to contain at least one such triad. You must identify one such triad of employees.

## Input
The first line provides two integers $n$ and $m$. The workforce size $n$ ranges from 3 up to the facility's maximum of 2000. The number of logged incompatibilities $m$ is at least 3, and goes up to 200000 or the maximum possible number of distinct employee pairs, whichever is smaller.

Each of the subsequent $m$ lines contains two integers $u$ and $v$ — the ID numbers of a pair of employees who are incompatible. Employees are identified by numbers from 1 to $n$.

It is guaranteed that at least one complete deadlock involving three employees exists in the log.

## Output
Print three integers $a$, $b$, and $c$ on a single line with $a < b < c$, representing the ID numbers of the three employees in the deadlock. They must satisfy the condition that the log contains incompatibilities for the pairs $\{a, b\}$, $\{a, c\}$, and $\{b, c\}$. If there are multiple valid triads, output the one with the smallest value for $a$; in case of a tie, the one with the smallest value for $b$; and if still tied, the one with the smallest value for $c$.

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