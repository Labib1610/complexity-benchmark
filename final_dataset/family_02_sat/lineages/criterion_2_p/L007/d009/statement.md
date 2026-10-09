# Problem B — Hypercube Projection Proximity

Time limit: 1 s
Memory limit: 256 MB

## Description
You are configuring a system of $n$ nodes. Each node $i$ ($1 \le i \le n$) must be assigned a discrete coordinate $x_i \in \{0, 1\}$. This assignment forms a global position vector $X = (x_1, x_2, \dots, x_n)$ in an $n$-dimensional hypercube.

The system's stability is governed by $m$ spatial constraints. Each constraint is defined by two non-zero integers $l_1$ and $l_2$. 
For each constraint, we extract a 2-dimensional projection of the global position: $P = (x_{|l_1|}, x_{|l_2|})$.
We also compute a target point $T = (t_1, t_2)$ defined by:
- $t_1 = \frac{1}{2} \left(1 + \frac{l_1}{|l_1|}\right)$
- $t_2 = \frac{1}{2} \left(1 + \frac{l_2}{|l_2|}\right)$

For the system to remain stable, every constraint must be satisfied. A constraint is satisfied if and only if the squared Euclidean distance between the projection $P$ and its target point $T$ is strictly less than $2$. 

Recall that the squared Euclidean distance between two points $(u_1, v_1)$ and $(u_2, v_2)$ is $(u_1 - u_2)^2 + (v_1 - v_2)^2$.

Your task is to determine if there exists a global position vector $X$ that satisfies all $m$ spatial constraints simultaneously.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 10^5$, $0 \le m \le 2 \cdot 10^5$), representing the number of nodes and the number of spatial constraints.
Each of the next $m$ lines contains two non-zero integers $l_1$ and $l_2$ ($1 \le |l_1|, |l_2| \le n$), defining a single constraint.

## Output
If no valid global position vector exists, print a single line `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $x_1, x_2, \dots, x_n$ (each in $\{0, 1\}$) forming any valid position vector.

## Example 1
Input:
```
2 2
1 2
-1 -2
```
Output:
```
YES
1 0
```

## Example 2
Input:
```
1 2
1 1
-1 -1
```
Output:
```
NO
```

## Note
Multiple valid position vectors may exist; any one is accepted. The same node index may appear in multiple constraints, and it is possible that $l_1 = l_2$ or $l_1 = -l_2$ within a single constraint.