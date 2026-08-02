# Factory Roster

Time limit: 1 s   Memory limit: 256 MB

A facility operates under two operational modes, designated as Mode 1 and Mode 2. There are $n$ personnel, numbered $1$ through $n$. Certain pairs of personnel cannot work under the same operational mode due to equipment sharing restrictions. You are given $m$ such mutual exclusion constraints, where each constraint identifies two personnel who must be assigned different modes.

Your task is to determine whether it is possible to assign every person a mode (either 1 or 2) such that no mutual exclusion constraint is violated. If a valid configuration exists, find the sequence of assigned modes $(s_1, s_2, \dots, s_n)$ that is lexicographically smallest.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$), representing the number of personnel and the number of mutual exclusion constraints, respectively.

Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$), indicating that person $u$ and person $v$ cannot share the same operational mode.

## Output
If no valid assignment satisfies all constraints, print a single line containing `NO`.

Otherwise, print `YES` on the first line, and on the second line print $n$ space-separated integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{1, 2\}$), representing the lexicographically smallest valid mode assignment.

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
