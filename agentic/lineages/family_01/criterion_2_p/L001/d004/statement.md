# Problem B — Micro-Robotic Assembly

Time limit: 1 s   Memory limit: 256 MB

You are programming a swarm of $n$ micro-robots, indexed from 1 to $n$, to form a linear structure. Each robot must be positioned at either coordinate 1 or coordinate 2 on a one-dimensional track. Because the robots are microscopic, any number of them can occupy the same coordinate simultaneously.

You are given $m$ linkage constraints. Each constraint specifies that robot $u$ and robot $v$ must be connected by a rigid strut of length exactly 1. Consequently, the absolute difference between their assigned coordinates must be exactly 1. 

You must determine if there is a valid placement for all $n$ robots. If it is impossible to satisfy all linkage constraints simultaneously, you must report this. If there are multiple valid placements, the swarm's collision-avoidance protocol requires you to output the sequence of coordinates that is lexicographically smallest.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$), representing the number of robots and the number of linkage constraints.
Each of the subsequent $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), indicating that a strut of length 1 must connect robot $u$ and robot $v$.

## Output
If no valid placement is possible, output a single line containing `NO`.
Otherwise, output a line containing `YES`. On the following line, output $n$ space-separated integers $x_1, x_2, \dots, x_n$ (where each $x_i \in \{1, 2\}$) representing the assigned coordinate for each robot. This sequence must be the lexicographically smallest among all valid placements.

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