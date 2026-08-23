# Problem B — Phase Alignment

Time limit: 1 s   Memory limit: 256 MB

A manufacturing plant is calibrating $n$ robotic actuators. Each actuator must have its operating phase set to either $1$ or $2$. 

There are $m$ critical joints, each connecting a pair of actuators. To maintain mechanical stability, the two actuators connected at any joint must be configured such that the sum of their assigned phase values is exactly $3$. 

You must determine a phase assignment for each actuator that satisfies all stability constraints, or report that no such arrangement is possible.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of actuators connected by a joint.

## Output
If no valid phase arrangement exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line, followed by a second line containing $n$ integers $s_1, \dots, s_n$ (each $s_i \in \{1, 2\}$), where $s_i$ is the phase assigned to actuator $i$. If there are multiple valid arrangements, output the one that is lexicographically smallest.

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