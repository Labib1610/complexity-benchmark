# Problem B — Power Scaling

Time limit: 1 s   Memory limit: 256 MB

A manufacturing facility employs $n$ robotic welders, which are identified by integers from 1 to $n$. The facility requires each welder to be configured with a phase setting of exactly 1 or 2. 

Over time, management has installed $m$ shared power buses. Each bus connects two specific welders. A strict operational rule dictates that to prevent electrical overload, the bitwise XOR of the phase settings of any two welders connected by a shared bus must evaluate to exactly 3.

Your task is to determine whether the entire set of welders can be configured in complete compliance with this operational rule. If a compliant configuration exists, you must provide the specific configuration sequence $s_1, s_2, \dots, s_n$ (where each $s_i \in \{1, 2\}$ is the phase setting assigned to welder $i$) that is lexicographically smallest. If no such configuration is possible, you must report that it cannot be done.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ — representing the two welders connected by a shared power bus.

## Output
If there is no way to assign the phase settings without violating the operational rule, print a single line containing NO.
Otherwise, print YES on the first line. On the second line, print $n$ space-separated integers $s_1, s_2, \dots, s_n$ (each either 1 or 2), representing the lexicographically smallest valid configuration sequence.

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