# Factory Duty Allocation

Time limit: 1 s   Memory limit: 256 MB

A manufacturing facility operates using two distinct work periods, labeled 1 and 2. There are $n$ personnel, numbered 1 through $n$, each of whom must be assigned to perform their duties during exactly one work period.

Certain pairs of personnel are designated as mutually exclusive: if person $u$ and person $v$ are mutually exclusive, they cannot be assigned to the same work period.

Your task is to determine whether it is possible to assign every person to a work period such that no mutually exclusive pair shares the same period. If such an assignment exists, choose the one that is lexicographically smallest when represented as the sequence $s_1, s_2, \dots, s_n$, where $s_i \in \{1, 2\}$ is the work period assigned to person $i$.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$), representing the number of personnel and the number of mutual exclusivity constraints, respectively.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), indicating that person $u$ and person $v$ cannot share the same work period.

## Output
If no valid assignment of work periods exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line, followed by a second line containing $n$ space-separated integers $s_1, s_2, \dots, s_n$ ($s_i \in \{1, 2\}$), representing the lexicographically smallest valid assignment.

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
