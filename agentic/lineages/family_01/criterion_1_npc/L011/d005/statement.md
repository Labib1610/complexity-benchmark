# Problem A — Global Energy State

Time limit: 2 s   Memory limit: 256 MB

You are analyzing a discrete system consisting of $n$ particles. Each particle $i$ (from $1$ to $n$) must be assigned an energy level $c_i \in \{1, 2, 3\}$. 

The system contains $m$ interacting pairs of particles. A complete configuration of the system $C = (c_1, c_2, \ldots, c_n)$ is considered stable if and only if for every interacting pair of particles $u$ and $v$, their assigned energy levels are different (that is, $c_u \neq c_v$).

Your objective is to determine a stable configuration for all $n$ particles. If multiple stable configurations exist, you must output the valid configuration $C$ that strictly minimizes the following structural objective function:
$$W(C) = \sum_{i=1}^n c_i \cdot 4^{n-i}$$

If it is impossible to find a stable configuration, report that no solution exists.

## Input
The first line provides two integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$), representing the number of particles and the number of interacting pairs, respectively.
The following $m$ lines each contain two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating that particle $u$ and particle $v$ form an interacting pair.

## Output
If no stable configuration can be formed, print a single line containing `NO`.
If a stable configuration is possible, print `YES` on the first line. On the second line, print $n$ integers $c_1, c_2, \ldots, c_n$, where $c_i \in \{1, 2, 3\}$ is the energy level assigned to particle $i$. If there are multiple stable configurations, you must output the sequence that minimizes the objective function $W(C)$.

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