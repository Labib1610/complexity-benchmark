# Problem B — Micro-Robotic Assembly

Time limit: 1 s   Memory limit: 256 MB

You are orchestrating a swarm of $n$ micro-machines, labeled from 1 to $n$, to build a linear framework. Each machine must be deployed to either position 1 or position 2 along a microscopic rail. Multiple machines can share the same position without interference.

The framework requires $m$ rigid struts to be installed. Each strut links a specific pair of machines, $u$ and $v$. To maintain the necessary mechanical tension across the strut, the combined sum of the positions of these two linked machines must be exactly 3.

Your task is to determine whether all machines can be deployed such that every strut's tension requirement is met. If no such configuration exists, you must indicate this failure. If several valid configurations exist, the deployment protocol demands the sequence of positions (from machine 1 to $n$) that forms the numerically smallest $n$-digit integer when the positions are written in order.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$), representing the number of machines and the number of struts.
Each of the subsequent $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), indicating that a strut must link machine $u$ and machine $v$.

## Output
If no valid deployment is possible, output a single line containing `NO`.
Otherwise, output a line containing `YES`. On the following line, output $n$ space-separated integers $x_1, x_2, \dots, x_n$ (where each $x_i \in \{1, 2\}$) representing the assigned position for each machine. This sequence must be the one that forms the smallest $n$-digit integer among all valid deployments.

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