# Problem B — Safety Scheduling

Time limit: 1 s   Memory limit: 256 MB

A manufacturing plant operates exactly two daily production periods, designated as period 1 and period 2. The plant employs $n$ technicians, numbered from 1 to $n$. To maintain safety standards, certain pairs of technicians who have previously disagreed on safety protocols must not be scheduled during the same production period.

You are provided with a list of $m$ such incompatible pairs. Your task is to determine if it is possible to assign every technician to either period 1 or period 2 such that no two incompatible technicians work during the same period. If this is possible, you must provide the assignment. To standardize the scheduling system across the plant, if there are multiple valid ways to assign the technicians, you must output the sequence of assignments that is lexicographically smallest.

## Input
The first line contains two integers $n$ and $m$ (1 ≤ $n$ ≤ 2·10⁵, 0 ≤ $m$ ≤ 2·10⁵), representing the number of technicians and the number of incompatible pairs.
Each of the following $m$ lines contains two integers $u$ and $v$ (1 ≤ $u, v$ ≤ $n$), indicating that technician $u$ and technician $v$ cannot be assigned to the same period.

## Output
If there is no way to assign the periods without violating the safety standards, output a single line containing `NO`.
If a valid assignment exists, output `YES` on the first line. On the second line, output $n$ integers $s_1, \dots, s_n$ (where each $s_i$ is either 1 or 2), representing the period assigned to each technician from 1 to $n$. This sequence must be the lexicographically smallest valid assignment.

## Example 1
Input:
```
4 4
1 2
2 3
3 4
1 4
```
Output:
```
YES
1 2 1 2
```

## Example 2
Input:
```
3 3
1 2
1 3
2 3
```
Output:
```
NO
```
