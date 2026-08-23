# Operational Shift Allocation Module

Time limit: 2 s   Memory limit: 256 MB

## Description
A facility management pipeline is responsible for assigning $n$ personnel (numbered $1$ through $n$) to work shifts. There are three available shift slots, designated by the integers $1$, $2$, and $3$.

Due to operational safety regulations, certain pairs of personnel are prohibited from working during the same shift. An assignment is valid if every employee $i$ is given a shift $s_i \in \{1, 2, 3\}$ such that no two mutually prohibited employees share the same shift index.

To ensure consistency across downstream tracking services, the system enforces the following constraints and guidelines:
1. **Capacity Limit**: The sum of all assigned shift values $\sum_{i=1}^n s_i$ cannot exceed $3n$.
2. **Deterministic Selection**: If at least one valid shift configuration exists, the system must output the lexicographically smallest sequence $(s_1, s_2, \dots, s_n)$. (That is, $s_1$ is minimized first; if ties remain, $s_2$ is minimized, and so on.)

Determine whether a valid assignment can be made. If no valid assignment exists, output `NO`. Otherwise, output `YES` followed by the lexicographically smallest assignment sequence.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le \frac{n(n-1)}{2}$) — the number of personnel and the number of pairwise safety prohibitions.

Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating that employee $u$ and employee $v$ cannot be assigned to the same shift.

## Output
If no valid shift assignment exists, print `NO` on a single line.

Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1, s_2, \dots, s_n$ ($s_i \in \{1, 2, 3\}$), representing the lexicographically smallest valid shift assignment.

## Example 1
Input:
```
4 5
1 2
1 3
2 3
1 4
2 4
```
Output:
```
YES
1 2 3 3
```

## Example 2
Input:
```
4 6
1 2
1 3
1 4
2 3
2 4
3 4
```
Output:
```
NO
```
