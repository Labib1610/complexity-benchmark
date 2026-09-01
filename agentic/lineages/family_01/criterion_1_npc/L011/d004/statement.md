# Problem A — Global Energy State

Time limit: 2 s   Memory limit: 256 MB

You are analyzing a discrete system consisting of $n$ particles. Each particle must be assigned an energy level $c_i \in \{1, 2, 3\}$. 

The system contains $m$ interacting pairs of particles. The total interaction energy of the system is given by the sum of interactions over all $m$ pairs. For a pair of interacting particles $u$ and $v$, their interaction energy is defined by the expression:
$$E(u, v) = 5(c_u - c_v)^2 - (c_u - c_v)^4$$

A complete configuration of the system $C = (c_1, c_2, \ldots, c_n)$ is considered stable if and only if the total interaction energy over all $m$ pairs is exactly $4m$. That is:
$$\sum_{i=1}^m E(u_i, v_i) = 4m$$

Your objective is to determine a stable configuration for all $n$ particles. A complete configuration is represented as a sequence of $n$ integers $C = (c_1, c_2, \ldots, c_n)$. If multiple stable configurations exist, you must output the sequence that is lexicographically smallest. Specifically, given two distinct stable configurations $C$ and $C'$, configuration $C$ is strictly smaller than $C'$ if $c_k < c'_k$ at the lowest index $k$ where the two sequences differ. If it is impossible to find a stable configuration, report that no solution exists.

## Input
The first line provides two integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$), representing the number of particles and the number of interacting pairs, respectively.
The following $m$ lines each contain two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating that particle $u$ and particle $v$ form an interacting pair.

## Output
If no stable configuration can be formed, print a single line containing `NO`.
If a stable configuration is possible, print `YES` on the first line. On the second line, print $n$ integers $c_1, c_2, \ldots, c_n$, where $c_i \in \{1, 2, 3\}$ is the energy level assigned to particle $i$. If there are multiple valid assignments, you must output the lexicographically smallest sequence.

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